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

import asyncio
import json
import sys

import aiomysql
import portalocker
import redis
import requests_cache
import yaml
from loguru import logger

print ("Initializing data...")
def safe_file_read(filename: str, encode: str = "UTF-8", mode: str = "r") -> str or bytes:
    if mode == 'r':
        with open(filename, mode, encoding=encode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            tmp = file.read()
            portalocker.unlock(file)
    else:
        with open(filename, mode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            tmp = file.read()
            portalocker.unlock(file)

    return tmp


def safe_file_write(filename: str, s, mode: str = "w", encode: str = "UTF-8"):
    if 'b' not in mode:
        with open(filename, mode, encoding=encode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            file.write(s)
            portalocker.unlock(file)
    else:
        with open(filename, mode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            file.write(s)
            portalocker.unlock(file)


loop = asyncio.get_event_loop()
try:
    config_yaml = yaml.safe_load(open('config.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('config.yaml', """qq: 10001  # 运行时登录的 QQ 号
verifyKey: "@(HANKuohu2)33###@MiraiApiHTTP"  # MAH 的 verifyKey
recall: 30  # 涩图撤回等待时长（单位：秒）
# 如果你没有那么多涩图API可以填一样的URL
setu_api: "https://api.jiecs.top/lolicon?r18=2"  # 涩图 API
setu_api2: "https://www.acy.moe/api/r18"  # 涩图 API 2
setu_api2_probability: 5 # 表示【涩图 API 2】的被调用的概率为 1/n
NewFriendRequestEvent: true  # 是否自动通过好友添加：true -> 自动通过 | false -> 自动拒绝
BotInvitedJoinGroupRequestEvent: true  # 是否自动通过加群邀请：同上
mirai_api_http: "http://localhost:8088"  # 连接到 MAH 的地址
count_ban: 4  # 木鱼调用频率限制""")
    logger.error(
        'config.yaml 未创建，程序已自动创建，请填写该文件的内容')
    sys.exit(1)
try:
    cloud_config_json = json.load(open('cloud.json', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('cloud.json', """{
    "QCloud_Secret_id": "",  # QCloud用户ID，可留空
    "QCloud_Secret_key": "", # QCloud密钥ID，可留空
    "MySQL_User": "", # 你的MySQL用户
    "MySQL_Pwd": "", # 你的MySQL密码
    "MySQL_Port": 3306, # 你的MySQL端口，一般都是3306，如果是其他的需要修改
    "MySQL_Host": "localhost", # MySQL主机
    "MySQL_db": "", # MySQL数据库名称
    "Redis_Host": "localhost", # Redis主机
    "Redis_port": 6379, # Redis主机端口，一般都是6379
    "Redis_Pwd": "", # Redis主机密码
    "snao_key": "" # Your SauseNAO key
  }
# 最后配置完后，请把所有的注释和#全部删除，避免发生错误（包括本条)""")
    logger.error(
        'cloud.json 未创建，程序已自动创建，请参考注释和 https://github.com/daizihan233/KuoHuBit/issues/17 填写该文件的内容')
    sys.exit(1)
try:
    dyn_yaml = yaml.safe_load(open('dynamic_config.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('dynamic_config.yaml', """mute:
- 767949862
- 556482025
- 781601227
- 689165612
- 211126861
- 643981003
- 347997878
- 772177022
word:
- 620563816
- 469903354
- 643981003""")
    logger.warning('dynamic_config.yaml 已被程序自动创建')
    dyn_yaml = yaml.safe_load(open('dynamic_config.yaml', 'r', encoding='UTF-8'))
try:
    light_khapi_yaml = yaml.safe_load(open('openlbit.yml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('openlbit.yml', """# OpenLightBit配置文件
api-ip: "0.0.0.0"
api-port: 8989
bot-name: "OpenLightBit"
bot-ver: "2.5" """)
    logger.warning('openlbit.yml 已被程序自动创建')
    light_khapi_yaml = yaml.safe_load(open('openlbit.yml', 'r', encoding='UTF-8'))

def get_config(name: str):
    try:
        return config_yaml[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return None


def get_cloud_config(name: str):
    try:
        return cloud_config_json[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return None


def get_dyn_config(name: str):
    try:
        return dyn_yaml[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return None

def lbit_conf(name: str):
    try:
        return light_khapi_yaml[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return None

async def select_fetchone(sql, arg=None):
    conn = await aiomysql.connect(host=get_cloud_config('MySQL_Host'),
                                  port=get_cloud_config('MySQL_Port'),
                                  user=get_cloud_config('MySQL_User'),
                                  password=get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                                  db=get_cloud_config('MySQL_db'), loop=loop)

    cur = await conn.cursor()
    if arg:
        await cur.execute(sql, arg)
    else:
        await cur.execute(sql)
    result = await cur.fetchone()
    await cur.close()
    conn.close()
    return result


async def select_fetchall(sql, arg=None):
    conn = await aiomysql.connect(host=get_cloud_config('MySQL_Host'),
                                  port=get_cloud_config('MySQL_Port'),
                                  user=get_cloud_config('MySQL_User'),
                                  password=get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                                  db=get_cloud_config('MySQL_db'), loop=loop)

    cur = await conn.cursor()
    if arg:
        await cur.execute(sql, arg)
    else:
        await cur.execute(sql)
    result = await cur.fetchall()
    await cur.close()
    conn.close()
    return result


async def run_sql(sql, arg):
    conn = await aiomysql.connect(host=get_cloud_config('MySQL_Host'),
                                  port=get_cloud_config('MySQL_Port'),
                                  user=get_cloud_config('MySQL_User'),
                                  password=get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                                  db=get_cloud_config('MySQL_db'), loop=loop)

    cur = await conn.cursor()
    await cur.execute(sql, arg)
    await cur.execute("commit")
    await cur.close()
    conn.close()


async def get_all_admin() -> list:
    tmp = await select_fetchall("SELECT uid FROM admin")
    t = []
    for i in tmp:
        t.append(i[0])
    logger.debug(t)
    return list(t)


async def get_all_sb() -> list:
    tmp = await select_fetchall('SELECT uid FROM blacklist')
    t = []
    for i in tmp:
        t.append(i[0])
    return t


if get_cloud_config("Redis_Pwd") is not None:
    backend = requests_cache.RedisCache(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port'),
        password=get_cloud_config('Redis_Pwd')
    )
    p = redis.ConnectionPool(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port'),
        password=get_cloud_config('Redis_Pwd')
    )
else:
    backend = requests_cache.RedisCache(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port')
    )
    p = redis.ConnectionPool(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port')
    )
session = requests_cache.CachedSession("global_session", backend=backend, expire_after=360)

p = redis.ConnectionPool(host=get_cloud_config('Redis_Host'), port=get_cloud_config('Redis_port'))
r = redis.Redis(connection_pool=p, decode_responses=True)
