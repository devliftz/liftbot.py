# liftbot.py

### Install
`pip install git+https://github.com/devliftz/liftbot.py`

### Example
```py
import liftbot
import os

@liftbot.bot.commnad()
async def example(ctx):
    await ctx.reply("Example command")

liftbot.login(token="USER TOKEN")
```