from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("23801870"))
API_HASH = getenv("9645cfafdfc9be9a7a46fb4874992cf6")

BOT_TOKEN = getenv("6130919619:AAHluwxZM3x8fdBcmWU3tPHu2pliMxVfDPE", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5443679321"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SDV_BOTS")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SDV_BOTS")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5443679321").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
