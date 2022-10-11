# 자율주행 기초 알고리즘

<img src="https://user-images.githubusercontent.com/19484971/194983674-4e7f11d8-4874-42ef-80de-7e1a2b0fb4cb.PNG" width=300>

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

## 주행 경로 저장

차량의 위치 데이터를 받아 txt 파일로 저장하는 실습(path_maker.py)을 진행한다. 저장한 txt 파일은 경로 계획에서 사용할 수 있다.

과정은 다음과 같다.

1. 원하는 경로의 txt 파일 생성 혹은 지정
1. (gpsimu_parser.py 코드에서 Publish 하는) Odometry 메세지 데이터를 Subscrib
1. Odometry 데이터의 조건이 맞으면 현재 위치의 좌표를 txt에 저장

결과화면은 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/189822182-e30a2b43-42c1-4146-81a4-2b216dddabb2.png" width=500>

path_maker.txt(혹은 원하는 txt파일)에 차량이 지나간 좌표가 저장된 것을 볼 수 있다.

저번 실습도 `rosrun` 할 것이 많았는데(rosbridge까지 5개;) 이번에는 launch 파일로 한번에 실행해서 실습해보았다. 그런데 혼자서 rosbridge보다 roslaunch를 먼저하는 바람에 혼자서 해매었다;

launch 파일은 다음과 같다. (실습 코드는 아니니 괜찮을 것 같아서 올렸다.)

```
<launch>
    <node pkg="pkg_2" type="gpsimu_parser.py" name="gpsimu_parser" />
    <node pkg="pkg_2" type="mgeo_pub.py" name="mgeo_pub"  />    
    <node pkg="pkg_2" type="tf_pub.py" name="tf"  />
    <node pkg="pkg_2" type="path_maker.py" name="path_maker"  />

    <node pkg="rviz" type="rviz" name="rviz" args="-d $(find pkg_2)/rviz/kcity_rviz.rviz" />
</launch>
```

마지막에 있는 rviz는 당연히 rviz를 키는 것이지만 args 내에 설정값이 있는 것인지 따로 설정을 하지 않아도 세팅이 이미 되어 있는 것을 볼 수 있었다.

<img src="https://user-images.githubusercontent.com/19484971/189823939-bf091dee-eec4-441d-9855-9a5175262ffd.png" width=500>

조작하지 않았던 display 설정과 topic 설정들이 이미 적용되어 있었다.

## 간단한 경로 계획을 통한 주행

global_path_pub.py 는 위에서 txt 파일에 저장한 Path 데이터를 global Path (전역경로) 로 읽어오는 실습코드, local_path_pub.py 는 global Path (전역경로) 데이터를 받아 Local Path (지역경로) 를 만드는 실습코드이다.

Local Path(지역경로) 는 global Path(전역경로) 에서 차량과 가장 가까운 포인트를 시작으로 전역경로의 경로 일부로 만들어진다.

의외인 것은 지역경로, 전역경로, txt의 Path 데이터 라고 말하지만 txt의 Path 데이터는 그냥 시뮬레이션 좌표계의 x, y, z을 String으로 저장한 것이고 지역경로와 전역경로는 Path라는 클래스에 txt의 데이터를 적절히 넣어 만든다.

과정은 다음과 같다.

1. 센서 데이터를 송신하는 실습 코드(gpsimu_parser.py)를 실행하여 Odometry 메세지 Publish
1. 브로드캐스팅을 하는 실습 코드(tf_pub.py)를 실행하여 Odometry 메세지를 TF 브로드캐스팅
1. MGeo 데이터를 가져와 Link와 Node 정보를 Point Cloud 형식 데이터로 변환하는 실습 코드(mgeo_pub.py)를 실행하여 Link와 Node 정보를 Publish
1. txt 파일로 저장한 Path 데이터를 global Path (전역경로) 로 읽어 publish (global_path_pub.py)
1. global Path와 Odometry 메세지를 subscribe 하여 얻은 데이터들로 Local Path 메세지 Publish (local_path_pub.py)

결과화면은 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/189942288-bcfd85d4-e2f0-46a4-8c80-60124f6775b6.png" width=800>

<img src="https://user-images.githubusercontent.com/19484971/189943485-d4080d00-2121-4319-8781-b83c0fc26510.png" width=800>

초록색이 전역경로, 빨간색이 지역경로이다.

객체의 객체의 객체의 속성을 찾고 알아보는 과정이 개인적으로는 귀찮았다. (Path의 PoseStamped의 Pose의 Position의 x, y, z 속성이라니..) 찾기 어렵지는 않았으나, ctrl+클릭을 모르고 주석을 읽는 습관이 없다면 진행이 매우 어려웠을 것 같다. 

## dijkstra 알고리즘

그래프 노드 간 최단 경로를 찾는 유명한 알고리즘인 dijkstra 알고리즘으로 Mgeo 데이터에서 시작 Node 와 목적지 Node의 전역경로를 만드는 실습

두 실습 코드가 있는데 mgeo_dijkstra_path_1.py는 dijkstra 알고리즘으로 코드에서 지정된 좌표의 최단 global path와 현재 차량 기준으로 local path를 만드는 실습이고

mgeo_dijkstra_path_2.py는 Rviz의 화면 상단에서 2D Pose Estimate와 2D Nav Goal로 두 좌표를 지정하여 path를 만드는 실습이다.

과정은.. 생략한다 바쁘다.

명세서 2 실습 7 과정 추가 요망

결과화면은 아래와 같다.

mgeo_dijkstra_path_1.py 실습코드 적용 시 캡쳐화면

<img src="https://user-images.githubusercontent.com/19484971/190154660-03d8e235-91b2-4bd1-8a2f-075e09edb201.png" width=800>

mgeo_dijkstra_path_2.py 실습코드 적용 시 gif

<img src="https://user-images.githubusercontent.com/19484971/190168388-e04e176a-6050-4b3f-8341-2ea3fd9b6ba7.gif" width=800>

## pure pursuit

핸들링 자동 조정
차량의 차량의 횡 방향 제어 예제
시간이 없어서 생략

## pid control

위 실습에서 속도 자동 조절이 추가
차량의 차량의 종 횡 방향 제어 예제
위와 동문

## velocity planning

위 실습에서 차량이 달리고 있는 도로의 곡률에 기반하여 계산하여 속도를 조절하는 기능이 추가된 실습

위와 같이 차량의 차량의 종 횡 방향 제어 예제

## advanced pure pursuit

위 실습에서 말 그대로 핸들링을 조절하는 pure pursuit을 조금 더 효율적으로 고친 것, 바로 속도에 따라서 목표로 하는 Path를 지정하는 것이다.

 ## adaptive cruise control

 위 실습에서 앞 차와의 간격을 유지를 위해서 속도를 조절하는 코드(acc)가 추가된 실습


 후욱.. pure pursuit 아래로는 거의 코드가 비슷해서 결과도 비슷한데 튜닝할 값이 너무 많아서 거의 차이가 없거나 잘 진행하지 못하고 있다.