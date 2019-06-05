import configparser
import json
import os

# This file performs dynamic config loading logic.
#
# Because of how python caches imports, we don't need to worry about
# this file being imported multiple times.

# Check if we actually have a config to load
if not os.path.exists("config.ini"):
    print()
    print("[!] No configuration file exists!")
    # If we have a default config available...
    if os.path.exists("config.ini.example"):
        # ... clone the default config...
        with open("config.default.ini") as default:
            with open("config.ini", "w") as new:
                new.write(default.read())
        # ... and tell the user!
        print("[-] A new config has been created from config.ini.example")

    # Even if we reloaded the default, it's going to need
    # tweaking
    print("[-] You should configure the server before attempting to start it")
    quit()

# Load from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Check if we're actually loading a default config
try:
    config.get("Config", "is_default")
except configparser.NoOptionError:
    pass
except configparser.NoSectionError:
    pass
else:
    print()
    print("[!] The loaded config appears to be a default config!")
    print("[!] Did you remember to remove is_default?")
    quit()

# [Login]
discord_token = config.get("Login", "discord_token")

# [Guild]
guild_id = config.getint("Guild", "guild_id")


# Clean up for when import *'ing
if __name__ != "__main__":
    del os, json, configparser, config
