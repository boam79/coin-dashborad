import requests
import json

url = "https://api.upbit.com/v1/market/all?isDetails=true"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

# JSON 데이터 파싱
data = response.json()

print("전체 응답 데이터:")
print(json.dumps(data, indent=2, ensure_ascii=False))

print("\n마켓 정보:")
for market in data:
    print(f"마켓: {market['market']}, 한국명: {market['korean_name']}, 영문명: {market['english_name']}")

