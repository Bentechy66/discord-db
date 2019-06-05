import requests
from json import loads

from .config import discord_token
from .exceptions import Discord403Exception, Discord404Exception

base_url = "https://discordapp.com/api/v6/{}"


def discord_post(endpoint, data):
    """
    Makes a POST request to the supplied endpoints. Adds the base_url and authorization token from the config file
    automatically.

    :param endpoint: The discord endpoint to make the request to. Do not add a proceeding slash.
    :param data: A JSON dictionary containing data to post to Discord
    :return: The response from the Discord gateway, parsed to JSON
    """
    auth_header = {
        "Authorization": discord_token
    }
    r = requests.post(base_url.format(endpoint), data=data, headers=auth_header)  # Make the request to discord

    if r.status_code == 404:
        raise Discord404Exception(f"The Discord Gateway returned a 404 response. \nResponse: {r.text}")
    elif r.status_code == 403:
        raise Discord403Exception(f"The Discord Gateway returned a 403 response. \nResponse: {r.text}")

    return loads(r.text)  # Return the request response, parsed as JSON


def send_message(channel_id, message_content):
    message_object = {
        "content": message_content
    }
    discord_post(f"channels/{channel_id}/messages", message_object)