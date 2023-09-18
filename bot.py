import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from core.llm import LLM
from core.util import extract_query
from core.prompt import response_template

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL')

intents = discord.Intents.all()
# bot = commands.Bot(command_prefix='$', intents=intents)
bot = commands.AutoShardedBot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('Ready!')


@bot.command(name='hbd', help='Command to wish happy birthday')
async def happy_birthday(ctx):
    if ctx.author.name == bot.user.name:
        return
    await ctx.send("Happy birthday" + ctx.author.mention)


@bot.command(name='chat', help=" Type $chat followed by your question", brief='AI Answers for your question.')
async def chat(ctx):
    llm = LLM()

    if ctx.author.name == bot.user.name:
        return

    query = extract_query(ctx.message.content)
    ai_response = llm.completion(question=query)['choices'][0]['message']['content']
    final_response = response_template.format(user=ctx.author.mention, response=ai_response)

    await ctx.send(final_response)


@bot.event
async def on_message_edit(before, after):

    if not "$chat" in after.content:
        return

    await bot.process_commands(after)


bot.run(TOKEN)
