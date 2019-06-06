from .discord_interface import DiscordInterface
from .exceptions import InvalidNameException


class DiscordDB:

    # ---------
    # Internals
    # ---------

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

        self.action_queue = []

        # Get discord channels and cache them
        self.category_cache = []
        self.update_channel_cache()

    def append_queue_action(self, type_index, arg_array):
        """

        :param type_index:
        :param arg_array:
        :return: The added QueueAction object
        """
        queue_object = QueueAction(type_index, arg_array)
        self.action_queue.append(queue_object)
        return queue_object

    def commit(self):
        """
        Commits all changes to the database

        :return: None
        """
        for action in self.action_queue:
            if action.type == 0:  # Database Create request
                channel_object = {  # The channel used as the "Database"
                    "name": action.args[0],
                    "type": 4
                }
                self.discord_interface.discord_post(f"guilds/{self.guild_id}/channels", channel_object)

            elif action.type == 1:
                # TODO: Delete child channels
                for channel in self.category_cache:
                    if channel["name"] == action.args[0]:
                        self.discord_interface.discord_delete(f"channels/{channel['id']}")
                        self.category_cache.remove(action.args[1])
                        return

        self.update_channel_cache()

    def update_channel_cache(self):
        """
        Updates the local cache of channels used to verify names etc

        :return: None
        """
        channel_objects = self.discord_interface.discord_get(f"guilds/{self.guild_id}/channels")
        category_objects = []
        for channel in channel_objects:
            if channel["type"] == 4:
                category_objects.append(channel)
        self.category_cache = category_objects

    # ------------------------
    #  # User-friendly methods
    # ------------------------

    # ------------------------
    #  ## Database methods
    # ------------------------

    def create_database(self, database_name):
        """
        Creates a database (category) in the Guild.

        :param database_name: The name of the database (category)
        :return: a QueueAction object
        """

        for channel_object in self.category_cache:  # Check name doesn't already exist
            if channel_object["name"] == database_name:
                raise InvalidNameException("Name already exists either as a Database or Table")

        category_object = {  # Temporary object to ensure you can't create another database with the same name
            "name": database_name,
            "temp": True
        }

        self.category_cache.append(category_object)

        return self.append_queue_action(0, [database_name])

    def delete_database(self, database_name):
        """
        Deletes a database (category) from the Guild. Also irreversibly deletes all tables in it.

        :param database_name: The name of the database (category) to delete
        :return: a QueueAction object
        """

        found = False
        to_delete = {}

        for category_object in self.category_cache:
            if category_object["name"] == database_name:
                found = True
                to_delete = category_object
                break

        if not found:
            raise InvalidNameException("Could not find that database to delete")

        self.append_queue_action(1, [database_name, to_delete])


class QueueAction:
    def __init__(self, type_index, arg_array=[]):
        """
        Constructor for QueueAction

        :param type_index: The index of the type of action to be performed. See SPEC.md
        :param arg_array: An array of args to act upon depending on type_index.
        :return: QueueAction object
        """
        self.type = type_index
        self.args = arg_array
