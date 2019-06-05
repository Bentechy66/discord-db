# discord-db
The World's Worst Database System™

*Yes, I'm aware this was a terrible idea. I got incredibly bored one time and this happened.*

# Setup / Usage
```python3
import discorddb

guild_db = discorddb.connect(bot_token, guild_id)

guild_db.create_database(db_name)
guild_db.commit()
[...]
```

# Important Note
Please never, ever use this in a real project, for the sake of:
 - Your Sanity
 - My Sanity
 - Your Project's Speed
 - Discord's Infrastructure
 - Your Discord API credentials
 - Probably More

# About this Project
## Motivation
N/A

## Author
Ben Griffiths (https://github.com/bentechy66)
