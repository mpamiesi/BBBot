import websocket
import json
import time
from config import TV_INDICATOR, TV_ASSETS
from bot import send_message

# Función que se ejecutará cuando se reciba una alerta
def on_message(ws, message):
    data = json.loads(message)
    if data['type'] == 'alert':
        alert = data['content']['message']
        # Filtrar las alertas por tipo de indicador
        if TV_INDICATOR in alert:
            # Filtrar las alertas por activo
            for asset in TV_ASSETS:
                if asset in alert:
                    # Obtener los datos de la alerta
                    parts = alert.split('\n')
                    pair = parts[0]
                    price = parts[1].split(':')[1].strip()
                    position = parts[2].split(':')[1].strip()
                    timeframe = parts[3].split(':')[1].strip()
                    
                    # Construir el mensaje a enviar al grupo de Telegram
                    message = MESSAGE_FORMAT.format(pair=pair, price=price, position=position, timeframe=timeframe)
                    
                    # Enviar la alerta al grupo de Telegram
                    send_message(message)


# Configuración del WebSocket de Trading View
def start_tradingview_websocket():
    ws = websocket.WebSocketApp('wss://data.tradingview.com/socket.io/websocket', on_message=on_message)

    # Iniciar el WebSocket
    ws.on_open = lambda ws: ws.send('{"_time":%d,"timezone":"Etc/UTC","_command":"subscribe","ticks":["%s"],"session":"{\"tz\":\"Etc/UTC\"}","id":"s1"}' % (int(time.time()), '","'.join(TV_ASSETS)))
    ws.run_forever()
