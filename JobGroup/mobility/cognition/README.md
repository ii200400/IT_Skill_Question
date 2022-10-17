# 인지(Cognition)

카메라나 라이더(LiDar)와 같은 센서를 통해서 이미지나 각종 데이터를 입력받아 객체를 인식하고 객체가 무엇인지 분류하는 기술

- [좌표계](./coordinate%20system/README.md)
- [Orientation(강체의 방향)](./orientation/README.md)
- [정밀도로지도](./precise%20road%20map/README.md)
- [차선인지](./lane%20recognition/README.md)
- [SVM(Surround View Monitor)](./SVM/README.md)

## Deep learning object detection

이론 자체는 상당히 오래전부터 있었으나 하드웨어의 제약으로 인하여 연구가 이루어지지 못하고 있다가 최근 하드웨어의 성능이 딥러닝을 진행할 수 있을만큼 좋아지면서 각광받게된 학문 중 하나

미리 준비된 데이터를 기계가 마치 사람이 학습하듯이 이미지 등을 학습하는 과정을 거쳐 물체를 인식하게 된다.

<img src="https://user-images.githubusercontent.com/19484971/186626911-630ed24b-a1aa-40d0-9854-942230c2fb94.png" width=600>

- Classification : 이미지에 따라서 labeling을 해주는 것
    - labeling : 이미지에 이름을 붙이는 것
- Localization : 이미지에 객체가 어디에 있는지 bounding box를 만들어 주는 것
    - Classification과 Localization이 결합되면 위와 같이 bounding box와 labeling을 동시에 표시한다.
- Detection : 이미지 내의 여러 이미지들을 찾아내는 것

- 자율주행에서 빠질 수 없는 요소 중 하나
    - Single shot detection, YOLO, Faster R-CNN 등
- 인간이 경험을 거치며 스스로 학습하는 과정을 모방
- 현재까지의 여러 머신러닝 기술 중 가장 주목받는 것은 인간의 뇌를 형성하는 신경망을 모방하여 학습하는 딥러닝
    - 2012년 imagenet? 대회에서의 물체 인식률은 75%가 넘지 못하였으나, 캐나다 토론토 대학의 알렌토 크리브스키(?)가 gpu기반의 딥러닝 기술을 가져와 인식률이 크게 뛰면서 해당 기술이 널리 알려지게 되었다.
- 자율주행 자동차가 스스로 주행하기 위해 주변 환경, 주행 도로 등을 인식하여 주행 판단을 내리고 안전한 기능 제어를 위해 꼭 필요한 기술
    - 실제로 여러 곳에서 자율주행 자동차의 인지/판단/제어 기능 향상에 딥러닝을 적용하는 연구가 활발하게 진행 중에 있음
- 현재는 사람이 인식하기 어려운 물체도 인식할 정도로 뛰어난 정확도를 선보임

## 정밀도로 지도

센서와 함께 자동차의 주행 환경을 확인하기 위한 말 그대로의 정밀한 도로 지도, 이 지도 없이 센서만으로 의존하는 것은 주변환경을 파악하기 힘들기 때문에 (센서를 활용할 때 발생하는 오차가 클 때는 수십~수백cm 가 생긴다고 언급) 활용하게 되었다. 물론 사용하는 정밀도로지도의 오차가 m 단위이면 안된다.    
특히 사진이나 센서만으로 알기 힘든 도로의 곡률이나 경사로 등에 대한 정보를 빠르게 얻을 때 좋다.

정적인 환경들은 정밀도로지도에서 파악하고 GPS 카메라 Lidar 등의 센서들을 통해 외부의 변수를 탐지하여 상황 인지를 보완한다.

- 용어
    - 가외성(redundancy) : 중복성 여유분 잉여 비슷한 단어로, 실재로 필요한 요소보다 더 많은 요소를 준비하여 보다 안정성을 유지할 수 있도록 하는 특성.   
    효율성과 대응되지만 환경의 불확실성을 고려하기 위해 생겨났으며 실재로 가외성이 오류발생 확률을 기하급수적으로 크게 낮춰준다는 사실을 알 수 있다.

