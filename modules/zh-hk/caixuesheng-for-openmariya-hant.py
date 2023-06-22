import random
from graiax import silkcoder
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Voice
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import langmanager
import botmanager

v = botmanager.students_voices('voice_paths')
channel = Channel.current()
channel.name("蔚藍檔案 猜學生")
channel.description("Translated by Emerald-AM9.")
channel.author("Emerald-AM9")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("猜學生")],
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage):
    voice_bytes = await silkcoder.async_encode(random.choice(v), ios_adaptive=True)
    if langmanager.enable_lang == "zh_cn":
        await app.send_group_message(group, MessageChain(Voice(data_bytes=voice_bytes)))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id), " 抱歉，您所在的国家/地区不支持此功能"))
