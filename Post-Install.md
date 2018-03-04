# Post-Install

## Necessities:
* macOS installed
* apfs.efi installed from [Pre-install guide](Pre-Install.md)

## Step 1 - Installing Clover to disk
This process is pretty similar to installing Clover to the bootable USB in the pre-install section.

Download the latest version of Clover from [here](https://github.com/Dids/clover-builder/releases/latest/) (click `Clover_vx.x_rxxxx.pkg`, should be ~18mb)

Right click (or CMD/Ctrl + right click) on the package and click Open. You will get a prompt telling you that the software is from an unidentified developer.

Click Continue, Continue, Agree and Agree. Now, click Customize and select the following for booting Clover UEFI:
```
    Install Clover for UEFI booting only
    Install Clover to the ESP
    Drivers64UEFI
        OsxAptioFix2Drv-64 or OsxAptioFix3Drv-64 (If you can't boot then install other one and remove the old one)
        OsxAptioFix2Drv-free2000.efi (For X99/X299 or MSI mobo, download from Stuff folder)
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
Now we're going to install our kexts (kernel extensions), just like we did in the [Pre-Install](Pre-Install.md#step-3---downloading-kexts).

First, [mount the EFI partition](Tips.md#how-to-mount-efi) of the disk you installed High Sierra on.

### Here are some general kexts you will definitely need:
* [FakeSMC](https://bitbucket.org/RehabMan/os-x-fakesmc-kozlek/downloads/) (This is needed to boot **any** hackintosh. This kext spoofs the presence of a valid SMC chip and stops the trigger of DontStealMacOS.kext when booting on non-Mac hardware.)
* [Lilu](https://github.com/vit9696/Lilu/releases) (Kext inject platform)
* [AppleALC](https://github.com/vit9696/AppleALC/releases) (For audio) (Need Lilu too)
* [USBInjectAll](https://bitbucket.org/RehabMan/os-x-usb-inject-all/downloads/) (More info [here](.Tips.md#usbinjectall))
* [XHCI-200-series-injector.kext](https://github.com/piiiggg/Ramblings-of-a-hackintosher-High-Sierra/blob/master/Stuff/XHCI-200-series-injector.kext.zip) (for 200/300-series motherboard) (Need USBInjectAll too)
* A LAN kext (We will go into more detail about this later.)

You can find the latest compiled kexts in [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ) (Massive thanks to GoldFish64 for setting up and maintaining his kext repo.)
Or you can find official versions compiled by the kext owner [here](https://docs.google.com/spreadsheets/d/1WQ87XQKgJVPPub_CbjoHsUscgyxrGg3DWzZz7Nnf_RU/)

### LAN Kext
Check your motherboard specifications and look for the LAN Chipset. This could be one of the following:
* Intel® GbE LAN chip ([IntelMausiEthernet](http://www.insanelymac.com/forum/files/file/396-intelmausiethernet/))
* Realtek RTL8111 ([RealtekRTL8111](http://www.insanelymac.com/forum/files/file/88-realtekrtl8111-binary/))
* Atheros E2200 ([AtherosE2200](http://www.insanelymac.com/forum/files/file/313-atherose2200ethernet/)
* Realtek RTL8100 ([RealtekRTL8100](http://www.insanelymac.com/forum/files/file/259-realtekrtl8100-binary/))
* Something else (check the [kext repo](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ) for a fitting kext)

## Step 3 - Setting up the config.plist
Yet again, for ease of use you'll have to install [Clover Configurator](http://mackie100projects.altervista.org/download-clover-configurator/) and configure our config.plist with that. Again you can also use [Clover Configurator Cloud](http://cloudclovereditor.altervista.org/cce/index.php). 

First, [mount the EFI partition](Tips.md#how-to-mount-efi) of the install media and the disk you installed High Sierra on.

Now let's copy over the config.plist we used on your install media.

* In boot you can now remove Verbose (-v) and debug=0x100

Practically you should be set up on this part.

## Step 4 - USB setup
You can download USBInjectAll [here](https://bitbucket.org/RehabMan/os-x-usb-inject-all/downloads/).

If you're on a 200-series mobo you want to get [XHCI-200-series-injector.kext](https://github.com/RehabMan/OS-X-USB-Inject-All/tree/master/XHCI-200-series-injector.kext/Contents).

If you're on a X79/X99 mobo you want to get [XHCI-x99-injector.kext](https://github.com/RehabMan/OS-X-USB-Inject-All/tree/master/XHCI-x99-injector.kext/Contents).

You should have either USBInjectAll, XHCI-200-series-injector.kext or XHCI-x99-injector.kext. You should never have more USB/XHCI injector.

To make all the USB ports on your build work, you need to raise the port limit. (more info [here](Tips.md#usbinjectall))

Go to Kernel and Kext Patches and add a new KextsToPatch entry with the following info:
```
Name:    com.apple.driver.usb.AppleUSBXHCIPCI
Find:    837d8c10
Replace: 837d8c1b
Comment: change 15 port limit to 26 in XHCI kext
```

NOTE: All these steps should be taken in combination with having the [USBInjectAll](https://github.com/RehabMan/OS-X-USB-Inject-All) kext.

## Step 5 - Install graphics drivers
### iGPU

- Install `IntelGraphicsFixup.kext` and Lilu
- Enable Inject Intel and [choose ig-platform-id](ig-platform-id.md) from config.plist - Graphics
- For Skylake & Kaby Lake & Coffee Lake users: add -disablegfxfirmware boot arg

### AMD

- Install `WhateverGreen.kext` and `Lilu`
- Enable RadeonDeInit: config.plist - Graphics - RadeonDeInit. [Needed for some AMD GPUs only](https://www.tonymacx86.com/threads/radeon-compatibility-guide-ati-amd-graphics-cards.171291/).

### NVIDIA

- Install `NvidiaGraphicsFixup.kext` and `Lilu`
- You need the NVIDIA WebDrivers for Graphics Acceleration. You can download the corresponding WebDriver from [this link](https://cookiemonster.pro/nvidia_driver_table).
- Enable NvidiaWeb and Inject System ID.

If your WebDrivers are not applied after reboot (you check this by clicking the NVIDIA driver button in the top bar), you need to check if your NVRAM is working the way it should be. For more in-depth [click here](Tips,md#nvidia-web-drivers-not-kicking-in).

If you are using an NVIDIA GPU like the 7/6-series or older, you don't need to install the WebDriver, it's natively supported by Apple.

## Step 6 - Audio
Check out the guide we made on audio [here](Audio.md).

For HDMI Audio, check [here](HDMI-Audio.md)

## Step 7 - Other

You may need to setup [iMessage/FaceTime](iMessage.md), [CPU SpeedStep](Speedstep.md), [Multiboot guide](Multiboot.md) or check out some [Tips](Tips.md)

If you want something a little risky, check out our [experiment test](Experiment.md)

If you're having problems, check out our [troubleshooting guide](Troubleshooting.md)
