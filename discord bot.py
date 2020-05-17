import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!일반1,2 !경쟁1,2")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("!일반1"):
        await message.channel.send("@here 일반전1채널에서 사람을 구합니다.")
    if message.content.startswith("!일반2"):
        await message.channel.send("@here 일반전2채널에서 사람을 구합니다.")
    if message.content.startswith("!경쟁1"):
        await message.channel.send("@here 경쟁전1채널에서 사람을 구합니다.")
    if message.content.startswith("!경쟁2"):
        await message.channel.send("@here 경쟁전2채널에서 사람을 구합니다.")

access_token = os.enciron["BOT_TOKEN"]

client.run(access_token)
