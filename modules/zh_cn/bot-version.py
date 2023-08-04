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
txt = "当前装载版本:OpenLightBit 2.2.8-release.b146(Tongtong)(with Mariya Stable 1.2.7 & some ObsidianBot compatibility)"


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