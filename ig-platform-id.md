# ig-platform-id list

### Notes:

- Some Apple products using Sandy Bridge CPU with higher version of Intel HD, same thing with Haswell (Apple magic?)
- Coffee Lake need some FakePCIID and using Kaby Lake ig-platform-id because Apple don't have any Coffee Lake product

## Sandy Bridge

- **0x00010000**: MacBookPro8,1 - Intel HD Graphics 3000 - VRAM: 384MB/512MB, Port Index: 01020400, Port Count: 4, Connector: LVDS1/DP3, BL: 0x0710
- **0x00020000**: MacBookPro8,2/MacBookPro8,3 - Intel HD Graphics 3000 - VRAM: 384MB/512MB, Port Index: 01020100, Port Count: 1, Connector: LVDS1, BL: 0x0710
- **0x00030010**: Macmini5,1 - Intel HD Graphics 3000 - VRAM: 384MB/512MB, Port Index: 00020300, Port Count: 3, Connector: HDMI1/DP2, BL:
- **0x00030020**: Macmini5,3 - Intel HD Graphics 3000 - VRAM: 384MB/512MB, Port Index: 01030400, Port Count: 4, Connector: HDMI1/DP3, BL: 0x0710
- **0x00040000**: MacBookAir4,1/MacBookAir4,2 - Intel HD Graphics 3000 - VRAM: 384MB/512MB, Port Index: 01020300, Port Count: 3, Connector: LVDS1/DP2, BL: 0x0710
- **0x00050000**: Intel HD Graphics 3000 - VRAM: 384MB/512MB, Port Index: 00020100, Port Count: 1, Connector: DP1, BL:

## Ivy Bridge

- **0x01660000**: Intel HD Graphics 4000 - Port Count: 4, Pipes: 3, BIOS-allocated memory: 96MB, FBM(cursor): 24MB, VRAM: 1024MB, Connector: LVDS1/DP3, BL: 0x0710
- **0x01660001**: MacBookPro10,2 - Intel HD Graphics 4000 - Port Count: 4, Pipes: 3, BIOS-allocated memory: 96MB, FBM(cursor): 24MB, VRAM: 1536MB, Connector: LVDS1/DP2/HDMI1, BL: 0x0710
- **0x01660002**: MacBookPro10,1 - Intel HD Graphics 4000 - Port Count: 1, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 24MB, VRAM: 1536MB, Connector: LVDS1, BL: 0x0710
- **0x01660003**: MacBookPro9,2 - Intel HD Graphics 4000 - Port Count: 4, Pipes: 2, BIOS-allocated memory: 64MB, FBM(cursor): 16MB, VRAM: 1536MB, Connector: LVDS1/DP3, BL: 0x0710
- **0x01660004**: MacBookPro9,1 - Intel HD Graphics 4000 - Port Count: 1, Pipes: 1, BIOS-allocated memory: 32MB, FBM(cursor): 16MB, VRAM: 1536MB, Connector: LVDS1, BL: 0x0710
- **0x01620005**: Intel HD Graphics 4000 - Port Count: 3, Pipes: 2, BIOS-allocated memory: 32MB, FBM(cursor): 16MB, VRAM: 1536MB, Connector: DP3, BL: 0x0710
- **0x01620006**: iMac13,1 - Intel HD Graphics 4000 - Port Count: 0, Pipes: 0, BIOS-allocated memory: 0MB, FBM(cursor): 0MB, VRAM: 1MB, Connector:, BL: 0x0710
- **0x01620007**: iMac13,2 - Intel HD Graphics 4000 - Port Count: 0, Pipes: 0, BIOS-allocated memory: 0MB, FBM(cursor): 0MB, VRAM: 1MB, Connector:, BL: 0x0710
- **0x01660008**: MacBookAir5,1 - Intel HD Graphics 4000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 34MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x0710
- **0x01660009**: MacBookAir5,2 - Intel HD Graphics 4000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 34MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x0710
- **0x0166000a**: Macmini6,1 - Intel HD Graphics 4000 - Port Count: 3, Pipes: 2, BIOS-allocated memory: 32MB, FBM(cursor): 32MB, VRAM: 1536MB, Connector: DP2/HDMI1, BL: 0x0710
- **0x0166000b**: Macmini6,2 - Intel HD Graphics 4000 - Port Count: 3, Pipes: 2, BIOS-allocated memory: 32MB, FBM(cursor): 34MB, VRAM: 1536MB, Connector: DP2/HDMI1, BL: 0x0710

## Haswell

- **0x04160000**: Intel HD Graphics 4600 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 16MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x0a160000**: Intel HD Graphics 4400 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 16MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x0ad9
- **0x04260000**: Intel HD Graphics 5000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 16MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x0a260000**: Intel HD Graphics 5000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 16MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x0ad9
- **0x0d260000**: Intel Iris Pro Graphics 5200 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 16MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x0d220003**: iMac14,1/iMac14,4 - Intel Iris Pro Graphics 5200 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 32MB, FBM(cursor): 19MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x1499
- **0x04120004**: Intel HD Graphics 4600 - Port Count: 0, Pipes: 0, BIOS-allocated memory: 32MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector:, BL:
- **0x0a260005**: Intel HD Graphics 5000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 32MB, FBM(cursor): 19MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x0ad9
- **0x0a260006**: MacBookAir6,1/MacBookAir6,2/Macmini7,1 - Intel HD Graphics 5000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 32MB, FBM(cursor): 19MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x0ad9
- **0x0d260007**: MacBookPro11,2/MacBookPro11,3 - Intel Iris Pro Graphics 5200 - Port Count: 4, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 34MB, VRAM: 1536MB, Connector: LVDS1/DP2/HDMI1, BL: 0x07a1
- **0x0a2e0008**: MacBookPro11,1 - Intel Iris Graphics 5100 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 64MB, FBM(cursor): 34MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x0412000b**: iMac15,1 - Intel HD Graphics 4600 - Port Count: 0, Pipes: 0, BIOS-allocated memory: 32MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector:, BL:

