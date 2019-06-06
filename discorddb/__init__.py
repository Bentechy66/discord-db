""""Main file for discord-db
Please, never use this in a real project
Ever
Seriously
Consider yourself warned"""

from .classes import *


def connect(token, discord_id):
    """
    For added memery, allows for sqlite-like syntax
    :param token: The Discord Token
    :param discord_id: The Guild ID
    :return: DiscordDB Object
    """
    return DiscordDB(token, discord_id)
