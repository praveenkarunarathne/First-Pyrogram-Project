from pyrogram import Client

app_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
bot_token="1682447920:AAF9U9KS_jrzQS2yTJqqwbbkLCcQq7lB_kA"

app = Client(":memory:",app_id,api_hash,bot_token=bot_token)

@app.on_message()
def hello(client, message):
  message.reply_cached_media("AgACAgUAAxkBAAMFYGAiwSdZuaXrPtxFXJ5kR-8gM3YAAruqMRsutAFX-lXAO6A13qNUTBpvdAADAQADAgADbQADnncDAAEeBA")
  
app.run()
