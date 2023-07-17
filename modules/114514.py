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

import loguru
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message import Source
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.saya import Channel
from graia.scheduler import timers
from graia.scheduler.saya import SchedulerSchema

import botfunc
import cache_var

channel = Channel.current()
channel.name("114514")
channel.description("臭死力")
channel.author("Emerald-AM9")


@channel.use(SchedulerSchema(timers.crontabify("45 11 * * * 14")))
async def inm(app: Ariadne):
    for group in cache_var.inm:
        try:
            await app.send_group_message(
                target=group,
                message=f"哼哼哼，{'啊' * random.randint(5, 20)}"
            )
        except ValueError:
            loguru.logger.warning(
                f'{group} 不存在！请检查机器人是否被踢出，请尝试让机器人重新加群或手动删除数据库数据并重启机器人！')


@listen(GroupMessage)
@decorate(MatchContent("臭死力"))
async def homo(app: Ariadne, group: Group, source: Source, event: GroupMessage):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    if group.id in cache_var.inm:
        return
    cache_var.inm.append(group.id)
    await botfunc.run_sql("INSERT INTO inm VALUES (%s)", (group.id,))
    await app.send_message(
        target=group,
        quote=source,
        message='草'
    )


@listen(GroupMessage)
@decorate(MatchContent("香死力"))
async def homo(app: Ariadne, group: Group, source: Source, event: GroupMessage):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    if group.id not in cache_var.inm:
        return
    cache_var.inm.remove(group.id)
    await botfunc.run_sql("DELETE FROM inm WHERE gid=%s", (group.id,))
    await app.send_message(
        target=group,
        quote=source,
        message='艹'
    )