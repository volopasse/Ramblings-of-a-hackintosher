# Power Management

Native macOS power management delivers the best combination of processor and graphics performance and efficiency. 

Native power management does not require you to change specific BIOS settings. You will only need to instal one power management ssdt.

Power management is not a must, however, working power management will result in lower temps and less energy usage.

## For Haswell or newer (desktop only)
This only work on Clover v4307 or newer.

Open your config.plist in Clover Configurator and go to the ACPI section. In there, under SSDT (bottom left), check PluginType.

![alt text](../master/Pictures/PluginType.png)

## For Ivy Bridge or older generation Intel CPUs or laptops:

Piker Alpha's [ssdtPRGen](https://github.com/Piker-Alpha/ssdtPRGen.sh) script will generate a SSDT you can use to achieve the maximum amount of power states for your desktop CPU.

### How to generate a SSDT with ssdtPRGen.sh

1. Setup your valid config.plist with the appropriate SMBIOS for your CPU using Clover Configurator.

2. Open Terminal and download Piker Alpha's ssdtPRGen.sh with the following command:

```
curl -o ~/ssdtPRGen.sh https://raw.githubusercontent.com/Piker-Alpha/ssdtPRGen.sh/Beta/ssdtPRGen.sh
```

3. The next step is to change the permissions of the executable so that it can be run.

```
chmod +x ~/ssdtPRGen.sh
```

4. For default SSDT generation, run this command:

```
sudo ~/ssdtPRGen.sh
```

5. If ssdtPRGen.sh ask you to open the generated SSDT in Finder, enter N.

6. Use Finder and find ~/Library/ssdtPRGen/SSDT.aml

7. Mount your EFI partition (howto [here](/..master/Tips.md#how-to-mount-efi)) and copy the generated SSDT.aml to /EFI/Clover/ACPI/patched.

NOTE: The Power Management SSDT should always be SSDT.aml. If you have an SSDT.aml there already, rename it SSDT-1.aml, etc...

8. Reboot
