# ©riz4d
import requests as req
import wget
import os
from pyrogram import *
from Config import *

base_url='https://api.xteam.xyz/dl/mediafire?url='
endpoint='&APIKEY='


app=Client('',
           api_id=API_ID,
           api_hash=API_HASH,
           bot_token=BOT_TOKEN)

@app.on_message(filters.command('start'))
async def start_msg(client,message):
    await message.reply('**Hey '+message.from_user.first_name+"  🖐**\n\nI can download MediaFire files by senting MediaFire URL\n\nExample URL :\n`https://www.mediafire.com/file/gqgz18jsaic3bbb/test_img.png/file`\n\n\nDev : @riz4d")

@app.on_message(filters.text)
async def media_dl(client,message):
   try: 
    Input=message.text
    url=base_url+Input+endpoint+API_KEY
    request_url=req.get(url)
    req_js=request_url.json()
    FileName=req_js['result']['title']
    FileSize=req_js['result']['size']
    await message.reply("**<u>File InFo</u>\n\n__File Name : `"+FileName+"`\nFile Size : `"+FileSize+"`__**")
    down=req_js['result']['url']
    file=wget.download(down)
    await message.reply_photo(file)
    os.remove(file)
   except:
       await message.reply('**__Sorry, Its Invalid Mediafire URL try again__**')   
       await message.reply("__Further Queries @riz4d__")
app.run()
# writtened by @riz4d
