import requests
res = requests.get("http://www.naver.com") # requests 라이브러리를 불러온 후, NAVER의 홈 페이지를 요청한 후 응답 받기

res.headers # Header를 확인

res.text[:1000] # Body를 텍스트 형태로 확인

payload = {"name": "Hello", "age": 13} # payload와 함께 POST를 보내기

res = requests.post("https://webhook.site/...", payload)
