# AppleALC for audio

This file will be focused around setting up audio.

## Necessities:
* AppleALC & Lilu (both can be downloaded from [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ))
* Your codec
* [Clover Configurator](http://mackie100projects.altervista.org/download-mac.php?version=classic)
* A mounted EFI partition (howto [here](../master/Tips.md#how-to-mount-efi))

## Cleanup
If you tried **anything** for audio before you tried this, we need to remove old audio attempts first.

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

Remove any AppleHDA related KextsToPatch entry.

## Installing the kexts
First of all, check if your codec is supported [here](https://github.com/vit9696/AppleALC/wiki/Supported-codecs), if it is, write down the layout(s) for your codec. (Most codecs support layout 1.)

Install both to kexts/other. How to [here](../master/Tips.md#how-to-mount-efi). Make sure that you're injecting kexts. (more info on installing kexts [here](../master/Tips.md#how-to-install-kexts))

Open your config.plist with [Clover Configurator](http://mackie100projects.altervista.org/download-mac.php?version=classic) and go to Devices > Audio. You will see a box with a down arrow. In that box you want to enter the layout for your codec and restart. 

After restart, go to System Preferences > Sound > Output. You should see output devices, here's an example of what you should see:
* Internal Speakers
* Line out
* Line out
* Digital Out

## Troubleshooting
If you see them but audio is not working, try one of the different layouts that corresponds to your codec.

If you don't see any audio devices at all. Download [IOREG](http://mac.softpedia.com/get/System-Utilities/IORegistryExplorer.shtml) and search for `HDEF`. If you don't get any results, search for `HDAS` and `AZAL`.

If you get a result with either, go to the ACPI section and click the `List Of Patches` dropdown button. Select either `change AZAL to HDEF` or `change HDAS to HDEF`. Reboot and see if audio devices are present and audio output is working.

If you have a X99 board, search for ALZA in IOREG. If you get a result, add the following DSDT patch in Clover Configurator:

```
Comment: change ALZA to HDEF
Find:    414c5a41
Replace: 48444546
```

Reboot and check if you have audio.

If you cannot have audio, contact me (camiel) on the hackintosh server. My mention is `@camiel#9084`.