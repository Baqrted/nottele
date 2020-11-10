"""Available Commands:

.froci

.duce

.patriarcato"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "froci":

        await event.edit(input_str)

        animation_chars = [

            "A MORTE",

            "                      I",

            "                           FROCI",

            "A MORTE I FROCI",
            "🔥🔥                 ",
            "         🔥🔥        ",
            "                   🔥🔥"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "duce":

        await event.edit(input_str)

        animation_chars = [

            "FIAMME      ",

            "                 NERE",
            
            "FIAMME NERE",
            
            "🖤🖤🔥🔥🖤🖤",
            
            "🔥🔥🖤🖤🔥🔥",
            "DUX MEA LUX"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


""


from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "patriarcato":

        await event.edit(input_str)

        animation_chars = [

            "kill the white man",

            "kill",

            "       the",

            "              white",
            
            "                          man",
            
            "ABBASSO GLI UOMINI BIANCHI",
            
            "ETERO, CIS, IN SALUTE",
            
            "VIVA IL MATRIARCATO"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])