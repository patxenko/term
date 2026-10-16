import logging
import requests

notif_logger = logging.getLogger('notification')
fh = logging.FileHandler('parser.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s (%(levelname)s):  %(message)s')
fh.setFormatter(formatter)
notif_logger.addHandler(fh)


def send_telegram(message):
    # https://www.youtube.com/watch?v=ozQfKhdNjJU
    token='7388738599:AAFQSPeKozuDpF0deR_FjTJWF8ORT61AIvY'
    # url = f"https://api.telegram.org/bot{token}/getUpdates"
    # print(requests.get(url).json())
    chat_id = '1609772951'
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    r = requests.get(url)
    res = r.json()
    if 'ok' not in res or res['ok'] is not True:
        print(r.json())
        exit('notification could not be sent')
        
import requests

def send_telegram_2(message):
    token='7388738599:AAFQSPeKozuDpF0deR_FjTJWF8ORT61AIvY'
    chat_id = '1609772951'

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    r = requests.post(
        url,
        data={
            "chat_id": chat_id,
            "text": message,
            "disable_notification": "false"
        },
        timeout=15
    )

    print("HTTP:", r.status_code)
    print("Telegram:", r.json())


send_telegram("SENAL_D");