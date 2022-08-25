import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

db_url = 'https://nuguna1-e84f8-default-rtdb.firebaseio.com/'

# 서비스 계정의 비공개 키 파일이름
cred = credentials.Certificate("C:/Users/USER/Desktop/권태현/nuguna/auth.json")

default_app = firebase_admin.initialize_app(cred, {'databaseURL':db_url})


## 새 record 등록하기
ref = db.reference()
ref.update({'2019-11-01':{'tradingideas':{'STEEM':100, 'SBD':10, 'SPA':1000}}}  )


ref = db.reference('2019-11-01')
row = ref.get()
print(row)

