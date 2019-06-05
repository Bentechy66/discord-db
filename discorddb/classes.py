from .discord_interface import DiscordInterface


class DiscordDB:
    def __init__(self, discord_token, guild_id):
        """
        DiscordDB Constructor
        :param token: The Discord Token
        :param id: The Guild ID
        :return: DiscordDB Object
        """
        self.discord_token = "Bot " + discord_token
        self.guild_id = guild_id
        self.discord_interface = DiscordInterface(self.discord_token)

    def create_database(self, database_name):
        """
        Creates a database (category) in the Guild.

        :param database_name: The name of the database (category)
        :return: a Database object
        """
        channel_object = {  # The channel used as the "Database"
            "name": database_name,
            "type": 4
        }
        created_channel = self.discord_interface.discord_post(f"guilds/{self.guild_id}/channels", channel_object)

        return None  # TODO: Make it return a Database() object
