# SMBIOS

Choosing SMBIOS for your system is very important, each SMBIOS has different power managment, feature, graphics policy,...

Booting with wrong SMBIOS can causing kernel panic,...

## What SMBIOS should you use? 

You can open Clover Configurator - SMBIOS, click to the button on the left side and it will show up all SMBIOS. Pick the one same with your CPU family, for example:

- If I have i3/i5/i7-7xxx, you should use iMac18,1/2/3. All of them using Kaby Lake CPU Family so it'll be correct. Same thing with older CPU family & older SMBIOS
- For laptop, some have U, M, QM family. If you have i3-7100U, you should use MacBookPro14,1/2. If you have i7-7xxxHQ, you should use MacBookPro14,3. Same thing with older CPU family & older SMBIOS
- For newer CPU family that Apple didn't use for their product yet, Coffee Lake. You can use latest iMac or MacBookPro just fine

## Notes:

- **iMac15,1**, **iMac17,1**, **MacPro 6,1**: For some reason, Apple graphics policy kext not allow those SMBIOS to use NVIDIA GPU. This has been fixed by NvidiaGraphicsFixup.kext
- If your series number not matching with your SMBIOS, your system won't boot. Clover Configurator always generate correct series number for your SMBIOS.
- Apple will save your SMBIOS information into your iCloud account if you login with your account, make sure you logout any service before changing SMBIOS