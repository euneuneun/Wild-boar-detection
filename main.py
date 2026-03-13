import cv2
import time
from ultralytics import YOLO
import os
import datetime


from firebase_utils import log_event
from camera_utils import capture_and_save_frame
from speaker_utils import init_speaker, play_sound, stop_sound
from sms_utils import send_line_notify, get_current_time

model = YOLO(r'/home/pi/Downloads/best (big).pt')


cap = cv2.VideoCapture(0)


sound = init_speaker(r'/home/pi/Downloads/sound.mp3')


line_token = 'NfxUs3YKqI5PtiEDwI50oLhhVWIgjiIqGHsGkv7XHEj'


start_time = time.time()
results = None
hog_detected_previous = False

while cap.isOpened():
    success, frame = cap.read()

    if success:

        if time.time() - start_time >= 0.5:
            results = model(frame)
            start_time = time.time()

        if results is not None:

            annotated_frame = results[0].plot()
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            try:

                hog_detected = False
                for r in results[0].boxes:
                    cls = int(r.cls)
                    if model.names[cls] == 'pig':  
                        hog_detected = True
                        break


                if hog_detected and not hog_detected_previous:
                    print('pig detected.')

                    detected_time = get_current_time()
                    print(f'detected time: {detected_time}')
 
                    image_filename = f"detected_{time.strftime('%Y%m%d%H%M%S')}.jpg"

                    capture_and_save_frame(frame, image_filename)

                    response_status = send_line_notify(line_token, f"pig detected..\ndetected time: {detected_time}", image_filename)
                    if response_status == 200:
                        print('The LINE Notify message has been sent successfully.')
                    else:
                        print(f'Failed to send LINE Notify message: {response_status}')

                    log_event('pig_detected', detected_time)

                    play_sound(sound)
                    log_event('noise_emitted', detected_time)

                elif not hog_detected and hog_detected_previous:
                    print('Its not a pig.')
                    stop_sound(sound)  

                hog_detected_previous = hog_detected

            except Exception as e:

                print(f'Error: {e}')
                print('Its not a pig.')


        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("p"): 
            cv2.waitKey(-1) 
    else:
        break


cap.release()
cv2.destroyAllWindows()
