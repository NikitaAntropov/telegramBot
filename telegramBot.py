import requests

TOKEN = ''
URL = 'https://api.telegram.org/bot'


def get_updates(offset=0):
    update = requests.get(f'{URL}{TOKEN}/getUpdates?offset={offset}').json()
    return update['result']

def send_message(chat_id, message):
    if  message in ['привет']:
        requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text=привет')

def run():
    update_id = get_updates()[-1]['update_id']
    while True:
        print(update_id)
        messages = get_updates(update_id)
        for message in messages:
            if update_id < message['update_id']:
                update_id = message['update_id']
                send_message(message['message']['chat']['id'],message['message']['text'])

if __name__ == '__main__':
    run()

