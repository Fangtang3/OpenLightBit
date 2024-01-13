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

import json

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.saya import Channel
from graia.saya.channel import ChannelMeta

import botfunc

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "摸鱼日历"
channel.meta['description'] = "摸🐟"
channel.meta['author'] = "KuoHu"

@listen(GroupMessage)
@decorate(MatchContent("鱼"))
async def fish(app: Ariadne, group: Group, event: GroupMessage):
    data: str = json.loads(botfunc.session.get("http://bjb.yunwj.top/php/mo-yu/php.php").text)['wb']
    data: str = data.replace('【换行】', '\n')
    await app.send_message(
        group,
        MessageChain([At(event.sender.id), Plain(f" \n{data}")]),
    )
