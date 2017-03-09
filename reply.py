import requests
import config

def send(user_id, msg):
    headers = {'content-type': 'application/json'}
    payload = '{"recipient": {"id": '+user_id+'},"message": {"text": "'+msg+'"}}'
    payload = payload.encode('utf-8')
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + config.TOKEN, data=payload, headers=headers)
