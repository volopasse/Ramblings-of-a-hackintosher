# Tips
## How to mount EFI
Open Terminal and run `diskutil list`, this will show you all your available Volumes. Look up your disk's name and remember the disk identifier that corresponds with your disk (this should look something like diskX). Once you're sure you have the right disk identifier that corresponds with your disk, run `diskutil mount diskXs1`, with the X being your disk number.

If you have only one EFI partition, you can also run `diskutil mount EFI`.

## How to install kexts
A small disclaimer first, please try to inject kexts whenever you can. There is a possibility that if you update, your kexts will be deleted because they're in a place they're not supposed to be in if you install them to either `/Library/Extensions` or `/System/Library/Extensions`. You should only install kexts to one of these locations if the author of the kexts tell you to do so.

To inject a kext, [mount your EFI]((../master/Tips.md#how-to-mount-efi)) and go to /EFI/EFI/Clover/kexts/Other and place your kext(s) in there. Also make sure that `InjectKexts` is set to `Yes` inside of your config.plist.

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

You do not have to manually modify anything inside of the kext that causes this issue since [lvs1974](https://sourceforge.net/projects/nvidiagraphicsfixup/) made a kext, called NvidiaGraphicsFixup, to patch this issue. You will need to install Lilu and NvidiaGraphicsFixup to apply this patch. You can download NvidiaGraphicsFixup and Lilu [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ).

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