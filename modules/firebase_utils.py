import firebase_admin
from firebase_admin import credentials, db


# Firebase 서비스 계정 키
cred = credentials.Certificate("config/firebase_key.json")


# Firebase 초기화
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com/'
})


def log_event(event_type, event_time):
    """
    이벤트 로그를 Firebase에 저장
    """

    try:

        ref = db.reference('logs')

        ref.push({
            'event_type': event_type,
            'event_time': event_time
        })

        print(f"Logged event: {event_type} at {event_time}")

    except Exception as e:

        print(f"Failed to log event: {e}")