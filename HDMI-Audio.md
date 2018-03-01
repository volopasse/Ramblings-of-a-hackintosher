# HDMI Audio

***Notes:***

- OS X/macOS does not provide HDMI audio controls (No volume, no mute, no balance, etc.)
- The connected HDMI device (TV, receiver, etc.) provides any and all audio controls

## AMD

For AMD user, upgrade to macOS 10.13 for best native kext support from Apple to enable HDMI/DP audio.

**Requirements:**

- WhateverGreen.kext, Lilu.kext installed
- config.plist - Graphics - RadeonDeInit (For some AMD GPU only)

## NVIDIA

**Requirements:**

- NvidiaGraphicsFixup.kext, Lilu.kext installed
- config.plist - System Parameters - NvidiaWeb (For 10xx/9xx/750/750Ti)

**Notes:**

- Nvidia **10xx/web driver**; no HDMI audio on HDMI port after boot. Try all DP connectors and/or DP/DVI -  HDMI or DVI - HDMI adapters for HDMI audio (4K@60 HDMI requires active DP adapter)
- macOS only supports video on one HDMI port on a Nvidia graphics card with more than one HDMI port. Use DP - HDMI or DVI - HDMI adapters for multiple HDMI displays (4K@60 HDMI requires active DP adapter).
- GTS 450, GTX 550/550ti, GTX 560/560ti; no native support

**For 550/550ti: Patch AppleHDA binary:**

- Find: 14 00 de 10
- Replace: 15 00 de 10

**For 560/560ti/Quadro 4000: Patch AppleHDAController binary:**

- Find: de 10 ea 0b
- Replace: de 10 e5 0b

## iGPU

**Requirements:**

- IntelGraphicsFixup.kext, Lilu.kext installed
- config.plist - Graphics - Inject Intel
- config.plist - Graphics - ig-platform-id (Pick the correct one for your iGPU)

**Notes:**

- HD 540: System Preferences/Sound/Output; HDMI shows as DP, DP shows as HDMI
- HD 540: Supports 1x display, boot fails with 2x display; 2nd display hot plug works
- HD 4600/HD 4400/Mobile - no native support ([check this](https://www.tonymacx86.com/threads/fix-hd4200-hd4400-hd4600-hd5600-on-10-11.175797/))
- HD 2000/HD 2500, not supported