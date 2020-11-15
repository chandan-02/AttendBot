import webbrowser
import discord 

bot = discord.Client()

@bot.event
async def on_ready():
    textChannel = bot.get_channel(525697390024589325)
    myMessage = [ "Aur Bhai TCSC Attend Extension ad karle nhi toh kam nhi hoga","Yaha se add Karle: https://github.com/chandan-02/TCSC-Attend" ]
    for mes in myMessage:
        await textChannel.send(mes)


@bot.event
async def on_message(message):
    textChannel = bot.get_channel("Enter your text channel id without quotes")
    if message.content.startswith("https://forms"):
        webbrowser.open(message.content)
        await textChannel.send("Mila Link")
        

bot.run('Enter your Token here')
