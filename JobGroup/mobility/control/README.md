# 제어(Control)

`목차`

* [개요](#개요)
* [속도 제어](#속도-제어)
* [경사로 속도 제어](#경사로-속도-제어)
  + [곡률 반지름](#곡률-반지름)
* [ACC(Adaptive Cruise Control)](#accadaptive-cruise-control)

## 개요

제어인식 및 판단 결과에 따른 자율주행 시스템의 동작, 실제 차를 어떻게 움직일지에 대해 구동계와 조향계에 명령을 내린다.

## 속도 제어

진행할 경로를 계획하는 것과 계획된 대로 움직이는 것은 별개의 문제이다. 어떤 상황에서 어떻게 속도를 가할지 제어하는 방법을 살펴보자.

- 전방 차량 추종(Adaptive Cruise Control)
- 긴급제동(Autonomous Emergency Braking)
- [PID 제어기](./pid/README.md)
    - 거리 및 속도 유지 제어기 설계에 사용
    - 비례-적분-미분(Proportional-Integral-Differential controller) 사용
    - 내 차량의 상태와 목표 차량의 상태와의 오차 값을 이용해 제어값 계산
    
## 경사로 속도 제어

참고로 경사로 속도 제어라는 제어법이 있는 것이 아니라 단순 물리 계산에 가깝다.   
아마.. 물리 공부를 거의 안한 사람에게는 도대체 무슨 말인가 싶을 것;;

- 경사진 도로에서의 주행은 다양한 힘을 고려해야 함
    - 중력(mg), 마찰력(μsN), 원심력(mv**2/r) 등
- 보통의 도로는 평평(flat)하므로 좌/우회전시 미끄러지지 않고 달릴 수 있는 최고 속도는 곡률 반지름과 도로의 정지마찰력의 루트 값에 비례
    - 아래의 그림의 `Flat roadway` 위의 수식 참고

<img src="https://user-images.githubusercontent.com/19484971/189119498-fc379b08-19e7-4c26-8bdc-197a7071e809.png" width=400>

> 출처 : http://hyperphysics.phy-astr.gsu.edu/hbase/Mechanics/carbank.html

- 해석

그림의 y축으로 자동차가 움직이지 않으므로(자동차가 땅으로 꺼지거나 하늘로 승천하지 않으므로) 아래의 수식이 성립

<img src="https://user-images.githubusercontent.com/19484971/189150663-fb8e9a14-cbbb-4495-868d-f3cd7bec2c13.png" width=400>

그림의 x축으로 자동차가 움직이는 최대 속도는 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/189154915-21bc14b1-427c-4583-b2bc-5496afb7f66e.png" width=400>

왼쪽의 힘은 원심력, 오른쪽은 중력에 의한 힘의 수직항력과 수직항력에 의한 마찰력을 기울기에 따라서 계산한 것이다.

<img src="https://user-images.githubusercontent.com/19484971/189157946-93f7884e-2aff-446d-9292-978d10c58c65.png" width=300>

> 출처 : http://www.tslining.co.kr/tech1_friction_ratio_n_wear_rate/

만약 왼쪽이 더 작다면 문제가 되지 않으나, 오른쪽의 값이 더 작게 되는 순간 정지마찰력이 운동마찰력이 되면서 자동차가 **미끄러지게 된다!**

간단히 생각하면 바깥으로 튕겨져 나가는 힘을 마찰력이 간당간당하게 막고 있었는데 임계치(최대 정지 마찰력)를 넘어서면서 마찰력이 막아주지 못하고 튕겨나가게 되는 것

<img src="https://user-images.githubusercontent.com/19484971/189157695-f8f08609-ee58-4d83-96fe-0ced43adcf44.png" width=300>

> 출처 : http://www.tslining.co.kr/tech1_friction_ratio_n_wear_rate/


### 곡률 반지름

- 경사로 속도 제어를 위해 곡률 반지름이 필요
- 최소제곱법, 최소자승법이라고 불리는 방정식 활용
    - 어떤 방정식의 해를 근사적으로 구하는 방법
    - 구하려는 해와 실재 해의 오차가 최소가 되도록 구하는 방법
    - <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Linear_least_squares%282%29.svg" width=400>

원의 방정식을 예시로 들었는데 갑자기 왜 `c=a^2+b^2-r^2`가 생긴것인지 이해가 잘 되지 않았지만 일단 진행하였다.

## ACC(Adaptive Cruise Control)

[참고 페이지](https://kr.mathworks.com/help/mpc/ug/adaptive-cruise-control-using-model-predictive-controller.html)

- 운전자가 설정한 속도로 주행을 하다가 센서를 통해 확인한 앞 차와의 간격을 유지하는 시스템
    - 다양한 ACC 알고리즘 중에서도 설명할 ACC 알고리즘은 고전적이고도 단순한 것
- 장애물을 속도가 0인 차량으로 생각하여 여러 곳에 적용 가능

<img src="https://user-images.githubusercontent.com/19484971/189482491-32fe7019-877a-4e3e-9ceb-07701b1ff723.png" width=600>


<img src="https://kr.mathworks.com/help/examples/mpc/win64/AdaptiveCruiseControlExample_eq16130372607239683991.png" width=300>

> 출처 : https://kr.mathworks.com/help/mpc/ug/adaptive-cruise-control-using-model-predictive-controller.html

- 용어
    - Speed control   
    ego 차량이 운전자 혹은 개발자가 설정한 속도로 주행하는 상태, 앞 차와의 거리가 안전거리보다 먼 경우의 상태
    - Spacing control   
    앞 차와의 안전거리를 유지하는 상태, 앞 차와의 거리가 안전거리보다 가까운 경우의 상태
    - D rel   
    (센서로부터) 앞 차와의 거리
    - V rel   
    (센서로부터) 앞 차의 상대 속도, ego 차량의 속도가 5이고 앞 차의 속도가 3이라면 앞 차의 상대속도는 -2
    - V ego   
    ego 차량의 속도
    - D safe   
    앞 차와의 안전거리
    - D default   
    기본 유지 거리
    - T gap
    판단에서 제어까지 차량을 안전하게 멈추는 시간으로 보통은 (two-second-rule에 기반하여) 2초로 설정

단순히 거리가 멀때 설정한 값으로만 움직이는 것은 거리가 조금이라도 안전거리보다 커지면 갑자기 엑셀을 세게 밟게 될 수 있기 때문에 거리에 비례하여 엑셀을 밟을 수 있도록 하는 것이 좋아보인다.
