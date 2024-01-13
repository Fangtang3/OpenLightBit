import requests
from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import Plain, At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "OneWord"
channel.meta['description'] = "超级群娱现在咋样了？"
channel.meta['author'] = "ltzXiaoYanMo"

# 获取api
hitokoto = "https://v1.hitokoto.cn/?c=f&encode=text"


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("一言")]
    )
)
async def oneword(app: Ariadne, event: GroupMessage, group: Group):
    # 收到API，获取一言
    data = requests.get(hitokoto)
    await app.send_message(
        group,
        MessageChain([
            At(event.sender),
            Plain("\n"),
            Plain(data.text)
        ])
    )
