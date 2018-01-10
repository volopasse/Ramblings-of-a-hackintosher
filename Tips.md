# Tips

## How to mount EFI
Open Terminal and run `diskutil list`, this will show you all your available Volumes. Look up your disk's name and remember the disk identifier that corresponds with your disk (this should look something like diskX). Once you're sure you have the right disk identifier that corresponds with your disk, run `diskutil mount diskXs1`, with the X being your disk number.

If you have only one EFI partition, you can also run `diskutil mount EFI`.

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