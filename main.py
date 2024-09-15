from fastapi import FastAPI, Request
import telegram
import os
import logging
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_API_TOKEN')
URL = os.getenv('DOMAIN_URL')

logging.basicConfig(level=logging.INFO)
app = FastAPI()
bot = telegram.Bot(TOKEN)

async def send_welcome_message(bot, chat_id):
    welcome_text = "Hello World 🤖"
    await bot.sendMessage(chat_id=chat_id, text=welcome_text)

# set the webhook for telegram bot
@app.get("/setwebhook")
async def set_webhook():
    s = await bot.setWebhook(URL)
    logging.info(f"webhook set: {s}")
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

# manage requests
@app.post("/")
async def respond(request: Request):
    data = await request.json()
    update = telegram.Update.de_json(data, bot)
    
    if update.message:
        chat_id = update.message.chat.id
        text = update.message.text.encode("utf-8").decode()
        if text == "/start":
            await send_welcome_message(bot, chat_id)
    return "ok"