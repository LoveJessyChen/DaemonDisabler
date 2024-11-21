# Daemon Disabler

[中文](https://github.com/ringoju1ce/DaemonDisabler/blob/main/README_CN.md)

A tool for disabling certain daemons in iOS.

**Use this software at your own risk. Make a backup before using it.**

Compatible with iOS 15.7+

<!--**Important**: Any modifications made to iOS using this software will persist even after upgrading iOS. However, upgrading to an unsupported version will prevent you from undoing these modifications through this software. Additionally, these modifications will be included in your device backups and restored to any device, as well as transferred when you use this device to set up a new device.

In short: **You must undo all modifications before upgrading iOS, make a backup, or transferring data to another device。**

On supported iOS version, undoing the modifications using this software is simple: just connect your device, ensure all checkboxes are unchecked, and click `Apply Changes`.

However, even if you upgrade to an unsupported version and forget to undo these modifications beforehand, **you still have a chance to reverse these modifications**.

You can look for software capable of editing iOS backups, select a backup, and edit `DatabaseDomain/com.apple.xpc.launchd/disabled.plist`. Then, locate and delete the following key-value pairs: (Note that some of these pairs may not be present in your file, depending on which daemons were disabled using this software. The order of key-value pairs in your file may also differ, which is acceptable. Do not touch anything else besides the key-value pairs listed below.)
```
com.apple.thermalmonitord
com.apple.mobile.softwareupdated
com.apple.OTATaskingAgent
com.apple.softwareupdateservicesd
com.apple.UsageTrackingAgent
com.apple.spotlightknowledged
com.apple.mobileaccessoryupdater
com.apple.UARPUpdaterServiceLegacyAudio
com.apple.accessoryupdaterd
```
For example: if your disabled.plist file looks like this and you find `com.apple.UsageTrackingAgent` key-value pair listed above, you will need to delete it.
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.UsageTrackingAgent</key>
	<true/>
	<key>com.apple.bootpd</key>
	<true/>
	<key>com.apple.dhcp6d</key>
	<true/>
	<key>com.apple.ftp-proxy-embedded</key>
	<false/>
	<key>com.apple.magicswitchd.companion</key>
	<true/>
	<key>com.apple.relevanced</key>
	<true/>
	<key>com.apple.security.otpaird</key>
	<true/>
</dict>
</plist>
```
After deleting `com.apple.UsageTrackingAgent` key-value pair, it should look like this:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.bootpd</key>
	<true/>
	<key>com.apple.dhcp6d</key>
	<true/>
	<key>com.apple.ftp-proxy-embedded</key>
	<false/>
	<key>com.apple.magicswitchd.companion</key>
	<true/>
	<key>com.apple.relevanced</key>
	<true/>
	<key>com.apple.security.otpaird</key>
	<true/>
</dict>
</plist>
```
Restoring this modified backup will undo all the modifications.
## Running-->

## Features

* Disable thermal monitor
* Disable system software update
* Disable firmware updates for accessories
* Disable unnecessary services  (UsageTrackingAgent and spotlightknowledged)

## Running the Program

**Requirements:**

* Python 3.8-3.11

**Additional requirement on Linux:**

* usbmuxd

### Clone the Repository

```
git clone https://github.com/ringoju1ce/DaemonDisabler.git
cd DaemonDisabler
```

### Create venv

```
python3 -m venv .venv
```

This will create a virtual environment in  `.venv` directory under the current directory.

### Activate venv (Windows)

```
.\.venv\Scripts\activate
```

If you see `(.venv)` appear in front of your prompt, it means you have successfully activated the virtual environment. The virtual environment will deactivate when you close the current terminal or execute `deactivate` command.

If PowerShell prompts that script execution is disabled on this system, you need to run the following command with administrator privileges:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

This will allow unsigned local scripts to run.

### Activate venv (Linux/macOS)

```
. .venv/bin/activate
```

The virtual environment will deactivate when you close the current terminal or execute `deactivate` command.

### Install Dependencies

```
pip3 install -r requirements.txt --ignore-requires-python
```

### Run the Program (Command Line)

```
python3 cli_app.py
```

### Run the Program (GUI)

```
python3 gui_app.py
```

If it can't start or isn't responding on Linux, make sure  `usbmuxd` service is running.

## Building

If you want to run the program on a system without Python installed, you can build an executable with following command:

```
python3 compile.py
```

Executables will be located in `./dist` .

To compile icon resources:

```
pyrcc5 resources.qrc -o resources_rc.py
```

## Credits

- [ringoju1ce](https://github.com/ringoju1ce)/[DaemonDisabler](https://github.com/ringoju1ce/DaemonDisabler)
- Modified from [rponeawa](https://github.com/rponeawa)/[thermalmonitordDisabler](https://github.com/rponeawa/thermalmonitordDisabler), [leminlimez](https://github.com/leminlimez)/[Nugget](https://github.com/leminlimez/Nugget)
- [JJTech](https://github.com/JJTech0130) for Sparserestore/[TrollRestore](https://github.com/JJTech0130/TrollRestore)
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3)
