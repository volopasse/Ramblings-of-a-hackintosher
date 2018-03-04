# Experiment test for hackintosh

## AptioMemoryFix & AptioInputFix

If you wanted to boot macOS succesfully, you needed one of the following:

- OsxAptioFix
- OsxAptioFix**2**
- OsxAptioFix-Free2000 (generally used with X99)

These fixed some issues with the macos kernel and memory.

There's now is a new EFI driver to replace OsxAptioFix2, called AptioMemoryFix. It shims the AMI Keycode protocol onto the Apple KeyMap protocols and fixes the global timer to prevent pointer coordinate overflows. This *should* also cure NVRAM in most cases.

I really, **really** recommend you to use this new driver. The old ones are busted and do not provide the level of patching this one brings.

Here's some advice about the new driver by someone who knows how it works: (Credits to Reddestdream)

![alt text](Pictures/The%20new%20hotness.png)

Remember to remove old efi driver when using the new one. And if you can't booting when using this new efi driver then you should use the old one.

### Sounds good! Where do I get it?

AptioMemoryFix and AptioInputFix are both able to be installed via the clover install package (latest [here](https://github.com/Dids/clover-builder/releases/latest)).

You can take a look at [the repo on github](https://github.com/vit9696/AptioFixPkg) for more information.

## VT-d

For some reason, I was able to enable VT-d on macOS 10.13 which it's not working and causing kernel panic on macOS 10.12.

To enable it, you need to remove DMAR drop table in config.plist - ACPI - Drop Tables. Remove dart=0 boot flag if you have, and enable VT-d in BIOS/UEFI settings

After that use [IOJones](https://sourceforge.net/projects/iojones/), search for AppleVTD. If you found that and it's working now.

If you got kernel panic after enable VT-d, try to disable it. It's not working with every machine yet!

## Enable hardware encoding

You may can playing normal video, audio,... But with DRM content like iTunes movies, Apple Music,... Some will not working because your iGPU/dGPU can't working with those DRM content. Also this will fix rendering issue on Final Cut Pro X

This guide only working on macOS 10.13, older macOS/OS X can causing black screen,...

### iGPU

- Install Shiki.kext, IntelGraphicsFixup.kext, Lilu.kext
- Add `shikigva=1` boot arg into config.plist
- Add `-disablegfxfirmware` if you using Skylake or up
- Enable Inject Intel and add [ig-platform-id](ig-platform-id.md) to config.plist - Graphics
- Add some [ACPI hotpatch](https://github.com/piiiggg/Ramblings-of-a-hackintosher-High-Sierra/blob/master/Tips.md#how-to-know-if-you-need-to-hot-patch-dsdt): `HECI -> IMEI`, `GFX0 -> IGPU` 

### AMD

- Install Shiki.kext, WhateverGreen.kext, IntelGraphicsFixup.kext, Lilu.kext
- Add `shikigva=4`, `-rad4200` boot arg into config.plist
- Add some [ACPI hotpatch](https://github.com/piiiggg/Ramblings-of-a-hackintosher-High-Sierra/blob/master/Tips.md#how-to-know-if-you-need-to-hot-patch-dsdt): `HECI -> IMEI`, `GFX0 -> IGPU`
- Enable Inject Intel and add [ig-platform-id](ig-platform-id.md) to config.plist - Graphics
- Add `-disablegfxfirmware` if you using Skylake or up
- Enable Integrated Graphics (a.k.a. iGPU), iGPU Multi-Monitor and set DVMT to 128M in BIOS/UEFI settings

### NVIDIA

- Install Shiki.kext, NvidiaGraphicsFixup.kext, IntelGraphicsFixup.kext, Lilu.kext
- Add `shikigva=60`, boot arg into config.plist
- Add some [ACPI hotpatch](https://github.com/piiiggg/Ramblings-of-a-hackintosher-High-Sierra/blob/master/Tips.md#how-to-know-if-you-need-to-hot-patch-dsdt): `HECI -> IMEI`, `GFX0 -> IGPU`
- Enable Inject Intel and add [ig-platform-id](ig-platform-id.md) to config.plist - Graphics
- Add `-disablegfxfirmware` if you using Skylake or up
- Enable Integrated Graphics (a.k.a. iGPU), iGPU Multi-Monitor and set DVMT to 128M in BIOS/UEFI settings

After that, to check your hardware encoding working or not. [Download this](Stuff/VDADecoderChecker.zip) and run, if you seeing something like this

`Hardware acceleration is fully supported`

Then it's working

## Patching older NVIDIA Web Driver

For some reason, latest NVIDIA Web Driver causing lag on Skylake and Kaby Lake systems. To prevent it, we need to install older Web Driver and use it.

Also, when Apple releases an update for macOS. You don't need to wait till NVIDIA release their Web Driver, you can patch older Web Driver and use it.

- You need to disable SIP first, config.plist - Rt Variables - CsrActiveConfig - 0x67 - Save & reboot.
- Then, [download this](https://github.com/corpnewt/Web-Driver-Toolkit/archive/master.zip) and unzip 
- Open Terminal, type `chmod +x Run.command`. Remember to point `Run.command` to your location you save it
- Now Ctrl + Right click, open it.
- You need to remove any Web Drivers you was install to your hack first, press `R` and go
- After removed, download older Web Driver. Press `S` then type this build number `17C2205` 
- Wait till it's done, press `I` then press `Yes` then `Set To Current Build Number`
- Drag and drop your older installer into Terminal
- After patching it, install the patched installer then reboot. 
- Now open `Run.command` again, press `P` and `Set to Current Build Number`
- Wait till it's done and reboot again. Now older Web Driver should working!
- Disable Automatically check for updates on NVIDIA Driver Manager.



