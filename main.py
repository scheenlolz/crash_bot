import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "توکن_ربات_تو_اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! برای دریافت ضریب آخر بازی Crash دستور /odds رو بفرست.")

async def odds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # به سایت وان‌ایکس‌بت وصل می‌شیم و HTML می‌گیریم (نمونه ساده - نیاز به بهبود برای لینک دقیق)
        response = requests.get("https://so.1xbet.com")
        soup = BeautifulSoup(response.text, "html.parser")

        # اینجا باید ساختار دقیق صفحه Crash بررسی و انتخاب شود
        # فرض بر این است که ضریب‌ها در یک عنصر با کلاس خاص هستند (به عنوان مثال)
        odds_element = soup.find("div", class_="crash__coefficient")
        odds = odds_element.text if odds_element else "ضریب پیدا نشد."

        await update.message.reply_text(f"ضریب آخر بازی Crash: {odds}")
    except Exception as e:
        await update.message.reply_text("خطا در دریافت ضریب.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("odds", odds))
    app.run_polling()
