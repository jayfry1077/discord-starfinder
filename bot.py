from config import BOT_KEY
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot)

bot.run(BOT_KEY)
