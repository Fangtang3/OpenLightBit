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
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.saya.channel import ChannelMeta

import botfunc
import depen

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "管理员"
channel.meta['description'] = "对群和机器人进行管理"
channel.meta['author'] = "KuoHu"

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[
            DetectPrefix("上管"),
            depen.check_authority_op(),
            depen.check_authority_not_black()
        ]
    )
)
async def add_admin(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("上管")):
    try:
        await botfunc.run_sql("INSERT INTO admin(uid) VALUES (%s)", (int(str(message).lstrip("上管")),))
    except Exception as err:
        await app.send_message(group, f"寄！{err}")
    else:
        await app.send_message(group, "OK!")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[
            DetectPrefix("下管"),
            depen.check_authority_op(),
            depen.check_authority_not_black()
        ]
    )
)
async def del_admin(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("下管")):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    try:
        await botfunc.run_sql("DELETE FROM admin WHERE uid = %s", (int(str(message)),))
    except Exception as err:
        await app.send_message(group, f"寄！{err}")
    else:
        await app.send_message(group, "OK!")
