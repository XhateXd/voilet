# ZeldrisRobot
# Copyright (C) 2017-2019, Paul Larsen
# Copyright (c) 2021, IDNCoderX Team, <https://github.com/IDN-C-X/ZeldrisRobot>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging
import os
import sys
import time

import spamwatch
import telegram.ext as tg
from pyrogram import Client, errors
from redis import StrictRedis
from telethon import TelegramClient
from telethon.sessions import MemorySession

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

LOGGER.info("[Zeldris] Starting Zeldris...")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "[Zeldris] You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("[Zeldris] Your OWNER_ID env variable is not a valid integer.")

    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
    except ValueError:
        raise Exception(
            "[Zeldris] Your dev users list does not contain valid integers."
        )

    try:
        SUPPORT_USERS = {int(x) for x in os.environ.get("SUPPORT_USERS", "").split()}
    except ValueError:
        raise Exception(
            "[Zeldris] Your support users list does not contain valid integers."
        )

    try:
        WHITELIST_USERS = {
            int(x) for x in os.environ.get("WHITELIST_USERS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Zeldris] Your whitelisted users list does not contain valid integers."
        )
    try:
        DEMONS = {
            int(x) for x in os.environ.get("DEMONS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Zeldris] Your demon users list does not contain valid integers."
        )

    try:
        WHITELIST_CHATS = {
            int(x) for x in os.environ.get("WHITELIST_CHATS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Zeldris] Your whitelisted chats list does not contain valid integers."
        )
    try:
        BLACKLIST_CHATS = {
            int(x) for x in os.environ.get("BLACKLIST_CHATS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Zeldris] Your blacklisted chats list does not contain valid integers."
        )

    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    DB_URI = "postgresql://lcxdmecj:fqnb5YV7fqrBTT2LFFsd9ZxWxR23x27T@castor.db.elephantsql.com/lcxdmecj"
    REDIS_URL = "redis://KawakiGod:KawakiGod64~@redis-12067.c285.us-west-2-2.ec2.cloud.redislabs.com:12067"
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    DONATION_LINK = os.environ.get("DONATION_LINK")
    LOAD = os.environ.get("LOAD", "").split()
    TEMP_DOWNLOAD_DIRECTORY = ("./")
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    DEL_CMDS = True
    STRICT_GBAN = True
 
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = True
    CUSTOM_CMD = os.environ.get("CUSTOM_CMD", False)
    API_WEATHER = os.environ.get("API_OPENWEATHER", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    SPAMWATCH = os.environ.get("SPAMWATCH_API", None)
    SPAMMERS = os.environ.get("SPAMMERS", None)

else:
    from zeldris.config import Config

    TOKEN = Config.TOKEN
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("[Zeldris] Your OWNER_ID variable is not a valid integer.")

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DEV_USERS = {int(x) for x in Config.DEV_USERS or []}
    except ValueError:
        raise Exception(
            "[Zeldris] Your dev users list does not contain valid integers."
        )

    try:
        SUPPORT_USERS = {int(x) for x in Config.SUPPORT_USERS or []}
    except ValueError:
        raise Exception(
            "[Zeldris] Your support users list does not contain valid integers."
        )

    try:
        WHITELIST_USERS = {int(x) for x in Config.WHITELIST_USERS or []}
    except ValueError:
        raise Exception(
            "[Zeldris] Your whitelisted users list does not contain valid integers."
        )
    try:
        DEMONS = {int(x) for x in Config.DEMONS or []}
    except ValueError:
        raise Exception(
            "[Zeldris] Your demons list does not contain valid integers."
        )
    try:
        WHITELIST_CHATS = {int(x) for x in Config.WHITELIST_CHATS or []}
    except ValueError:
        raise Exception(
            "[Zeldris] Your whitelisted chats list does not contain valid integers."
        )
    try:
        BLACKLIST_CHATS = {int(x) for x in Config.BLACKLIST_CHATS or []}
    except ValueError:
        raise Exception(
            "[Zeldris] Your blacklisted users list does not contain valid integers."
        )

    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    DB_URI = "postgresql://lcxdmecj:m1DTxq9pIupZW06XLM4AN89xsNIcbGJe@castor.db.elephantsql.com/lcxdmecj"
    REDIS_URL = "redis://KawakiGod:KawakiGod64~@redis-12067.c285.us-west-2-2.ec2.cloud.redislabs.com:12067"
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 8
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = True
    CUSTOM_CMD = Config.CUSTOM_CMD
    API_WEATHER = Config.API_OPENWEATHER
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = "Villainevil_Support"
    API_HASH = Config.API_HASH
    API_ID = Config.API_ID
    SPAMWATCH = Config.SPAMWATCH_API
    SPAMMERS = Config.SPAMMERS

# Dont Remove This!!!
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1791795037)
DEV_USERS.add(2043468602)
BOT_ID = 5092248582
DEMONS.add(977805775)
DEMONS.add(5288203109)
SUPPORT_USERS.add(5128342147)
SUPPORT_USERS.add(1835783426)
SUPPORT_USERS.add(5555455171)
SUPPORT_USERS.add(5147265129)

# Pass if SpamWatch token not set.
if SPAMWATCH is None:
    spamwtc = None
    LOGGER.warning("[Zeldris] Invalid spamwatch api")
else:
    spamwtc = spamwatch.Client(SPAMWATCH)

REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info("[Zeldris] Your redis server is now alive!")
except BaseException:
    raise Exception("[Zeldris] Your redis server is not alive, please check again.")
finally:
    REDIS.ping()
    LOGGER.info("[Zeldris] Your redis server is now alive!")

# Telethon
client = TelegramClient(MemorySession(), API_ID, API_HASH)
updater = tg.Updater(
    TOKEN,
    workers=min(32, os.cpu_count() + 4),
    request_kwargs={"read_timeout": 10, "connect_timeout": 10},
)
dispatcher = updater.dispatcher

pbot = Client("ErenPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
pbot.start()
    

DEV_USERS = list(DEV_USERS)
WHITELIST_USERS = list(WHITELIST_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)
DEMONS = list(DEMONS)

# Load at end to ensure all prev variables have been set
# pylint: disable=C0413
from zeldris.modules.helper_funcs.handlers import CustomCommandHandler

if CUSTOM_CMD and len(CUSTOM_CMD) >= 1:
    tg.CommandHandler = CustomCommandHandler


def spamfilters(text, user_id, chat_id):
    # print("{} | {} | {}".format(text, user_id, chat_id))
    if int(user_id) not in SPAMMERS:
        return False

    print("[Zeldris] This user is a spammer!")
    return True
