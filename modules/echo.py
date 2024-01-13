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

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, ActiveGroupMessage
from graia.ariadne.event.mirai import GroupRecallEvent
from graia.ariadne.message import Source
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.saya.channel import ChannelMeta

import botfunc

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "Hello World!"
channel.meta['description'] = "哼哼哼，啊啊啊啊啊"
channel.meta['author'] = "KuoHu"

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def echo(app: Ariadne, group: Group, source: Source, message: MessageChain = DetectPrefix("/echo ")):
    for w in (
            "echo", "6", "9", "c", "草", "c", "tcl", "典"
    ):
        if message.display.startswith(w):
            return
    m: ActiveGroupMessage = await app.send_group_message(
        group,
        message,
    )
    botfunc.r.hset('echo', source.id, m.source.id)


@channel.use(
    ListenerSchema(
        listening_events=[GroupRecallEvent]
    )
)
async def echo(app: Ariadne, group: Group, event: GroupRecallEvent):
    if botfunc.r.hexists("echo", event.message_id):
        await app.recall_message(botfunc.r.hget("echo", event.message_id), group)
        botfunc.r.hdel("echo", event.message_id)
