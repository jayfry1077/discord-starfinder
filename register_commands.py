from config import BOT_KEY, GUILD_IDS, SPELL_OPTIONS
import discord
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all())
# Declares slash commands through the client.
slash = SlashCommand(client, sync_commands=True)


@slash.slash(name="spells", description='look up information about a particular spell', guild_ids=GUILD_IDS, options=SPELL_OPTIONS)
async def _(ctx):
    pass

client.run(BOT_KEY)
