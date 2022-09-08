# 좌표계

[참고 블로그](https://blog.tadadakcode.com/3)

- 물체의 위치를 표현하는 체계
- 목적과 상황에 따라 물체의 위치와 자세를 여러 좌표로 표현
- (3차원 좌표계) 종류
    - 직교좌표계   
    가장 흔히 사용하는 좌표계로 서로 직각을 이루는 x, y, z 3개의 축이 3차원을 표현하는 좌표계
    - 원통좌표계   
    물체의 위치를 반지름과 각도, 높이를 통해 3차원 공간을 표현하는 좌표계
    - 구면좌표계   
    원점에서 x축과 이루는 각도, z축과 이루는 각도, 물체와의 반지름으로 물체의 위치를 표현하는 좌표계   
    x축과 이루는 각도를 경도, z축과 이루는 각도를 위도로 표현하는 경우도 있다.

<img src="https://user-images.githubusercontent.com/19484971/188689279-aac6bb10-dee3-4510-8893-e45efa42d7b3.png" width=500>

> 출처 : http://changephysics.blogspot.com/2019/04/blog-post.html

- 추가 내용

좌표계를 여러 개 사용하는 경우도 있다.   
다절 링크(multi linkage)의 경우 물체의 운동을 계산할 때 월드좌표계와 로컬좌표계 모두를 사용한다.

<img src="https://user-images.githubusercontent.com/19484971/188690764-fb2e1647-01f1-4b33-a9b8-8dbfaaeeace2.png" width=500>

> 출처 : https://www.mdpi.com/1999-4893/13/9/203/htm

## GPS

- Global Positioning System(글로벌 포지셔닝 시스템) 약어
    - 좌표계나 측지계가 아닌 그저 시스템
- 최소 24 개 이상의 위성으로 이루어진 위성 항법 시스템
- GPS 수신기는 세 개 이상의 GPS 위성에서 송신된 신호를 수신하여 위성과 수신기의 위치를 결정
    - 오차를 보정하고자 보통 네 개 이상의 위성을 이용
- 위성에서 송신된 신호와 수신기에서 수신된 신호의 시간차이를 측정하여 위성과 수신기 사이의 거리를 통해 위치를 측정
- 기본적으로 WGS84 측지기준계를 기반으로 위치정보 데이터를 제공
    - 보통 UTM 좌표계를 통해 평면좌표계로 변환함

## 측지기준계

- 지구상에서의 특정 위치를 경도와 위도로써 나타내기 위한 기준체계이자 지구의 형상을 나타내는 타원체를 총칭
    - 진짜로 체계와 타원체를 혼용해서 사용함..;
    - 간단히 말해서 지구의 위치를 표현하는 방법을 기술한 기준과 그 때 사용하는 타원체
    - 이때 사용하는 타원체는 지구와 유사하게 만들며 Geoid(지오이드)라고 부름
- 종류
    - GRS80
    - ITRF-2000
    - WGS84
        - World Geodetic System의 약어, 84년도에 제정됨

### 지리좌표계

- 측지기준계를 기반으로 타원체(대표적으로 지구)상의 한 지점 표현
    - 위도와 경도, 평균해수면으로부터의 높이인 고도를 통해서 표기
- 일반적으로는 (도)형식, (도/분/초)형식 두 가지 표기법을 사용
- 경위도좌표계라고도 부름

<img src="https://user-images.githubusercontent.com/19484971/188810471-05586110-4cd1-47bb-8c58-262e4d49e221.png" width=500>

> 출처 : https://blog.tadadakcode.com/3


(도)형식
- 도(˚)단위 정수 이하를 소수로 표현한 경우로, 소수 여섯째자리에서 반올림하여 소수 다섯째짜리까지 표기
- 경기도 기역에서 위도 0.00001˚ 차이는 약 1.1m 거리, 경도 0.00001˚ 차이는 약 0.9m 정도 차이가 생김
- ex) 강남역 사거리 - 37.4974909 / 127.0270229

