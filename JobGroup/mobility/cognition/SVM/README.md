# Surround View Monitor

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

## Camera Calibration

- 참고
    - [Reprojection을 위한 카메라 캘리브레이션 실습](https://www.youtube.com/watch?v=iOmYtms45ho)
    - [카메라 캘리브레이션 (Camera Calibration)](https://darkpgmr.tistory.com/m/32)

세상은 3차원이지만 카메라로 사진을 찍으면 2차원의 평면 이미지로 변하게 된다. 이 때 카메라의 위치 및 방향, 사용된 렌즈, 렌즈와 이미지 센서와의 거리 등등 다양한 요인의 영향을 받는데 이러한 요인을 수치화 하는 과정을 카메라 캘리브레이션이라 부른다.

3차원 점들이 영상에 투영된 위치를 구하거나 역으로 영상좌표로부터 3차원 공간좌표를 복원할 때 주로 사용된다! 어안렌즈는 시야각이 넓지만 왜곡이 심하기 때문에 꼭 `Camera Calibration`과정이 필요하다.

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
    -  `normalized image plane`은 실제는 존재하지 않는 가상의 이미지 평면이다.

<img src="https://user-images.githubusercontent.com/19484971/196072573-2ef1e473-d78f-4d94-8b36-f7e70144a390.png" width=200>

> 도형의 닮음비만 이용해도 충분히 수식 도출이 가능하다;

카메라 좌표계 상의 한 점 P(X, Y, Z)를 영상좌표계 (x, y)로 변환할 때 먼저 Xp, Yp를 Zp(카메라 초점에서의 거리)로 나누어 거리가 1인 가상의 정규 이미지 평면`normalized image plane` 상의 좌표로 변환한다. 여기에 다시 초점거리 f를 곱하면 우리가 원하는 가상의 이미지 평면에서의 영상좌표(pixel)가 나온다.

카메라 좌표계 기준으로 물체를 투영하영 가상의 평면(normalized image plane)에 투영시키면 중앙점이 (0, 0, 1)이다. 그런데 우리가 원하는 이미지 좌표계는 중앙점이 (cx, cy, 1)이기 때문에 여기에 (cx, cy)를 더한 값이 이미지 좌표계로 변환하였을 때의 위치가 된다.

> x = fx * X/Z + cx
y = fy * Y/Z + cy

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



### 핀홀 카메라 모델(Pinhole camera model)

어안렌즈 카메라는 핀홀 카메라라는 좁은 구멍으로 통과한 빛을 렌즈로 모아서 찍는 카메라 종류 중 하나이다. 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Pinhole-camera.svg/330px-Pinhole-camera.svg.png" width=300>

    