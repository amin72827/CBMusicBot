import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("AgEtqVYAGz638XNJqcWbN-ucFRrNL7DVYs63aqq-Q8ub8bLhjrZrIrggI566Zcg0ksoiJ3OVKlaBhzUn17t6dYWvpYjtSMB7xa9Atf0vTuMKj5n4uMjakJIkgh7cNubq4I5llrf2PeFxwnVyDu1PnZP0j0wGoHl1G8FPY6uV2mAVTtPV8uXAxw4NjASUfLbZ-o6qA6fuf5C738gtl6dgRQU3PNZCmeIV9ZxeQHdjR_ZJU5v_qATWE12bt9LhUXEUruqR7cvu8Juh4AXyHbBe_veLWNtzOisXfzUmpfX4Fs-dH5Ykk0FGnQSkQ6UkWylUdPYtj7wWHZfnIGztSC26IWUaLoFv_wAAAAGC_6I6AA", "session")
BOT_TOKEN = getenv("7128782242:AAENypkyECvS57mm7nGhIQNvqkTWQS2VLeI")
BOT_NAME = getenv("BOT_NAME", "Nergiz Music Bot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("19769686"))
API_HASH = getenv("515b64f5d2d955cdd6aa85a808fd4cb4")
BOT_USERNAME = getenv("BOT_USERNAME", "NergizMusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Nergizmusicasistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NergizSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Nergizmusicsupport")
OWNER_NAME = getenv("OWNER_NAME", "Elsur_Psixoloq") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("6671591267")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://ravigotdu18272:<db_password>@cluster0.ifr2tes.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002621326403")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("7652416346").split()))
LANG = getenv("LANG", "id")
