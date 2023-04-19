import discord
from discord.ext import commands
from datetime import datetime

from liftbot import gradient
from liftbot.styler import Colorate, Colors, Center

bot = commands.Bot(command_prefix="?", help_command=None, self_bot=True)

@bot.event
async def on_ready():
    current_dateTime = datetime.now()
    logomn = gradient.purplepink(f"""


                    ██╗     ██╗███████╗████████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
                    ██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                    ██║     ██║█████╗     ██║   ██║     ██║   ██║██████╔╝██║  ██║
                    ██║     ██║██╔══╝     ██║   ██║     ██║   ██║██╔══██╗██║  ██║
                    ███████╗██║██║        ██║   ╚██████╗╚██████╔╝██║  ██║██████╔╝
                    ╚══════╝╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

                                                                         
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
                        Connected {bot.user.name}#{bot.user.discriminator} | Version: 1.1.0 | Time: {current_dateTime.hour}:{current_dateTime.minute}
     └────────────────────────────────────────────────────────────────────────────────────────┘""")
    print(logomn)

@bot.event
async def on_command(ctx):
    log = gradient.purplepink(f"""Command {ctx.command.name} used by {ctx.author.name}""")
    print(log)
    print(Center.XCenter(Colorate.Horizontal(Colors.purple_to_blue, f"Command {ctx.command.name} was used", 1)))

def login(token):
    bot.run(f"{token}")