- 자율주행 등에 필요한 정보를 3차원으로 제작한 전자 지도
    - 차선(도로 경계선, 정지선)   
      도로 시설(중앙분리대, 터널, 지하차도)   
      표지시설 (교통안전표지, 노면표시)
- 해상도 0.25 급
- 국토지리정보원에서 제작하고 배포

- 종류
    - PointCloud Map
        - PointCloud란, 3차원 좌표를 가지는 점들로 불규칙하게 구선된 데이터를 의미한다. 점구름 또는 점군데이터로 불린다.
        - LiDAR 센서나 RGB-D 센서등으로부터 수집된 데이터를 의미
        - 센서들은 물체에 빛이나 신호를 보내어 되돌아오는 시간과 속도를 계산하여 거리정보를 얻고 하나의 포인트를 생성하고 이러한 포인트가 모여 지도를 만드는 원리
    - HD Map (Vector Map)
        - 도로 위의 신호등, 차선, 교차로 등을 벡터 데이터로 표현하여 지도를 구성
        - 형상만이 남고 차선등의 정보는 없는 포인트 클라우드와는 다르게 주행에 의미있는 정보들을 표현한다.
        - HD map의 차선 등의 정보가 자율주행 차량의 성능에 큰 영향을 끼친다.
    - Grid Map
        - 격자 지도로 자료가 격자의 형태로 전달되는 지도
        - 경로 계획, 경로 생성 등에 많이 활용
        - 포인트 클라우드 맵보다 상대적으로 용량은 작지만, 좌표의 정밀도가 떨어진다.

## 센서

자율주행에서 사람의 눈과 같은 역할을 한다.

- 카메라 (Camera)
- 라이다 (LiDAR)
- 레이더 (Radar)
- GPS
- IMU

카메라, 라이다, 레이더는 인지를 위한 인지센서에 들어가며 GPS, IMU는 대략 Localization(위치를 파악하는) 센서이면서도 인지센서를 보완하는 센서이기도 하다.

센서의 분류(인지센서, Localization센서)는 발전 따라서 회사에 따라서 분류하는 방법이 다르기도 하니 명확한 부분은 아니다.

### 카메라 (Camera)

- 사진을 찍어 시각적으로 보이는 다양한 정보를 얻음
    - 딥 러닝(Deep Learning)을 통한 차량 및 보행자 인지
    - 교통표지판의 제한 속도 정보
    - 차선, 신호등 인지 등등
    - 카메라를 통해 인식한 차선을 위치와 곡률을 계산하여 하늘에서 보는 것과 같이 재현은 가능
- 비교적 낮은 단가
- 밤이나 날씨 등에 대한 품질이 떨어지기 쉽고 거리 파악에 어려움

- 종류
    - pinhole camera   
    렌즈를 사용하지 않고 작은 구멍을 통해서 빛을 받아들여 촬영하는 사진 (일반적으로 흔히 보는 카메라)
    - Fisheye Lens Camera (어안 렌즈 카메라)   
    빛의 굴절로 인해서 생기는 둥근 사진이 특징인 카메라

#### Ground Truth

