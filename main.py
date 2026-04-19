import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"성우는 귀여우며 똑똑하고 세상에서 가장 위대한 이 지구의 자랑이다 나는 그러한 위대하고도 정의로우며 귀엽고 똑똑한 성우를 모방한 {bot.user.name}이다")

@bot.event                   # 대충 잡것
async def on_member_join(member):
    await member.send(f"{member.name}님, 환영해요! 🎉")



@bot.event                    # 금지어 설정
async def on_message(message):
    if message.author == bot.user:
        return
    if "섹스" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, `섹스, 또는 성관계(性關係, Sexual intercourse)는 생식 기관을 이용하는 육체적인 관계를 맺는 행위를 의미한다.`..... 나무위키에서 긁어온거 맞다")
    await bot.process_commands(message)



@bot.event                    # 명령어 설정
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.strip()

    # "성우봇아"로 시작하는지 확인
    if content.startswith("성우봇아"):
        command = content[len("성우봇아"):].strip()

        if command == "안녕":
            await message.channel.send("안녕하세요!")
        elif command == "도움":
            await message.channel.send("도움말입니다!")
        else:
            await message.channel.send("무슨 말인지 모르겠어요 😅")

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)