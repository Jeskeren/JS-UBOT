# Port By @VckyouuBitch From Geez-Projects
# recode from rizkypratama2
# # Copyright (C) 2021 Geez-Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.ftype(?: |$)(.*)")
async def _(rizky):
    t = rizky.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await rizky.ban_time(t)
            except BaseException:
                return await rizky.edit("`Incorrect Format`")
    await rizky.edit(f"`Kebanyakan fake hidup lu ngentot!`")
    await rizky.edit(f"`Memulai Fake Typing {t} detik.`")
    async with rizky.client.action(rizky.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(rizky):
    t = rizky.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await rizky.ban_time(t)
            except BaseException:
                return await rizky.edit("`Incorrect Format`")
    await rizky.edit(f"`Memulai Fake Audio dalam {t} detik.`")
    async with rizky.client.action(rizky.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(rizky):
    t = rizky.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await rizky.ban_time(t)
            except BaseException:
                return await rizky.edit("`Incorrect Format`")
    await rizky.edit(f"`Memulai Fake video dalam {t} detik.`")
    async with rizky.client.action(rizky.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(rizky):
    t = rizky.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await rizky.ban_time(t)
            except BaseException:
                return await rizky.edit("`Incorrect Format`")
    await rizky.edit(f"`Memulai Fake Play game dalam {t} detik.`")
    async with rizky.client.action(rizky.chat_id, "game"):
        await asyncio.sleep(t)

CMD_HELP.update(
    {
        "faction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ftyping : .faudio : .fvideo : .fgame <jumlah text>`"
        "\n• : Fake action ini Berfungsi dalam group"
    }
)
