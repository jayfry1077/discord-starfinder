from discord_slash.utils.manage_commands import create_option
from dotenv.main import load_dotenv
import os
load_dotenv()


GUILD_IDS = [int(_id) for _id in os.getenv("guild_ids").split(',')]
BOT_KEY = os.getenv("bot_key")


SPELL_OPTIONS = [create_option(name='title', description='Name of the spell', option_type=3, required=True),
                 create_option(
                     name='level_requirements', description='level requirements lookup', option_type=3, required=False)
                 ]
