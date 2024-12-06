# 守护进程禁用工具

用于禁用 iOS 系统中的一些守护进程。

**使用本软件的风险由您自行承担，使用前请备份设备**

适用于 iOS 15.7+

<!--**重要**：您使用本软件对系统的修改在升级系统后也**依然保留**。但是，**升级到不支持的系统会让您无法再使用本软件撤销修改**。
此外，这些修改在您备份设备的时候**也会被一同备份，然后在还原备份的时候被带回到设备上**；**对于将这台设备的数据转移到新设备的情况也是如此**。

简而言之：当您使用本软件修改 iOS 之后，在升级系统、备份您的设备、将此设备的数据转移到另一台设备之前，**必须**撤销您使用本软件对 iOS 的所有更改。

在支持的 iOS 版本上使用本软件撤销修改很简单：只需要连接设备，保持所有复选框不勾选，点击`应用更改`即可。

不过，即使您还是在既没有使用前的备份，也没有撤销修改的情况下升级到了不支持的版本，**您依然有机会撤销这些修改**。

您可以寻找一些能够修改 iOS 备份的软件，打开一个备份，修改`DatabaseDomain/com.apple.xpc.launchd/disabled.plist`，寻找并删除以下的键值对：(可能有些键值对不在你的文件里，这取决于你用本软件禁用了哪些服务；你的文件中键值的顺序也可能不同，这是正常的；除了下面列出的键值对，不要碰其他任何东西)
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
举例：假设您的`disabled.plist`文件是这样，您发现上面列出的`com.apple.UsageTrackingAgent`键值对在里面。因此您需要删除它。
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
删除`com.apple.UsageTrackingAgent`键值对之后看起来是这样：
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
恢复这个修改过的备份即可撤销所有修改。-->

## 功能

* 禁用温度监测 (App 将不会在发热时主动降低运行速度)
* 禁用系统更新
* 禁用配件固件更新 (Airpods等)
* 禁用其他非必要且影响性能的服务 (UsageTrackingAgent 和 spotlightknowledged)

## 运行

**需要：**

- Python 3.8-3.11

**在 Linux 上运行还需要：**

- usbmuxd

### 拉取仓库

```
git clone https://github.com/ringoju1ce/DaemonDisabler.git
cd DaemonDisabler
```

### 创建虚拟环境

```
python -m venv .venv
```

这将会在当前目录下的 `.venv` 目录中创建虚拟环境。

### 启用虚拟环境 (Windows)

```
.\.venv\Scripts\activate
```

如果您看到您的 prompt 前出现了 `(.venv)` 字样，说明您启用了虚拟环境。虚拟环境会在您关闭当前终端，或者是您执行 `deactivate` 之后关闭。在虚拟环境关闭后您需要重新启用才能运行程序。

如果 Powershell 提示您在此系统上禁止运行脚本，您需要以管理员权限执行下面的命令

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

这将允许执行未签名的本地代码

### 启用虚拟环境 (Linux/macOS)

```
. .venv/bin/activate
```

虚拟环境会在您关闭当前终端，或者是您执行 `deactivate` 之后关闭。在虚拟环境关闭后您需要重新启用才能运行程序。

### 安装依赖

```
pip install -r requirements.txt
```

### 运行程序 (命令行)

```
python cli_app.py
```

### 运行程序 (GUI)

```
python gui_app.py
```

如果 Linux 运行报错或无响应，首先检查 usbmuxd 服务是否运行。

## 构建程序

如果您希望在没有安装 Python 环境的系统中运行程序，可以执行下面的命令构建可执行档。

```
python compile.py
```

构建的可执行档位于 `./dist`

要构建资源文件，执行下面的命令

```
pyrcc5 resources.qrc -o resources_rc.py
```

## 致谢

- 修改自 [rponeawa](https://github.com/rponeawa)/[thermalmonitordDisabler](https://github.com/rponeawa/thermalmonitordDisabler), [leminlimez](https://github.com/leminlimez)/[Nugget](https://github.com/leminlimez/Nugget)
- 感谢 [JJTech](https://github.com/JJTech0130) 提供的 Sparserestore/[TrollRestore](https://github.com/JJTech0130/TrollRestore)
- 感谢 [pymobiledevice3](https://github.com/doronz88/pymobiledevice3)
