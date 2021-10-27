from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    joinButton = InlineKeyboardMarkup([[
         InlineKeyboardButton("📢 Update Channel 📢", url="https://t.me/Mo_Tech_YT"),
         InlineKeyboardButton("☺️ Deploy Now ☺️", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
