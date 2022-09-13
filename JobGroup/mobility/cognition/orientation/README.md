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