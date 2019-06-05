from .discord_interface import DiscordInterface


class DiscordDB:
    def __init__(self, discord_token, guild_id):
        """
        DiscordDB Constructor

        :param discord_token: The Discord Token
        :param guild_id: The Guild ID
        :return: DiscordDB Object
        """
        self.discord_token = "Bot " + discord_token
        self.guild_id = guild_id
        self.discord_interface = DiscordInterface(self.discord_token)

        self.queue = []

        # Get discord channels and cache them
        self.channel_cache = []
        self.update_channel_cache()

    def commit(self):
        """
        Commits all changes to the database

        :return: None
        """
        pass

    def update_channel_cache(self):
        """
        Updates the local cache of channels used to verify names etc

        :return: None
        """
        channel_objects = self.discord_interface.discord_get(f"guilds/{self.guild_id}/channels")
        self.channel_cache = channel_objects

    def create_database(self, database_name):
        """
        Creates a database (category) in the Guild.

        :param database_name: The name of the database (category)
        :return: a QueueAction object
        """
        channel_object = {  # The channel used as the "Database"
            "name": database_name,
            "type": 4
        }
        created_channel = self.discord_interface.discord_post(f"guilds/{self.guild_id}/channels", channel_object)

        return None  # TODO: Make it return a Database() object


class QueueAction:
    def __init__(self, type_index, action_object):
        """
        Constructor for QueueAction

        :param type_index: The index of the type of action to be performed. See SPEC.md
        :param action_object: The object to take action upon.
        """