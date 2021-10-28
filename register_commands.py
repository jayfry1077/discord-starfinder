##############################################
# Run this script locally to add bot commands
##############################################
import requests
import os
from dotenv import load_dotenv
from config import BOT_KEY, GUILD_IDS

load_dotenv()

bot_id = os.getenv('bot_id')
bot_key = os.getenv('bot_key')


commands = {
    "name": "lookup",
    "description": "Starfinder lookup actions",
    "options": [
        {
            "name": "spell",
            "description": "Look up a spell by title",
            "type": 1,
            "options": [
                {
                    "name": "title",
                            "description": "Title of the spell",
                            "type": 3,
                            "required": True
                },
                {
                    "name": "attributes",
                            "description": "Get attribute information",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {
                                    "name": "All",
                                    "value": "ALL"
                                },
                                {
                                    "name": "Level Requirements",
                                    "value": "level_requirements"
                                }, {
                                    "name": "School",
                                    "value": "school"
                                }, {
                                    "name": "Casting Time",
                                    "value": "casting_time"
                                }, {
                                    "name": "Range",
                                    "value": "range"
                                }, {
                                    "name": "Area",
                                    "value": "area"
                                }, {
                                    "name": "Targets",
                                    "value": "targets"
                                }, {
                                    "name": "Effect",
                                    "value": "effect"
                                }, {
                                    "name": "Duration",
                                    "value": "duration"
                                }, {
                                    "name": "Saving Throw",
                                    "value": "saving_throw"
                                }, {
                                    "name": "Spell Resistance",
                                    "value": "spell_resistance"
                                }, {
                                    "name": "Description",
                                    "value": "description"
                                }, {
                                    "name": "Brief Description",
                                    "value": "brief_description"
                                }, {
                                    "name": "Requires Resolve",
                                    "value": "requires_resolve"
                                }
                            ]
                }
            ]
        },
        {
            "name": "ability",
            "description": "Look up a ability by title",
            "type": 1,
            "options": [
                {
                    "name": "title",
                            "description": "Title of the ability",
                            "type": 3,
                            "required": True
                },
                {
                    "name": "attributes",
                            "description": "Get ability information",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {"name": "All", "value": "ALL"}, {"name": "title", "value": "title"}, {"name": "body", "value": "body"}, {
                                    "name": "prerequisites", "value": "prerequisites"}, {"name": "level_requirement", "value": "level_requirement"}
                            ]
                }
            ]
        },
        {
            "name": "weapon",
            "description": "Look up a weapon by title",
            "type": 1,
            "options": [
                {
                    "name": "title",
                            "description": "Title of the weapon",
                            "type": 3,
                            "required": True
                },
                {
                    "name": "attributes",
                            "description": "Get weapon information",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {"name": "All", "value": "ALL"}, {"name": "title", "value": "title"}, {"name": "abbrev", "value": "abbrev"}, {"name": "bulk", "value": "bulk"}, {"name": "price", "value": "price"}, {"name": "description", "value": "description"}, {"name": "item_level", "value": "item_level"}, {
                                    "name": "damage", "value": "damage"}, {"name": "range", "value": "range"}, {"name": "critical", "value": "critical"}, {"name": "special", "value": "special"}, {"name": "weapon_categories", "value": "weapon_categories"}, {"name": "capacity", "value": "capacity"}, {"name": "usage", "value": "usage"}
                            ]
                }
            ]
        },
        {
            "name": "armor",
            "description": "Look up a armor by title",
            "type": 1,
            "options": [
                {
                    "name": "title",
                            "description": "Title of the armor",
                            "type": 3,
                            "required": True
                },
                {
                    "name": "attributes",
                            "description": "Get armor information",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {"name": "All", "value": "ALL"}, {"name": "title", "value": "title"}, {"name": "abbrev", "value": "abbrev"}, {"name": "bulk", "value": "bulk"}, {"name": "price", "value": "price"}, {"name": "description", "value": "description"}, {
                                    "name": "item_level", "value": "item_level"}, {"name": "eac_bonus", "value": "eac_bonus"}, {"name": "kac_bonus", "value": "kac_bonus"}, {"name": "max_dex_bonus", "value": "max_dex_bonus"}, {"name": "armor_check_penalty", "value": "armor_check_penalty"}
                            ]
                }
            ]
        },
        {
            "name": "creature",
            "description": "Look up a creature by title",
            "type": 1,
            "options": [
                {
                    "name": "title",
                            "description": "Title of the creature",
                            "type": 3,
                            "required": True
                },
                {
                    "name": "attributes_1",
                            "description": "Get creature information",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {"name": "All", "value": "ALL"}, {"name": "title", "value": "title"}, {"name": "flavor_text", "value": "flavor_text"}, {"name": "cr", "value": "cr"}, {"name": "xp", "value": "xp"}, {"name": "size", "value": "size"}, {"name": "alignment", "value": "alignment"}, {"name": "creature_type", "value": "creature_type"}, {"name": "creature_subtype", "value": "creature_subtype"}, {"name": "initiative", "value": "initiative"}, {"name": "senses", "value": "senses"}, {"name": "perception", "value": "perception"}, {
                                    "name": "aura", "value": "aura"}, {"name": "hp", "value": "hp"}, {"name": "rp", "value": "rp"}, {"name": "eac", "value": "eac"}, {"name": "kac", "value": "kac"}, {"name": "fort_save", "value": "fort_save"}, {"name": "ref_save", "value": "ref_save"}, {"name": "will_save", "value": "will_save"}, {"name": "defensive_abilities", "value": "defensive_abilities"}, {"name": "immunities", "value": "immunities"}, {"name": "resistances", "value": "resistances"}, {"name": "weaknesses", "value": "weaknesses"}
                            ]
                },
                {
                    "name": "attributes_2",
                            "description": "Get creature information",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {"name": "spell_resistance",
                                 "value": "spell_resistance"}, {"name": "damage_reduction", "value": "damage_reduction"}, {"name": "speed", "value": "speed"}, {"name": "melee", "value": "melee"}, {"name": "ranged", "value": "ranged"}, {"name": "space", "value": "space"}, {"name": "reach", "value": "reach"}, {"name": "offensive_abilities", "value": "offensive_abilities"}, {"name": "spell_like_abilities", "value": "spell_like_abilities"}, {"name": "spells_known", "value": "spells_known"}, {"name": "str", "value": "str"}, {"name": "dex", "value": "dex"}, {"name": "con", "value": "con"}, {"name": "int", "value": "int"}, {"name": "wis", "value": "wis"}, {"name": "cha", "value": "cha"}, {"name": "skills", "value": "skills"}, {"name": "languages", "value": "languages"}, {"name": "gear", "value": "gear"}, {"name": "other_abilities", "value": "other_abilities"}, {"name": "environment", "value": "environment"}, {"name": "organization", "value": "organization"}, {"name": "special_abilities", "value": "special_abilities"}, {"name": "description", "value": "description"}
                            ]
                }
            ]
        }
    ]
}


headers = {
    "Authorization": f"Bot {bot_key}"
}


def update_commands(url, json):
    r = requests.post(url, headers=headers, json=json)

    print(r.content)


def get_commands(url):
    r = requests.get(url, headers=headers)

    print(r.content)


def delete_commands(url):
    r = requests.delete(url, headers=headers)

    print(r.content)


# update_commands(
#     f"https://discord.com/api/v8/applications/{bot_id}/commands", commands)

# for id in GUILD_IDS:
#     update_commands(
#         f"https://discord.com/api/v8/applications/{bot_id}/guilds/{id}/commands", commands)

# get_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# delete_commands(
#     f"https://discord.com/api/v8/applications/{bot_id}/commands/903101966304051241")
