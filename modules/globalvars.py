from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("Linkbit")
channel.description("使khbit兼容2kbit-py插件")
channel.author("Emerald-AM9")

try:
    linkbit_ni = yaml.safe_load(open('linkbit.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    botfunc.safe_file_write('linkbit.yaml', """# LinkBit配置文件
owner-qq: 10001
old-hanbot-api-ip: ""
old-hanbot-api-key: ""
current-unix-timestamp: """)
    logger.error('linkbit.yaml 未创建，程序已自动创建，请填写该文件的内容')
    sys.exit(1)

ops = await botfunc.get_all_admin()
g_ops = await botfunc.get_all_admin()
blocklist = await botfunc.get_all_sb()
g_blocklist = await botfunc.get_all_sb()
ignores = await botfunc.get_all_sb()
g_ignores = await botfunc.get_all_sb()
time_now = linkbit_ni[current_unix_timestamp]
owner_qq = linkbit_ni[owner-qq]
api = linkbit_ni[old-hanbot-api-ip]
api_key = linkbit_ni[old-hanbot-api-key]
bot_qq = botfunc.get_config('qq')
verify_key = botfunc.get_config('verifyKey')
database_host = botfunc.get_cloud_config('MySQL_Host')
database_user = botfunc.get_cloud_config('MySQL_User')
database_passwd = botfunc.get_cloud_config('MySQL_Pwd')
database_name = botfunc.get_cloud_config('MySQL_db')