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

from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.util.saya import listen
from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("黑名单")
channel.description("屌你老母")
channel.author("HanTools")


@listen(GroupMessage)
async def nmms(app: Ariadne, event: GroupMessage, message: MessageChain = DetectPrefix("刪黑")):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    try:
        await botfunc.run_sql('DELETE FROM blacklist WHERE uid = %s',
                              (int(str(message)),))
        await app.send_message(event.sender.group, "好了！")
    except Exception as err:
        await app.send_message(event.sender.group, f"Umm，{err}")
