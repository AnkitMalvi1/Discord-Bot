import discord


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hi"):
        await message.channel.send("Hello")

    if message.content.startswith('image'):
        await message.channel.send(file=discord.File("kuchbhi.png"))

    if message.content.startswith('video'):
        await message.channel.send(file=discord.File("kuchbhi.mp4"))

    if message.content.startswith('audio'):
        await message.channel.send(file=discord.File("kuchbhi.mp3"))

    if message.content.startswith('file'):
        await message.channel.send(file=discord.File("kuchbhi.pdf"))


client.run("Enter Your Token")
