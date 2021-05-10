import discord
from discord.ext import commands
from mcrcon import MCRcon

#You have to install discord.py and mcrcon with pip install

TOKEN = 'BOT TOKEN' #Your bot token from https://discord.com/developers/applications

NickChannelID = 1234 #Put here your Nick chennel ID drom discord
LogChannel = 1234 #Put here your Log channel

SubRoleName = "SUBS" #Put here your sub role name from your discord server
WhitelistRoleName = "Whitelist" #Put here your whitelist role from discord server (you have to create it)

bot = commands.Bot(command_prefix = '__')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="mc whitelist"))
    await bot.get_channel(LogChannel).send('Bot ready to work')


@bot.command()
async def mainkra(ctx):
    await ctx.send("MA MA MA MAINKRAAAA")


@bot.event
async def on_message(message):
    if message.channel.id == NickChannelID:
        i = 0
        for r in message.author.roles:
            if r.name == SubRoleName:
                i = 2
                for r2 in message.author.roles:
                    if r2.name == WhitelistRoleName:
                        i = 1
        if i == 1:
            await message.channel.send('You have already sent a nickname, if you want to change contact a mod')
            print('no')
        elif i == 2:
            role = discord.utils.get(message.guild.roles, name="Whitelist")
            await message.author.add_roles(role)
            command = 'whitelist add ' + str(message.content)
            with MCRcon("localhost", "YourRconPass") as mcr: #Go to server.preferences and set to true enable.rcon and set a password to rcon.password
                resp = mcr.command(command)
            print(resp)
    await bot.process_commands(message)


bot.run(TOKEN)
