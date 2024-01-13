#    OpenLightBit-KuoHuBit
#    Copyright (C) 2024  Emerald-AM9
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

import datetime

from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import MemberLeaveEventQuit, MemberJoinEvent, MemberLeaveEventKick
from graia.ariadne.message.element import Plain, At
from graia.ariadne.model import Group, Member
from graia.ariadne.util.saya import listen
from graia.saya import Channel
from graia.saya.channel import ChannelMeta

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "event"
channel.meta['description'] = "有些事总是不知不觉的……"
channel.meta['author'] = "KuoHu"

@listen(MemberLeaveEventQuit)
@listen(MemberLeaveEventKick)
async def leave(app: Ariadne, group: Group, member: Member):
    await app.send_message(
        target=group,
        message=f'✈️成员发生变更：\n'
                f'QQ号为： {member.id} 的小伙伴退出了本群，对他/她的离开表示惋惜，期待他/她能够与我们再次相遇~'
    )


@listen(MemberJoinEvent)
async def leave(app: Ariadne, group: Group, member: Member):
    now = datetime.datetime.now()
    await app.send_message(
        target=group,
        message=MessageChain(
            [
                Plain('😘热烈欢迎 '),
                At(member.id),
                Plain(
                    f' 加入本群，入群时间为'
                    f'[{now.year}年{now.month}月{now.day}日 {now.hour}:{now.minute}:{now.second}]'
                    f'我是本群机器人（）,快来与群友们来互动吧~')
            ]
        )
    )
