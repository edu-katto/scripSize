from decouple import config
import requests

def sendTelegram(Asunto, message):
    r = requests.post('https://api.telegram.org/bot' + config('BOT_TOKEN') + '/sendMessage',
                data = {'chat_id': config('CHAT_ID'), 'text': message})