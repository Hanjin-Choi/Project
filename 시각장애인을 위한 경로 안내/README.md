# WE(Watch Everything)
## 프로젝트 배경
- 도보 위의 여러 위험으로 인해 외출하기 어려운 시각장애인들
- 도보 위에 아무렇게 놓인 킥보드
- 음향신호기가 고장나거나 없는 횡단보도
- 도착 버스 번호를 알 수 없는 버스 정류장
![alt text](image/위험성.png)![alt text](image/음향신호기.png)
## 팀원
- 정노원 : 팀장, Infra, BackEnd, Android
- 유성주 : FrontEnd, Android
- 강성구 : BackEnd
- 최한진 : AI, Embedded
- 한동민 : AI, Embedded
- 김보성 : AI, Embedded
## 기술 스택
- Infra : Docker, Jenkins, NGINX, AWS EC2
- Front-End : Android Studio, Figma
- Back-End : MySQL, Spring Boot, Firebase
- Embedded : NVIDIA JETSON, AWS Iot MQTT, GTTS
- AI : OpenCV, YOLOv5, Google Vision API 
## ERD
![alt text](image/ERD.PNG)
## Infra
![alt text](image/Infra.png)
## Application
### Front-End
-  Android Studio Koala 2024.1.1 / Java 언어 사용

---

- 제작할 애플리케이션을 피그마를 통해 앱 페이지들의 디자인 및 동작을 먼저 구상
![alt text](image/android_5.png)

---

- 해당 결과물을 토대로 안드로이드 스튜디오 프로젝트로 애플리케이션 개발
- 앱 페이지들의 디자인인 xml 파일들과, 해당 페이지들의 동작을 정의하는 Activity.java 파일로 나누어 작성

![alt text](image/android_1.png)
![alt text](image/android_2.png)

---
- 최종 완성 애플리케이션 실행 캡처본
![alt text](image/android_3.png)
![alt text](image/android_4.png)
### Back-End
1. 회원 가입 및 유저 관리
    - 회원 가입 및 로그인
    - 중복 이메일 방지를 위한 이메일 검사
    - 유저 정보 수정 및 프로필 이미지 등록
    - 유저의 기기 정보 등록
2. 음성을 이용한 길 찾기
    - Jsoup과 크롤링을 이용한 목표 위치 탐색
    - 카카오맵 Api를 이용한 위도, 경도 검색 
    - SK Api를 이용한 경로 탐색
3. 이동 중 GPS 정보를 이용
    - 현재 위치에 따른 카메라 모드 변경
    - 방향 정보를 이용한 경로 이탈 방지
    - 보호자의 장애인 현재 위치 조회
4. 하드웨어 통신
    - 현재 위치에 따른 카메라 모듈 변경
    - 응급 상황 발생 시 긴급 연락
    - 탑승 후보 버스 리스트 송신

## Hardware(AI & Iot)
### IMU Sensor
* MPU-6050 모듈과 해당 모듈에서 지원하는 라이브러리를 사용하여 I2C 통신으로 기울기 정보 수신
* IMU sensor의 값을 사용하는 데 있어서 정확한 값으로 보정하기 위해 상보필터 사용
* 가속도 센서의 노이즈 문제와 자이로 센서의 드리프트 문제를 해결함으로써 사용자의 몸 기울기를 측정 가능

```py     
rollA = math.atan2(xAccel, zAccel) / (2 * math.pi) * 360
pitchA = math.atan2(yAccel, zAccel) / (2 * math.pi) * 360
    
rollComp = rollA * 0.005 + 0.995 * (rollComp + yGyro * tLoop)
pitchComp = pitchA * 0.005 + 0.995 * (pitchComp + xGyro * tLoop)
```


### MQTT

* N : N 하드웨어 기기와 핸드폰간의 통신을 위해 MQTT 프로토콜 사용
* AWS IoT Core에서 제공하는 MQTT BROKER를 사용하여 핸드폰과 젯슨 나노가 연결 및 데이터를 송수신함
* TOPIC_1 : 명령어, 탑승 버스 후보 리스트 정보 수신
* TOPIC_2 : 사용자의 위험 상태 정보 + 객체 인식 및 동작 수행 완료 정보 송신
* TOPIC_3 : 핸드폰으로 부터 연결 요청 수신
* TOPIC_4 : 젯슨 나노가 전원이 켜지면 주기적으로 연결 요청을 송신


### Multi Thread
* Thread 1 : 사용자의 GPS 위치에 따라 카메라 모듈 동작
* Thread 2 : IMU 센서의 데이터 수신 및 후처리
* Thread 3 : MQTT 통신을 통해 폴링(POLLING) 방식으로 TOPIC_1 토픽으로 부터 데이터를 수신
* Thread 3에서 데이터를 수신하는 경우 JSON 파일에 write, Thread 1에서 read를 통해 해당 데이터를 확인 함
* 이 때 Mutex Lock를 사용하여 파일에 대한 동시 접근을 못하게 함

### 버스 번호 인식
* Yolov5s 모델 학습(1549개 Dataset - 버스 번호, 버스 앞면부 Labeling 후 학습)
* 학습 모델을 Yolo OpenSource 중 detect.py로 객체 탐지
* 인식한 영역을 Crop을 통해 OCR 모듈로 전송
* OCR 모듈 - Google Cloud Vision API
* 서버에서 전송 받은 탑승 버스 후보군과 대조하여 해당 번호를 감지했을 경우 소리 알림
* 소리 알림 - gTTS API 활용


![버스 번호 인식 결과](image/Bus_Detection.png)


### 신호등 인식 분류
* Yolov5s 모델 학습(4201개 Dataset, Augmentation(Rotation, Flip)추가 8955개 Dataset - 신호등 전면부 Labeling 후 학습)
* 학습 모델을 Yolo OpenSource 중 detect.py로 객체 탐지
* 인식한 영역을 Crop 후 색 구분 코드를 사용
* 색 구분 방식 : numpy 데이터를 HSV(색조, 채도, 명도) 데이터로 변환 후 해당 영역에 따른 빨간색,초록색의 비율을 비교 후 높은 값을 선택
* 초록을 인지하는 프레임 횟수를 확인, 빨강을 인지하면 횟수 초기화, 빨강에서 초록으로 변환될 경우 소리알림
* 소리알림 : gTTS를 localfile로 저장하여 소리 재생
    * Python playsound 모듈사용

![신호등 인식 결과](image/Traffic_Detection.png)

### 장애물 인지 알림
* Yolov5s 모델 학습(5742개 Dataset, Augmentation(Rotation, Flip)추가 13669개 Dataset - 킥보드 360˚ 모습 Labeling 후 학습)
* 학습 모델을 Yolo OpenSource 중 detect.py로 객체 탐지
* Python Shapely 모듈을 이용하여 시야 영역과 객체 영역 겹침 감지 후 소리 알림
* 소리 알림 : gTTS를 localfile로 저장하여 소리 재생
    * Python playsound 모듈사용 

![킥보드 인식 결과](image/Kickboard_Detection.png)