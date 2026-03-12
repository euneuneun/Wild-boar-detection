
import cv2
import time
from ultralytics import YOLO

from modules.firebase_utils import log_event
from modules.camera_utils import capture_and_save_frame
from modules.speaker_utils import init_speaker, play_sound, stop_sound
from modules.sms_utils import send_line_notify, get_current_time


print("System Starting...")


# YOLO 모델 로드
model = YOLO("models/best.pt")


# 카메라 연결
cap = cv2.VideoCapture(0)


# 스피커 초기화
sound = init_speaker("sound/sound.mp3")


# LINE Notify Token
line_token = "YOUR_LINE_TOKEN"


start_time = time.time()
results = None
hog_detected_previous = False


while cap.isOpened():

    success, frame = cap.read()

    if success:

        # 0.5초마다 YOLO 실행 (성능 최적화)
        if time.time() - start_time >= 0.5:
            results = model(frame)
            start_time = time.time()

        if results is not None:

            annotated_frame = results[0].plot()
            cv2.imshow("Wild Boar Detection", annotated_frame)

            try:

                hog_detected = False

                for r in results[0].boxes:

                    cls = int(r.cls)

                    if model.names[cls] == "pig":
                        hog_detected = True
                        break


                # 멧돼지 탐지 이벤트
                if hog_detected and not hog_detected_previous:

                    print("Pig detected")

                    detected_time = get_current_time()

                    image_filename = f"detected_{time.strftime('%Y%m%d_%H%M%S')}.jpg"

                    capture_and_save_frame(frame, image_filename)

                    send_line_notify(
                        line_token,
                        f"Pig detected\nTime: {detected_time}",
                        image_filename
                    )

                    log_event("pig_detected", detected_time)

                    play_sound(sound)

                    log_event("noise_emitted", detected_time)


                elif not hog_detected and hog_detected_previous:

                    print("No pig")

                    stop_sound(sound)


                hog_detected_previous = hog_detected


            except Exception as e:

                print(f"Error: {e}")


        key = cv2.waitKey(1)

        if key == ord("q"):
            break

        elif key == ord("p"):
            cv2.waitKey(-1)

    else:
        break


cap.release()
cv2.destroyAllWindows()