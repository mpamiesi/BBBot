import os

# Configuración del bot de Telegram
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Configuración de Trading View
TV_INDICATOR = 'mi-indicador'
TV_ASSETS = ['BTC/USD', 'ETH/USD', 'EUR/USD', 'Gold']
