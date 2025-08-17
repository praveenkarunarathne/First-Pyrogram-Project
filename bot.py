from pyrogram import Client

app_id=123456
api_hash="123456asdf"
bot_token="123456:bot_token"

app = Client(":memory:",app_id,api_hash,bot_token=bot_token)

@app.on_message()
def hello(client, message):
  message.reply_cached_media("AgACAgUAAxkBAAMFYGAiwSdZuaXrPtxFXJ5kR-8gM3YAAruqMRsutAFX-lXAO6A13qNUTBpvdAADAQADAgADbQADnncDAAEeBA")
  
app.run()
