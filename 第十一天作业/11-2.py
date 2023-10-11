import requests
import uuid
import time
import hashlib
url = 'https://openapi.youdao.com/api'
translate_text = (input())
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
print(str(r['translation'][0]))