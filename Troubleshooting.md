# Common problems when installing Web Drivers

## Black screen
You should use other display cable/other output port on your GPU (tested with some cases, and happened with me too)

Check [this if you using NVIDIA GPU](Tips.md#nvidiagraphicsfixup-and-some-smbioses-explained)

## NVIDIA Web drivers not apply after reboot
If you have NvidiaWeb checked in your config and webdrivers are still not working, try the following:

- Open Terminal and do the following one line at a time:
  - `sudo -s`
  - `nvram -c`
  - `nvram myvar=test`
  - `exit`
- Reboot
- Open Terminal and do `nvram -p | grep -i myvar`

If you don't get any output fromt the last command, install EmuVariableUefi-64.efi and the RC Scripts via the [latest clover install package](https://github.com/Dids/clover-builder/releases/latest/).

For some case, you need to remove -v boot flag if you using High Sierra in order to apply NVIDIA Web Driver.

## Massive ACPI kernel panic on Gigabyte boards
You can fix this by dropping the MATS table in your config.plist. Open your config.plist with Clover Configurator and Go to ACPI > Drop Tables (bottom left). Click the + button and set Signature to `MATS`.
