import socketio

# standard Python
sio = socketio.Client()

# asyncio
# sio = socketio.AsyncClient()

print(sio)


@sio.event
def message(data):
    print('I received a message!')


@sio.on('my message')
def on_message(data):
    print('I received a message!')


sio.connect('http://192.168.1.3:8081')
