# Bot.py
import asyncio
import random
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from Interface import Interface


class Bot:
    def __init__(self):
        self._is_inappropriate = {"bitch"}
        self._attempts = 3
        self._generated_code = None
        self.student = None
        self.professor = None
        self._interface = Interface()
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
            professor_flag: bool = True
            student_flag: bool = True
            guild = bot.guilds[0]
            if guild.name == "Cold_Foam's server":
                for role in await guild.fetch_roles():
                    if role.name != "Professor":
                        # need to create professor role just once, maybe set a boolean flag to true and make role l8r
                        professor_flag = professor_flag and True
                    else:
                        professor_flag = professor_flag and False
                    if role.name != "Student":
                        # set boolean flag for student
                        student_flag = student_flag and True
                    else:
                        student_flag = student_flag and False
                if professor_flag:
                    # make professor flag and assign owner, otherwise already assigned
                    self.professor = await guild.create_role(name="Professor",
                                                             colour=discord.Colour.dark_gold())
                    await guild.owner.add_roles(self.professor)
                if student_flag:
                    # make student role
                    self.student = await guild.create_role(name="Student", colour=discord.Colour.dark_red())
                self._interface.sign_up("justin", "abc", 123)

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
            # need to check if channel is the proper channel
            message = await bot.wait_for('message', timeout=30)
            async with channel.typing():
                await asyncio.sleep(2)
            await member.send(f'ok {message.author}, i will store your name forever as {message.content} :)')
            name = message.content

            async with channel.typing():
                await asyncio.sleep(2)

            await member.send("What is your student email?")
            message = await bot.wait_for('message', timeout=30)
            async with channel.typing():
                await asyncio.sleep(2)
            await member.send(f'ok {message.author}, i will store your email forever as {message.content} :)')
            email = message.content

            async with channel.typing():
                await asyncio.sleep(2)
            id = member.id
            await member.send(str(id))

            self._interface.sign_up(name, email, id)

            await member.add_roles(self.student)

        # @bot.event
        # async def on_message(message):
        # if message.author == bot.user:
        # return
        # if message.content.startswith("hello"):
        # await message.channel.send("hello!")

        @bot.command()
        async def echo(ctx, message):
            """
                "You're copying me!" "nuh uh"
                This command repeats your message back to you
            """
            async with ctx.channel.typing():
                await asyncio.sleep(2)
            await ctx.send(message)
            print(ctx.guild.id)

        @bot.command()
        @commands.has_role('Student')
        async def personal_attendance(ctx):
            channel = await ctx.author.create_dm()
            attendance = self._interface.view_attendance(ctx.author.id)
            await channel.send(str(attendance))
        @bot.command(name="record_presence")
        @commands.has_role('Student')
        async def record_presence(ctx, code):
            channel = await ctx.author.create_dm()
            if self._attempts > 0:
                if int(code) == self._generated_code:
                    self._interface.mark_present(ctx.author.id, int(code))
                    await channel.send("Attendance successfully recorded")
                    return
                else:
                    self._attempts = self._attempts - 1
                    await channel.send(f"Attendance code was inputted incorrectly, you have {self._attempts} "
                                       f"to re-enter the code before chat explodes")
                    code = await bot.wait_for('messsage', timeout=30)
            else:
                await channel.send("you dun fucked up AAron")

        @bot.command()
        @commands.has_role('Professor')
        async def generate_code(ctx):
            channel = await ctx.author.create_dm()
            code = await channel.send("Attendance Code: ")
            async with channel.typing():
                await asyncio.sleep(2)
            # await code.edit()
            self._generated_code = self._interface.take_attendance()
            await channel.send(str(self._generated_code))

        @bot.command()
        @commands.has_role('Professor')
        async def class_attendance(ctx):
            channel = await ctx.author.create_dm()
            await channel.send("Calculating...")
            async with channel.typing():
                await asyncio.sleep(2)
            attendance = self._interface.view_class_attendance()
            await channel.send(str(attendance))

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
