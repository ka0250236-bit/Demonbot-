from pyrogram import Client, filters

API_ID = 29386859
API_HASH = "b8971fad50c4646fbb719d844f1ed5e0"
BOT_TOKEN = "8783657275:AAHkCEyTHMdd5EAW2I6UDbnvKVEOO3yQwEg"

bot = Client("botdemohhgs_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! Movie search bot ready 🎬")

@bot.on_message(filters.text)
async def search(client, message):
    movie = message.text
    await message.reply_text(f"Searching for: {movie}")

bot.run()
