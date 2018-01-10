# Post-Install

## Necessities:
* macOS installed

## Step 1 - Installing clover to disk
This process is pretty similar to installing clover to the bootable usb in the pre-install section

Download the latest version of clover from [here](https://github.com/Dids/clover-builder/releases/tag/v2.4k_r4370) (click `Clover_vx.x_rxxxx.pkg`, should be ~18mb)

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

## Step 2 - Kexts
Now we're going to install more kexts (kernel extensions), just like we did in the [Pre-Install](../master/Pre-Install.md).

First of all copy over the kexts from your `USB > Clover > Kexts > Other` to `Hackintosh > Clover > Kexts > Other`
To make this process easier read the [tips](../master/Tips.md#how-to-mount-efi)

Once you've done that there are a few more kexts to install, as we still need Internet, Audio and some other fixups.

Check your motherboard specifications and look for the LAN Chipset.
* 
* 
* 

Now find the corresponding kext from the [kext repo](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ)



If you have an AMD GPU, make sure to get `WhateverGreen.kext` as well. If you have an NVIDIA GPU you'll have to worry about that later.

Drag all the kexts over to `Hackintosh > Clover > Kexts > Other`
All kexts mentioned above can be downloaded from [here] (https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ)

## Step 3 - Config
