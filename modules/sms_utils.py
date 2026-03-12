import requests
import time
import os


def get_current_time():
    """
    현재 시간 반환
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


def send_line_notify(token, message, image_path=None):
    """
    LINE Notify 메시지 전송
    """

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "message": message
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

    return response.status_code