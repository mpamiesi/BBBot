from bot import send_message
from tradingview import start_tradingview_websocket

if __name__ == '__main__':
    send_message('El bot de alertas de Trading View se ha iniciado.')
    start_tradingview_websocket()
