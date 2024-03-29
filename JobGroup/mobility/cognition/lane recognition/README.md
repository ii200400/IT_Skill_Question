# Lane Recognition

`목차`

* [개요](#개요)
* [이진화](#이진화)
* [Region of interest](#region-of-interest)
* [Bird's eye view](#birds-eye-view)
* [Curve fitting](#curve-fitting)

## 개요

GPS를 사용할 수 없는 터널 같은 구간이나 다른 센서를 활용할 수 없는 구간에서 의미있게 활용되는 차선인지는 아래의 총 4 단계로 나뉜다.

1. 이진화
2. Bird's eye view
3. Regin of interest
4. Curve fitting

앞의 3단계는 개발자나 회사에 따라서 달라지는 경우가 많다고 한다.

## 이진화

이름 그대로 숫자의 값을 0이나 1로 변환하는 것을 의미하는데 대표적으로는 0\~255의 값을 0\~1로 변환하여 컬러사진을 흑백사진으로 변환할 때 사용되는 것이 대표적이다.

이진화를 위해서는 기준값(threhold)가 필요한데 이 값보다 크면 1을 작으면 0을 반환한다. 해당 기능은 scikit-learn을 활용하여 진행하였다.

<img src="https://user-images.githubusercontent.com/19484971/194850405-f451905d-4995-48a8-a27f-1518dd15905c.png" width=500>

하지만...
- RGB에는 다양한 색상이 혼재됨
- 이미지의 밝기에 영향이 미침
- 차선의 노후도

등등의 원인으로 인하여 단순히 특정값 이상만 255로 만들고 나머지를 0으로 만드는 작업을 그대로 사용하면 어려울 수 있다. 때문에 RGB 이미지를 그대로 사용하지 않고 HSV라는 채널로 변경해 사용한다.

- H : Hue(색조) - 색의 질을 의미하며 빨강, 노랑, 초록 등을 표현한다.
- S : Saturation(채도) - 원색에 가까울수록 높다.
- V : Value(명도) - 밝기를 의미하며 높을수록 흰색, 낮을수록 검은색에 가까워진다.

<img src="https://user-images.githubusercontent.com/19484971/194856686-ce75b0f1-c4fc-4e3c-93b0-96e0c7933f70.png" width=500>

## Region of interest

하늘이나 도로 바깥 영역등의 필요없는 부분을 잘라내고 필요한 영역만 보기위한 영상처리 기법을 의미한다. 줄여서 RoI라고 부른다.

차선을 제외한 다른 구간을 잘라내어야 오인지를 줄일 수 있지만 너무 많이 잘라버리면 곡률구간이 큰 도로에서는 차선을 놓칠 수 있으므로 적당한 영역을 잘라내어야 한다.

다음의 조건에서 아래와 같은 사진이 나온다.

- 320*280 크기의 이미지
    - 참고로 이미지는 좌측 상단이 (0, 0)
- 차선을 위한 영역 지정 및 삭제
    - 전방 카메라의 경우 차선은 앞쪽으로 좁아지는 형태이기 때문에 마름모꼴의 영역 지정

<img src="https://user-images.githubusercontent.com/19484971/194860451-295b6159-619e-4f40-b8ef-e5392a2d9d99.png" width=600>

## Bird's eye view

이름 그대로 하늘에서 내려다보는 시점을 의미한다.

이진화 처리가 된 이미지는 사진의 특성상 원근감이 생길 수 밖에 없기 때문에 차선의 곡률을 알기 어렵기 때문에 `Bird's eye view` 로 바꾸어 곡률을 확인해주어야 한다. 이때 이미지는 왜곡시키는 이미지 와핑(warping)작업이 필요하다.

- warping
    - 이미지를 왜곡시키는 작업
    - x축이나 y축, scale 등을 이용하여 이미지를 보정하거나 찌그러진 이미지를 정규화하기 위한 처리 방법 혹은 기법
    - RoI 지점 정의 필요

위의 와핑기능은 OpenCV에서 이미 구현되어있어 사용하기만하면 되는데 해당 기능을 작업하는 함수는 `getPerspectiveTransform()`과 `warpPerspective()`함수가 있다.

3차원 공간에 대한 정보 없이 단순 wraping시키는 것이기 때문에 정확한 좌표를 알 수 없어 LookUp table을 통해 특정 값으로 지정하거나 특정 함수를 활용하기도 한다.

<img src="https://user-images.githubusercontent.com/19484971/194863338-4940f315-cfb3-4596-83d6-e29bc8d2f12d.png" width=600>

## Curve fitting

최소제곱법을 통한 차선인지를 진행한다는 내용이 있는데 당장은 `Bird's eye view`만 필요하기 때문에 생략한다.
