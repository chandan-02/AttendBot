#import webbrowser
import discord 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("adminKey.json") 
firebase_admin.initialize_app(cred,{
    'databaseURL': '<Enter_your_database_url_here>'
})

name = []
status = []

refS = db.reference('/Status/')

ref = db.reference('/Enrolled/')

refM = db.reference('/Main/')

def enroll():
    for x in ref.get().values():
        for i in x.values():
            name.append(i)
enroll()

offline = name
def getStat():
    for eachValue in refS.get():
        status.append(eachValue)

bot = discord.Client()

@bot.event
async def on_ready():
    textChannel = bot.get_channel(779222416986996767)
    myMessage = ["I am ready !","Commands : ","-> !link : For TCSC Extension Download link","-> !enroll : For confirming enrolment","-> !status : Get current attendance status ","-> !names : Debug "]
    for mes in myMessage:
        await textChannel.send(mes)
        
#779222416986996767

@bot.event
async def on_message(message):
    
    textChannel = bot.get_channel(779222416986996767)
    link = message.content 
    global ref
    global name
    global refM
    global refS
    global status 
    global offline

    if message.content.startswith("!enroll"):
        enroll()
        await textChannel.send("New pupils enrolled successfully !")
    
    if message.content.startswith("https://forms"):
        refS.delete()
        for eachName in name:
            refM.update({eachName:link})
        await textChannel.send("Database Updated with new link !")
        
    if message.content.startswith("https://docs"):
        refS.delete()
        for eachName in name:
            refM.update({eachName:link})
        await textChannel.send("Database Updated with new link !")
        
    if message.content.startswith("!link"):
        await textChannel.send('https://github.com/chandan-02/TCSC-Attend')
        
    if message.content.startswith("!names"):
        mes = "Database / Enrolled - Branch : {nameV}" 
        mesNew = mes.format(nameV = name) #here
        await textChannel.send(mesNew)
        
        
    if message.content.startswith("!status"):
        newStatus =  refS.get()
        for eachVal in newStatus:    
            # nameN = eachVal,":",newStatus[eachVal]
            nameN = "{each} : {stat}"
            nameNew = nameN.format(each=eachVal,stat=newStatus[eachVal])
            await textChannel.send(nameNew)

        getStat()
        for eZ in status:
            for el in offline :
                if eZ == el:
                    offline.remove(eZ)

        # await textChannel.send(offline)
        for eachVal in offline:
            val = "{each} : Maybe Offline"
            valNew = val.format(each = eachVal)
            await textChannel.send(valNew)

bot.run('Nzc3MTcwNTEzMDYzNzA2NjY1.X6_icQ.qDf9NIpF3MCB4XyNHLFn17ArFJg')
