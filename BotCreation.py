import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Obtener el token de acceso del archivo .env
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Crear una instancia del bot
bot = Bot(token=TELEGRAM_TOKEN)
