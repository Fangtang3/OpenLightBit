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
from graia.ariadne.event.message import FriendMessage, TempMessage
from graia.ariadne.model import Member, Friend
from graia.ariadne.util.saya import listen
from graia.saya import Channel

channel = Channel.current()
channel.name("如来")
channel.description("在有人找机器人私聊的时候，如来")
channel.author("HanTools")

rutext = botfunc.lbit_conf('rulai').split('\n')

index = 0


async def send_ru(app: Ariadne, sender: Member or Friend):
    global index
    await app.send_message(sender, rutext[index])
    index += 1
    if index > len(rutext) - 1:
        index = 0


@listen(TempMessage)
async def rulai(app: Ariadne, sender: Member):
    await send_ru(app, sender)


@listen(FriendMessage)
async def rulai(app: Ariadne, sender: Friend):
    await send_ru(app, sender)