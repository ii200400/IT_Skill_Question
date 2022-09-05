# ROS

ROS를 통해 topic과 service가 통신하는 예제를 진행하고 기록하기 위해 작성한다. morai 시뮬레이션과 연결하는 것이기 때문에 시뷸레이션이 없으면 ROS를 설치해도 진행을 할 수 없다.

우선 필자의 환경은 다음과 같다.

- Oracle VM Virtual Box 버전 (Extension_Pack-6.1.36a)
- Ubuntu (ubuntu-18.04.6-desktop-amd64)
- Morai (22.R2.1)
- python 2.7

설치한 주요 라이브러리는 다음과 같다. 라이브러리 버전은 단순히 최신것으로 설치했는데 확인하기 귀찮아서 지금은 생략해버렸다.. 크흠..

- ROS
- python-rosinstall
- python-rosinstall generator
- python-wstool
- build-essential

## ROS 설치

라이브러리 설치시에 사용한 명령어들이다.

```
# -sc 사이에 띄어쓰기가 없는 줄 알고 해맷다...
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# 여기서는 고정 IP 설정이 잘못되어있어 설치가 진행이 되지 않아 힘들었다... 네트워크 설정은 가장 아래에 정리하였다.
$ sudo apt install curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add –

# apt 업데이트 후 ros 설치!
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
$ sudo apt-get install python-rosdep

# ros 기본설정 진행
$ sudo rosdep init
$ rosdep update
$ echo “source /opt/ros/melodic/setup.bash” >> ~/.bashrc

```

위의 명령어를 사용하면 잘 설치되었는지 확인이 가능하다.

```
$ roscore
```

