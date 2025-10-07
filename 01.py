import requests
import json

url = "https://api.upbit.com/v1/candles/days"
params = {
    'market': "KRW-BTC",
    "count": 100,
    "to": "2025-03-24 00:00:00"
}
headers = {"accept": "application/json"}
response = requests.get(url, params=params, headers=headers)

# 응답 데이터를 JSON으로 파싱
data = response.json()

# 파일명 생성: {market}_{to}_{count}.json
market = params['market']
to = params['to'].replace(' ', '_').replace(':', '-')
count = params['count']
filename = f"{market}_{to}_{count}.json"

# JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"데이터가 {filename} 파일로 저장되었습니다.")
print(f"총 {len(data)}개의 일봉 데이터를 가져왔습니다.")