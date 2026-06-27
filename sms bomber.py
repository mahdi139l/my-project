
# import requests

# number = input("شماره گیرنده را وارد کنید: ")
# message = "سلام"
# api_url = "https://api.yourservice.com/send"
# api_key = "YOUR_API_KEY" 
# headers = {"Authorization": f"Bearer {api_key}"}

# response = requests.post(api_url, json={"to": number, "text": message}, headers=headers)
# print(response.status_code, response.text)









import requests
import time
number = input("enter your number?").strip()
message = "salam"
api_url = "https://example.com/send"  
for _ in range(100):
    response = requests.post(api_url, data={"to": number, "text": message})
    print(response.status_code, response.text)
    time.sleep(1)  