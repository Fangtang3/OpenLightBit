#    OpenLightBit-KuoHuBit
#    Copyright (C) 2023  Emerald-AM9
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("linkbit-olb")
channel.author("Emerald-AM9")

ops = botfunc.get_all_admin()
g_ops = botfunc.get_all_admin()
blocklist = botfunc.get_all_sb()
g_blocklist = botfunc.get_all_sb()
ignores = botfunc.get_all_sb()
g_ignores = botfunc.get_all_sb()
time_now = botfunc.lbit_conf('current-unix-timestamp')
owner_qq = botfunc.lbit_conf('owner-qq')
bot_qq = botfunc.get_config('qq')
verify_key = botfunc.get_config('verifyKey')
database_host = botfunc.get_cloud_config('MySQL_Host')
database_user = botfunc.get_cloud_config('MySQL_User')
database_passwd = botfunc.get_cloud_config('MySQL_Pwd')
database_name = botfunc.get_cloud_config('MySQL_db')