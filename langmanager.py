from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import DetectPrefix, MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import botmanager

su = botmanager.bot_config('su')
lang = {
    "zh_cn": (" Bot默认语言已更改为简体中文(中国大陆)", " 默认语言已是简体中文(中国大陆)，无需更改"),
    "zh_hk": (" Bot語言已更改為繁體中文（中華人民共和國香港特別行政區）", " 默認語言已是繁體中文（中華人民共和國香港特別行政區），無需更改")
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
                         "Chinese Simplified(China Mainland/PRC)\n"
                         "Chinese Chinese Traditional(PRC SAR HongKong)")
        )
    else:
        await app.send_message(group, MessageChain(At(event.sender.id), " You don't have check privileges"))