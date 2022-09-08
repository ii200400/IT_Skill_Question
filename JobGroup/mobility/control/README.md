# 제어(Control)

제어인식 및 판단 결과에 따른 자율주행 시스템의 동작, 실제 차를 어떻게 움직일지에 대해 구동계와 조향계에 명령을 내린다.

- [PID 제어기](./pid/README.md)

## 속도 제어

진행할 경로를 계획하는 것과 계획된 대로 움직이는 것은 별개의 문제이다. 어떤 상황에서 어떻게 속도를 가할지 제어하는 방법을 살펴보자.

- 전방 차량 추종(Adaptive Cruise Control)
- 긴급제공(Autonomous Emergency Braking)
- PID 제어기
    - 거리 및 속도 유지 제어기 설계에 사용
    - 비례-적분-미분(Proportional-Integral-Differential controller) 사용
    - 내 차량의 상태와 목표 차량의 상태와의 오차 값을 이용해 제어값 계산
    

