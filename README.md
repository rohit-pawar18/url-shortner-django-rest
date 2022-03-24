##url-shortner-django-rest

## requirements

#python3.8
#redis
#requirements.txt


## GET API (DATABASE)

http://localhost:8000/api/get-short-url/?short_url=http://127.0.0.1:8000/BvTn4s

header ==>   content-type = application/json

## GET API (Cache)
http://localhost:8000/api/get-short-url-cache/?short_url=http://127.0.0.1:8000/BvTn4s

header ==>   content-type = application/json


## create APIS DATABASE(POST)
http://localhost:8000/api/create-short-url/

raw body => {"long_url":"https://test123.com/discover/test"}

header ==>   content-type = application/json

## create APIS Cache (POST)
http://localhost:8000/api/create-short-url-cache/

raw body => {"long_url":"https://test123.com/discover/test"}

header ==>   content-type = application/json