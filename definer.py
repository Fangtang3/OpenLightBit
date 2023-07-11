# 芝士模仿Hanbot制作的集中化管理模块，大家也要多多支持Hantools
# 芝士他的github:https://kgithub.com/daizihan233
import json

import yaml
# 文本文件的读取可以在程序启动时完成，不必每次调用都打开，减少内存占用（虽然你大概感受不到）
# 但有个缺点就是无法实现热更新（你还不至于懒到重启一次程序都不愿意罢？）
#url_config_yaml = yaml.safe_load(open('./yamls/urls.yaml', 'r', encoding='UTF-8'))
eji_yaml = yaml.safe_load(open('./yamls/eji.yaml', 'r', encoding='utf-8'))
try:
    linux_knowledge_yaml = yaml.safe_load(open('./yamls/linux_knowledge.yaml', 'r', encoding='utf-8'))
except FileNotFoundError:
    safe_file_write('./yamls/linux_knowledge.yaml', """linux_knowledge : [
    "usr不等于user哦，而是\"Unix Software Resource\"的缩写",
    "/etc目录存放的主要是配置文件，如用户信息、服务的启动脚本、常用服务的配置文件等",
    "/bin目录存放的主要是系统命令，如sudo，普通用户和root用户都可以执行",
    "rm是一个神奇的命令，用于删除文件，文件夹，目录，甚至是/,-rf参数表示的是强制执行，如果想删除一个或者大多个文件（文件夹），可以使用:sudo rm -rf file1 file2 file3或者sudo rm -rf folder1 folder2 folder3等",
    "不同的系统拥有不同的包管理，如deb系统的包管理为apt，dpkg RHEL系统为yum，dnf（openSUSE为zypper），Arch系统主要为pacman等",
    "mkdir命令主要用于创建文件夹/目录，用法为mkdir <folder name>",
    "tar命令的参数有很多，如-c,-x,-t,-z,-j,-v,-f,-p,-P,-N,-exclude FILE等"

    ]""")
    logger.success(
        './yamls/linux_knowledge.yaml 未创建，程序已自动创建.')
    linux_knowledge_yaml = yaml.safe_load(open('./yamls/linux_knowledge.yaml', 'r', encoding='utf-8'))
#update_log_yaml = yaml.safe_load(open('./yamls/update_log.yaml', 'r', encoding='utf-8'))
rand_sentence_yaml = yaml.safe_load(open('./yamls/rand_sentence.yaml', 'r', encoding='utf-8'))

#shit_yaml = yaml.safe_load(open('./yamls/shit.yaml', 'r', encoding='utf-8'))
#settings_yaml = yaml.safe_load(open('./yamls/settings.yaml', 'r', encoding='UTF-8'))
try:
    global_yaml = yaml.safe_load(open('./yamls/global.yaml','r',encoding='utf-8'))
except FileNotFoundError:
    safe_file_write('./yamls/global.yaml', """bot_qq_id : 
verifykey : ""
su_id : [

]
bot_admin_id : """)
    logger.error(
        './yamls/global.yaml 未创建，程序已自动创建，请填写该文件的内容')
    sys.exit(1)

#take_menu_yaml = yaml.safe_load(open('./yamls/menu.yaml','r',encoding='utf-8'))
#def url_config(name: str):
#    try:
#        return url_config_yaml[name]
#    except KeyError:
#        return None


def eji(name: str):
    try:
        return eji_yaml[name]
    except KeyError:
        return None


def linux_knowledge(name: str):
    try:
        return linux_knowledge_yaml[name]
    except KeyError:
        return None

#def update_log(name: str):
#    try:
#        return update_log_yaml[name]
#    except KeyError:
#        return None


def rand_sentence(name: str):
    try:
        return rand_sentence_yaml[name]
    except KeyError:
        return None


#def shit(name: str):
#    try:
#        return shit_yaml[name]
#    except KeyError:
#        return None




#def settings(name: str):
#    try:
#        return settings_yaml[name]
#    except KeyError:
#        return None

def bot_global(name: str):
    try:
        return global_yaml[name]
    except KeyError:
        return None
#def take_menu(name: str):
#    try:
#        return take_menu_yaml[name]
#    except KeyError:
#        return None    