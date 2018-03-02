# INFO
Hi, I'm Pig. This is a fork of @camielverdult hackintosh guide, I will continue maintaining this guide for /r/hackintosh subreddit and people of [hackintosh Discord server](http://discord.io/hackintosh)

# Install macOS on a hackintosh

You've read it, this guide/repo will guide you on how to install macOS to your desktop computer (laptop could work too, I am not going to do that in this guide though since laptops aren't in the general 
level of difficulty hackintoshing wise).

# Disclaimer

In this guide we don't cover AMD CPU's, this guide is primarily focussed around Intel CPU's

This guide is meant for desktop PC's, you could follow the same steps for laptops but most laptops will require extra patches and fixes.

We are not "professional" hackintoshers in any way. We know how to get a hackintosh working and we would like to spread our knowledge.

This guide is made by a few people. All have different opinions and different approaches.

# Table of contents
* [Picking hardware for macOS](Hardware.md)
* [Pre-Install](Pre-Install.md)
* [Post-Install](Post-Install.md)
* [Tips](Tips.md)
* [iMessage/Facetime](iMessage.md)
* [Audio](Audio.md)
* [HDMI Audio](HDMI-Audio.md)
* [Power Management](Speedstep.md)
* [SMBIOS](SMBIOS.md)
* [Troubleshooting](Troubleshooting.md)
* [Credits/Acknowledgements](Credits.md)

# Useful links
* [Vanilla guide](https://www.reddit.com/r/hackintosh/comments/68p1e2/ramblings_of_a_hackintosher_a_sorta_brief_vanilla/) by [CorpNewt](https://www.reddit.com/user/corpnewt).
* [Kext spreadsheet](http://docs.google.com/spreadsheets/d/1WQ87XQKgJVPPub_CbjoHsUscgyxrGg3DWzZz7Nnf_RU/)
* [Latest Clover](https://github.com/Dids/clover-builder/releases/latest)
* [Official latest Clover](https://sourceforge.net/projects/cloverefiboot/)
* [Nvidia Web Drivers](https://cookiemonster.pro/nvidia_driver_table)
* [Hackintosh Discord server](http://discord.io/hackintosh)

# Some questions

## What is a hackintosh?

A hackintosh is a pc running MacOS. There is no actual "Hacking" involved as you might think because of the name. 

More info can be found [here](https://www.lifewire.com/what-is-hackintosh-832719).

## How do I "make" a hackintosh?

You will need a list of your computer's specifications, a general idea of how an operating system works and a high pain tolerance.

More instructions [here](Pre-Install.md).

## What are kexts?

Kext files are essentially drivers for Mac OS X. "Kext" stands for Kernel Extension; kext files "extend" Mac OS X's kernel, the core part of the operating system, by providing additional code to be loaded when your computer boots. "Hackintoshes" often require special kexts to enable sound, ethernet, and more. Some Hackintosh-specific kexts are modified versions of existing Mac OS X kexts, such as AppleHDA.kext. Other kexts are extra additions to the normal list of kexts that OS X runs on startup. In the end, all of these Hackintosh kexts serve the same purpose: to add support to hardware that isn't officially supported by Apple.

Technically, kexts aren't individual files. In fact, .kext "files" are essentially packaged like .zip files. If you copy a .kext file onto a Windows installation, it becomes a folder. That's because that's what kexts are-- folders. Much like Apple's .app files, you can access the inside of a kext by right-clicking the kext file and clicking "Show Package Contents". Once you've entered the contents of the kext file, you will be able to edit the plist (settings) files and make other modifications, if necessary. Editing the contents of kext files is occasionally necessary to activate certain graphics card kexts or fix glitchy kexts. However, we won't go into that process here.

For more [here](http://www.macbreaker.com/2012/01/what-are-kexts.html)

## What is Clover?

What is Clover about? Obviously not about the grass growing on a meadow for the cows' pleasure. It is about a software, a boot loader of a new type, that allows Mac OS X to run on a common PC.

Apple restricts the usage of its operating system to its own devices, arguing that it can not provide functionality on devices it didn't produce in the first place. Well, users will take the risk. No commercial advantage is taken in order to avoid other legal complications. A non-Apple computer into which Mac OS X is installed is called *Hackintosh*; the label's origin is self-explanatory.

In order to start a hackintosh, a special boot loader is needed. There is a big variety of boot loaders, but they can be divided into two groups: FakeEFI and RealEFI.

For more [here](https://clover-wiki.zetam.org/Preface)

## Will you guide me through every single step personally?

I will not do this, please don't ask anyone but a good friend to do this for you. You can always ask for help from Discord server or anyone with some experience. Please don't be that person who wants his hand held through the process of this. If you want to get mac running the easy way, I recommend you check out [this](https://www.apple.com/mac/).

## Something broke/ isn't working (correctly)! What do I do?

I recommend you check out this page [here](Troubleshooting.md)

## Contact
If you feel the need to say something about the guide you can do that in the hackintosh discord server.

http://discord.io/hackintosh
