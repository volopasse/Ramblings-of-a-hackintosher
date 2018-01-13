# Post-Install

## Necessities:
* macOS installed

## Step 1 - Installing clover to disk
This process is pretty similar to installing clover to the bootable usb in the pre-install section

Download the latest version of clover from [here](https://github.com/Dids/clover-builder/releases/) (click `Clover_vx.x_rxxxx.pkg`, should be ~18mb)

Right click (or CMD+click) on the package and click Open, you will get a prompt telling you that the software is from an unidentified developer instead. ([how to disable this](http://osxdaily.com/2016/09/27/allow-apps-from-anywhere-macos-gatekeeper/))

Click Continue, Continue, Agree and Agree. Now, click Customize and select the following for booting Clover UEFI:
```
    Install Clover for UEFI booting only
    Install Clover to the ESP
    Drivers64UEFI
        OsxAptioFix2Drv-64
        apfs
        PartitionDxe-64
```

For booting Legacy:
```
    Install Clover to the ESP
    Bootloader
        Install boot0ss in MBR
    CloverEFI
        CloverEFI 64-bits SATA
```

Select your USB drive and click Install.

## Step 2 - Kexts
Now we're going to install our kexts (kernel extensions), just like we did in the [Pre-Install](../master/Pre-Install.md#step-3---downloading-kexts).

First, [mount the EFI partition](../master/Tips.md#how-to-mount-efi) of the disk you installed High Sierra on.

### Here are some general kexts you will definitely need:
* FakeSMC (This is needed to boot **any** hackintosh.)
* Lilu (Kext patch platform)
* AppleALC (For audio)
* USBInjectAll (More info [here](.../master/Tips.md#usbinjectall))
* A LAN kext (we will go into more detail about this later.)

You can find the latest compiled kexts in [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ) (Massive thanks to GoldFish64 for setting up and maintaining his kext repo.)
Or you can find official compiled by kext owner in [here](https://docs.google.com/spreadsheets/d/1WQ87XQKgJVPPub_CbjoHsUscgyxrGg3DWzZz7Nnf_RU/)

### LAN Kext
Check your motherboard specifications and look for the LAN Chipset. This could be one of the following:
* Intel® GbE LAN chip ([IntelMausiEthernet](https://github.com/Mieze/IntelMausiEthernet))
* Realtek RTL8111 ([RealtekRTL8111](https://github.com/Mieze/RTL8111_driver_for_OS_X))
* Atheros E2200 ([AtherosE2200](https://github.com/Mieze/AtherosE2200Ethernet))
* Realtek RTL8100 ([RealtekRTL8100](https://github.com/Mieze/RealtekRTL8100))
* Something else (check the [kext repo](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ) for a fitting kext)

### Graphics Kexts
If you do not have an SMBIOS listed [here](../master/Tips.md#nvidiagraphicsfixup-and-some-smbioses-explained) or  if you do not have an AMD gpu, skip this step.

If you have an AMD GPU, make sure to get `WhateverGreen.kext` and Lilu. 
(Disclaimer: This works on some cards. There are often extra steps that need to take place for you to get full graphics acceleration.)

If you have the iMac15,1 and up (iMac17,1, iMac18,x) or MacPro6,1 SMBIOS, you will need to follow the instructions [here](../master/Tips.md#nvidiagraphicsfixup-and-some-smbioses-explained).

All kexts can be downloaded from [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ)

## Step 3 - Config
