# 🐗 YOLO 기반 멧돼지 탐지 및 경고 시스템
## 1. 주제

라즈베리파이 기반 환경에서 YOLO 객체 탐지 모델을 활용하여 멧돼지를 실시간으로 탐지하고,
탐지 시 경고음 출력, 사용자 알림 전송, 탐지 로그 저장 기능을 제공하는 스마트 방지 시스템을 구현한다.

농가 주변에 출몰하는 멧돼지를 자동으로 탐지하여 피해를 예방하는 것을 목적으로 한다.

## 2. 주요 기능
### 1️⃣ 실시간 멧돼지 탐지

카메라 영상 프레임을 입력받아 YOLO 모델을 이용하여 멧돼지 객체를 탐지한다.

OpenCV 기반 영상 처리

YOLOv8 객체 탐지 모델 사용

0.5초 간격 추론으로 라즈베리파이 성능 최적화

### 2️⃣ 경고음 출력

멧돼지가 탐지되면 스피커를 통해 경고음을 출력하여 멧돼지를 쫓는다.

Pygame 기반 오디오 출력

멧돼지 탐지 시 반복 재생

멧돼지 미탐지 시 자동 정지

### 3️⃣ 탐지 이미지 저장

멧돼지가 탐지된 순간의 이미지를 자동으로 캡처하여 저장한다.

탐지 시 이미지 파일 생성

탐지 시간 기반 파일 이름 생성

### 4️⃣ 사용자 알림 기능

멧돼지 탐지 시 LINE Notify API를 이용하여 사용자에게 알림을 전송한다.

전송 정보

탐지 시간

탐지 이미지

### 5️⃣ 탐지 로그 저장

탐지 이벤트를 Firebase Realtime Database에 저장하여 기록 관리 기능을 제공한다.

저장 정보

3. 시스템 아키텍처
''' Camera
   ↓
Raspberry Pi
   ↓
YOLOv8 Object Detection
   ↓
Pig Detection
   ↓
 ┌───────────────┬───────────────┬───────────────┐
 │               │               │               │
Speaker Alarm   Image Capture   LINE Notify    Firebase Log '''

동작 흐름

카메라로 영상 입력

YOLO 모델로 객체 탐지 수행

멧돼지(pig) 클래스 탐지 여부 확인

멧돼지 탐지 시

경고음 출력

이미지 저장

사용자 알림 전송

Firebase 로그 저장

## 4. 기술 스택
#### Language

Python

AI / Computer Vision

YOLOv8

OpenCV

#### Hardware / Edge Device

Raspberry Pi

USB Camera

Speaker

#### External Service

Firebase Realtime Database

LINE Notify API

Library

Pygame

Requests

#### Development Environment

Google Colab (모델 학습)

### 5. 핵심 기술 및 문제 해결
1️⃣ 데이터셋 직접 구축

멧돼지 탐지를 위해 커스텀 데이터셋을 직접 제작하였다.

멧돼지 인형 및 모형을 활용하여 이미지 촬영

다양한 각도에서 데이터 수집

객체 라벨링 수행

이후 Google Colab 환경에서 YOLO 모델을 학습하였다.

2️⃣ Edge AI 환경 최적화

라즈베리파이는 연산 성능이 제한적이기 때문에
모든 프레임에 대해 YOLO 추론을 수행하지 않고 0.5초 간격으로 모델을 실행하여 성능을 최적화하였다.

if time.time() - start_time >= 0.5:
    results = model(frame)
3️⃣ 이벤트 기반 시스템 설계

멧돼지 탐지 이벤트 발생 시 다음 기능이 동시에 수행되도록 구현하였다.

경고음 출력

이미지 캡처

사용자 알림 전송

탐지 로그 저장

4️⃣ 코드 모듈화

시스템 유지보수성과 확장성을 위해 기능별로 모듈을 분리하였다.

main.py
camera_utils.py
speaker_utils.py
sms_utils.py
firebase_utils.py

이벤트 유형

탐지 시간
