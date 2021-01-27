from discord import Intents
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase

PREFIX = "b-"
OWNER_IDS = [689158123352883340]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intents=Intents.all()
        )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running byul...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("byul connected")
    
    async def on_disconnect(self):
        print("byul disconnected")
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(693443636406386760)
            print("byul ready")

            channel = self.get_channel(697769479710703777)
            #await channel.send("**Byul** is online.")

            embed = Embed(title="Now online!!", description = "**Byul** is now online.", 
                            colour=0xC2EABD, timestamp=datetime.utcnow())
            fields = [("***Mood***", "*Sleepy zzz*", True),
                        ("***Favourite parent***", "***Dawnu***", True)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            embed.set_footer(text="Take a lollipop!")
            embed.set_author(name="Dawnu", icon_url=self.guild.icon_url)
            await channel.send(embed=embed)

        else:
            print("byul reconnected")

    async def on_message(self, message):
        pass


bot = Bot()