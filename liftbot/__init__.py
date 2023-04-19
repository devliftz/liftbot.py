import discord
from discord.ext import commands
from datetime import datetime

from liftbot import gradient
from liftbot.styler import Colorate, Colors, Center

print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"""


                    ██╗     ██╗███████╗████████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
                    ██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                    ██║     ██║█████╗     ██║   ██║     ██║   ██║██████╔╝██║  ██║
                    ██║     ██║██╔══╝     ██║   ██║     ██║   ██║██╔══██╗██║  ██║
                    ███████╗██║██║        ██║   ╚██████╗╚██████╔╝██║  ██║██████╔╝
                    ╚══════╝╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

                                                                         """)))
print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"Connected {bot.user.name}#{bot.user.discriminator} | Version: 1.6.3 | Time: {current_dateTime.hour}:{current_dateTime.minute}")))

bot = commands.Bot(command_prefix="?", help_command=None, self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"👻 | {bot.user.name}"))
    current_dateTime = datetime.now()


@bot.event
async def on_command(ctx):
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"Used command: {ctx.command.name}", 1)))

def login(token):
    bot.run(f"{token}", log_handler=None)