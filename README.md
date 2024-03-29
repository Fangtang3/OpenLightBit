# OpenLightBit

一个QQBot | 基于 Mirai  Graia 与 [KuoHuBit](https://github.com/daizihan233/KuoHuBit)<br>
本项目参照 [Mirai](https://github.com/mamoe/mirai) 的许可证，使用 AGPL-3.0 开源<br>

# 系统要求

1. 若使用Windows，请确保使用Windows8.1+
2. 若使用带有GLIBC的GNU/Linux发行版，请使用GLIBC2.12+（对于32位x86）或GLIBC2.17+（对于64位x86）
3. Python 3.10+
4. MySQL 5.5.3+（MariaDB 10.5已测试，可用）
5. Redis/Valkey 4.0.0+
6. Mirai API HTTP
7. 已知GNU/Linux glibc平台下Ubuntu 22.04和RHEL 9可用

# 使用方法

目前建议使用github的main分支（或者fork到自己仓库进行git clone，请在gitee提交issue和pr）

安装git的方式：

Windows:
```PowerShell
winget install Git.Git
```
Debian/Ubuntu:
```bash
sudo apt-get install -y git
```

CentOS/Red Hat/Fedora（旧版）:
```bash
sudo yum install -y git
```
AlmaLinux/Red Hat/Fedora/Mageia/OpenEuler（新版）:
```bash
sudo dnf install -y git
```
安装pdm，输入以下字符安装pdm
Windows:
```PowerShell
pip install pdm
```

Linux:
```bash
pip3 install pdm 
```
若未安装pip，在此目录下输入:
Windows:
```bash
python get-pip.py
```
Linux：
```bash
python3 get-pip.py
```
安装完毕后，进入OpenLightBit的目录，输入pdm install（数据支持来自KuoHu，也就是括弧），即使打“X”也无需慌张。此刻你已经安装完毕了依赖。

### 换源
因为pip服务器未在中国大陆，所以我们需要换源

阿里源：
```bash
pdm config pypi.url https://mirrors.aliyun.com/pypi/simple
```

官源：
```bash
pdm config pypi.url https://pypi.org/simple
```

若需要查看配置源:
```bash
pdm config pypi.url
```

## 安装QQBot支持-Mirai Console Loader

这个其实挺简单的，特别是Linux用户，iTXTech已经做出了一站式服务，你只需要在GitHub上找到MCL一键安装程序，且找到适用于你操作系统版本的程序即可完成安装。

### 安装Mirai Console Loader HTTP依赖-MAH（Mirai API HTTP）

因为QQBot的依赖是需要Mirai的模块-MAH，所以我们需要去GitHub处找到MAH的Java程序文件，也就是.jar文件。安装在MCL的plugin目录中，启动MCL，使MAH创建配置文件。

创建完成后，你可以在config目录中找到MAH的配置文件，也就是net.mamoe.mirai-api-http。根据GraiaX的文档中，我们需要打开setting.yaml文件。且更改为以下字符： 
```yaml
adapters:
- http
- ws
debug: false
enableVerify: true
verifyKey: GraiaxVerifyKey # 你可以自己设定，这里作为示范
singleMode: false
cacheSize: 4096
adapterSettings:
http:
    host: localhost
    port: 8080
    cors: [*]
ws:
    host: localhost
    port: 8080
    reservedSyncId: -1
```
则MAH的配置文件部署完毕。

## 配置OpenLightBit
    
OpenLightBit与KuoHuBit的配置其实都很简单，都是更改cloud.json和config.yaml文件。最新版本当中需运行main.py才可出现cloud.json文件。

## 配置结束，启动和使用YanBot

打开Mirai登录你的QQ号即可，但前提在启动MCL前，你看到了以下字符 

```mirai
2022-07-04 19:11:11 I/Mirai HTTP API: ********************************************************
2022-07-04 19:11:12 I/http adapter: >>> [http adapter] is listening at http://localhost:8080
2022-07-04 19:11:12 I/ws adapter: >>> [ws adapter] is listening at ws://localhost:8080
2022-07-04 19:11:12 I/Mirai HTTP API: Http api server is running with verifyKey: GraiaxVerifyKey
2022-07-04 19:11:12 I/Mirai HTTP API: adaptors: [http,ws]
2022-07-04 19:11:12 I/Mirai HTTP API: ********************************************************
```
此处无需完全一样

如果看见，则成功启动了MAH。

在OpenLightBit的设置中，也只需要控制台中输入以下字符

Windows：
```PowerShell
pdm run python main.py
```
Linux：
```bash
pdm run python3 main.py 或 pdm run python3.11 main.py
```

如果出现SUCCESS，则成功与Mirai连接。

# 其他的机器人

可以学习一下，我可能为这些项目做出过贡献<br>

- [Abjust](https://github.com/Abjust/)
    - [~~Abjust/2kbit-cs~~](https://github.com/Abjust/2kbit-cs)
        - [~~123Windows31/2kbot~~](https://github.com/123Windows31/2kbot)
        - [~~Emerald-AM9/Mica-App-Bot-~~](https://github.com/Emerald-AM9/Mica-App-Bot-)
            - [~~emerald-am9/mica-app-extension~~](https://gitee.com/emerald-am9/mica-app-extension/)
    - [~~Abjust/2kbot-java~~](https://github.com/Abjust/2kbot-java)
    - [~~Abjust/2kbot-py~~](https://github.com/Abjust/2kbot-py)
    - [Abjust/2kshit](https://github.com/Abjust/2kshit)
- [ObsidianCatalina](https://github.com/ObsidianCatalina/)
    - [~~ObsidianCatalina/ObsidianBot~~](https://github.com/ObsidianCatalina/ObsidianBot)
    - [ObsidianCatalina/OpenMariya](https://github.com/ObsidianCatalina/OpenMariya)
        - [ltzXiaoYanMo/YanBot-OpenMariya_Edition](https://github.com/ltzXiaoYanMo/YanBot-OpenMariya_Edition)
- [daizihan233](https://github.com/daizihan233)
    - [daizihan233/KuoHuBit](https://github.com/daizihan233/KuoHuBit/)
        - [~~ltzXiaoYanMo/YanBot-KHB_Edition_Older~~](https://github.com/ltzXiaoYanMo/YanBot-KHB_Edition_Older)
        - [ltzXiaoYanMo/YanBot_KHB_Edition](https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition)
        - [emerald-am9/lightbit](https://gitee.com/Emerald-AM9/lightbit)
    - [daizihan233/KuoHuShit](https://github.com/daizihan233/KuoHuShit)
