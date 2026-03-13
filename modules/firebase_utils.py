import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate('/home/pi/my_project/config/farmsecurity-4c847-firebase-adminsdk-sm305-6de3134385.json')


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://farmsecurity-4c847-default-rtdb.firebaseio.com/'
})

def log_event(event_type, event_time):

    try:

        ref = db.reference('logs')

        ref.push({
            'event_type': event_type,
            'event_time': event_time
        })
        print(f"Logged event: {event_type} at {event_time}")
    except Exception as e:

        print(f"Failed to log event: {e}")


log_event('test_event', '2024-06-21 12:00:00')
