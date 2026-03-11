
import firebase_admin
from firebase_admin import credentials, storage, firestore
import datetime
import cv2

# Firebase 초기화
cred = credentials.Certificate("path/to/your/firebase/credential.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-project-id.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

# 사진 촬영
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('/home/pi/wildboar.jpg', image)
camera.release()

# 파이어베이스에 사진 업로드
blob = bucket.blob('wildboar.jpg')
blob.upload_from_filename('/home/pi/wildboar.jpg')

# 데이터베이스에 정보 저장
data = {
    'name': '멧돼지',
    'time': datetime.datetime.now().isoformat(),
    'imageUrl': blob.public_url
}
db.collection('wildlife').add(data)

print("Data uploaded successfully")
