# Power Management

Native macOS power management delivers the best combination of processor and graphics performance and efficiency. 

## Necessities:
* A CPU 
* A XCPM enabling SSDT
* A compatible System Definition (SMBIOS) 

Native power management does not require specific BIOS settings or anything more than installing one power management ssdt.

To be clear, native power management is not mandatory. The consequences are not severe. Performance is similar, however, higher temps (~10 C), more power (5-10 W) and sleep problems are likely.

So there's 2 ways to fix Power Management.

**For Haswell to latest generation Intel CPU (desktop only):**

- **Requirements**

  - Clover Bootloader v4307 and newer

    Enable PluginType in config.plist - ACPI - SSDT - Generate - PluginType

    [PluginType](https://i.imgur.com/0ut6Ule.png)

- **Notes**

  - Broadwell/5xxx - frequency vectors required
    - https://github.com/Piker-Alpha/freqVectorsEdit.sh
  - 9 Series/LPC
    - https://github.com/toleda/audio_hdmi_9series/blob/master/ssdt_lpc/ssdt_lpcb-9series.zip
  - System Definition/macpro6,1: socket LGA 2011 only

**For Ivy Bridge or older generation Intel CPU or laptop CPU:**

Piker Alpha's [ssdtPRGen](https://github.com/Piker-Alpha/ssdtPRGen.sh) script will generate a SSDT you can use to achieve the maximum amount of power states for your desktop CPU.

- **Requirements:**

  - Working internet connection

- **How to generate a SSDT by ssdtPRGen.sh**

  1. Configure system with appropriate SMBIOS for your CPU using Clover Configurator

  2. Open Terminal and download Piker Alpha's ssdtPRGen.sh by this command

     ```
     curl -o ~/ssdtPRGen.sh https://raw.githubusercontent.com/Piker-Alpha/ssdtPRGen.sh/Beta/ssdtPRGen.sh
     ```

  3. This will download ssdtPRGen.sh to your home directory (~) and the next step is to change the permissions of the file (add +x) so that it can be run.

     ```
     chmod +x ~/ssdtPRGen.sh
     ```

  4. For default SSDT generation, run this command

     ```
     sudo ~/ssdtPRGen.sh
     ```

  5. If ssdtPRGen.sh ask you to open SSDT, enter N

  6. Use Finder and find ~/Library/ssdtPRGen/SSDT.aml

  7. Now [mount your EFI partition](https://github.com/camielverdult/Ramblings-of-a-hackintosher-High-Sierra/blob/master/Tips.md#how-to-mount-efi), and copy SSDT.aml to /EFI/Clover/ACPI/patched

     NOTE: The Power Management SSDT should always be SSDT.aml. If you have an SSDT.aml there already, rename it SSDT-1.aml, etc...

  8. Reboot
