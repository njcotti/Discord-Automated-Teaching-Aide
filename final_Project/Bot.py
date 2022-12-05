# Bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


class Bot:
    def __init__(self):
        self._token = self.get_token()
        self.run_bot(self._token)

    def get_token(self):
        load_dotenv()
        token = os.getenv('DISCORD_TOKEN')
        return token

    def run_bot(self, token):
        intent_arg = discord.Intents.all()
        bot = commands.Bot(command_prefix="!", intents=intent_arg)

        @bot.event
        async def on_ready():
            # send it to another class, which implements
            print(f'{bot.user} has connected to the server!')

        #@bot.event
        #async def on_message(message):
            #if message.author == bot.user:
                #return
            #if message.content.startswith("hello"):
                #await message.channel.send("hello!")

        @bot.command()
        async def echo(ctx, message):
            await ctx.send(message)

        bot.run(token)


