import discord
from discord.ext import commands
from datetime import datetime

from liftbot import gradient
from liftbot.styler import Colorate, Colors, Center, Box

bot = commands.Bot(command_prefix="?", help_command=None, self_bot=True)

@bot.event
async def on_ready():
    current_dateTime = datetime.now()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"""


                    ██╗     ██╗███████╗████████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
                    ██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                    ██║     ██║█████╗     ██║   ██║     ██║   ██║██████╔╝██║  ██║
                    ██║     ██║██╔══╝     ██║   ██║     ██║   ██║██╔══██╗██║  ██║
                    ███████╗██║██║        ██║   ╚██████╗╚██████╔╝██║  ██║██████╔╝
                    ╚══════╝╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

                                                                         """)))
    print(Center.XCenter(Box.Lines(Colorate.Horizontal(Colors.red_to_yellow, f"Connected {bot.user.name}#{bot.user.discriminator} | Version: 1.5.5 | Time: {current_dateTime.hour}:{current_dateTime.minute}"))))

@bot.event
async def on_command(ctx):
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"Command {ctx.command.name} was used", 1)))

def login(token):
    bot.run(f"{token}")