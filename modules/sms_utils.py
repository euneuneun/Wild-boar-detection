import requests
import time
import os


line_token = 'NfxUs3YKqI5PtiEDwI50oLhhVWIgjiIqGHsGkv7XHEj'

def get_current_time():

    return time.strftime("%Y-%m-%d %H:%M:%S')

def send_line_notify(token, message, image_path=None):

    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "message": f"{message}\n{get_current_time()}"
    }
    files = None
    if image_path is not None and os.path.exists(image_path):
        files = {'imageFile': open(image_path, 'rb')}
    response = requests.post(
        "https://notify-api.line.me/api/notify",
        headers=headers,
        data=payload,
        files=files
    )
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    return response.status_code


send_line_notify(line_token, "Test message from Raspberry Pi")
