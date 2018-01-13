# Tips
## How to mount EFI
Open Terminal and run `diskutil list`, this will show you all your available Volumes. Look up your disk's name and remember the disk identifier that corresponds with your disk (this should look something like diskX). Once you're sure you have the right disk identifier that corresponds with your disk, run `diskutil mount diskXs1`, with the X being your disk number.

If you have only one EFI partition, you can also run `diskutil mount EFI`.

You can also mount your EFI partition with Clover Configurator.

## How to install kexts
A small disclaimer first, please try to inject kexts whenever you can. There is a possibility that if you update, your kexts will be deleted because they're in a place they're not supposed to be in if you install them to either `/Library/Extensions` or `/System/Library/Extensions`. You should only install kexts to one of these locations if the author of the kexts tell you to do so.

To inject a kext, [mount your EFI]((../master/Tips.md#how-to-mount-efi)) and go to /EFI/EFI/Clover/kexts/Other and place your kext(s) in there. Also make sure that `InjectKexts` is set to `Yes` inside of your config.plist.

## How to know if you need to hot-patch DSDT
Download [IOREG](http://mac.softpedia.com/get/System-Utilities/IORegistryExplorer.shtml) and search for what a patch tells you to replace in it's comment.

- Example:
So let's say you want to rename HDAS to HDEF, please search if you even have HDEF first and if you do, this patch is not needed. If you do not have HDEF, apply the patch and reboot. You should now see HDEF in your IOREG

Be **very** careful while entering the patching info.

## Choosing a SMBIOS
There are a lot of SMBIOSes, you need to pick the correct one for your hardware. Here are some examples:
* iMac14,1 for Haswell (ix-4xxx) systems **without** a dgpu.
* iMac14,2 for Haswell (ix-4xxx) systems **with** a dgpu.
* iMac15,1 for Z97 motherboads.
* iMac17,1 for Skylake (ix-6xxx).
* iMac18,2 for Kaby-Lake (ix-7xxx) systems **without** a dgpu.
* iMac18,3 for Kaby-Lake (ix-7xxx) systems **with** a dgpu.
* iMac18,2 for Coffee-Lake (ix-8xxx) systems **without** a dgpu.
* iMac18,3 for Coffee-Lake (ix-8xxx) systems **with** a dgpu.
* MacPro6,1 for X99, X299, X399 motherboards.

## NvidiaGraphicsFixup and some SMBIOSes explained
Because of the way how vanilla iMacs work, a small piece of a kernel extension that comes with macOS needs to be modified to prevent a black screen on some SMBIOSes after booting. Here is the list of affected SMBIOSes:
* iMac15,1 and up (iMac17,1, iMac18,x)
* MacPro6,1

You do not have to manually modify anything inside of the kext that causes this issue since [lvs1974](https://github.com/lvs1974) made a kext, called [NvidiaGraphicsFixup](https://github.com/lvs1974/NvidiaGraphicsFixup), to patch this issue. You will need to install Lilu and NvidiaGraphicsFixup to apply this patch. You can download NvidiaGraphicsFixup and Lilu [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ).

NvidiaGraphicsFixup can do a lot of things:
* Adds the AGDP fix to iMac15,1;, iMac17,1;, iMac18,x and MacPro6,1 SMBIOSes to prevent a black screen after boot.
* Modifies macOS to recognize NVIDIA's web drivers as platform binaries. This resolves the issue with transparent windows without content, which appear for applications that use Metal and have Library Validation enabled. Common affected applications are iBooks and Little Snitch Network Monitor, though this patch is universal and fixes them all.
* Injects IOVARendererID into GPU properties (required for Shiki-based solution for non-freezing Intel and/or any discrete GPU)
* Allows to use ports HDMI, DP, Digital DVI with audio (Injects @0connector-type - @5connector-type properties into GPU)

## IntelGraphicsDVMTFixup
Quoted from [the IntelGraphicsDVMTFixup Github repo](https://github.com/BarbaraPalvin/IntelGraphicsDVMTFixup):
`
A common problem with Broadwell/Skylake/KabyLake is relatively small DVMT-prealloc setting by PC OEMs. The Apple framebuffer kexts generally assume 64mb or larger, and most PC OEMs use only 32mb. And often, there is no way to change it easily due to limited BIOS, locked down BIOS, etc.
`

In other words, this kext is meant for users who have now ay to change the pre-allocated DVMT.

This kext features the following:
* Fixes an issue related to a DVMT panic when entering the installation screen.
* Fixes the need for "FakeID = 0x12345678" in the config.plist.

You can download the latest compiled kext from [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ). How to install [here](../master/Tips.md#how-to-install-kexts)

## USBInjectAll
This kext injects all available USB ports to the OS. This is absolutely necessary when installing, you will get the `Still waiting for root device...` hang otherwise.

Only Intel controllers are currently supported and the most commonly used SMBIOS model identifiers are in the kext.

[link to repo](https://github.com/RehabMan/OS-X-USB-Inject-All)

Patches needed:
- Port limit patch (raw XML)
```plist
<dict>
    <key>Comment</key>
    <string>change 15 port limit to 26 in XHCI kext</string>
    <key>MatchOS</key>
    <string>10.13.x</string>
    <key>Name</key>
    <string>com.apple.driver.usb.AppleUSBXHCIPCI</string>
    <key>Find</key>
    <data>g32MEA==</data>
    <key>Replace</key>
    <data>g32MGw==</data>
</dict>
```

- Clover configurator friendly:
```
Comment: change 15 port limit to 26 in XHCI kext
Name:    com.apple.driver.usb.AppleUSBXHCIPCI
Find:    837d8c10
Replace: 837d8c1b
```

DSDT Patches (All of these are Clover Configurator friendly, raw patches [here](https://github.com/RehabMan/OS-X-USB-Inject-All/blob/master/config_patches.plist#L8-L53)):
(DISCLAIMER: These patches should only be used when they are needed. More info [here](../master/Tips.md#how-to-know-if-you-need-to-hot-patch-dsdt))

```
Comment: change _OSI to XOSI
Find:    5f4f5349
Replace: 584f5349
```

```
Comment: change EHC1 to EH01
Find:    45484331
Replace: 45483031
```

```
Comment: change EHC2 to EH02
Find:    45484332
Replace: 45483032
```

```
Comment: change XHCI to XHC
Find:    58484349
Replace: 5848435f
```

```
Comment: change XHC1 to XHC
Find:    58484331
Replace: 5848435f
```
