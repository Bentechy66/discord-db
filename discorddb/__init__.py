'''Main file for discord-db
Please, never use this in a real project
Ever
Seriously
Consider yourself warned'''

from .classes import *


def connect(token, id):
    """
    For added memery, allows for sqlite-like syntax
    :param token: The Discord Token
    :param id: The Guild ID
    :return: DiscordDB Object
    """
    return DiscordDB(token, id)
