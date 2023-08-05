# Dismusic
Making music bot in two lines of code

# Installation
`pip install dismusic`

# Usage

Making a simple bot

```python
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('dismusic')

TOKEN = 'TOKEN_HERE'
bot.run(TOKEN)
```

# Commands

**play** - `Play a song or playlist` \
**pause** - `Pause player` \
**connect** - `Connect to vc` \
**seek** - `Seek player` \
**nowplaying** - `Now playing` \
**queue** - `See queue` \
**equalizer** - `Set equalizer` \
**volume** - `Set volume` \
**resume** - `Resume player` \
**loop** - `Loop song/playlist`

[Join Discord](https://discord.gg/7SaE8v2) For any kind of help