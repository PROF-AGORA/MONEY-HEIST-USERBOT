import os

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    ms = 4
    ALIVE = Config.ALIVE_NAME
    await tgbot.send_message(
        event.chat_id,
        LEGEND_IMG,
        f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』",
    )
