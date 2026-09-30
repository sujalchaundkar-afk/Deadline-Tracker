import smtplib
import asyncio
from email.mime.text import MIMEText
from telegram import Bot
import streamlit as st

def send_email(to_address: str, subject: str, body: str) -> bool:
    """Sends deadline summary via Gmail SMTP."""
    try:
        gmail_address = st.secrets["GMAIL_ADDRESS"]
        gmail_password = st.secrets["GMAIL_APP_PASSWORD"]

        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = gmail_address
        message["To"] = to_address

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_address, gmail_password)
            server.send_message(message)
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

def send_telegram(chat_id: str, text: str) -> bool:
    """Sends deadline summary via Telegram Bot API."""
    try:
        bot_token = st.secrets["TELEGRAM_BOT_TOKEN"]
        bot = Bot(token=bot_token)
        asyncio.run(bot.send_message(chat_id=chat_id, text=text))
        return True
    except Exception as e:
        st.error(f"Failed to send Telegram message: {e}")
        return False