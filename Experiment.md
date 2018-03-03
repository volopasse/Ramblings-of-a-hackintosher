# Experiment test for hackintosh

## AptioMemoryFix & AptioInputFix explained

If you wanted to boot macos succesfully, you needed one of the following:

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
- Add some ACPI hotpatch: `HECI -> IMEI`, `GFX0 -> IGPU` 

### AMD

- Install Shiki.kext, WhateverGreen.kext, IntelGraphicsFixup.kext, Lilu.kext
- Add `shikigva=4`, `-rad4200` boot arg into config.plist
- Add some ACPI hotpatch: `HECI -> IMEI`, `GFX0 -> IGPU` , `PEGP -> GFX0` 
- Enable Inject Intel and add ig-platform-id of your iGPU to config.plist - Graphics
- Enable Integrated Graphics (a.k.a. iGPU), iGPU Multi-Monitor and set DVMT to 128M in BIOS/UEFI settings

### NVIDIA

- Install Shiki.kext, NvidiaGraphicsFixup.kext, IntelGraphicsFixup.kext, Lilu.kext
- Add `shikigva=6`, boot arg into config.plist
- Add some ACPI hotpatch: `HECI -> IMEI`, `GFX0 -> IGPU`
- Enable Inject Intel and add ig-platform-id of your iGPU to config.plist - Graphics
- Enable Integrated Graphics (a.k.a. iGPU), iGPU Multi-Monitor and set DVMT to 128M in BIOS/UEFI settings

After that, to check your hardware encoding working or not. [Download this](Stuff/VDADecoderChecker.zip) and run, if you seeing something like this

`Hardware acceleration is fully supported`

Then it's working

## Use older NVIDIA Web Driver for latest macOS

For some reason, NVIDIA causing latest Web Driver lag for Skylake and Kaby Lake users. To prevent it, we need to install older Web Driver and use it.

- First, [download this](https://github.com/corpnewt/Web-Driver-Toolkit/archive/master.zip)
- Then open Terminal, type `chmod +x Run.command`. Remember to point Run.command to your location you save it
- Now Ctrl + Right click, open it.



