# Bot.py
import asyncio
import random
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


class Bot:
    def __init__(self):
        self._is_inappropriate = {"bitch"}
        self._generated_code = None
        self._token = self.get_token()
        self.run_bot(self._token)

    def get_token(self):
        load_dotenv()
        token = os.getenv('DISCORD_TOKEN')
        return token

    def run_bot(self, token):
        intent_arg = discord.Intents.default()
        intent_arg.message_content = True
        intent_arg.members = True
        bot = commands.Bot(command_prefix="!", intents=intent_arg)

        @bot.event
        async def on_ready():
            # send it to another class, which implements
            print(f'{bot.user} has connected to the server!')

        @bot.event
        async def on_member_join(member):
            # when the user joins the server
            channel = await member.create_dm()
            await member.send(f"Hello {member.name}, welcome to class!")
            async with channel.typing():
                await asyncio.sleep(6)
            await member.send("In order to get things set up, I'm going to ask you a few questions")
            async with channel.typing():
                await asyncio.sleep(2)
            await member.send("What is your name on Canvas?")
            # need to check if channel is the proper channel todo
            message = await bot.wait_for('message', timeout=30)
            async with channel.typing():
                await asyncio.sleep(2)
            await member.send(f'ok {message.author}, i will store your name forever as {message.content} :)')
            name = message.content



        #@bot.event
        #async def on_message(message):
            #if message.author == bot.user:
                #return
            #if message.content.startswith("hello"):
                #await message.channel.send("hello!")

        @bot.command()
        async def echo(ctx, message):
            """
                "You're copying me!" "nuh uh"
                This command repeats your message back to you
            """
            async with ctx.channel.typing():
                await asyncio.sleep(2)
            await ctx.send(message)

        @bot.command(name="record_presence")
        async def record_presence(ctx, code: int):
            attempts = 3
            channel = await ctx.author.create_dm()
            if code == self._generated_code:
                # todo record successful attendance
                await channel.send("Attendance successfully recorded")
            else:
                # todo offer 2 more attempts to correctly input the code
                attempts = attempts - 1
                await channel.send(f"Attendance code was inputted incorrectly, you have {attempts} "
                                   f"to re-enter the code before chat explodes")

        @bot.command()
        async def generate_code(ctx):
            channel = await ctx.author.create_dm()
            code = await channel.send("Attendance Code: ")
            async with channel.typing():
                await asyncio.sleep(2)
            # await code.edit()
            self._generated_code = int((random.random() * 10000) // 1)
            await channel.send(str(self._generated_code))

        @bot.event
        async def on_message(message):
            # bot will immediately check message instead of everything else
            if message.author == bot.user:
                return
            if message.content.lower() in self._is_inappropriate:
                await message.channel.send("Ay keep my channel clean ya pricks")
            else:
                await bot.process_commands(message)

        bot.run(token)


