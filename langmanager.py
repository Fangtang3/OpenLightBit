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
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import botmanager

su = botmanager.bot_config('su')
lang = {
    "zh_cn": (" Bot默认语言已更改为简体中文(中国大陆)", " 默认语言已是简体中文(中国大陆)，无需更改")
}
enable_lang = "zh_cn"

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def change_lang(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("Lang --set-default-lang = ")):
    global enable_lang
    if str(message) in lang:
        if enable_lang != str(message):
            enable_lang = str(message)
            await app.send_message(
                group,
                MessageChain(At(event.sender.id), lang[enable_lang][0])
            )
        else:
            await app.send_message(group, MessageChain(At(event.sender.id),
                                                       lang[enable_lang][1]))
    else:
        await app.send_message(group, MessageChain(At(event.sender.id)," Cannot find the language"))


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --list-a")],
    )
)
async def Lang_list(app: Ariadne, group: Group, event: GroupMessage):
    if event.sender.id in su:
        await app.send_message(
            group,
            MessageChain(At(event.sender.id),
                         " Installed language:\n"
                         "简体中文(中国大陆)\n")
        )
    else:
        await app.send_message(group, MessageChain(At(event.sender.id), " 权限不足"))