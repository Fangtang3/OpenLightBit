#    OpenLightBit-KuoHuBit
#    Copyright (C) 2024  Emerald-AM9
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

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen
from graia.ariadne.util.saya import decorate
from graia.saya import Channel
from graia.saya.channel import ChannelMeta

import botfunc

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "版本查询"
channel.meta['description'] = "查看设置的机器人版本"
channel.meta['author'] = "Emerald-AM9"
@listen(GroupMessage)
@decorate(MatchContent("版本"))
async def ver(app: Ariadne, group: Group, event: GroupMessage):
    olbname = botfunc.lbit_conf('bot-name')
    olbcfver = botfunc.lbit_conf('bot-ver')
    await app.send_message(
        group,
        MessageChain([At(event.sender.id), Plain(f"{olbname} {olbcfver}")]),
    )
