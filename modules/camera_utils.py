import cv2

def capture_and_save_frame(frame, filename):
    """
    현재 프레임을 이미지 파일로 저장
    """
    cv2.imwrite(filename, frame)