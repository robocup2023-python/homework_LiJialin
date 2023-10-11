import requests
import uuid
import time
import hashlib
import threading
import socket
import time
def translate(text):
  url = 'https://openapi.youdao.com/api'
  translate_text = text
  if(len(translate_text)<=20):
    sign_text = translate_text
  else:
    sign_text = translate_text[:10] + str(len(translate_text)) + translate_text[-10:]
  uid = uuid.uuid1()
  appid = '4046deee17ee7f37'
  key = 'CL8VJP2C9pFo25RQcbXrQg8CwnvnwO9m'
  pr_time = int(time.time())
  sign = hashlib.sha256((appid + sign_text + str(uid) + str(pr_time) + key).encode('utf-8')).hexdigest()
  data = {
    'q':translate_text,
    'from':'auto',
    'to':'zh-CHS',
    'appKey':appid,
    'salt':uid,
    'sign':sign,
    'signType':'v3',
    'curtime':pr_time
  }
  result = requests.post(url,data)
  r = result.json()
  return r['translation'][0]
def connect():
  while True:
    client,address = server.accept()
    thread = threading.Thread(target=run,args=(client,address))
    thread.start()
  pass
def run(client,address):
  t = client.recv(1024)
  r = translate(t.decode()).encode('utf-8')
  client.sendall(r)
  pass

server = socket.socket()
server.bind(('127.0.0.1',8680))
server.listen(5)
thread_main = threading.Thread(target=connect)
thread_main.start()
while True:
  time.sleep(0.1)