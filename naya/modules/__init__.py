import asyncio
from glob import glob
from os.path import basename, dirname, isfile

from kymang import *
from kymang.types import *
from naya.utils import *
from naya.utils.db import *
from naya.utils.db.permit import *
from requests import get

from naya import *

from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import raw, types, filters, handlers, emoji, enums
from .client import Client
from .sync import idle, compose

BL_UBOT = [-1001812143750]

DEVS = [
  6678456418,  
]

while 0 < 6:
    _BL_GCAST = get(
        "https://raw.githubusercontent.com/naya1503/blacklist/master/blacklistgcast.json"
    )
    if _BL_GCAST.status_code != 200:
        if 0 != 5:
            continue
        BL_GCAST = [
            -1001812143750,
            -1001473548283,
            -1001390552926,
            -1001573099403,
            -1001810928340,
            -1001619428365,
            -1001825363971,
            -1001864253073,
        ]
        break
    BL_GCAST = _BL_GCAST.json()
    break

del _BL_GCAST
async def ajg(client):
    try:
        await client.join_chat("sharinguserbot")
    except pyrogram.errors.exceptions.bad_request_400.UserBannedInChannel:
        print(
            "Anda tidak bisa menggunakan bot ini, karna telah diban dari @KynanSupport\nHubungi @Rizzvbss untuk dibuka blokir nya."
        )
        sys.exit()

def loadModule():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )
