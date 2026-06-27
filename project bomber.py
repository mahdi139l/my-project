import requests
import time

# شماره گیرنده
number = "+989938929001"

# متن پیام
message = "salam"

# آدرس API (اینجا باید آدرس درست API سرویس پیام‌رسان خودت رو وارد کنی)
api_url = "https://api.open-meteo.com/v1/forecast?latitude=35.6892&longitude=51.3890&hourly=temperature_2m"


# ارسال 100 پیام
for _ in range(100):
    response = requests.post(api_url, data={"to": number, "text": message})
    print(response.status_code, response.text)  # نمایش نتیجه درخواست
    time.sleep(1)  # یک ثانیه مکث بین هر پیام
