# PID control

[위키](https://en.wikipedia.org/wiki/PID_controller) 참고

- proportional–integral–derivative controller (PID controller)의 약어
    - three-term controller 라고도 함
- 다양한 제어 시스템에서 널리 사용되는 제어 메커니즘
    - 피드백(feedback)을 사용하는 제어루프(control loop) 라고 언급함

## 기본 연산

<img src="https://user-images.githubusercontent.com/19484971/188306477-f674529b-3650-4da8-8e0b-653d8d7ba673.png" width=400> 

> 출처 : https://en.wikipedia.org/wiki/PID_controller 의 Controller theory

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/PID_en.svg/600px-PID_en.svg.png" width=400>

- 수식
    - SP = r(t)   
    목표로 설정한, 도달하길 원하는 값(setpoint)
    - PV = y(t)   
    현재 측정되는 값 (process variable)
    - e(t) =  r(t) - y(t)   
    원하는 상태와 현재 상태의 차이값 (error value)
    - e(τ)   
    e(t)를 잘못 작성한 것 같다. 설명에도 각속도나 토크 설명은 전혀 없다.
- MV(t) 해석
    - 비례항   
    e(t) 크기에 비례한 제어작용
    - 적분항   
    과거의 e(t) 값들의 총합에 대한 제어 작용
    - 미분항   
     e(t)의 오차변화율을 비례하는 제어 작용으로 `예측제어`라고도 부름
    - 매개변수들   
    Kp, Ki, Kd는 비례, 적분, 미분항에 적용되는 매개변수들로 피드백에 따라서 조정된다.
    - tuning   
    위의 제어 기능들의 효과가 최적이 되도록 매개변수를 조절하는 과정을 의미

r(t)가 속도라고 생각하면 비례항은 속도제어, 적분항은 거리제어, 미분항은 가속도 제어라고 이해하면 조금 쉬운데.. 그렇게 설명하지 않는 것을 보면 지양해야겠다.

<img src="https://upload.wikimedia.org/wikipedia/commons/3/33/PID_Compensation_Animated.gif" width=400>

> 출처 : https://en.wikipedia.org/wiki/PID_controller