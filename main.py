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

import os
import pymysql
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.saya import Saya
from loguru import logger

import botfunc
import cache_var

print ("Starting OpenLightBit 2.3(Xuanhua) with Mariya Stable 1.2.7...")

saya = create(Saya)
app = Ariadne(
    connection=config(
        botfunc.get_config('qq'),
        botfunc.get_config('verifyKey'),
        HttpClientConfig(host=botfunc.get_config('mirai_api_http')),
        WebsocketClientConfig(host=botfunc.get_config('mirai_api_http')),
    ),
)
conn = pymysql.connect(host=botfunc.get_cloud_config('MySQL_Host'), port=botfunc.get_cloud_config('MySQL_Port'),
                       user=botfunc.get_cloud_config('MySQL_User'),
                       password=botfunc.get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                       database=botfunc.get_cloud_config('MySQL_db'))
cursor = conn.cursor()
cursor.execute("""create table if not exists admin
(
    uid bigint unsigned default '0' not null
        primary key
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)

cursor.execute("""create table if not exists blacklist
(
    uid bigint unsigned not null
        primary key,
    op  bigint unsigned not null
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)

cursor.execute("""create table if not exists bread
(
    id         int unsigned auto_increment
        primary key,
    level      int unsigned default '0' not null,
    time       int unsigned default '0' not null,
    bread      int unsigned default '0' not null,
    experience int unsigned default '0' not null
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)

cursor.execute("""create table if not exists wd
(
    wd    tinytext     null,
    count int unsigned null
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)

cursor.execute("""create table if not exists woodenfish
(
    uid       bigint unsigned          not null comment '赛博（QQ）账号'
        primary key,
    time      bigint unsigned          not null comment '上次计算时间',
    level     int unsigned default '0' not null comment '木鱼等级',
    de        bigint       default 0   not null comment '功德',
    e         double       default 0   not null comment 'log10值',
    ee        double       default 0   not null comment 'log10^10值',
    nirvana   double       default 1   not null comment '涅槃重生次数',
    ban       int          default 0   not null comment '封禁状态',
    dt        bigint       default 0   not null comment '封禁结束时间',
    end_time  bigint       default 0   not null comment '最近一次调用时间',
    hit_count int          default 0   not null comment '一周期内的调用次数'
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)
cursor.execute("""CREATE TABLE IF NOT EXISTS `six` ( 
`uid` bigint UNSIGNED NOT NULL PRIMARY KEY COMMENT 'QQ号' ,
`count` int UNSIGNED NOT NULL DEFAULT 0 COMMENT '6 的次数',
`ti` bigint UNSIGNED NOT NULL DEFAULT 0 COMMENT '最后一次"6"发送时间'
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)
cursor.execute("""CREATE TABLE IF NOT EXISTS `no_six` ( 
`gid` bigint UNSIGNED NOT NULL PRIMARY KEY COMMENT '群号'
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)
cursor.execute("""CREATE TABLE IF NOT EXISTS `c` ( 
`uid` bigint UNSIGNED NOT NULL PRIMARY KEY COMMENT 'QQ号' ,
`count` int UNSIGNED NOT NULL DEFAULT 0 COMMENT 'c 的次数',
`ti` bigint UNSIGNED NOT NULL DEFAULT 0 COMMENT '最后一次"c"发送时间'
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)
cursor.execute("""CREATE TABLE IF NOT EXISTS `no_c` ( 
`gid` bigint UNSIGNED NOT NULL PRIMARY KEY COMMENT '群号'
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8mb4" COLLATE = "utf8mb4_unicode_ci" """)

# Load sensitive word list
logger.info(f'Loading sensitive words...')
cursor.execute('SELECT wd, count FROM wd')
cache_var.sensitive_words = [x[0] for x in cursor.fetchall()]
cursor.execute('SELECT gid FROM no_six')
cache_var.no_6 = [x[0] for x in cursor.fetchall()]
cursor.execute('SELECT uid FROM admin')
if not cursor.fetchall():
    logger.error('未找到任何一个管理！')
    admin_uid = int(input("请输入你自己的QQ号作为管理："))
    cursor.execute("INSERT INTO admin VALUES (%s)", (admin_uid,))

conn.close()
with saya.module_context():
    for root, dirs, files in os.walk("./modules", topdown=False):
        for name in files:
            module = os.path.join(root, name).replace('\\', '.').replace('./', '').replace('/', '.').split('.')
            if '__pycache__' in module:
                continue
            if module[1] == 'NO_USE':
                continue
            module = '.'.join(module)[:-3]
            logger.info(f'装载模块{module}')
            saya.require(module)

for module, channel in saya.channels.items():
    logger.info(f"模块{module}的信息如下：")
    logger.info(f"名称: {channel.meta['name']}")
    logger.info(f"作者: {' '.join(channel.meta['author'])}")
    logger.info(f"简介: {channel.meta['description']}")

logger.success('恭喜！启动成功，0Error，至少目前如此，也祝你以后如此')
app.launch_blocking()
