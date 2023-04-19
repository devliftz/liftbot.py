import discord
from discord.ext import commands
from datetime import datetime

from liftbot import gradient
from liftbot.styler import Colorate, Colors, Center

bot = commands.Bot(command_prefix="?", help_command=None, self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"👻 | {bot.user.name}", url="https://twitch.tv/at_drmr/"))
    current_dateTime = datetime.now()
    
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"""


                        ██╗     ██╗███████╗████████╗██████╗  ██████╗ ████████╗
                        ██║     ██║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝
                        ██║     ██║█████╗     ██║   ██████╔╝██║   ██║   ██║   
                        ██║     ██║██╔══╝     ██║   ██╔══██╗██║   ██║   ██║   
                        ███████╗██║██║        ██║   ██████╔╝╚██████╔╝   ██║   
                        ╚══════╝╚═╝╚═╝        ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   

                                                      """)))
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"Connected \033[1m{bot.user.name}#{bot.user.discriminator}\033[0m | Version: 12.1.8 | Local Time: {current_dateTime.hour}:{current_dateTime.minute}")))


@bot.event
async def on_command(ctx):
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, f"\033[1mUsed command:\033[0m {ctx.command.name}", 1)))

@bot.command()
async def ping(ctx):
    await ctx.reply(f"> **Pong!** `{bot.latency}`")

@bot.command()
async def help(ctx):
    await ctx.reply(f"""> **LiftBot Help**
    
    `?help` *-* **Shows this output**
    `?ping` *-* **Get SelfBot Latency**
    `?av` *-* **Get User avatar**
    `?info` *-* **Get User Info**""")

@bot.command()
async def av(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    await ctx.reply(f"""> **{user.mention}`s avatar** {user.avatar}""")

@bot.command()
async def info(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    await ctx.reply(f"""> **{user.mention}`s info** `beta`
    
    Creation Date: {user.created_at}""")

def login(token):
    bot.run(f"{token}", log_handler=None)