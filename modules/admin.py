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

from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen
from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("管理员")
channel.description("就事超管的意思")
channel.author("Emerald-AM9")


@listen(GroupMessage)
async def add_admin(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("上管")):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    try:
        await botfunc.run_sql("INSERT INTO admin(uid) VALUES (%s)", (int(str(message)),))
    except Exception as err:
        await app.send_message(group, f"寄！{err}")
    else:
        await app.send_message(group, "OK!")


@listen(GroupMessage)
async def del_admin(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("去管")):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    try:
        await botfunc.run_sql("DELETE FROM admin WHERE uid = %s", (int(str(message)),))
    except Exception as err:
        await app.send_message(group, f"寄！{err}")
    else:
        await app.send_message(group, "OK!")
