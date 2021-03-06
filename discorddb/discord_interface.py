import requests
from json import loads

from .exceptions import Discord403Exception, Discord404Exception

base_url = "https://discordapp.com/api/v7/{}"


class DiscordInterface:
    # ---------------
    # Class functions
    # ---------------
    def __init__(self, discord_token):
        self.discord_token = discord_token

    # -------------------
    # Interface functions
    # -------------------

    def discord_post(self, endpoint, data):
        """
        Makes a POST request to the supplied endpoints. Adds the base_url and Discord token automatically.

        :param endpoint: The discord endpoint to make the request to. Do not add a proceeding slash.
        :param data: A JSON dictionary containing data to post to Discord

        :raises: Discord404Exception: If the Discord API returns a 404, this exception is thrown
        :raises: Discord403Exception: If the Discord API returns a 403, this exception is thrown

        :return: The response from the Discord gateway, parsed to JSON
        """
        auth_header = {
            "Authorization": self.discord_token
        }
        r = requests.post(base_url.format(endpoint), json=data, headers=auth_header)  # Make the request to discord

        if r.status_code == 404:
            raise Discord404Exception(f"The Discord Gateway returned a 404 response. \nResponse: {r.text}")
        elif r.status_code == 403:
            raise Discord403Exception(f"The Discord Gateway returned a 403 response. \nResponse: {r.text}")

        return loads(r.text)  # Return the request response, parsed as JSON

    def discord_get(self, endpoint):
        """
        Makes a GET request to the supplied endpoints. Adds the base_url and Discord token automatically

        :param endpoint: The Discord endpoint to make the request to. Do not add a proceeding slash.

        :raises: Discord404Exception: If the Discord API returns a 404, this exception is thrown
        :raises: Discord403Exception: If the Discord API returns a 403, this exception is thrown

        :return: The response from the Discord gateway, parsed to JSON
        """

        auth_header = {
            "Authorization": self.discord_token
        }
        r = requests.get(base_url.format(endpoint), headers=auth_header)  # Make the request to discord

        if r.status_code == 404:
            raise Discord404Exception(f"The Discord Gateway returned a 404 response. \nResponse: {r.text}")
        elif r.status_code == 403:
            raise Discord403Exception(f"The Discord Gateway returned a 403 response. \nResponse: {r.text}")

        return loads(r.text)  # Return the request response, parsed as JSON

    def discord_delete(self, endpoint):
        """
        Makes a GET request to the supplied endpoints. Adds the base_url and Discord token automatically

        :param endpoint: The Discord endpoint to make the request to. Do not add a proceeding slash.

        :raises: Discord404Exception: If the Discord API returns a 404, this exception is thrown
        :raises: Discord403Exception: If the Discord API returns a 403, this exception is thrown

        :return: The response from the Discord gateway, parsed to JSON
        """

        auth_header = {
            "Authorization": self.discord_token
        }
        r = requests.delete(base_url.format(endpoint), headers=auth_header)  # Make the request to discord

        if r.status_code == 404:
            raise Discord404Exception(f"The Discord Gateway returned a 404 response. \nResponse: {r.text}")
        elif r.status_code == 403:
            raise Discord403Exception(f"The Discord Gateway returned a 403 response. \nResponse: {r.text}")

        return loads(r.text)  # Return the request response, parsed as JSON
