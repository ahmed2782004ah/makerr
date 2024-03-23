from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="25336226",
    api_hash="fc6670f0d2070c0a6defb9c25b92c384",
    bot_token="6477407510:AAH7qtd4tabFhx7o5wzwsB-mwUd_TqIozFk",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    A_q_lp = "IIUll_l"
    await bot.send_message(A_q_lp, "** اشتغلت يولبولبول . **")
    print("[INFO]:   ")
    await idle()
