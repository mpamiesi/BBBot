import telegram
from config import TELEGRAM_TOKEN

# Inicializar el bot de Telegram
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Función para enviar mensajes al grupo
def send_message(text):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
