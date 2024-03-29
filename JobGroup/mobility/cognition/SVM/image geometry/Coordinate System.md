# 좌표계 (Coordinate System)

`목차`

* [개요](#개요)
* [월드 좌표계 (World Coordinate System)](#월드-좌표계-world-coordinate-system)
* [카메라 좌표계 (Camera Coordinate System)](#카메라-좌표계-camera-coordinate-system)
* [영상 좌표계(Image Coordinate System)](#영상-좌표계image-coordinate-system)
* [정규 이미지 좌표계 (Normalized Image Coordinate System)](#정규-이미지-좌표계-normalized-image-coordinate-system)

## 개요

공간에 있는 물체 혹은 점 등의 위치를 표시하기 위해 하나 이상의 숫자로 만든 좌표를 사용하는 체계.. 라고 한다.

필자는 그냥 단순히 특정 공간에서 물체를 표시하기 위한 수학적 체계라고 생각하고 있다.

영상 기하학에서 사용하는 좌표계는 크게 4가지가 있는데 아래와 같다.

- 월드좌표계
- 카메라좌표계
- 정규좌표계
- 영상좌표계

이중 월드 좌표계와 카메라 좌표계는 3차원 좌표계이고, 정규좌표계와 픽셀좌표계는 2D 좌표계이다. 내가 참고한 블로그에서는 아래의 사진을 기반으로 작성하였다.

<img src="https://user-images.githubusercontent.com/19484971/196711634-ec83b0ae-b3a6-4fbf-9149-4d52bc8f3c5f.png" width=600>

위의 네 좌표계 각각을 이해하고 특징을 살펴보는 것은 카메라 geometry를 이해하는데 있어서 매우 중요하다.  

아래에서 각각의 좌표계에 대해 하나씩 살펴보겠다.

## 월드 좌표계 (World Coordinate System)

사물(물체)의 위치를 표현할 때 기준으로 삼는 좌표계

- 절대적인 기준이 있는 좌표계가 아니다.
    - 개인 임의로 한 곳을 기준으로 삼을 수 있다.
    - 예를 들어, 자신의 안방 한쪽 모서리를 원점으로 잡고 한쪽 벽면 방향을 X축, 다른쪽 벽면 방향을 Y축, 하늘을 바라보는 방향을 Z축으로 잡을 수 있다. 
    - 좌표의 단위도 임의로 만들 수 있다. 미터(meter)로 해도 되고 센티미터(centimeter)로 해도 된다. 
    - 중요한 점은 좌표계로 한 위치를 하나의 표현으로 특정할 수 있어야 된다는 것!
- 월드좌표계 상의 점은 일반적으로 아래와 같이 대문자로 표기한다.
    - <img src="https://user-images.githubusercontent.com/19484971/196717074-ec26a671-9c24-4d35-8d74-98421a208ed0.png" width=100>


## 카메라 좌표계 (Camera Coordinate System)

카메라 좌표계는 카메라를 기준으로 한 좌표계

<img src="https://user-images.githubusercontent.com/19484971/196719897-7eee1947-a2f5-4945-8ee3-1e5c6f318f19.png" width=400>

- 위 그림과 같이 카메라의 초점(렌즈의 중심)을 원점으로, 카메라의 정면 광학축 방향을 Z축, 카메라 아래쪽 방향을 Y축, 오른쪽 방향을 X축으로 잡는다.
- 카메라 좌표계의 단위는 카메라가 속한 월드좌표계와 같아야 한다.
- 카메라 좌표계를 기준으로 한 점의 좌표는 다음과 같이 아랫첨자 c를 사용한 대문자로 표기한다.
    - <img src="https://user-images.githubusercontent.com/19484971/196720872-5e842ab8-52af-4de1-8ab9-f09b953076d0.png" width=100>

## 영상 좌표계(Image Coordinate System)

카메라를 통해 찍은 이미지(사진)에 대한 좌표계

- 이미지의 좌상단 모서리를 원점(0, 0), 오른쪽 방향을 x축 증가방향, 아래쪽 방향을 y축 증가방향으로 한다.
- 영상좌표계로 표현되는 평면을 이미지 평면 (image plane)이라 부른다.
- 단위는 픽셀(pixel)
- 영상 좌표계를 기준으로 한 점의 좌표는 다음과 같이 소문자로 표기한다.
    - <img src="https://user-images.githubusercontent.com/19484971/196723463-61473e1c-b869-4a16-8fa1-9c1fb724b04f.png" width=100>
- 월드좌표계에서 영상좌표계로 투영하면 각 점은 대응하는 점이 있지만 반대로 영상좌표계에서 월드 좌표계로 대응하는 점은 찾을 수 없다.
    - 월드좌표계에서 영상좌표계로 변환할 때 z축에 대한 정보를 잃기 때문

## 정규 이미지 좌표계 (Normalized Image Coordinate System)

카메라의 내부 파라미터(intrinsic parameter)의 영향을 제거한 가상의 좌표계 

- 카메라 초점과의 거리가 1인 가상의 이미지 평면을 정의하는 좌표계
- 정규 좌표계의 원점은 정규 이미지 평면의 중점(광학축 Zc와의 교점)입니다 (그림 1 참조). 픽셀 좌표계와 원점의 위치가 다름에 주의하기 바랍니다. 그리고 좌표축은 픽셀 좌표계와 구분하기 위해 u, v를 사용하겠다.
    - <img src="https://user-images.githubusercontent.com/19484971/196748355-0336b799-c37a-4eea-af11-791c6d8af834.png" width=100>
- 카메라 내부 파라미터를 알면 다음과 같이 영상 좌표와 정규 좌표 사이의 변환이 가능하다.
    - 여기서 K는 카메라 내부 파라미터를 의미하는 행렬이다.
    - <img src="https://user-images.githubusercontent.com/19484971/196749708-1a71f867-71b0-45be-bd2c-e0a26763fff5.png" width=100>
    - 위의 내용을 행렬로 표현하면 아래와 같다.
    - <img src="https://user-images.githubusercontent.com/19484971/196752088-80c020bf-a4cc-40ab-8f4c-bf779a9ce2c3.png" width=100>
    - 식으로 표현하면 아래와 같다.   
    - <img src="https://user-images.githubusercontent.com/19484971/196828935-0d48d3bb-e07a-46b8-8fd0-c386692b7eec.png" width=100>
    - 역으로, 이미지 상의 픽셀 (x, y)에 대응하는 정규좌표(u, v)로 변환하는 것을 수식으로 표현하면 다음과 같다.   
    - <img src="https://user-images.githubusercontent.com/19484971/196829119-eba9b0f2-ba9d-4f75-97bd-3dc60354297b.png" width=100>
- 최대한 물리적 요소를 제거한 정규화된 이미지 평면에서 공통된 기하학적 특성을 분석하기 위해서 사용한다.
    - 동일한 위치와 동일한 각도에서 찍더라도 사용한 카메라의 물리적 특성(렌즈, 이미지 센서 등)에 의해 다른 이미지를 얻기 때문
