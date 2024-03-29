# Raspberry pi 

- [경험한 에러를 정리한 페이지](./problems/README.md)

## 활용 방식

처음에는 라즈베리파이와 다양한 보조기기(마이크, 센서 등등)을 활용하여 프로젝트를 진행하려고 하였으나, 3D 캐릭터 모델링을 위해 사용한 blender를 three.js에 삽입하여 웹 페이지에서 3D 캐릭터가 나오도록 만든 것이 라즈베리파이에서는 너무 부하가 크다고 판단하여 다르게 진행하기로 하였다.

화면은 노트북의 화면을 보여주고 센서 값들은 node.js와 socket 연결을 통해 넘겨주는 방식으로, 통신에 대한 작업이 늘어나게 되었다. (웹에서는 CORS 문제까지 발생했다고 한다.)

## 환경설정

1. 고정 IP 설정 방법
그 강의의 강의장은 와이파이를 통해 데이터를 주고 받는 것을 제한해 두었는데 이 때문에 특정한 IP를 사용하지 않으면 SSH나 VNC를 사용하지 못해서 아래의 블로그를 참고하였다.
https://ansan-survivor.tistory.com/44 참고

2. Raspberry pi 환경설정   
https://sergeswin.com/1268/ 참고.. 하긴 했는데 나중에 보니   
<img src="https://user-images.githubusercontent.com/19484971/182140581-762441bb-2ad3-4aa1-a3c8-dd497d1f3107.png"  width="400">   
설치할 OS를 선택하고 언어와 wifi 자동연결 등 다양한 초기설정을 입력할 수 있는 설정 버튼이 있었다..!!   
<img src="https://user-images.githubusercontent.com/19484971/182141611-fc3d5446-8fdd-4dc5-8cc8-332b26f79ffb.png"  width="400">

## 리눅스 명령어

