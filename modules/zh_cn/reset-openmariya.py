from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import  DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import botmanager
import langmanager
su = botmanager.bot_config('su')
channel = Channel.current()
channel.name("重置")
channel.description("重置所有设置（OpenMariya）")
channel.author("Emerald-AM9")
channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def rec(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("rec ")):
    if str(message) in ["--all,","-a"]:
       if event.sender.id in su: 
        langmanager.enable_lang = "zh_cn"
        await app.send_message(
                group,
                MessageChain(At(event.sender.id), "OpenMiriya设定已重置!")
            )
       else:
            await app.send_message(group, MessageChain(At(event.sender.id), "权限不足！"))
    else:
        await app.send_message(group, MessageChain(At(event.sender.id), f"无效参数：'{str(message)}'。"))