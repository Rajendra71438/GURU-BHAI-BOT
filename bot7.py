import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ChatJoinRequestHandler,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

VIDEO_PATH = "assets/video.mp4"
VOICE_PATH = "assets/voice.ogg"
APK_PATH = "assets/OFFICIAL-NUMBER-HACK.apk"
VOICE2_PATH = "assets/voice2.ogg"

WELCOME_MSG = """💸✨ 𝑯𝒊 {name} 👋 ✨💸
━━━━━━━━━━━━━━━━━━━
✅ 𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝑱𝒐𝒊𝒏 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝒎𝒊𝒍 𝒈𝒂𝒚𝒊 𝒉𝒂𝒊  
⏳ 𝑱𝒂𝒍𝒅𝒊 𝒉𝒊 𝒂𝒑𝒑𝒓𝒐𝒗𝒆 𝒉𝒐 𝒋𝒂𝒚𝒆𝒈𝒊  
━━━━━━━━━━━━━━━━━━━
🎥 𝑽𝑰𝑫𝑬𝑶 • 🎧 𝑽𝑶𝑰𝑪𝑬 𝑮𝑼𝑰𝑫𝑬  
👇 𝑵𝒊𝒄𝒉𝒆 𝒇𝒐𝒍𝒍𝒐𝒘 𝒌𝒂𝒓𝒐  
⚠️ 𝑺𝒂𝒓𝒆 𝒔𝒕𝒆𝒑𝒔 𝒅𝒉𝒚𝒂𝒏 𝒔𝒆 𝒇𝒐𝒍𝒍𝒐𝒘 𝒌𝒂𝒓𝒏𝒂!
━━━━━━━━━━━━━━━━━━━
"""

VIDEO_CAPTION = """BHARAT CLUB REGISTER LINK
https://bhtclub2.com/#/register?invitationCode=178485976538
"""

REGISTER_MSG = """🚀 𝑩𝑯𝑨𝑹𝑨𝑻 𝑪𝑳𝑼𝑩 𝑹𝑬𝑮𝑰𝑺𝑻𝑬𝑹 𝑳𝑰𝑵𝑲  

🔗 https://bhtclub2.com/#/register?invitationCode=178485976538
"""

VOICE_CAPTION = """🎧 𝑨𝒖𝒅𝒊𝒐 𝒈𝒖𝒊𝒅𝒆 𝒔𝒖𝒏 𝒍𝒐
⚡ 𝑺𝒂𝒃 𝒄𝒍𝒆𝒂𝒓 𝒉𝒐 𝒋𝒂𝒚𝒆𝒈𝒂
"""

APK_CAPTION = """📲 𝑨𝑷𝑲 𝑫𝑶𝑾𝑵𝑳𝑶𝑨𝑫  
━━━━━━━━━━━━━━━━━━━
🔥 𝑭𝒂𝒔𝒕 • 𝑺𝒂𝒇𝒆 • 𝑼𝒔𝒆𝒓 𝑭𝒓𝒊𝒆𝒏𝒅𝒍𝒚  
⚡ 𝑨𝒃𝒉𝒊 𝒊𝒏𝒔𝒕𝒂𝒍𝒍 𝒌𝒂𝒓𝒐 𝒂𝒖𝒓 𝒔𝒕𝒂𝒓𝒕 𝒌𝒂𝒓𝒐!
━━━━━━━━━━━━━━━━━━━
"""

VOICE2_CAPTION = "𝑰𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕 𝒗𝒐𝒊𝒄𝒆! 𝑺𝒉𝒊 𝒔𝒖𝒏 𝒍𝒐 𝒃𝒂𝒉𝒖𝒕 𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕!"

FINAL_MSG = """━━━━━━━━━━━━━━━━━━━
⬇️ 𝑲𝒐𝒊 𝒑𝒓𝒐𝒃𝒍𝒆𝒎 𝒂𝒂𝒚𝒆? ⬇️  
💬 𝑨𝒅𝒎𝒊𝒏 𝒔𝒆 𝒕𝒖𝒓𝒂𝒏𝒕 𝒄𝒐𝒏𝒕𝒂𝒄𝒕 𝒌𝒂𝒓𝒐  
━━━━━━━━━━━━━━━━━━━
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Admin shortcut
    if user.id == ADMIN_ID:
        await update.message.reply_text("👑 Admin panel active.")
        return

    await send_full_flow(user.id, context, user.first_name)


async def send_full_flow(user_id, context, name="User"):
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=WELCOME_MSG.format(name=name)
        )

        await context.bot.send_video(
            chat_id=user_id,
            video=open(VIDEO_PATH, "rb"),
            caption=VIDEO_CAPTION
        )

        await context.bot.send_message(
            chat_id=user_id,
            text=REGISTER_MSG
        )

        await context.bot.send_voice(
            chat_id=user_id,
            voice=open(VOICE_PATH, "rb"),
            caption=VOICE_CAPTION
        )

        await context.bot.send_document(
            chat_id=user_id,
            document=open(APK_PATH, "rb"),
            caption=APK_CAPTION
        )

        await context.bot.send_voice(
            chat_id=user_id,
            voice=open(VOICE2_PATH, "rb"),
            caption=VOICE2_CAPTION
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{ADMIN_USERNAME}")]
        ])

        await context.bot.send_message(
            chat_id=user_id,
            text=FINAL_MSG,
            reply_markup=keyboard
        )

    except Exception as e:
        print(f"Error sending to {user_id}: {e}")


async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    # Try sending message (will only work if user started bot)
    await send_full_flow(user.id, context, user.first_name)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(handle_join_request))

    print("Bot running...")
    app.run_polling()
