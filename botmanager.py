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

import yaml
import json
from loguru import logger

try:
    global_setting = yaml.safe_load(open('yamls/General.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('yamls/General.yaml', """bot_qq : 
su : []
verifyKey : ""
setuapi : "https://iw233.cn/API/Random.php" 
setuapi1 : "https://api.jiecs.top/lolicon?r18=0"
headapi: "https://q4.qlogo.cn/headimg_dl?dst_uin={six_qid}&spec=640"
ban_group : [


]
ban_user : [


]""")
    logger.error('./yamls/General.yaml 未创建，程序已自动创建，请填写该文件的内容')
    sys.exit(1)

try:
    rand_sents = yaml.safe_load(open('./yamls/rand_sentence.yaml','r',encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('yamls/rand_sentence.yaml', """rand_sentence : [
                "这是机器人随机发送的内容",
                "可以通过更改这里的内容来实现不同效果",
                "祝你好运"
                ]""")
    logger.success('./yamls/rand_sentence.yaml 未创建，程序已自动创建。')
    rand_sents = yaml.safe_load(open('./yamls/rand_sentence.yaml','r',encoding='UTF-8'))

voices = yaml.safe_load(open('./yamls/Voices.yaml', 'r', encoding='UTF-8'))
def bot_config(name: str):
    try:
        return global_setting[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None


def sents_config(name: str, lang: str):
    try:
        return rand_sents[lang][name]
    except KeyError:
        logger.error(f'宁确定有{lang} - {name}这个东西?')
        return None


def students_voices(name: str):
    try:
        return voices[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None