import yaml
import json
from loguru import logger

global_setting = yaml.safe_load(open('./yamls/General.yaml', 'r', encoding='UTF-8'))
rand_sents = {
    "zh-cn": json.load(open('./jsons/zh-cn/rand_sents.json', 'r', encoding='UTF-8')),
    "zh-hk": json.load(open('./jsons/zh-hk/rand_sents_hk.json', 'r', encoding='UTF-8')),
}
def bot_config(name: str):
    try:
        return global_setting[name]
    except KeyError:
        logger.warning(f'{name}:Not avaliable')
        return None


def sents_config(name: str, lang: str):
    try:
        return rand_sents[lang][name]
    except KeyError:
        logger.warning(f'{name}:Not available in {lang}')
        return None


def students_voices(name: str):
    try:
        return voices[name]
    except KeyError:
        logger.warning(f'{name}:Not available')
        return None