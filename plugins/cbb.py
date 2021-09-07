#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🟢 My Name : @𝕱𝖎𝖑𝖒 𝕾𝖕𝖆𝖈𝖊 𝕷𝕶 - Bot \n🟢 Creator : @SLDarkGhoast  \n🟢 Our Channel : @filmspacelk\n🟢 Our Group : @fslklinks</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ CREATOR", url="https://telegram.dog/SLDarkGhoast"),
                        InlineKeyboardButton("CLOSE 🚫", callback_data = "close"),
                    ],
                    [
                        InlineKeyboardButton("💚 FEEDBACKS & SUGGESTIONS 💚", url="https://t.me/joinchat/8gnLbB83IRhjZTE1")
                   
                ]     
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
