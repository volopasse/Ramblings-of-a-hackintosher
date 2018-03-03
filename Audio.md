# Audio

This file will be focused around setting up audio.

## Necessities:
* `AppleALC.kext` & `Lilu.kext`
* Your codec (you can get this from your motherboard's specification page)
* [Clover Configurator](http://mackie100projects.altervista.org/download-clover-configurator/)
* A mounted EFI partition (how to [here](Tips.md#how-to-mount-efi))

## Remove old audio patch
If you tried **anything** for audio before you tried this, we need to remove old audio attempts first.

If you don't want to touch your system file or have some free time, re-install macOS to remove old audio patch is a better way

We're looking for:
* realtekALC.kext
* CloverALC.kext
* VoodooHDA.kext
* HDA Blocker.kext
* HDAEnabler#.kext (# being a layout)
* AppleALC

Look in the following directories for these:
* /Library/Extensions/
* /System/Library/Extensions/
* In /EFI/EFI/Clover/kexts/, /10.xx (10.9, 10.10, etc.) and /other

Once you're sure that you are totally clean kext-wise, we are going to clean the config.plist. Open your config.plist and remove the following patches from KextsToPatch (all are clover configurator friendly):

```
Comment: 10.11-AppleHDA/Realtek ALC...
Name:    AppleHDA
Find:    8319d411
Replace: 00000000
```

```
Comment: 10.9-10.11-AppleHDA/Realtek ALC1150
Name:    AppleHDA
Find:    8b19d411
Replace: 0009ec10
```

```
Comment: AppleHDA/Resources/xml&gt;zml
Name:    AppleHDA
Find:    786d6c2e7a6c
Replace: 7a6d6c2e7a6c
```

Remove any AppleHDA, VoodooHDA,... related KextsToPatch entry.

## Installing the kexts
First of all, check if your codec is supported [here](https://github.com/vit9696/AppleALC/wiki/Supported-codecs), if it is, write down the layout(s) for your codec.

Install both to kexts/other. How to [here](Tips.md#how-to-mount-efi). Make sure that you're injecting kexts. (more info on installing kexts [here](Tips.md#how-to-install-kexts))

Open your config.plist with [Clover Configurator](http://mackie100projects.altervista.org/download-clover-configurator/) and go to Devices > Audio. You will see a box with a down arrow. In that box you want to enter a supported layout that works with your audio codec. Save and restart. 

After restart, go to System Preferences > Sound > Output. You should see output devices, here's an example of what you should see:

![alt text](Pictures/Audio%20Devices.png)

## Troubleshooting
If you see them but audio is not working, too loud or you can't hear it. Try one of the different layouts that corresponds to your codec.

If you don't see any audio devices at all. Download [IOJones](https://sourceforge.net/projects/iojones/) and search for `HDEF`. If you don't get any results, search for `HDAS` and `AZAL`.

If you get a result with either, go to the ACPI section and click the `List Of Patches` dropdown button. Select either `change AZAL to HDEF` or `change HDAS to HDEF` based on what was found in your IOREG and what was not. Reboot and see if audio devices are present and audio output is working.

Reboot and check if you have audio.

If you have a X99 board, search for ALZA in IOREG. If you get a result, add the following DSDT patch in Clover Configurator:

```
Comment: change ALZA to HDEF
Find:    414c5a41
Replace: 48444546
```

Reboot and check if you have audio.
