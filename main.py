from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 텔레그램 환경변수 가져오기
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

@app.route('/tradingview', methods=['POST'])
def tradingview_webhook():
    data = request.get_json()

    symbol = data.get('symbol', 'N/A')
    price = data.get('price', 'N/A')
    signal = data.get('signal', 'N/A')
    time = data.get('time', 'N/A')

    message = f"📈 트레이딩뷰 시그널\n\n🪙 종목: {symbol}\n💵 가격: {price}\n📌 시그널: {signal}\n⏰ 시간: {time}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, data=payload)

    return 'ok', 200

# ✅ Render 포트 바인딩 명시
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
