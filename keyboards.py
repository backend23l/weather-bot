from telegram import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='weather', request_location=True)]
    ]
)
