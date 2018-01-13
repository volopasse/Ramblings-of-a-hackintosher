# Common problem when install Web Driver

- Black screen
- Can't inject Web Driver

**Black screen**

- Black screen when using iMac15,1 or iMac17,1 or MacPro 6,1 system definition
- Black screen when using bad display cable
- Black screen when install Web Driver without S.I.P.

**Can't inject Web Driver**

- NvidiaWeb system parameters not inject
- No native NVRAM support

--------------------------------------------------

**Black screen when using iMac15,1 or iMac17,1 or MacPro6,1 system definition**

So, somehow AppleGraphicsDevicePolicy.kext block iMac15,1 or iMac17,1 or MacPro6,1 from using NVIDIA Web Driver. You need to install NvidiaGraphicsFixup.kext and Lilu.kext to bypass it

**Black screen when using bad display cable**

Yes, some bad quality cable prevent macOS booting with NVIDIA Web Driver. Even you can boot with Windows,.... Use high quality cable to solve this problem.

**Black screen when install Web Driver without S.I.P.**

This problem may not happens on every machine but if you are trying to install Web Driver on macOS High Sierra and got blackscreen. You should enable S.I.P. "before" install Web Driver.

In order to enable S.I.P. you need to inject 0x0 to config.plist - Rt Variables - CsrActiveConfig using Clover Configurator. Then reboot

If you was install Web Driver then you have to reinstall macOS then try to install Web Driver with S.I.P. enabled

\---------------------------------------------------------------------------------------------------------------

**NvidiaWeb system parameter not inject**

Open config.plist with Clover Configurator and goes to System Parameters, tick NvidiaWeb to inject NVIDIA Web Driver on next boot

**No native NVRAM support**

Some mainboard don't have NVRAM support, this has been fixed with latest Clover Bootloader. Or if you using latest but still don't have NVRAM support, then you have to emulate NVRAM. If you don't have NVRAM then macOS can't inject NvidiaWeb system parameter because system won't save it for next boot

But first, let try to check your system first.

Open the terminal and do the following one line at a time:

`sudo -s

nvram -c

nvram myvar=test

exit`

Now reboot. After than open terminal and run this nvram -p | grep -i myvar

If you get any output from that last command (after a reboot) then your NVRAM works!

If not you have to emulate NVRAM by install EmuVariableUefi-64.efi and RC scripts via Clover Bootloader installer


---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
