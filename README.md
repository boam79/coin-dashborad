# 🚀 암호화폐 완전 분석 대시보드

> Upbit API를 활용한 실시간 암호화폐 데이터 조회, 시각화 및 기술적 분석 도구

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white)
![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=flat&logo=chart.js&logoColor=white)

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [시작하기](#-시작하기)
- [사용 방법](#-사용-방법)
- [파일 구조](#-파일-구조)
- [API 정보](#-api-정보)
- [스크린샷](#-스크린샷)
- [라이선스](#-라이선스)

## 🎯 프로젝트 소개

이 프로젝트는 Upbit 거래소의 공개 API를 활용하여 암호화폐 시장 데이터를 실시간으로 조회하고, 직관적인 웹 대시보드로 시각화하는 올인원 분석 도구입니다.

### 특징

- ✅ **200+ 암호화폐 지원** - Upbit의 모든 KRW 마켓 코인 분석
- ✅ **실시간 데이터** - Upbit API 직접 연동
- ✅ **완전한 시각화** - 캔들차트, 가격 추이, 거래량 등 다양한 차트
- ✅ **기술적 분석** - 이동평균선, 변동성, 추세 분석
- ✅ **반응형 디자인** - 데스크톱, 태블릿, 모바일 지원
- ✅ **No Server Required** - 클라이언트 사이드만으로 완전 동작

## ✨ 주요 기능

### 📊 데이터 시각화

#### 1. 일봉 캔들스틱 차트
- OHLC (시가, 고가, 저가, 종가) 표시
- 상승/하락 색상 구분
- 인터랙티브 툴팁

#### 2. 가격 추이 차트
- 종가 라인 차트
- 5일/20일 이동평균선
- 추세 분석

#### 3. 거래량 차트
- 일별 거래량 막대 차트
- 상승/하락일 색상 구분

#### 4. 변동성 분석 차트
- 일일 변동률 차트
- 가격 변동폭 분석

### 📈 통계 및 분석

#### 주요 가격 정보
- 현재가, 시가, 고가, 저가
- 전일 종가 대비 변동액/변동률
- 평균 거래가

#### 기간 통계
- 기간 최고가/최저가
- 평균가격
- 총 거래량
- 누적 수익률

#### 변동성 분석
- 평균 변동률
- 최대 변동률
- 평균 일일 변동폭

#### 추세 분석
- 상승일/하락일 통계
- 승률 계산
- 기간 누적 수익률

### 🎛️ 필터 및 설정

- **암호화폐 선택** - 200+ 코인 중 선택
- **데이터 개수** - 30/60/100/200일
- **기준일 설정** - 특정 날짜 기준 과거 데이터
- **날짜 범위 필터** - 시작일/종료일 지정

### 📋 상세 데이터 테이블

- 날짜별 OHLC 데이터
- 변동률, 거래량, 거래대금
- 스크롤 가능한 전체 데이터 뷰

## 🛠️ 기술 스택

### Frontend
- **HTML5** - 웹 페이지 구조
- **CSS3** - 모던 UI 디자인 (그라데이션, 애니메이션)
- **JavaScript (ES6+)** - 비동기 처리, DOM 조작
- **Chart.js** - 데이터 시각화 라이브러리
- **chartjs-chart-financial** - 캔들스틱 차트 플러그인

### Backend (Python Scripts)
- **Python 3.7+**
- **requests** - HTTP 요청
- **json** - 데이터 처리

### API
- **Upbit Open API** - 암호화폐 시장 데이터

## 🚀 시작하기

### 필요 조건

#### 웹 대시보드 사용
- 모던 웹 브라우저 (Chrome, Firefox, Safari, Edge)
- 인터넷 연결 (API 호출용)

#### Python 스크립트 실행 (선택사항)
```bash
# Python 3.7 이상
python --version

# 필요한 패키지 설치
pip install requests
```

### 설치 방법

1. **저장소 클론**
```bash
git clone https://github.com/yourusername/crypto-dashboard.git
cd crypto-dashboard
```

2. **웹 대시보드 실행**
```bash
# 방법 1: 브라우저에서 직접 열기
open dashboard.html

# 방법 2: Python 간이 서버 (선택사항)
python -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

## 📖 사용 방법

### 웹 대시보드 사용하기

#### 1. 암호화폐 선택 및 데이터 로드

```
1. 드롭다운에서 암호화폐 선택 (예: 이더리움, 리플)
2. 데이터 개수 선택 (30/60/100/200일)
3. 기준일 선택 (기본: 오늘)
4. "데이터 로드" 버튼 클릭
```

#### 2. 날짜 필터 적용

```
1. 시작일과 종료일 선택
2. "필터 적용" 버튼 클릭
3. 선택한 기간의 데이터만 표시됨
```

#### 3. 차트 인터랙션

- **마우스 오버** - 상세 정보 툴팁 표시
- **줌/패닝** - 차트 확대/이동 (일부 차트)
- **반응형** - 화면 크기에 따라 자동 조정

### Python 스크립트 사용하기

#### 1. 일봉 데이터 수집 (01.py)

```bash
python 01.py
```

**기능:**
- Upbit API에서 일봉 데이터 조회
- JSON 파일로 저장 (형식: `{market}_{date}_{count}.json`)
- 기본 설정: BTC 100일 데이터

**커스터마이징:**
```python
# 01.py 파일 수정
params = {
    'market': "KRW-ETH",  # 이더리움으로 변경
    "count": 200,         # 200일 데이터
    "to": "2025-01-01 00:00:00"  # 기준일 변경
}
```

#### 2. 마켓 정보 조회 (마켓.py)

```bash
python 마켓.py
```

**기능:**
- Upbit의 모든 마켓 정보 조회
- 마켓 코드, 한글명, 영문명 출력
- API 응답 전체 데이터 표시

## 📁 파일 구조

```
crypto-dashboard/
│
├── dashboard.html                          # 메인 대시보드 (웹 인터페이스)
├── 01.py                                   # 일봉 데이터 수집 스크립트
├── 마켓.py                                 # 마켓 정보 조회 스크립트
├── KRW-BTC_2025-03-24_00-00-00_100.json   # 샘플 데이터 (BTC 100일)
└── README.md                               # 프로젝트 문서
```

### 파일 설명

#### `dashboard.html` (1346 lines)
메인 웹 대시보드 파일입니다.

**주요 구성:**
- HTML 구조 및 UI 컴포넌트
- CSS 스타일링 (반응형 디자인)
- JavaScript 로직:
  - Upbit API 연동
  - 데이터 처리 및 필터링
  - Chart.js를 이용한 시각화
  - 통계 계산 및 업데이트

**핵심 함수:**
- `loadMarkets()` - 마켓 목록 로드
- `loadCoinData()` - 선택한 코인의 데이터 로드
- `updateDashboard()` - 대시보드 전체 업데이트
- `createCandlestickChart()` - 캔들차트 생성
- `createPriceChart()` - 가격 차트 생성 (이동평균선 포함)
- `updatePeriodStats()` - 기간 통계 계산

#### `01.py` (27 lines)
Upbit API에서 일봉 데이터를 가져와 JSON 파일로 저장하는 스크립트입니다.

**사용 예시:**
```python
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
data = response.json()

# JSON 파일로 저장
filename = f"{market}_{to}_{count}.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

#### `마켓.py` (20 lines)
Upbit의 모든 마켓 정보를 조회하는 스크립트입니다.

**출력 형식:**
```
마켓: KRW-BTC, 한국명: 비트코인, 영문명: Bitcoin
마켓: KRW-ETH, 한국명: 이더리움, 영문명: Ethereum
...
```

#### `KRW-BTC_2025-03-24_00-00-00_100.json`
비트코인 100일 일봉 데이터 샘플 파일입니다.

**데이터 구조:**
```json
[
  {
    "market": "KRW-BTC",
    "candle_date_time_kst": "2025-03-23T09:00:00",
    "opening_price": 124150000.0,
    "high_price": 126938000.0,
    "low_price": 124026000.0,
    "trade_price": 126937000.0,
    "candle_acc_trade_price": 100275702981.50278,
    "candle_acc_trade_volume": 799.40587556,
    "change_price": 2787000.0,
    "change_rate": 0.0224486508
  }
]
```

## 🌐 API 정보

### Upbit Open API

**Base URL:** `https://api.upbit.com`

#### 1. 마켓 코드 조회
```
GET /v1/market/all
```

**파라미터:**
- `isDetails` (optional): 상세 정보 포함 여부

**응답:**
```json
[
  {
    "market": "KRW-BTC",
    "korean_name": "비트코인",
    "english_name": "Bitcoin"
  }
]
```

#### 2. 일봉 시세 조회
```
GET /v1/candles/days
```

**파라미터:**
- `market` (required): 마켓 코드 (예: KRW-BTC)
- `count` (optional): 조회 개수 (최대 200)
- `to` (optional): 마지막 캔들 시각 (YYYY-MM-DD HH:mm:ss)

**응답:**
```json
[
  {
    "market": "KRW-BTC",
    "candle_date_time_kst": "2025-03-23T09:00:00",
    "opening_price": 124150000.0,
    "high_price": 126938000.0,
    "low_price": 124026000.0,
    "trade_price": 126937000.0,
    "timestamp": 1742774399406,
    "candle_acc_trade_price": 100275702981.50278,
    "candle_acc_trade_volume": 799.40587556,
    "prev_closing_price": 124150000.0,
    "change_price": 2787000.0,
    "change_rate": 0.0224486508
  }
]
```

**참고:**
- API 요청 제한: 분당 600회, 초당 10회
- 인증 불필요 (공개 API)
- 공식 문서: https://docs.upbit.com/

## 🎨 스크린샷

### 메인 대시보드
```
┌─────────────────────────────────────────────┐
│  🚀 암호화폐 완전 분석 대시보드            │
│  비트코인(BTC) 모든 데이터 및 기술적 분석  │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ 🪙 암호화폐 선택 & 기간 설정               │
│ [비트코인 ▼] [100일 ▼] [2025-03-24] [로드]│
└─────────────────────────────────────────────┘

┌──────────┬──────────┬──────────┬──────────┐
│ 💵 현재가│📊 일일변동│💎 거래량 │📈 기간통계│
│126,937,000│시: 124,150│799.4 BTC│최고: ...│
│  +2.24%  │고: 126,938│100억 원 │최저: ...│
└──────────┴──────────┴──────────┴──────────┘

📊 일봉 캔들차트
[캔들스틱 차트 영역]

📈 가격 추이 & 이동평균선    💹 거래량 추이
[라인 차트]                 [바 차트]
```

## 🔧 커스터마이징

### 차트 색상 변경

`dashboard.html` 파일에서 CSS 변수 수정:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --up-color: #2e7d32;
    --down-color: #c62828;
}
```

### 데이터 소스 변경

다른 거래소 API를 사용하려면:

1. `loadCoinData()` 함수의 URL 변경
2. 데이터 구조에 맞게 파싱 로직 수정
3. 필요시 API 인증 추가

### 이동평균선 기간 수정

```javascript
// dashboard.html 내
const ma5 = calculateMA(data, 5);   // 5일 → 원하는 기간
const ma20 = calculateMA(data, 20); // 20일 → 원하는 기간
```

## 📱 반응형 디자인

### 지원 화면 크기

- **데스크톱** (1400px+) - 완전한 대시보드 뷰
- **태블릿** (768px - 1400px) - 2열 그리드
- **모바일** (~ 768px) - 1열 스택 레이아웃

### 모바일 최적화

- 터치 친화적 UI
- 간소화된 차트
- 스크롤 가능한 테이블

## 🐛 문제 해결

### CORS 오류

**문제:** 브라우저에서 API 호출 시 CORS 오류

**해결책:**
1. 로컬 서버 사용 (Python HTTP Server)
2. 브라우저 CORS 확장 프로그램 설치
3. Python 스크립트로 데이터 미리 다운로드

### 데이터가 로드되지 않음

**체크리스트:**
- [ ] 인터넷 연결 확인
- [ ] Upbit API 상태 확인
- [ ] 올바른 마켓 코드 선택
- [ ] 브라우저 콘솔에서 에러 확인

### 차트가 표시되지 않음

**해결책:**
1. 브라우저 새로고침 (Ctrl+F5)
2. Chart.js CDN 로드 확인
3. JavaScript 콘솔 에러 확인

## 🤝 기여하기

프로젝트 개선에 기여하고 싶으신가요? 환영합니다!

### 기여 방법

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 개선 아이디어

- [ ] 추가 기술적 지표 (RSI, MACD, 볼린저 밴드)
- [ ] 실시간 가격 업데이트 (WebSocket)
- [ ] 포트폴리오 추적 기능
- [ ] 알림 기능 (가격 알림)
- [ ] 데이터 내보내기 (CSV, Excel)
- [ ] 다국어 지원
- [ ] 다크 모드

## 📜 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 👨‍💻 개발자

**프로젝트 제작:** Park Jaemin

## 🙏 감사의 말

- **Upbit** - 공개 API 제공
- **Chart.js** - 훌륭한 차트 라이브러리
- **MDN Web Docs** - 웹 개발 참고 자료

## 📞 연락처

프로젝트 관련 문의나 제안사항이 있으시면 언제든 연락주세요!

- **이메일:** your.email@example.com
- **GitHub:** [@yourusername](https://github.com/yourusername)

## 🔗 관련 링크

- [Upbit API 문서](https://docs.upbit.com/)
- [Chart.js 문서](https://www.chartjs.org/docs/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!

**Made with ❤️ and ☕**

