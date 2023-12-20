from telegram.ext import CallbackContext
from telegram import Update
from keyboards import keyboard
from weahter import get_current


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    
    update.message.reply_html(
        text=f'Hello {user.full_name}, welcome to weather bot! Press the button to get current weather info.',
        reply_markup=keyboard
    )

def current_weather(update: Update, context: CallbackContext):
    location = update.message.location

    curr_weather = get_current(lon=location.longitude, lat=location.latitude)

    msg = f'{curr_weather["weather"][0]["main"]}: {curr_weather["weather"][0]["description"]}'
    update.message.reply_text(msg)