라즈베리파이의 OS인 라즈비안은 리눅스를 기본으로 하는 운영체제이기 때문에 기본적인 리눅스 명령어를 알아야 사용이 편하다. 간단히 정리된 [블로그](https://mickael-k.tistory.com/36)를 찾아 글을 읽어보았다.

리눅스 명령어는 대학교 1학년때 리눅스 환경에서 C언어 공부할 때 어느정도 숙지를 했었지만, 라즈비안의 셸 프롬프트 (shell prompt) 용어는 처음 알게 되었다.

크게 도움이 되는 내용은 아니었고 이름을 통해서 대충 느낌으로 알고 있었지만, 이렇게 확실하게 설명해주는 글이 있으니 좋았다.

## GPIO(General Purpose Input/Output)

센서의 데이터를 활용하기 위해서 사용하는 입출력 단자.. 라고 알고있다, 위키백과에서는 아래와 같이 정의하였다.

```
다용도 입출력(general-purpose input/output, GPIO)은 입력이나 출력을 포함한 동작이 런타임 시에 사용자에 의해 제어될 수 있는, 집적 회로나 전기 회로 기판의 디지털 신호 핀이다.

-위키백과-
```

필자는 단순하게 핀과 GPIO에 대한 기억은 아래와 같다.

- 라즈베리파이에는 전력이 공급되는 핀(Power), 전력이 나가는 핀(Ground) 등 다양한 핀이 있다.
- 개발자가 입출력에 사용할 수 있는 핀은 GPIO라고 불린다.
  - 입출력 외에도 다양한 역할을 가지는 경우가 있다. 핀 맵의 괄호의 내용을 보면 알 수 있다.
  - 필자의 기억으로는 특별한 역할을 가진 센서의 핀은 라즈베리파이의 적절한 GPIO에 넣어야지만 작동했던 것 같다. (불확실)

![image](https://user-images.githubusercontent.com/19484971/181657619-1490b328-0a19-4bc7-82bc-157616ac25bf.png)

참고

- [라즈베리파이 GPIO 핀 번호](https://fishpoint.tistory.com/6181)

## SSH를 통해 라즈베리파이 파일을 VisualStudio에서 확인하기

그 강의에서 컨설턴트님이 환경설정에 대해 알려준 내용을 정리한 내용

라즈베리파이의 SSH 설정을 켜주세요. (VNC 아니여도 raspi-config 명령어를 통해 설정 가능)  
<img src="https://user-images.githubusercontent.com/19484971/181669292-722f7fc7-ce79-44bc-b296-47a20e180049.png"  width="400">

VS에서 아래의 Extension을 설치합니다.  
<img src="https://user-images.githubusercontent.com/19484971/181669335-ddf66546-fabe-4e3a-8e0b-d3c2cb86cb40.png"  width="400">

Remote Explorer에 들어가서 ‘+’를 누릅니다.  
<img src="https://user-images.githubusercontent.com/19484971/181669353-16db619e-4e85-4b9d-b020-e1dbaf18eded.png"  width="400">

‘ssh 계정명@ip주소 -A’ 를 입력해줍니다.  
<img src="https://user-images.githubusercontent.com/19484971/181669361-ddcbf029-3c01-4085-aef4-fc1153d17ab8.png"  width="600">

기본 구성파일인 가장 위 선택지를 선택  
<img src="https://user-images.githubusercontent.com/19484971/181669369-d2c490fa-e3c5-46c6-8664-9346b6cc701c.png"  width="600">

왼쪽에 ssh가 추가된 것을 확인(안 생기면 조금 기다려보자)  
해당 호스트로 접속하는 창 생성(이미 접속되었다면 아래와 같이 컴퓨터에 체크 표시가 생성된다.)  
<img src="https://user-images.githubusercontent.com/19484971/181669383-2ac8cf69-6254-4b07-841b-89ee4decc47c.png"  width="400">

계정에 대한 암호 입력  
<img src="https://user-images.githubusercontent.com/19484971/181669397-086c78e5-32b6-488a-ae29-ada1b7ec0233.png"  width="400">

explorer에서 아래의 버튼을 클릭하면  
<img src="https://user-images.githubusercontent.com/19484971/181669429-fcf54054-5878-48f9-8ce2-93c5fb7a5acb.png"  width="400">

원격으로 폴더를 확인할 수 있다.  
<img src="https://user-images.githubusercontent.com/19484971/181669462-25086584-a8b4-4271-bb41-a91de47c32db.png"  width="400">

편하게 VS에서 자신의 코드가 에러나는 것을 확인해보자!  
<img src="https://user-images.githubusercontent.com/19484971/181669814-c98b9afa-259e-4bb5-82a2-e0350dfdd552.png"  width="800">

참고

- https://shshsh.tistory.com/163

## get-apt와 apt의 차이

대부분의 블로그가 차이가 없다는 말 밖에 없어서 컨설턴트님과 필자의 경험을 미루어 볼 때, 둘의 차이점은 크게 의존성 관리 여부이다.

`apt-get`으로 했을 때 설치가 안되는 라이브러리가 있었는데 `apt`로 바꿔주자마자 설치가 되었다. 의존성 파일에 또 의존성 파일이 있어서 설치에 어려움이 있었는데 그것을 모두 고려해서 설치를 진행해준 것이었다.

[`What is the difference between apt and apt-get?`](https://askubuntu.com/questions/445384/what-is-the-difference-between-apt-and-apt-get)라는 글에 따르면 거의 대부분은 비슷하지만, `apt-get`는 사람보다는 `lower-level` 혹은 `back-end`에 맞춰 다양한 APT 도구 모음을 지원하고 `apt`는 사람(`end-users`)에 맞춰 개발되었다고 한다.

## pip와 apt-get의 차이

`apt`는 `Advanced packaging tool`의 약자로 이고 `pip`는 파이썬으로 작성된 패키지 소프트웨어를 다운로드, 설치, 관리하는 패키지 관리 시스템이다.

사실 둘 다 패키지를 관리한다는 점에서는 같지만, `apt-get`는 Ubuntu 리포지토리에서, `pip`는 `PyPI`(파이썬 패키지 인덱스, 파이썬 모듈의 저장소)에서 다운로드 받기 때문에 파이썬 패키지만을 다룬다는 차이점이 있다.

## 라즈베리파이 SD카드 이미지 백업

[한 블로그](https://withcoding.com/99)를 보고 진행하였다.

`win32diskimager`라는 프로그램을 이용해서 백업을 하고 `Etcher`라는 프로그램을 사용하여 복원을 진행하는데 단순히 프로그램을 이용하는 것이라서 어렵지 않았다.

환경설정을 다 해놓은 상태에서 한번 백업을 해놓으니 든든하게 사용할 수 있었다. 백업 파일은 60G라고 쓰여있지만, 단순히 SD카드의 용량이 60G라서 그런 것 같고 실재로는 60G를 사용하지 않는다.

그래서 그런지 백업은 5분인가 10분인가 걸렸지만, 복원은 3분 정도면 끝난다. 에러 해결해본다고 이것저것 설치하고 설정 변경하다가 라즈베리파이가 켜지지도 않는 경우가 꽤 있었는데 몰랐으면 울뻔했다!

## JS에서 Python 파일 실행하기

해당 방법은 socket.io를 사용하면서 활용하지 않게 되었지만, 실습했던 내용을 정리하였다.

프로젝트 중 라즈베리파이 센서의 값을 웹으로 송신해야하는 경우가 생겨 컨선턴트님께 여쭤보았더니 방법이 있으시다고 하셔서 검색해서 아래와 같이 실습을 해보았다.

잘 작동해서 놀랐다..

test.js 파일

```
var spawn = require("child_process").spawn;

// 2. spawn을 통해 "python 파이썬파일.py" 명령어 실행
const result = spawn("python", ["./hello.py"]);

// 3. stdout의 'data'이벤트리스너로 실행결과를 받는다.
result.stdout.on("data", function (data) {
  console.log("111", data.toString());
});

// 4. 에러 발생 시, stderr의 'data'이벤트리스너로 실행결과를 받는다.
result.stderr.on("data", function (data) {
  console.log("222", data.toString());
});
```

hello.py

```
def getValue():
    print ("value")

if __name__ == '__main__':
  a='a'
  a.toInt()
  getValue()
```

결과 (정상 작동시)

```
[Running] node "c:\Users\IM\Desktop\test.js"
111 value


[Done] exited with code=0 in 0.806 seconds
```

결과 (에러 발생시)

```
[Running] node "c:\Users\IM\Desktop\test.js"
222 Traceback (most recent call last):
  File "./hello.py", line 7, in <module>
    a.toInt()
AttributeError: 'str' object has no attribute 'toInt'


[Done] exited with code=0 in 1.013 seconds
```

### 참고

- [[Node.js] 자바스크립트로 파이썬 연동 실행 방법(함수 매개변수 전달 호출 : child-process)](https://curryyou.tistory.com/225)
- [자바스크립트에서 Python 파일 실행하기](https://doongdoongeee.tistory.com/148)

## [teachableMachine](https://teachablemachine.withgoogle.com/)

빠르게 웹, 앱에 적용할 수 있는 간단한 머신러닝 모델을 만들 수 있도록 도와주는 사이트로 구글에서 제작하였다.

초등학생들에게 AI를 쉽게 가르치기 위해서 만들었다고 기억하고 있지만, 확실하지 않아서 다시 찾아봐야 할 것 같다.

필자는 해당 사이트를 활용하여 간단한 자세인식 모델을 만들어 프로젝트에 적용할 예정이다. 아이들의 자세를 인식하여 특정 행동을 취하면 다음으로 넘어가는 기능을 구현할 때 사용한다.

### Teachable Machine Library - Pose

[자세인식에 대한 API 다큐먼트](https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/pose)가 따로 있어서 참고하였으나.. 생각보다 다양하지 않고 대부분은 이미 TM 예시 코드에서 사용하는 것들이라서 참고하는 정도로만 사용하였다.

코드는 기본으로 제공해주는 예시코드를 사용하였다. 해당 예시코드는 위의 다큐먼트 링크에서도 볼 수 있었고 학습 후 모델을 내보낼 때도 볼 수 있었다.

<img src="https://user-images.githubusercontent.com/19484971/184523879-99befa9f-7872-45b2-975e-3681b692d80a.png" width=800>

### Canvas 이미지

필자의 경우에는 프로젝트에서 자세인식 이미지를 전송할 필요가 있었기 때문에 해당 이미지를 담고있는 변수를 찾아야 했는데, `webcam.canvas`와 `ctx.canvas` 라는 변수가 그럴듯해보여서 콘솔에 출력해보았더니

<img src="https://user-images.githubusercontent.com/19484971/184523449-1a19a7ce-b5cc-4954-a90d-8a74d435c056.png" width=400>

둘 모두 캔버스 태그인 것은 맞지만 다른 캔버스 태그를 담고있는 듯이 보였다. 해당 캔버스의 파일을 임의로 다운로드해서 아래와 같이 살펴보았다.

<img src="https://user-images.githubusercontent.com/19484971/184523616-2e366aaa-21bc-4e58-abbf-f6fc7395bcbc.png" width=800>

왼쪽의 사진이 `ctx.canvas` 이미지, 오른쪽의 사진이 `webcam.canvas`이다. 처음에는 자세인식 이전에 다운로드를 해서 다르게 찍힌 것인가 생각해서 코드를 수정해서 다운로드를 했으나 같은 결과를 볼 수 있었다. 

참고로 캔버스 이미지 다운로드 코드를 참고한 사이트는 [이곳](https://joylee-developer.tistory.com/134)이다.

결과를 요약하자면 `webcam.canvas`는 일반적인 웹캠 사진을 담는 캠버스, `ctx.canvas`는 `webcam.canvas` 사진에서 자세인식을 하여 `keypoint`를 그린 사진을 담는 캔버스라는 것을 알 수 있었다.

위의 정보를 토대로 `socket.io`를 통해 이미지를 발송할 예정이다!

TM과 Socket.io를 활용하여 프로젝트에 적용한 [파일 링크](./codes/poseRecognition-NodeJs/README.md)

## node.js

TM에서 만든 모델을 적용하고 인식한 자세를 React로 전달하기 위해서 라즈베리파이에 [Node.js를 설치](https://it-jm.tistory.com/19)하였다.

2022년 8월 12일 기준 [nodejs](https://nodejs.org/en/)공식 홈페이지에서 추천하는 버전은 16.16.0버전으로 필자도 해당 버전으로 설치하였다.

<img src="https://user-images.githubusercontent.com/19484971/184197121-ebf8bef7-2561-4719-b75c-b64e928ab012.png" width=500>

<img src="https://user-images.githubusercontent.com/19484971/184197377-e24f9c44-7bdc-490f-a570-431f33cf5822.png" width=300>

그리고 자연스럽게 npm 8.11.0버전도 설치가 되였다.

기본적인 폴더를 생성해야할 것 같아 [구글링하여 찾은 블로그](https://dion-ko.tistory.com/123)와 [nodejs 공식 홈페이지](https://nodejs.org/dist/latest-v16.x/docs/api/synopsis.html)를 보면서 진행하였다.

<img src="https://user-images.githubusercontent.com/19484971/184212192-982a10d9-3819-4522-a9c1-1e6462525fb1.png" width=300>

자세인식이 되는 것을 확인하고 혹시 모르니 다시 라즈베리파이를 백업한 후 잤다.

### [Socket.io](https://socket.io/)

간단한 텍스트와 이미지를 전송하기 위해서 사용한다.

공식 홈페이지의 다큐먼트를 참고하긴 하였으나, 추가적인 설명이 조금 더 필요하다고 느껴서 [한 블로그](https://inpa.tistory.com/entry/SOCKET-%F0%9F%93%9A-SocketIO-%EC%82%AC%EC%9A%A9-%ED%95%B4%EB%B3%B4%EA%B8%B0)를 참고하였다.


TM과 Socket.io를 활용하여 프로젝트에 적용한 [파일 링크](./codes/poseRecognition-NodeJs/README.md)

## porting

컨설턴트님이 언급하신 말을 유추하면 다양한 라이브러리나 패키지를 서로 호환되는 버전을 신경써서 컴퓨터에 설치하는 작업같다. 해당 작업을 필자가 하기는 했지만 전문용어로 따로 있는 것은 모르고 진행했기 때문에 찾아보기로 하였다.

## Stadia

```
구글의 클라우드 게임 서비스. 개발단계에서는 Project stream이라 불렸으며, 유튜브 기반으로, 사실상 유튜브 동영상을 보며 조작을 하는 컨셉이기 때문에 유튜브 재생만 가능하다면 저사양 PC든 스마트폰이든 태블릿 PC든 실시간 스트리밍을 통해 FHD 60프레임으로 게임을 할 수 있게 된다. 

정식 출시때는 무려 4K 60프레임으로 게임을 즐길 수 있게 만들겠다고 발표하며 저사양 PC 유저들에게 충격을 주었다.

-나무위키-
```

해당 기술을 활용하면 노트북을 꼭 사용할 필요가 없어서 위의 [통신 흐름도](../colaberation/README.md#결과)를 크게 간소화가 가능한 동시에 노드 서버도 하나로 통합할 수 있어 다음에 꼭 활용하고 싶다.

[Stadia GDC 2019 Gaming Announcement](https://www.youtube.com/watch?v=nUih5C5rOrA&t=14s)

솔직히 시간 생기면 라즈베리파이 사서 적용해 볼 생각도 난다.