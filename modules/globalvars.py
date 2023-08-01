from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("Linkbit")
channel.description("使khbit兼容2kbit-py插件")
channel.author("Emerald-AM9")

try:
    linkbit_not_in_auto_mode = yaml.safe_load(open('linkbit.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    botfunc.safe_file_write('linkbit.yaml', """# LinkBit配置文件
owner-qq: 10001
old-hanbot-api-ip: ""
old-hanbot-api-key: ""
current-unix-timestamp: """)
    logger.error('linkbit.yaml 未创建，程序已自动创建，请填写该文件的内容')
    sys.exit(1)

def linkbit_niam_conf(name: str):
    try:
        return linkbit_not_in_auto_mode[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到，将尝试空载配置文件')
        return None

ops = await botfunc.get_all_admin()
g_ops = await botfunc.get_all_admin()
blocklist = await botfunc.get_all_sb()
g_blocklist = await botfunc.get_all_sb()
ignores = await botfunc.get_all_sb()
g_ignores = await botfunc.get_all_sb()
time_now = linkbit_niam_conf('current-unix-timestamp')
owner_qq = linkbit_niam_conf('owner-qq')
api = linkbit_niam_conf('old-hanbot-api-ip')
api_key = linkbit_niam_conf('old-hanbot-api-key')
bot_qq = botfunc.get_config('qq')
verify_key = botfunc.get_config('verifyKey')
database_host = botfunc.get_cloud_config('MySQL_Host')
database_user = botfunc.get_cloud_config('MySQL_User')
database_passwd = botfunc.get_cloud_config('MySQL_Pwd')
database_name = botfunc.get_cloud_config('MySQL_db')