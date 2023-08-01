from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("linkbit-olb")
channel.author("Emerald-AM9")

ops = await botfunc.get_all_admin()
g_ops = await botfunc.get_all_admin()
blocklist = await botfunc.get_all_sb()
g_blocklist = await botfunc.get_all_sb()
ignores = await botfunc.get_all_sb()
g_ignores = await botfunc.get_all_sb()
time_now = botfunc.lbit_conf('current-unix-timestamp')
owner_qq = botfunc.lbit_conf('owner-qq')
bot_qq = botfunc.get_config('qq')
verify_key = botfunc.get_config('verifyKey')
database_host = botfunc.get_cloud_config('MySQL_Host')
database_user = botfunc.get_cloud_config('MySQL_User')
database_passwd = botfunc.get_cloud_config('MySQL_Pwd')
database_name = botfunc.get_cloud_config('MySQL_db')