- 기상학에서 유래된 용어로 어느 한 장소에서 수집된 정보를 의미
- 보통 `지상 실측 정보`로 해석
- 기계학습의 관점에서는 GT는 학습하고자 하는 `데이터의 원본` 혹은 `실제 값`을 표현
    - 딥러닝 모델이 예측을 잘 했는지를 가늠할 때 기준이 되는 데이터를 의미
    - [블로그 참고](https://eair.tistory.com/16)
- 빛이 구름이나 대기를 통과하게 되면서 실제 모습이 왜곡되는 경우가 있어 보정이 필요

- 종류
    - RGB
        - 카메라를 통해 받은 기본적인 이미지
    - Semantic (class based segmentation)
        - 같은 객체끼리 색상으로 구분을 하는 기능
        - Seen을 나타낼 때 사용
        - 객체들이 묶여있어 차량이 주행 할 영역을 판단할 수 있음
    - Instance (instance based segmentation)
        - 객체를 각각 식별하는 기능
        - 각 객체에 바운딩 박스가 생성
        - 객체의 위치와 속도에 대한 정보를 가짐

시뮬레이션에서는 각 객체의 위치를 알고있기 때문에 `Semantic`이나 `Instance`는 카메라의 이미지를 통해 인식하여 분류하는 것이 아니라 시뮬레이션이 직접 데이터를 제공한다.

#### Camera Simulator

카메라를 시뮬레이터에서 사용하기 위해서는 3가지 절차를 따라야 한다. 순서 상관은 없다.

1. 센서(카메라) 모델 선택
2. Ground Truth 선택
3. 카메라 파라미터 설정

<img src="https://user-images.githubusercontent.com/19484971/188307948-5c25344c-d290-4c67-89fa-95e15a58fac7.png" width=500>

카메라 설정은 시뮬레이션 내에서 설정할 수 있다. 

크게 내부요인(intrinsic)인 카메라 센서 크기, 초점거리(Focal Length), 주점(Principal Point)과 외부요인(extrinsic) 장착 위치나 자세, 각도 등의 설정이 있다.

마지막으로 통신방식(CommunicationInterface) UDP와 ROS 중 하나를 선택하면 되는데 필자는 보통 ROS를 사용하였다.

### 라이다 (LiDAR)

Laser Imaging Detection And Ranging (레이저 화상 검출과 거리 측정)의 약어로 자율주행 자동차의 센서로 자주 채택된다.

- 레이저 펄스를 쏘아 반사되어 돌아오는 시간으로 사물 간 거리를 파악
- 정밀하고 형태 인식 가능 (3D 이미지)
- 가격이 비싸고 외부환경에 영향을 많이 받음
- 큰 외형과 에너지 소비율
- 눈이나 비에 반사되어 악천후에 약함
- 최근 라이다 센서의 발전으로 많이 활용됨

- 모델
    - VLS 128
    - HDL 64
    - Velarray

- LiDAR Ground Truth
    - Intensity   
    레이저 펄스가 물체에 반사되어 돌아오는 강도   
    부딪힌 물체의 매질이나 강도, 매끄러움 등으로 강도가 달라지는 점을 활용하여 시각적으로 다르게 표현이 가능하다.
    - Semantic   
    카메라와 동문
    - Instance
    카메라와 동문

<img src="https://user-images.githubusercontent.com/19484971/188313102-b6c30462-17d4-4dc8-a53b-a5a2baf21cdf.png" width=500>

현실의 라이더는 시뮬레이터와는 다르게 많은 노이즈가 있으므로 실제 라이더와 비슷하게 진행할 수 있도록 가우시안 노이즈를 설정할 수 있다.

### 레이더 (Rader)

- 전파를 매개체로 사물 간 거리 및 형태 파악
- 소형화가 가능하고 비교적 저렴
- 라이다 센서보다 정밀도는 떨어짐 
- 작은 물체 식별과 자세한 형태 파악이 어려움
- 날씨의 영향이 적음
- 사이즈와 성능이 비례

### GPS

GPS(Global Positioning System, 글로벌 포지셔닝 시스템)의 약자

- 인공위성을 이용하여 현재위치를 알아내는 센서
- 31개의 인공위성 중 최소 4개 이상의 위성과 연결되어 있어야 위치 계산이 가능함
- 경로 계획에 사용하기 위해서는 3D인 좌표값(WGS84)을 2D 좌표값(UTM)으로 변환이 필수
    - 단순하게 지구본을 종이 지도로 바꾸는 계산법이 필요하다는 것
- 숲이나 고층 건물, 터널 등의 장애물에 대한 영향을 많이 받음

- 모델
    - WGS84

LiDAR와 비슷하게 가우시안 노이즈를 추가할 수 있으며 frame 을 조절하는 설정을 조정할 수 있다.

<img src="https://user-images.githubusercontent.com/19484971/188319899-639af80e-9e51-455e-ab01-5bf27c3741d8.png" width=500>

### IMU(Inertial Measurement Unit, 관성 측정 장치)

- 3축에 대한 각속도를 측정하는 자이로센서와 3축의 가속도를 측정하는 가속도센서로 구성됨
    - x축(물체의 정면 기준) 회전은 Roll
    - y축(물체의 측면 기준) 회전은 Yaw
    - z축(물체의 상단 기준) 회전은 Pitch
- 지자기센서와 가속도센서 등으로 측정한 가속도 및 각속도 값을 적분하여 나온 값으로 이동거리를 계산
- 시간이 지날수록 오차가 누적되어 정확도가 하락

<img src="https://user-images.githubusercontent.com/19484971/188320310-38e10376-beb3-48ff-96f3-fffa756ff23b.png" width=500>

다른 센서와 마찬가지로 가우시안 노이즈를 추가할 수 있다.

<img src="https://user-images.githubusercontent.com/19484971/188320393-eecbb164-a91e-4da3-94d9-89403c510f79.png" width=300>


### 센서 범위

센서들의 특징에 따라서 차량에 설치하는 위치와 각도가 다른데 일반적으로 아래와 같다고 한다.

<img src="https://user-images.githubusercontent.com/19484971/188316004-9ce88204-0fd0-4cb7-a146-1ce9aefd157d.png" width=600>

글로 풀어서 해석하면 아래와 같다.

- LiDAR : 긴급제동장치에 사용
- Camera : 전방위 물체인식(교통상황, 차선확인, 사람인식, 주차보조 등)에 사용
- Short-Middle Range Radar : 사각지대나 근접한 다른 차량과의 거리 확인에 사용
- Ultrasound : 전후방 주차보조용

- 회사별 센서 배치
    - Waymo   
    <img src="https://user-images.githubusercontent.com/19484971/188316363-b286fd3f-72c8-4b2a-9681-a4307d3769f3.png" width=400>
    - Motinal   
    <img src="https://user-images.githubusercontent.com/19484971/188316416-295f5831-8c35-4b8a-8881-a66806b376a3.png" width=400>
    - Baidu(Apollo)   
    <img src="https://user-images.githubusercontent.com/19484971/188316449-a8687948-4ff9-4a30-8ce3-d02c5b1a13f0.png" width=400>
    - Tesla (당시 높은 LiDAR 가격으로 카메라가 주요함)   
    <img src="https://user-images.githubusercontent.com/19484971/188316520-cdd3e3d1-a5a0-4171-b0ef-3c2d21c48217.png" width=400>

### 센서 범위 계산

- 용어
    - FoV(Field of View) : 시야각

위에서 보았을 때

<img src="https://user-images.githubusercontent.com/19484971/188318307-d8a1f124-ba02-4361-a2b6-a2891f044889.jpg" width=600>

옆에서 보았을 때

<img src="https://user-images.githubusercontent.com/19484971/188318458-007d76e2-4e5f-482a-8ca6-862f873c9cb4.png" width=600>
<img src="https://user-images.githubusercontent.com/19484971/188318487-c3ba2f7b-6faf-41b5-b0cf-a6a136dc2694.png" width=400>

LiDAR의 경우 채널에 따라서 최대 감지 거리가 변할 수 있다는 점에 유의해야 한다.

또한 레이더의 경우 이론적으로는 확인하기 어려워 CAE라는 프로그램을 통해서 해석을 거쳐야 한다.

<img src="https://user-images.githubusercontent.com/19484971/188318670-c0428d09-2408-4b73-9ae5-eff2ae4a33b4.jpg" width=600>

## 라이더 클러스터

센서파트의 라이다 부분을 맡게 되었다.

클러스터라는 것을 군집화 작업을 해야 하는데 아래의 블로그를 참고하였다.

esp라는 것이 높을수록 더 큰 영역을 하나의 군집으로, min_sample이라는 것이 높을수록 잡음 포인트로 간주한다.

https://m.blog.naver.com/ssdyka/221273386455