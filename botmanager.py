import yaml
import json
from loguru import logger

import botfunc

global_setting = yaml.safe_load(open('./config.yaml', 'r', encoding='UTF-8'))

def bot_config(name: str):
    try:
        if name == "bot_qq":
            return botfunc.get_config('qq')
        else:
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
