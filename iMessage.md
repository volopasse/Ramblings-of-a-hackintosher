**How to fix iMessage & FaceTime**

**Requirement:**

- - Clover Bootloader only
  - Clover Configurator: <http://mackie100projects.altervista.org>

**Step 1: Set correct BSD name**

Open Terminal, run this command (run one command and type pw, then run the rest)

sudo rm -rf /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist

sudo rm -rf /Library/Preferences/SystemConfiguration/preferences.plist

By now, OS X (macOS) should re-discover all your Network Interfaces and rebuild the network configuration files, hopefully now with the correct BSD names. If the BSD names are still not correct and you have additional add-on PCI or USB NIC's then try removing them and delete the two files again, reboot and let OS X assign the 'built-in' NIC's first, then re-install your add-on NIC's one by one.

You can check your BSD name by System Profiler - Network

**Step 2: Reset iMessage Configuration files**

If you are starting with a clean OS X install then there is no need for you to perform any of the procedures in this chapter .... however if you have been trying to get iMessage to work for sometime and have been using different System ID's and/or Apple_ID's then the chances are that the iMessage configuration and cache files could contain invalid or non-useful data.

By deleting these files we can force iMessage to reset-itself and re-build the configuration files which will force iMessage to re-authenticate it-self with Apples iMessage servers. I always recommend performing this procedure after making any significant changes to OS X's System ID's such as the S/N, SmUUD (System_Id), System Type, MLB & ROM.

Before commencing you should logout of **all** Apple iCloud services and disconnect from your network, then reboot this way OS X will not start the iCloud services and allow us to remove the config files.

Open Terminal, run this command (run one command and type pw, then run the rest)

sudo rm -rf /StartupDrive/Users/~Username/Library/Caches/com.apple.iCloudHelper*

sudo rm -rf /StartupDrive/Users/~Username/Library/Caches/com.apple.Messages*

sudo rm -rf /StartupDrive/Users/~Username/Library/Caches/com.apple.imfoundation.IMRemoteURLConnectionAgent*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.iChat*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.icloud*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.imagent*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.imessage*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.imservice*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.ids.service*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.madrid.plist*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.imessage.bag.plist*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.identityserviced*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.ids.service*

sudo rm -rf /StartupDrive/Users/~Username/Library/Preferences/com.apple.security*

sudo rm -rf /StartupDrive/Users/~Username/Library/Messages

StartupDrive is your name of macOS partition

After that, empty your trash (if has) then reboot.

**Step 3: Generate SMBIOS value**

Open Clover Configurator and mount your EFI partition, open config.plist. Goes to SMBIOS, select your SMBIOS again, click to "Generate" few times

Now open <https://checkcoverage.apple.com> , fill your Series Number from Clover Configurator. If you got something like this

![alt text](https://i.imgur.com/InK7KM6.png)

Then go back to Clover Configurator, save your Board Series Number to a note and continues to click "Generate" few more times and check your Series Number again. If you got something like "We’re sorry, but this serial number isn’t valid. Please check your information and try again." then you are good. Now use that invalid Series Number you just have and Board Series Number based from "valid" Series Number and fill to Clover Configurator.

Open Terminal, run "uuidgen". Repeat it few times then copy last value to SmUUID 

**Step 4: ROM value**

Open System Profiler - Network, you should see your MAC Address like this 88:88:a8:88:8a:88, now put it to Clover Configurator - Rt Variables - ROM without ":" and all letter must be uppercase. When done you should have something like 8888A8888A88. 

Now save your settings and reboot. After that try to login to iMessage

**Step 5: Troubleshooting**

- If you getting Customer Code after a failed login then try everything from step 1 again
- If you getting failed to login error then check your BSD name, try to login again few more times or try everything from step 1 again