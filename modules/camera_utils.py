import cv2

def capture_and_save_frame(frame, filename):

    cv2.imwrite(filename, frame)
