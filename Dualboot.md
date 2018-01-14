# Dual Boot

## Dual Boot on Same Drives

#### macOS -> Windows

When you have a working macOS with Clover Bootloader and you want to install Windows on it. You just need to create a partition for Windows and install, easy.

1. Open Disk Utility.app.

   (If you using macOS 10.13 and up, click to View - Show other drives) 

2. Click to your drive then click to Partition button.

3. Add another partition for Windows, then format it to Mac OS Extended (Journaled).

4. Boot into Windows installer, [delete the partition that you just format to Mac OS Extended filesystem](https://i.imgur.com/wmlhIJs.png).

5. Then install on that free space, Windows will override boot priority when install. You can fix it later.

####Windows -> macOS####

When you want to install macOS without losing Windows data. You need to re-size EFI partition to 300MBs, then you can install macOS or Disk Utility will fail.

1. Download your favorite partition tool. (I'll use [MiniTool Partition Wizard](https://www.partitionwizard.com/free-partition-manager.html))
2. Normally, Windows will create EFI partition with only 100MBs. [You will need to re-size to 300MBs, learn how to do that with Mini Partition Wizard.](https://www.partitionwizard.com/help/resize-partition.html)
3. Create a partition for macOS and format to NTFS, macOS can't create a partition from free space so you have to do it now.
4. Now boot into macOS installer with Clover Bootloader, use Disk Utility.app erase that partition
5. Exit Disk Utility.app and install macOS.
6. After that if you want to install Clover Bootloader to hard drive, you have to use Clover Bootloader package to install (not copy EFI folder) or Windows EFI will be broken

## Dual Boot on Separate Drives 

update....