필자의 경우 에러가 나서 구글링을 진행하였다. [ROS community](https://answers.ros.org/question/60366/problem-with-roscore/)에서 `sudo rosdep fix-permissions`을 실행하고 진행하라고 해서 따라했더니 잘 된다!

## ROS 패키지 생성

필자는 아래와 같이 패키지를 생성하였다.

```
# 홈 디렉토리로 이동
$ cd ~/

# catkin_ws/src 폴더 생성
$ mkdir –p catkin_ws/src
# catkin_ws 폴더에서 워크 스패이스 생성
$ cd catkin_ws
$ catkin_make

# catkin_ws/src로 이동
$ cd ~/catkin_ws/src
# beginner_tutorials라는 이름으로 패키지 생성 (std_msgs 의존성 추가)
$ catkin_create_pkg beginner_tutorials rospy std_msgs
# catkin_ws 폴더로 이동하여 ROS 패키지 빌드
$ cd ~/catkin_ws
$ catkin_make

# catkin 환경변수 선언
$ source ~/catkin_ws/devel/setup.bash
# catkin 패키지 재구축
$ rospack profile
```

## morai msg 다운로드

시뮬레이션과 통신할 때는 msg라는 특정한 데이터 형식으로 주고 받는데 그 msg를 다운로드 한다.

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/morai-developergroup/morai_msgs.git
```

## rosbridge 설치

window에서 실행되는 시뮬레이터와 virtualbox의 우분투에서 실행되는 ros를 연결해주는 rosbridge를 설치한다.

```
# rosbidge 설치
$ sudo apt-get install ros-melodic-rosbridge-suite

# rosbridge 실행
$ roslaunch rosbridge_server rosbridge_websocket.launch
```

## ROS 노드 메시지 예제

먼저 예시를 진행할 프로젝트 파일의 종속 패키지부터 설치한다. 좀 많았다.

```
# 종속 패키지 설치
$ sudo apt-get install git
$ sudo apt-get install net-tools
$ sudo apt-get install ros-melodic-rosbridge-server
$ sudo apt-get install ros-melodic-velodyne
$ sudo apt install terminator
$ pip install pyproj
$ pip install scikit-learn

# src 폴더에 morai에서 msgs 폴더 다운로드
$ cd ~/catkin_ws/src
# 사실 시뮬레이터에서 사용하는 메시지에 대한 코드이지 예시 코드의 폴더는 아니다.
$ git clone https://github.com/morai-developergroup/morai_msgs.git

```

그리고 VisualCode 설치하고 extension에서 python과 ros를 install한다. 둘 모두 `Microsoft`에서 만들었다. 필자처럼 다른 것과 햇갈리지 말자.

ctrl + shift + P 를 눌러 `Python: Select Interpreter`에서 우분투 가상환경에서 사용하는 파이썬 환경을 선택하였다. 왜 하는지는 정확히 모르겠다.

<img src="https://user-images.githubusercontent.com/19484971/188327177-d21f3f77-330a-46cd-b721-f1d8cb78c012.png" width=600>

드디어 통신할 준비가 되었다. 통신을 진행해보자.   
필자가 [실습에 사용한 파일](./beginner_tutorials/scripts/)도 폴더에 같이 있으니 참고하자!

```
# scripts 폴더로 이동해서 예제코드 다운로드
$ cd ~/catkin_ws/src/beginner_tutorials/scripts
$ wget https://raw.github.com/ros/ros_tutorials/melodic-devel/rospy_tutorials/001_talker_listener/talker.py
$ wget https://raw.github.com/ros/ros_tutorials/melodic-devel/rospy_tutorials/001_talker_listener/listener.py

# scripts 폴더에 있는 talker.py와 listener.py 실행 권한 설정을 해주어야 실행이 가능하다.
$ roscd beginner_tutorials/scripts
$ chmod +x talker.py
$ chmod +x listener.py

# 터미널 3개가 필요하다.

# 터미널 1 : 마스터 노드 실행
$ roscd ./
$roscore

# 터미널 2 : talker.py 실행
$ rosrun beginner_tutorials talker.py

# 터미널 3 : listener.py 실행
$ rosrun beginner_tutorials listener.py
```

캡처를 까먹었다..

### launch

- 여러 노드(talker.py, listener.py)를 동시에 실행시키기 위해서 사용
- roscore가 실행되어있지 않아도 자동으로 실행
- xml 형식으로 작성

[필자가 사용한 파일](./beginner_tutorials/launch/talker_listener.launch)이 있으니 참고하자.

실행은 다음과 같이 한다.

```
$ roslaunch beginner_tutorials talker_listener.launch
```

이것도 캡처를 까먹었다..

## 시뮬레이터와 ROS 연동 

설치할 때 한꺼번에 모두 설치하는 것이 좋을 것 같아서 위에서 rosbridge 설치 명령어를 적었다. 순서대로 따라했다면 catkin_ws/src 폴더 내에 `morai_msgs` 폴더가 있을 것이다.

설치한 rosbridge를 사용하여 윈도우의 morai 시뮬레이션과 우분투의 ROS를 연동하여 메시지를 주고 받을 것이다. 이 때 



## 네트워크 설정

고정 IP를 설정할 때 설정을 바꾸면 안 되는 것을 바꾸어 네트워크 연결이 되지 않아서 힘들었다. 네트워크 연결이 되었을 때 적용한 설정은 아래와 같다.

virtual box의 호스트 네트워크 관리자

<img src="https://user-images.githubusercontent.com/19484971/187367952-88739d64-48db-484f-b9be-518c3a9129f3.png" width=600>

<img src="https://user-images.githubusercontent.com/19484971/187368318-9873efe8-1109-44da-8da5-c778420ea478.png" width=600>

<img src="https://user-images.githubusercontent.com/19484971/188325961-28e89512-684e-49a6-ae7f-299510cdc546.png" width=600>

<img src="https://user-images.githubusercontent.com/19484971/188325973-b423bc40-bd1f-459e-9e3b-fbe7bf44602c.png" width=600>


우분투의 ip

<img src="https://user-images.githubusercontent.com/19484971/187369941-282fdf42-e4c0-4f03-b82c-ac23a001491b.png" width=600>

(snp0s3)

<img src="https://user-images.githubusercontent.com/19484971/187369623-fd8f5369-67eb-40db-a49e-6503168ba753.png" width=600>

(snp0s8)

<img src="https://user-images.githubusercontent.com/19484971/187369530-d197410b-4908-4727-ab1f-1a2e334650f2.png" width=600>

<img src="https://user-images.githubusercontent.com/19484971/187370140-e7290fbb-34c7-4a45-9c5d-5a8ee241d8b7.png" width=600>

morai 시뮬레이터 설정

<img src="https://user-images.githubusercontent.com/19484971/187371029-77e065bc-fd05-4b98-826f-e472287d4b76.png" width=600>

<img src="https://user-images.githubusercontent.com/19484971/187371155-eb55f97d-3bbb-49eb-a23f-c918124e5d9e.png" width=600>