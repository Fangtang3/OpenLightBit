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
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import definer

channel = Channel.current()
channel.name("版本查询")
channel.description("查看机器人当前版本")
channel.author("Emerald-AM9")

r = definer.rand_sentence('rand_sentence')
# 版本号随机句子的参数
txt = "当前装载版本:OpenLightBit 2.3.1-release.b216(Xuanhua)\n质量更新版本:2.3\n紧急更新补丁版本:0\n"


@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("版本")]
    )
)
async def bot_version(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain([txt, "------------\n", Plain(random.choice(r))])
    )