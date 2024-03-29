### 관련 정리글

- [영상 기하학 (Image Geomatry)](./image%20geometry/README.md)
- [openGL](./openGL/README.md)

# Surround View Monitor

`목차`

- [개요](./개요)
- [핀홀 카메라 모델(Pinhole camera model)](#핀홀-카메라-모델pinhole-camera-model)
- [Camera Calibration](#camera-calibration)
  - [초점거리(focal length)](#초점거리focal-length)
  - [주점(principal point)](#주점principal-point)
  - [비대칭 계수(skew coefficient)](#비대칭-계수skew-coefficient)
  - [카메라 외부 파라미터(extrinsic parameters)](#카메라-외부-파라미터extrinsic-parameters)
  - [자동초점조절(auto focusing)](#자동초점조절auto-focusing)
  - [영상 해상도](#영상-해상도)
  - [캘리브레이션 결과가 달라지는 이유](#캘리브레이션-결과가-달라지는-이유)
  - [참고사항](#참고사항)

`관련 내용`

- [openGL](./openGL/README.md)
  - [Tutorial 1 : Opening a window](./openGL/tutorial1.md)
  - [Tutorial 2 : The first triangle](./openGL/tutorial2.md)
  - [Tutorial 3 : Matrices](./openGL/tutorial3.md)
  - [Tutorial 4 : A Colored Cube](./openGL/tutorial4.md)
  - [Tutorial 5 : A Textured Cube](./openGL/tutorial5.md)
  - [Tutorial 6 : Keyboard and Mouse](./openGL/tutorial6.md)
- 영상 기하학 (Image Geomatry)
  - [좌표계 (Coordinate System)](./image%20geometry/Coordinate%20System.md)
  - [동차좌표 (Homogeneous Coordinates)](./image%20geometry/Homogeneous%20Coordinates.md)
  - [2D 변환 (2D Transformations)](./image%20geometry/2D%20Transformations.md)

## 개요

주차할 때 보는 바로 그 화면의 기능, `Around View Monitor(AVM)`이라고 하기도 한다.

수평시야각(Field Of View,FOV) 170도 이상인 어안렌즈 카메라 4대를 차량 주변(전후좌우)에 설치해야만 한다. 일반 카메라는 시야각이 좁기 때문에 반드시 어안렌즈 카메라를 사용해야한다.

<img src="https://user-images.githubusercontent.com/19484971/195967763-39d0f057-50c7-4eff-9dbc-07858281a9ac.png" width=400>

해당 기능을 구현하기 위해서는 몇 가지 과정이 필요한데 아래와 같다.

1. 카메라 왜곡 보정 (Camera Calibration)
   - 어안렌즈 카메라의 왜곡을 보정하기 위해서 필요한 과정
2. 카메라 이미지 와핑(Wapping)
   - 카메라 주변의 환경을 마치 위에서 내려다보는 것처럼 바꿔주기 위한 과정
3. 이미지 스티칭(Stitching)
   - 차량 주변을 찍은 이미지들을 하나의 이미지로 합성하기 위한 기술

- [핀홀 카메라 모델(Pinhole camera model)](./README.md#핀홀-카메라-모델pinhole-camera-model)
- [Camera Calibration](./README.md#camera-calibration)
  - [초점거리(focal length)](./README.md#초점거리focal-length)
  - [주점(principal point)](./README.md#주점principal-point)
  - [비대칭 계수(skew coefficient)](./README.md#비대칭-계수skew-coefficient)
  - [카메라 외부 파라미터(extrinsic parameters)](./README.md#카메라-외부-파라미터extrinsic-parameters)
  - [자동초점조절(auto focusing)](./README.md#자동초점조절auto-focusing)
  - [영상 해상도](./README.md#영상-해상도)
  - [캘리브레이션 결과가 달라지는 이유](./README.md#캘리브레이션-결과가-달라지는-이유)
  - [참고사항](./README.md#참고사항)

## 핀홀 카메라 모델(Pinhole camera model)

핀홀 카메라 모델은 아래 그림과 같이 하나의 바늘구멍(pinhole)을 통해 외부의 상이 이미지로 투영된다는 모델을 의미한다. 그리고 어안렌즈 카메라는 핀홀 카메라라는 좁은 구멍으로 통과한 빛을 렌즈로 모아서 찍는 카메라 종류 중 하나이다.

- 바늘구멍(pinhole)이 렌즈 중심
- 렌즈 중심에서 뒷면의 상이 맺히는 곳까지의 거리가 카메라 초점거리 (설명은 아래 서술)
- 광학적으로 렌즈의 중심을 투과하는 빛은 굴절되지 않고 그대로 직선으로 투과하여 이미지 렌즈에 좌우 반전의 상이 맺힌다.
- 초점으로부터 거리가 1(unit distance)인 평면을 `normalized image plane`이라고 부른다. (설명은 아래 서술)
  - 거리 -1이 아니라 1이다, 아래 사진은 -1 거리의 평면에 좌우 반전된 상이 맺히는 것을 보여주는 예시사진이다.
- 매우 이상적인 카메라 모델로, 실제로는 렌즈계의 특성에 따른 영상 왜곡 등도 같이 고려되어야 한다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Pinhole-camera.svg/330px-Pinhole-camera.svg.png" width=300>

## Camera Calibration

- 참고
  - [Reprojection을 위한 카메라 캘리브레이션 실습](https://www.youtube.com/watch?v=iOmYtms45ho)
  - [카메라 캘리브레이션 (Camera Calibration)](https://darkpgmr.tistory.com/m/32)

세상은 3차원이지만 카메라로 사진을 찍으면 2차원의 평면 이미지로 변하게 된다. 이 때 카메라의 위치 및 방향, 사용된 렌즈, 렌즈와 이미지 센서와의 거리 등등 다양한 요인의 영향을 받는데 이러한 요인을 수치화 하는 과정을 카메라 캘리브레이션이라 부른다.

3차원 점들이 영상에 투영된 위치를 구하거나 역으로 영상좌표로부터 3차원 공간좌표를 복원할 때 주로 사용된다! 어안렌즈는 시야각이 넓지만 왜곡이 심하기 때문에 꼭 `Camera Calibration`과정이 필요하다.

<details>
<summary>캘리브레이션을 활용한 어안렌즈 카메라 이미지 보정 예시</summary>
<div markdown="1">

  <img src="https://user-images.githubusercontent.com/19484971/220579310-f68ceb8c-8e59-4a0e-b8cc-03ece6323165.png" width=400>

> 어안렌즈 카메라 이미지 원본(좌), 보정 후 이미지(우)

</div>
</details>

이 때 내부 파라미터와 외부 파라미터가 필요한데 아래와 같다.

- 내부 파라미터(Intrinsic parameter)
  - 카메라 공정 과정에서 결정되는 파라미터
  - 해당 부분을 행렬로 만든 것을 A라고 간략하게 작성한다.
  - 초점거리(focal length) fx, fy: 렌즈 중심과 이미지 센서(CCD, CMOS 등)와의 거리를 의미
  - 주점(principal point) cx, cy: 카메라 렌즈의 중심
  - 비대칭 계수(skew coefficient, skew_e): 이미지 센서의 y축 기울어진 정도, 최신 카메라는 없다고 한다.
- 외부 파라미터(Extrinsic Parameters)
  - 3차원 원드 좌표계와 카메라 좌표계의 상대적 위치를 정의
  - 카메라가 실제의 원점으로부터 얼마만큼 회전 및 이동했는지에 대한 정보
  - 해당 부분을 행렬로 만든 것을 [R|t]라고 간략하게 작성한다.
  - 회전(Rotation) 3X3 행렬과 이동(Translation) 3X1 행렬로 구성
- 내부, 외부 파라미터의 행렬을 합쳐 A[R|t]라고 작성한다.
  - 이를 camera matrix 또는 projection matrix라고 부른다.

<img src="https://user-images.githubusercontent.com/19484971/195994088-60bc5dc2-44f7-40ac-9f21-74cadcaf842f.jpg" width=600>

<img src="https://user-images.githubusercontent.com/19484971/195995318-b72821eb-9de0-48dc-9c24-30eba77b4efc.png" width=300>

> 위의 사진에서 살구색이 내부 파라미터, 초록색이 회전행렬, 노란색이 이동행렬을 의미한다. X, Y, Z는 월드 좌표계에서의 카메라에 찍히는 물체의 위치이다.

위와 같은 과정으로 월드 좌표계의 물체가 어떻게 찍힐지 유추할 수 있다. 조금 더 쉽게 풀어쓰면 아래와 같다.

- (X, Y, Z)는 월드 좌표계 기준으로 물체의 한 점을 의미한다.
  - 이것을 [X, Y, Z, 1]^T로 표현한 것은 단순히 회전과 이동행렬을 동시에 적용시키기 위해서로 보인다.
- 위의 점을 외부 파라미터를 통해 알아낸 회전/이동행렬([R|t])을 활용하면 카메라 좌표계 기준으로 해당 점의 위치를 계산할 수 있다.
- 다시 내부 파라미터를 통해 한 번 더 연산을 하면 이번에는 카메라에 찍힐 때 해당 점의 위치를 계산할 수 있다, 하지만 사진은 2D 이므로 높이에 대한 정보가 손실되어 [x, y, 1]로 표현된다.

<img src="https://user-images.githubusercontent.com/19484971/195995727-21640f06-53a7-4f14-9207-6031482de4db.png" width=300>

`Camera Calibration`위에서 계산한 [x, y, 1]과 실재 찍힌 물체 위치의 오차를 `Reprojection error`라고 한다. 이 오차값을 최적화하여 3D 위치 데이터로부터 내 위치를 추정하는데 보다 정확한 값을 추정할 수 있도록 한다.

### 초점거리(focal length)

렌즈 중심과 이미지 센서(CCD, CMOS 등)와의 거리를 의미한다.

- 독특하게도 픽셀 단위로, 픽셀(셀)의 크기가 클수록 작아진다.
  - 영상에서의 기하학적 해석을 용이하게 하기 위함이라고 한다.
- 카메라의 빛을 받아들이는 부분을 셀(cell)이라고 하는데 해당 부분이 사진의 한 픽셀에 해당하므로 픽셀의 크기는 카메라마다 다르다.
- 현대 카메라는 보통 가로/세로 셀 간격이 같으므로 f = fx = fy 라고 생각해도 무방하다.
- 렌즈의 중심은 핀홀 카메라 모델에서 모든 빛이 한 점에 집중되는 곳을 의미한다.
- 초점으로부터 거리가 1(unit distance)인 평면을 `normalized image plane`, 좌표계를 `normalized image coordinate` 이라고 부르는데 해당 평면을 행렬로 표현하여 [x, y, 1]이라고 작성한다.
  - `normalized image plane`은 실제는 존재하지 않는 가상의 이미지 평면이다.

<img src="https://user-images.githubusercontent.com/19484971/196072573-2ef1e473-d78f-4d94-8b36-f7e70144a390.png" width=200>

> 도형의 닮음비만 이용해도 충분히 수식 도출이 가능하다;

카메라 좌표계 상의 한 점 P(X, Y, Z)를 영상좌표계 (x, y)로 변환할 때 먼저 Xp, Yp를 Zp(카메라 초점에서의 거리)로 나누어 거리가 1인 가상의 정규 이미지 평면`normalized image plane` 상의 좌표로 변환한다. 여기에 다시 초점거리 f를 곱하면 우리가 원하는 가상의 이미지 평면에서의 영상좌표(pixel)가 나온다.

카메라 좌표계 기준으로 물체를 투영하영 가상의 평면(normalized image plane)에 투영시키면 중앙점이 (0, 0, 1)이다. 그런데 우리가 원하는 이미지 좌표계는 중앙점이 (cx, cy, 1)이기 때문에 여기에 (cx, cy)를 더한 값이 이미지 좌표계로 변환하였을 때의 위치가 된다.

> x = fx _ X/Z + cx
> y = fy _ Y/Z + cy

만약 반대로 2D 영상좌표 p(x, y)에 대응하는 3D 공간좌표를 구하고자 할 때에는 위의 연산을 역으로만 진행하면 된다! 먼저 (x-cx, y-cy)로 영상좌표 원점을 영상중심으로 옮긴 후 Z거리가 1인 정규이미지 평면에서의 좌표 ((x-cx)/fx, (y-cy)/fy)로 바꾼 다음 실제 물체와의 거리 Z를 반영해 주면 ((x-cx)/fx*Z, (y-cy)/fy*Z, Z)가 구하고자 하는 3차원 공간좌표가 됩니다

### 주점(principal point)

주점 cx, cy는 카메라 렌즈의 중심인 핀홀에서 이미지 센서에 내진 수선의 발의 영상좌표

- 단위는 픽셀
- 영상영상 중심점(image center)과는 다른 의미
  - 카메라 조립과정에서 오차로 인해 렌즈와 이미지 센서가 수평이 어긋나면 주점과 영상중심은 다른 값을 가진다.
- 영상기하학에서는 단순한 이미지 센터보다는 주점이 훨씬 중요하다.
  - 영상의 모든 기하학적 해석은 이 주점을 이용하여 이루어진다.
  - 이미지 센서가 기울어지면 찍히는 것도 기울어지고 이것도 일종의 왜곡이 되기 때문이라고 추측하고 있다.

### 비대칭 계수(skew coefficient)

이미지 센서의 cell array의 y축이 기울어진 정도를 나타낸다.

<img src="https://user-images.githubusercontent.com/19484971/196576578-94b2802a-1cdc-4a64-806a-2c45809dd56b.png" width=300>

> skew_c = tanα

그런데.. 현대 카메라들은 이러한 skew 에러가 거의 없기 때문에 카메라 모델에서 보통 비대칭 계수까지는 고려하지 않는다고 한다.

즉, skew_c = 0 이라고 생각해도 무방하다.

### 카메라 외부 파라미터(extrinsic parameters)

카메라 좌표계와 월드 좌표계 사이의 변환 관계를 설명하는 파라미터로서, 두 좌표계 사이의 회전(rotation) 및 평행이동(translation) 행렬로 표현된다.

- 당연히 카메라를 어떤 위치에 어떤 방향으로 설치했는지에 따라 달라진다.

카메라 외부 파라미터를 구하기

1. 캘리브레이션 툴 등을 이용하여 카메라 고유의 내부 파라미터들을 구한다.
2. 미리 알고 있는 또는 샘플로 뽑은 3D월드좌표–2D영상좌표 매칭 쌍들을 이용하여 [식](./README.md#camera-calibration)에서 변환행렬을 구한다.
   - OpenCV에 있는 solvePnP함수를 이용하면 이러한 계산을 손쉽게 할 수 있다!

### 자동초점조절(auto focusing)

어떤 카메라에는 자동으로 초점을 조절하는 기능이 있는데 캘리브레이션 목적에는 적합하지 않다!

이유는 계속 초점거리가 바뀔 수 있기 때문에 캘리브레이션을 수행하고 캘리브레이션 결과를 다른 계산 목적에 사용하고자 한다면 오토 포커싱 기능은 꺼 놓고 사용하는게 좋다.

### 영상 해상도

카메라에는 보통 영상 해상도를 QVGA(320x240), VGA(640x480), 960x480, ... 등 다양하게 설정할 수 있다. 런데, 영상 해상도를 바꾸면 카메라 캘리브레이션 결과도 바뀌는 것을 확인 할 수 있다!

카메라 내부 파라미터중 초점거리 fx, fy, 주점 cx, cy은 픽셀단위인데, 물리적인 초점거리나 이미지 센서의 크기는 변하지 않지만 한 픽셀이 나타내는 물리적 크기가 변하기 때문이다.

아래와 같은 일이 생길 수 있다고 한다.

- 영상해상도가 VGA인 것과 QVGA인 것을 비교하면 QVGA의 경우가 fx, fy, cx ,cy의 값이 1/2씩 줄어든다.
- 렌즈왜곡계수(k1, k2, p1, p2)는 normalized 좌표계에서 수행되기 때문에 영상 해상도와 관계없이 항상 동일하여 한 해상도에서 구한 캘리브레이션을 수행해도 다른 모든 해상도에 대한 파라미터 값을 구할 수 있다.
  - 필자는 무슨 말인지 모르겠다;

### 캘리브레이션 결과가 달라지는 이유

캘리브레이션을 통해 얻은 파라미터는 구할 때마다 달라질 수 있는데 이유는 아래와 같다.

- 캘리브레이션은 완벽한 핀홀 카메라 모델을 가정하고 파라미터를 찾지만 실제 카메라는 핀홀 카메라 모델이 아닐 수도 있다.
- 카메라 캘리브레이션 과정에 렌즈계 왜곡모델이 들어가는데, 일반적으로 사용되는 렌즈계 왜곡모델은 왜곡 특성을 저차의 다항함수로 근사하는 것이기 때문에 실제의 렌즈계 왜곡과는 차이가 발생할 수 있다.
- 해에 대한 초기 추정치부터 시작해서 최적화 기법을 적용하여 반복적인 탐색 과정을 거쳐 **근사적인 해**를 찾는 것이기 때문에 매번 해가 달라질 수 있다.

즉, 카메라의 내부 파라미터 자체는 고유값이지만 캘리브레이션 모델 자체가 근사적인 모델이기 때문에 사용한 이미지에 따라 최적 근사해가 달라질 수 있다.

### 참고사항

캘리브레이션을 계산하기 위해서 체크보드 패턴을 자주 사용하는데 이를 사용할 때 참고하면 좋은 내용

<<<<<<< HEAD

- 패턴과의 거리는 최대한 가까울수록 좋다.
  - 캘리브레이션 자체는 패턴과의 거리와 관계없지만 패턴과의 거리가 가까우면 영상에서 좀더 정밀하게 코너점의 위치를 찾을 수 있기 때문
  - # 패턴 영상의 개수는 4개 이상이면 어느정도 캘리브레이션이 가능하지만 많을수록 좋으며 20장 이상 정도가 좋다고 한다.
- 패턴과의 거리는 최대한 가까울수록 좋다. - 캘리브레이션 자체는 패턴과의 거리와 관계없지만 패턴과의 거리가 가까우면 영상에서 좀더 정밀하게 코너점의 위치를 찾을 수 있기 때문 - 패턴 영상의 개수는 4개 이상이면 어느정도 캘리브레이션이 가능하지만 많을수록 좋으며 20장 이상 정도가 좋다고 한다.
  > > > > > > > 3f9341539a8129a4603e7a6aa51a550648170388
- 마지막으로 패턴 영상을 획득할 때에는 되도록 다양한 각도에서 영상을 획득하면 좋다.
