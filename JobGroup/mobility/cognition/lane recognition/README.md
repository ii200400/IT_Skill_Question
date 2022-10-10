# Lane Recognition

GPS를 사용할 수 없는 터널 같은 구간이나 다른 센서를 활용할 수 없는 구간에서 의미있게 활용되는 차선인지는 아래의 총 4 단계로 나뉜다.

1. 이진화
2. Bird's eye view
3. Regin of interest
4. Curve fitting

앞의 3단계는 개발자나 회사에 따라서 달라지는 경우가 많다고 한다.

## 이진화

이름 그대로 숫자의 값을 0이나 1로 변환하는 것을 의미하는데 대표적으로는 0~255의 값을 0~1로 변환하여 컬러사진을 흑백사진으로 변환할 때 사용되는 것이 대표적이다.

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

