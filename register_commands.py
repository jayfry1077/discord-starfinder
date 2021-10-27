from config import BOT_KEY, GUILD_IDS
import discord
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all())
# Declares slash commands through the client.
slash = SlashCommand(client, sync_commands=True)


@slash.slash(name="ping", guild_ids=GUILD_IDS)
async def _(ctx):
    pass

client.run(BOT_KEY)
