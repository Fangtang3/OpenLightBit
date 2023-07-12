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
from graia.ariadne.message.element import Plain, At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.saya import Channel

import botfunc
import cache_var

channel = Channel.current()
channel.name("6榜")
channel.description("666")
channel.author("HanTools")


@listen(GroupMessage)
@decorate(MatchContent("6，閉嘴"))
async def no_six(app: Ariadne, group: Group, event: GroupMessage):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    if group.id not in cache_var.no_6:
        cache_var.no_6.append(group.id)
        await botfunc.run_sql("""INSERT INTO no_six VALUES (%s)""", (group.id,))
        await app.send_group_message(
            group,
            MessageChain(
                [
                    At(event.sender.id),
                    Plain(" 好啊，很好啊")
                ]
            ),
            quote=event.source
        )


@listen(GroupMessage)
@decorate(MatchContent("6，張嘴"))
async def yes_six(app: Ariadne, group: Group, event: GroupMessage):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    if group.id in cache_var.no_6:
        cache_var.no_6.remove(group.id)
        await botfunc.run_sql("""DELETE FROM no_six WHERE gid = %s""", (group.id,))
        await app.send_group_message(
            group,
            MessageChain(
                [
                    At(event.sender.id),
                    Plain(" 好啊，很好啊")
                ]
            ),
            quote=event.source
        )
