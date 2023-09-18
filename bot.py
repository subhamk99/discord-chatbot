import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from core.llm import LLM
from core.util import extract_query

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('Ready!')


@bot.command(name='hbd', help='Command to wish happy birthday')
async def happy_birthday(ctx):
    if ctx.author.name == bot.user.name:
        return
    await ctx.send("Happy birthday" + ctx.author.mention)


@bot.command(name='chat', help='Command interactively chat with gpt')
async def chat(ctx):
    llm = LLM()

    if ctx.author.name == bot.user.name:
        return

    query = extract_query(ctx.message.content)
    ai_response = llm.completion(question=query)['choices'][0]['message']['content']

    await ctx.send(ai_response)


bot.run(TOKEN)