(도/분/초)형식
- 분단위 소수를 대신하여 초(")단위를 사용
    - 60초 각도는 1분 각도와 같음
    - 초단위 정수 이하는 소수로 표현, 소수 둘째자리에서 반올림하여 소수 첫째자리까지 표기
- ex)  N37°25'12.5"  E126°59'30.2"
- 가끔 고대 기록(10여년 전 기록)을 보면 해당 형식을 사용하는 것을 볼 수도 있다.

### 투영좌표계

- 지리좌표계를 정해진 투영법에 따라 투영한 좌표계
    - 쉽게말하면, 지구본을 벽지도로 만드는 방법
- 투영법(projection)에 따라 다르게 표현됨
    - 투영은 원점 기준과 타원체 모델 등등에 따라 달라짐
    - 아래의 그림을 참고하면 이해가 훨씬 더 쉽다.
- 대표적으로 메르카토르 투영법(Transverse Mercator)이 존재
- 보통은 평면에 투영하므로 평면좌표계라고도 하는 경우가 있다.

<img src="https://user-images.githubusercontent.com/19484971/188794759-11544074-3b59-4166-a7cd-771c5d1a0b7e.png" width=500>

> 출처 : 에듀넷, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=moeblog&logNo=220378935363

위에 말했던 대로 투영법과 사용하는 타원체에 따하서 투영좌표계의 표현은 크게 달라지는데 대표적으로 사용되는 투영좌표계는 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/188810978-b221da46-4546-4984-9336-e11c363c81e4.png" width=500>

> 출처 : https://blog.tadadakcode.com/3

TM(Transverse Meractor) 좌표계

- 우리나라에서 주로 사용되는 좌표계
    - 일제강점기에 만들어져 현재까지 사용
- 베셀(Bessel)타원체를 사용하여 투영

UTM(Universal Transverse Mercator) 좌표계

- 군사용으로 GPS를 개발하면서 함께 개발
- 지구 중심을 원점, 지구의 회전 축을 Z축으로 하는 GRS80 타원체를 기준으로 함
- GPS를 통해 얻은 위치 데이터(위도, 경도 좌표)를 평면에 표현하는 대표적인 좌표계
- 영국의 그리니치 천문대를 기준으로 동서로, 적도를 기준으로 남북으로 구분
    - 천문대가 지나는 위치를 경도 0˚으로 하며 해당 자오선은 본초자오선으로 표기
    - 우리나라는 UTM 좌표계에서 `S52`에 위치

<img src="https://user-images.githubusercontent.com/19484971/188798229-95918b42-cd64-45f5-ae16-4c9a7deb651e.png" width=500>

<img src="https://user-images.githubusercontent.com/19484971/188798441-5cd20cd0-0fe5-4e3c-86fb-ee0747b3fce8.png" width=300>

> 출처 : https://ko.wikipedia.org/wiki/UTM_%EC%A2%8C%ED%91%9C%EA%B3%84

# Orientation

[참고 블로그](https://hub1234.tistory.com/21)

- 물체가 공간에서 얼마나 회전한 상태인지 표시하는 방식
- 비슷한 용어로는 angular position, attitude
- 대표적으로 오일러 각도(Euler Angle), Quaternion(쿼터니언)이 존재

## Euler Angle

- 물체의 자세를 Roll Pich Yaw 3축으로 표현
- 짐벌락 현상이 존재
    - 두 개 이상의 회전축이 겹쳐 특정 축으로 회전이 불가능해지는 현상

<img src="https://upload.wikimedia.org/wikipedia/commons/4/49/Gimbal_Lock_Plane.gif" width=200>

> 출처 : https://en.wikipedia.org/wiki/Gimbal_lock

## Quaternion

- 오일러 각도의 짐벌락 현상을 피하기 위해 고안된 방식
- x, y, z 3개의 벡터와 w 하나의 스칼라 값으로 표현
- 어떤 회전각이든 계산가능하며 빠른 연산이 가능
- 사람이 이해하기 어려움
    - 이 때문에 사람에게 보일때는 오일러 각도로 변환해서 보이기도 함
    - 이미 만들어놓은 함수를 사용할 것을 강력히 권장할 정도로 이해가 어려움
