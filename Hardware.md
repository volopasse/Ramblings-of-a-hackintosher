# Hardware

Follow this guide to pick a correct hardware part for your new Hackintosh.

## Motherboard:

- **Brand:** ASUS, ASRock, Gigabyte

  For MSI: There is some problem with MSI & OsxAptioFixDrv, better to stay away from it.

- **Chipset:** Intel 300/200/100/5/6/7/8/9-series

  X299: https://www.tonymacx86.com/threads/skylake-x-x299-live-the-future-now-on-macos-sierra-10-12-successful-build-extended-guide.229354/

  AMD: https://forum.amd-osx.com/viewforum.php?f=35

- **Audio codec:** Check out [this list](https://github.com/vit9696/AppleALC/wiki/Supported-codecs)

- **Network:** Almost any ethernet controller are supported like: 

  - Intel 82578 LC/DM/DC
  - Intel 82579 LM/V
  - Intel I217LM/V
  - Intel I218LM/V/LM2/V2/LM3
  - Intel I219V/LM/V2/LM2/LM3
  - Realtek RTL8111/8168 B/C/D/E/F/G/H
  - Qualcomm Atheros AR816x
  - Qualcomm Atheros AR817x
  - Qualcomm Atheros Killer E220x
  - Qualcomm Atheros Killer E2400
  - Qualcomm Atheros Killer E2500

  Stay away from mainboard have wifi/bt built-in, it's hard to make it working with macOS

- **Thunderbolt port:** Intel controller only

  Other controllers: Some report says ASMedia Thunderbolt controller working with macOS too, but I'm not 100% sure about it

- **USB port:** Use Intel controller to prevent sleep/wake problem


## CPU:

- **Core i3/i5/i7**: Native support to the latest 8th generation
- **Xeon/Core i9**
- **Pentium**: SpeedStep may not working properly and you will need to FakeCPUID to make it boot
- **AMD**: You may want to check [this](https://forum.amd-osx.com/viewforum.php?f=35)


## Storage:

- **SATA**
- **NVMe/PCI-e**: native support since macOS 10.13, need some patch if you use macOS 10.12


## GPU/iGPU:

- **Intel**:
  - Intel UHD 630
  - Intel HD 630
  - Intel HD 530
  - Intel HD 6000+
  - Intel HD 4600+
  - Intel HD 4000
  - Intel HD 3000

- **NVIDIA**:
  - 6-series and older may have some native support from Apple
  - 7-series and newer may need to use Web Driver for it, some card like GT 710 has native support from Apple

  ASUS GTX 750TI problem: https://www.tonymacx86.com/threads/successful-yosemite-install-with-asus-gtx-750-ti-but-with-hdmi-not-working-on-nvidia-web-drivers-3.148657/

  GTX 1060 problem: https://www.tonymacx86.com/threads/05-02-added-temporary-fix-pascal-gtx-1060-glitching-after-waking-from-sleep.220670/

- **AMD**: https://www.tonymacx86.com/threads/radeon-compatibility-guide-ati-amd-graphics-cards.171291/


## Mouse/keyboard:

Better to use Logitech or Apple input device to prevent sleep/wake problem, some keyboard from Corsair,... may prevent sleep on macOS

## Wi-Fi/Bluetooth card:

- **Fenvi FV-T919**: https://www.aliexpress.com/item/Fenvi-FV-T919-802-11AC-Desktop-Wifi-Card-802-11-A-B-G-N-AC-BCM94360CD/32778371977.html
- **BCM94360CS2**: https://www.ebay.com/itm/BT4-0-BCM94360CS2-PCI-E-867Mbps-802-11AC-Dual-Band-Wifi-PCI-Express-Adapter-Card/361828095572
- **BCM94360CD**: https://www.amazon.com/PC-Hackintosh-Continuity-BCM94360CD-Bluetooth/dp/B012LOT512/
- **BCM94352Z** (for M.2 port, mostly laptop): https://www.ebay.com/itm/Broadcom-BCM94352Z-M-2-NGFF-802-11AC-867Mbps-BT-4-0-DW1560-for-Mac-Hackintosh-/252319175707

