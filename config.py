import os

# Configuración del bot de Telegram
TELEGRAM_TOKEN = '6119983782:AAGwSeqDU2E7UfyhIz6t2wh81AGopsMjZx8'
TELEGRAM_CHAT_ID = 'https://t.me/SignalBot100'

# Configuración de Trading View
TV_INDICATOR = 'Ampel.inv'
TV_ASSETS = ['BTC/USD', 'ETH/USD', 'EUR/USD', 'Gold']

# Configuración de los mensajes de alerta
ALERT_MESSAGE_FORMAT = """
{pair}
Precio: {price}
Tipo de posición: {position_type}
Temporalidad: {timeframe}
"""
