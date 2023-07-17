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

import random

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import definer

channel = Channel.current()
channel.name("linux_knowledge")
channel.description("*nix芝士")
channel.author("Emerald-AM9")

# Read json
su = definer.bot_global('su_id')
linux_knowledge = definer.linux_knowledge('linux_knowledge')


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[]
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("unix芝士")):
    if  message:  # 因为如果没有参数则 message 为空，可以直接取反判断是否有值
        await app.send_message(
            group,
            MessageChain(random.choice(linux_knowledge))
        )