## Broadwell

- **0x16160000**: Intel HD Graphics 5500 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 16MB, FBM(cursor): 15MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x161e0000**: Intel HD Graphics 5300 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 16MB, FBM(cursor): 15MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x16220000**: Intel Iris Pro Graphics 6200 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 16MB, FBM(cursor): 15MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x16260000**: Intel HD Graphics 6000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 16MB, FBM(cursor): 15MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x162b0000**: Intel Iris Graphics 6100 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 16MB, FBM(cursor): 15MB, VRAM: 1024MB, Connector: LVDS1/eDP1/HDMI1, BL: 0x1499
- **0x161e0001**: MacBook8,1 - Intel HD Graphics 5300 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x16160002**: Intel HD Graphics 5500 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x16220002**: Intel Iris Pro Graphics 6200 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x16260002**: Intel HD Graphics 6000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x162b0002**: MacBookPro12,1 - Intel Iris Graphics 6100 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x16120003**: Intel HD Graphics 5600 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x07a1
- **0x16260004**: Intel HD Graphics 6000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x1499
- **0x162b0004**: Intel Iris Graphics 6100 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x1499
- **0x16260005**: Intel HD Graphics 6000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x0ad9
- **0x16260006**: iMac16,1/MacBookAir7,1/MacBookAir7,2 - Intel HD Graphics 6000 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x0ad9
- **0x16220007**: iMac16,2 - Intel Iris Pro Graphics 6200 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 38MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x1499
- **0x16260008**: Intel HD Graphics 6000 - Port Count: 2, Pipes: 2, BIOS-allocated memory: 34MB, FBM(cursor): 34MB, VRAM: 1536MB, Connector: LVDS1/DP1, BL: 0x1499
- **0x162b0008**: Intel Iris Graphics 6100 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x1499

## Skylake

- **0x19120000**: Intel HD Graphics 530 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: DP3, BL: 0x056c
- **0x19160000**: Intel HD Graphics 520 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x19260000**: Intel Iris Graphics 540 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x19270000**: Intel Iris Graphics 550 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x191b0000**: MacBookPro13,3 - Intel HD Graphics 530 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x191e0000**: Intel HD Graphics 515 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x193b0000**: Intel Iris Pro Graphics 580 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP1/HDMI1, BL: 0x056c
- **0x19120001**: iMac17,1 - Intel HD Graphics 530 - Port Count: 0, Pipes: 0, BIOS-allocated memory: 0MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector:, BL:
- **0x19160002**: Intel HD Graphics 520 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 57MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x19260002**: MacBookPro13,1 - Intel Iris Graphics 540 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 57MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x191e0003**: MacBook9,1 - Intel HD Graphics 515 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x19260004**: Intel Iris Graphics 540 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x19270004**: MacBookPro13,2 - Intel Iris Graphics 550 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x191b0006**: Intel HD Graphics 530 - Port Count: 1, Pipes: 1, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1, BL: 0x056c
- **0x19260007**: Intel Iris Graphics 540 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c

## Kaby Lake

- **0x59120000**: Intel HD Graphics 630 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: DP3, BL: 0x056c
- **0x59160000**: Intel HD Graphics 620 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP1/HDMI1, BL: 0x056c
- **0x59260000**: Intel Iris Plus Graphics 640 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x59270000**: Intel Iris Plus Graphics 650 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x591b0000**: MacBookPro14,3 - Intel HD Graphics 630 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP1/HDMI1, BL: 0x056c
- **0x591e0000**: Intel HD Graphics 615 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 34MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x59230000**: Intel HD Graphics 635 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x591e0001**: MacBook10,1 - Intel HD Graphics 615 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x59260002**: MacBookPro14,1/iMac18,1 - Intel Iris Plus Graphics 640 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 57MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x59120003**: iMac18,2/iMac18,3 - Intel HD Graphics 630 - Port Count: 0, Pipes: 0, BIOS-allocated memory: 0MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector:, BL: 0x056c
- **0x59270004**: MacBookPro14,2 - Intel Iris Plus Graphics 650 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 57MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x591b0006**: Intel HD Graphics 630 - Port Count: 1, Pipes: 1, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1, BL: 0x056c
- **0x59260007**: Intel Iris Plus Graphics 640 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 57MB, FBM(cursor): 21MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c
- **0x59270009**: Intel Iris Plus Graphics 650 - Port Count: 3, Pipes: 3, BIOS-allocated memory: 38MB, FBM(cursor): 0MB, VRAM: 1536MB, Connector: LVDS1/DP2, BL: 0x056c