# 자율주행 기초 알고리즘

그 강의 특화 프로젝트의 두번째 명세서 내용을 기반으로 한다.

차량의 인지/판단/제어 알고리즘 들 중 위치 인식을 진행하고 이를 기반한 간단한 판단/제어 알고리즘을 진행할 것이다.

먼저 기본적으로 활용하는 센서와 알고리즘의 역할은 다음과 같다.

- GPS   
차량의 현재 위치 인식
- IMU   
차량의 자세 파악
- 정밀도로지도   
- ROS TF 좌표계   
ego 차량의 현재 위치와 자세 데이터를 정밀도로지도 상에서 확인
- 종/횡 방향 알고리즘   
차량의 주행 경로 생성 및 주행 겅로 추종

그 강의의 대외비로 인하여 코드를 작성할 수는 없지만 이론적인 내용만은 정리할 예정이다.

## GPS 데이터 수신 및 변환

GPS 센서 데이터는 3D 위치 데이터(WGS84 좌표계)이므로 2D 위치 데이터를 사용하는 정밀도로지도와 함께 사용하기 위해서는 UTM 좌표계로 변경하는 과정이 필요하다. (gps_parser.py 코드)

이론상 자세한 내용은.. [이곳](../../cognition/coordinate%20system/README.md#투영좌표계)의 내용을 참고하자.

시뮬레이션의 센서 설정은 잘 되어있다는 가정하에 작성한다. 대략적인 과정은 다음과 같다. 

1. GPS 센서 데이터를 수신할 Subscriber 생성
1. Subscriber에서 GPS 센서 데이터 수신
1. GPS 센서 데이터 좌표계('WGS84')에서 UTM 좌표계로 변환 및 확인

이때 `Proj`라는 클래스를 사용했는데 코드에서 [참고하라는 가이드](https://pyproj4.github.io/pyproj/stable/api/proj.html)와 비슷한 [pyproj 파일 자체](https://pyproj4.github.io/pyproj/v2.5.0rel/_modules/pyproj/proj.html)를 참고하였다.

여기에서 `map projections`에 대한 [목록이 정리된 곳](https://proj.org/operations/projections/index.html)을 볼 수 있었는데 당연히 [`Universal Transverse Mercator (UTM)`](https://proj.org/operations/projections/utm.html#usage)도 있었고 UTM이면 추가로 작성해주어야 하는 파라미터를 확인하였다.

결과화면은 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/189629982-6993c33b-5b4f-4c99-b31d-9dd99eb86018.png" width=300>

이런.. 나중에 알았는데 명세서의 46페이지에 쓰여있었다. 그런데.. 저렇게 쓰면 왠만하면 못 알아볼 것 같다. 이유는 단순하다, 명세서나 사전학습 UTM 좌표계 설명과 사진이 없어서 보통은 `zone`이라고 써놔도 전혀 모르는 경우가 일반적이기 때문. 

필자는 정밀도로지도를 만드는 회사에 있었기 때문에 UTM 사진 정도는 본 경험이 있다. 또한 이론은 조금 자세하게 공부하는 편이어서 다큐먼트에서 보았을 때 금방 알았다.

## 차량 위치 추정

이번에는 GPS, IMU 센서 데이터를 받아 차량의 상대위치와 자세를 추정하는 코드(gpsimu_parser.py)를 실습한다.

여기서 상대위치란 시뮬레이터에 맵 좌표계를 의미하는 것으로 추정하였다. 더 이상의 설명은 없지만 시뮬레이션 MAP 기준 좌표계가 새롭게 자주 언급되기 때문이다.

이때 IMU 센서 메시지와 Odometry 메시지도 새롭게 추가된다. 전자는 차량의 자세를 수신받기 위해, 후자는 차량의 위치와 자세 데이터를 담아서 다른 노드로 송신하기 위해서 사용한다. 특이한 점은 Odometry 메시지에 담기는 데이터는 MAP 기준 좌표계로 WGS84에서 UTM으로 바꿔준 좌표계를 다시 MAP 기준 좌표계로 변환해준다. offset만 빼주면 되므로 어렵지는 않았다.

시뮬레이션의 센서 설정은 잘 되어있다는 가정하에 작성한다. 과정은 다음과 같다.

1. GPS 및 IMU 센서 데이터를 수신할 Subscriber 생성
1. Odometry 메시지를 송신하기 위한 Publisher 생성
1. (Subscriber를 통해) GPS 센서 데이터 수신
1. GPS 센서 데이터 좌표계('WGS84')에서 UTM 좌표계로 변환
1. 좌표 데이터 UTM 좌표계에서 시뮬레이터 맵 좌표계로 한 번 더 변환
1. 시뮬레이터 맵 좌표계로 변환된 좌표 데이터를 Odometry 메시지에 저장
1. IMU 센서 데이터를 받아 차량의 자세 데이터를 Odometry 메시지에 저장
1. Odometry 메세지 Publish (해당 코드에서 Publish한 내용을 활용하지는 않음)

시뮬레이션을 실행한 상태로 휠을 클릭하면 시뮬레이터에 맵 좌표계에서의 커서의 위치를 알 수 있는데 이것을 보고 ego 차량의 위치를 확인해주었다.

아래와 같이 보인다.

<img src="https://user-images.githubusercontent.com/19484971/189643573-d19ed763-f91a-4926-aa53-f184423bc047.png" width=300>

결과화면은 다음과 같다.

<img src="https://user-images.githubusercontent.com/19484971/189642692-f35ae111-71fc-43f0-8be6-cb0c742a356b.png" width=300>

## TF 브로드캐스팅(Broadcasting)

시뮬레이터 차량의 좌표와 자세를 브로드캐스팅하는 실습(tf_pub.py), 직전의 Odometry 메세지 Publish한 메시지를 Subscribe하고 해당 정보를 브로드캐스팅하여 진행한다.

시뮬레이션에서 기본적으로 제공하는 TF2Publisher라는 publisher가 이미 있으므로 해당 기능을 끄고 진행해주어야 한다.

<img src="https://user-images.githubusercontent.com/19484971/189661494-e236d8dc-5566-4e7d-b23a-51fdc1517427.png
" width=400>

시뮬레이션의 센서 설정은 잘 되어있다는 가정하에 작성한다. 과정을 간단히 설명하면 다음과 같다.

1. 이전의 실습 코드(gpsimu_parser.py)를 실행하여 Odometry 메세지 Publish
1. TF 브로드캐스팅하는 코드에서 위의 Odometry 메세지를 Subscrib
1. `tf.TransformBroadcaster` 클래스를 만들고 브로드캐스팅 진행

결과화면은 조금 크다;

<img src="https://user-images.githubusercontent.com/19484971/189656873-04501e11-649d-4d8c-8aeb-f3946eba67cd.png" width=800>

잘 보일지 모르겠지만 설명하면..

- 좌측 첫번째(최상단) rosbridge   
- 좌측 두번째 tf 브로드캐스팅
- 좌측 세번째 rqt 실행 - 우측에 rqt 화면
- 좌측 네번째(최하단)  차량 위치 추정 코드 실행

음.. 명세서에서는 `quaternion_from_euler`라는 함수를 사용한다고 작성되어있는데 코드에는 전혀 보이지 않고 오히려 quaternion 각도를 브로드캐스팅하는 것으로 보아.. 내용 수정이 덜 되었나보다.

## MGeo publish

정밀도로지도 데이터인 MGeo 데이터(MORAI Geometry)를 읽어오고 MGeo 데이터를 Point Cloud 데이터로 변환하는 실습(mgeo_pub.py), rviz를 통해 시각화하는 실습까지 이어서 진행한다.

mgeo.py 실습 파일은 정밀도로지도 데이터만을 받아오는 실습코드로 다른 실습과는 다르게 상수처럼 고정된 데이터인 지도 데이터(Json 형식)만를 가져오는 것이기 때문에 해당 실습 코드만은 ROS 에서 제공하는 Python 함수는 사용하지 않는다.

하지만 실습에서 사용해야하는 mgeo_pub.py이다, 해당 코드 기준으로 과정은 다음과 같다.

1. 센서 데이터를 송신하는 실습 코드(gpsimu_parser.py)를 실행하여 Odometry 메세지 Publish
1. 브로드캐스팅을 하는 실습 코드(tf_pub.py)를 실행하여 Odometry 메세지를 TF 브로드캐스팅
1. (여기부터 mgeo_pub.py 코드) MGeo 데이터를 가져와 Link와 Node 정보를 Point Cloud 형식 데이터로 변환
1. Point Cloud 형식 데이터를 Publish
1. 우분투 터미널에서 `Rviz` 명령어를 통해 Point Cloud 형식 데이터를 Subscribe 하여 시각적으로 확인

결과화면은 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/189715525-43f98369-5f18-4ba3-8779-30fb541d6045.gif" width=800>

작은 흰색 점으로 보이는 것이 link에 들어가있던 points들이고 잘 안보이지만 초록 점으로 보이는 것이 node의 point이다.

## 