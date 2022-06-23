import logging

import requests

#url = "http://217.71.129.139:4820"

url = "http://127.0.0.1:5000"
def req(question,token):
    body = {'question':question, 'token': token}
    header = {'Accept': 'application/json','Content-Type': 'application/json'}
    r = requests.get(url+"/getAnswer", json=body, headers=header)
    return  r.json()


def createToken(data):
    body = {'tgId': data['tgId'], 'token': data['token']}
    header = {'Accept': 'application/json','Content-Type': 'application/json'}
    r = requests.get(url+"/addUser", json=body, headers=header)

    if str(r.status_code) == "401":
        return {"msg": "Ошибка"}
    else:
        return r.json()

def getToken(tgId):
    logging.info(tgId)
    body = {'tgId': tgId}
    header = {'Accept': 'application/json','Content-Type': 'application/json'}
    r = requests.get(url+"/getUser", json=body, headers=header)
    if str(r.status_code) == "401":
        return {"msg": "Ошибка"}
    else:
        return  r.json()

