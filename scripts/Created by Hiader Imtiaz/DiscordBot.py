# Discord Bot
# pip install discord
from discord.ext import commands
import discord
from discord import *
token = "Enter your token here"
bot = commands.Bot(command_prefix='!')
@ bot.event
async def on_ready():
    print("Bot is ready.")
# Welcome New Members
@ bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Medium server!')
# Leave Message
@ bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name} has left the server.')
# Print All Members
@ bot.command()
async def members(ctx):
    members = ctx.guild.members
    for member in members:
        print(member)
# Ban Member
@ bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} has been banned.')
# Respond to a message
@ bot.event
async def on_message(msg):
    if msg.content.startswith("!help"):
        await msg.channel.send("Medium is Here")
await bot.process_commands(msg)
# Bot Commands
@ bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
bot.run(token)