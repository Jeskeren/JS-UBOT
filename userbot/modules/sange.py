# ยฉtofik_dn
# Minta tipis tipis

import random

from userbot import CMD_HELP
from userbot.events import register
from userbot import DEFAULTUSER
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.vidkep$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@asupanbanget", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"๐๐ผ๐๐ผ๐๐ผ ๐๐ผ๐๐๐๐ผ๐, ๐๐๐ ๐ผ๐๐๐๐ผ๐๐๐๐ผ ๐๐๐ฟ [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("๐๐ถ๐ณ๐ข๐ฏ๐จ ๐ฃ๐ฆ๐ณ๐ถ๐ฏ๐ต๐ถ๐ฏ๐จ ๐บ๐ข, ๐๐ข๐ฅ๐ข๐ฉ๐ข๐ญ ๐ฎ๐ข๐ถ ๐ค๐ฐ๐ญ๐ช.")

@register(outgoing=True, pattern=r"^\.deswe$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"๐พ๐๐๐๐๐๐!!! ๐๐๐ ๐๐ ๐ฟ๐๐๐ผ๐ ๐พ๐๐๐ [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`๐ ๐ข๐ฉ ๐๐ถ๐ณ๐ข๐ฏ๐จ ๐ฃ๐ฆ๐ณ๐ถ๐ฏ๐ต๐ถ๐ฏ๐จ ๐ญ๐ถ ๐ฃ๐ข๐ฏ๐จ...`")


@register(outgoing=True, pattern=r"^\.deswo$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowo", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"๐พ๐๐๐๐๐๐!!! ๐๐๐ ๐๐ ๐ฟ๐๐๐ผ๐ ๐พ๐๐๐[{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`๐ ๐ข๐ฉ ๐๐ถ๐ณ๐ข๐ฏ๐จ ๐๐ฆ๐ณ๐ถ๐ฏ๐ต๐ถ๐ฏ๐จ ๐ญ๐ถ ๐ฏ๐ฆ๐ฏ๐จ...`")

        
@register(outgoing=True, pattern=r"^\.syg$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Nih Ayang Aku ๐ [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("๐๐ข๐ฅ๐ข ๐ ๐ข๐ฏ๐จ ๐๐ข๐ถ ๐๐ข๐ฎ๐ข ๐๐ฐ ๐๐ข๐ณ๐ฆ๐ฏ๐ข ๐๐ฐ ๐๐ฆ๐ฌ๐ช๐ญ ๐ฌ๐ข๐บ๐ข ๐ฃ๐ข๐ซ๐ถ ๐ฑ๐ข๐ณ๐ต๐ข๐ช ๐ฃ๐ฆ๐ฌ๐ข๐ด๐ข๐ฏ๐คญ.")


CMD_HELP.update(
    {
        "asupan": "**Plugin : **`asupan`\
        \n\n  โข  **Syntax :** `.vidkep`\
        \n  โข  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  โข  **Syntax :** `.deswo` `.deswe`\
        \n  โข  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
        \n\n  โข  **Syntax :** `.syg`\
        \n  โข  **Function : **Untuk Mencari ayang buat cowok yang jomblo.\
    "
    }
)
