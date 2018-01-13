# AppleALC for audio

This file will be focused around setting up audio.

## Necessities:
* AppleALC & Lilu (both can be downloaded from [here](https://1drv.ms/f/s!AiP7m5LaOED-mo9XA4Ml-69cwAsikQ))
* Your codec

First of all, check if your codec is supported [here](https://github.com/vit9696/AppleALC/wiki/Supported-codecs), if it is, write down the layout(s) for your codec. (Most codecs support layout 1.)

Install both to kexts/other. How to [here](../master/Tips.md#how-to-mount-efi).

Open your config.plist with [Clover Configurator](http://mackie100projects.altervista.org/download-mac.php?version=classic) and go to Devices > Audio. You will see a box with a down arrow. In that box you want to enter the layout for your codec and restart. 

After restart, go to System Preferences > Sound > Output. You should see output devices, here's an example of what you should see:
* Internal Speakers
* Line out
* Line out
* Digital Out

If you see them but audio is not working, try one of the different layouts that corresponds to your codec.

If you don't see any audio devices at all. Download [IOREG](http://mac.softpedia.com/get/System-Utilities/IORegistryExplorer.shtml) and search for `HDEF`. If you don't get any results. Search for the following:
* HDAS
* AZAL

If you get a result with either, go to the ACPI section and click the `List Of Patches` dropdown button. Select either `change AZAL to HDEF` or `change HDAS to HDEF`. Reboot and see if audio devices are present and audio output is working.