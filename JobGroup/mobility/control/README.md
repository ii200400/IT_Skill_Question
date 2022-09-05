# 제어(Control)

제어인식 및 판단 결과에 따른 자율주행 시스템의 동작, 실제 차를 어떻게 움직일지에 대해 구동계와 조향계에 명령을 내린다.

## 경로 제어

판단에 따라 경로대로 움직이는 것은 별도의 문제이다. 현재 이동속도와 각도에 따라서 임의적으로 경로에서 약간 어긋나도록 진행할 수도 있다.

개인적으로 계획은 판단 영역이고 경로대로 움직이는 것은 제어 영역이라고 생각하여 분리하게 되었다.

### 경로 궤적

경로 계획에 따라 차선 변경이나 경로를 따라가기 위한 궤적이 필요하다. 

- 경로 궤적 생성
    - 궤적을 만들 때 가장 쉬운 방법으로는 시작점과 끝점을 이어 조향하는 방법 (1차 함수 궤적)
        - 이 방법은 차선 변경이 시작되는 순간과 완료되는 순간에 큰 각도의 변화를 요구하여 실재로는 힘듦
        - <img src="https://user-images.githubusercontent.com/19484971/188302479-854b8216-6deb-448c-93c3-3418177588a8.png" width=300>
    - 높은 각속도를 피하기 위해서 시작점과 끝점을 잇는 3차 함수 곡선을 생성
        - 1차 함수 궤적보다 훨씬 적은 순각 각도 변화량으로 안정적으로 차량 변경이 가능하도록 한다.
        - <img src="https://user-images.githubusercontent.com/19484971/188302968-0469cdfd-cde3-4ab7-ac7d-1b6353ade3bd.jpg" width=300>
        > < 경로 생성 - 3차 함수 궤적 >

### 경로 추적

경로를 추종하는 방법은 여러가지가 있으나, 대표적으로 `Pure pursuit guidance`가 있다.

- Pure pursuit guidance
    - `path tracking algorithm(경로 추적 알고리즘)` 중 하나
    - 경로 위의 한 점을 원호를 그리며 추적하는 알고리즘
    - 자동차의 기구학과 전방주시거리(Look Ahead Distance)라는 파라미터를 가지고 조향각을 간단하게 계산한다.
    - 실제 자동차 모델(Ackerman geometry)을 단순화 한 Bicycle 모델을 사용
    - 자세한 내용을 [MathWorks](https://kr.mathworks.com/help/robotics/ug/pure-pursuit-controller.html)에서 찾아볼 수 있다.
        - 대충 전방주시거리를 너무 멀리하면 조향이 느려지고 너무 가깝게 하면 과한 조향으로 궤적을 따라가지 못한다는 내용이 있다.

<img src="https://user-images.githubusercontent.com/19484971/188305260-43d53167-2ddd-4693-8700-dab1fd65b501.png" width=400>

`전방주시거리`라는 단어를 설명해주시지 않고 진행하셔서 처음에는 이미지의 변수가 어떤 의미인지 몰랐다;

## 속도 제어

진행할 경로를 계획하는 것과 계획된 대로 움직이는 것은 별개의 문제이다. 어떤 상황에서 어떻게 속도를 가할지 제어하는 방법을 살펴보자.

- 전방 차량 추종(Adaptive Cruise Control)
- 긴급제공(Autonomous Emergency Braking)
- PID 제어기
    - 거리 및 속도 유지 제어기 설계에 사용
    - 비례-적분-미분(Proportional-Integral-Differential controller)
    - 내 차량의 상태와 목표 차량의 상태와의 오차 값을 이용해 제어값 계산
        - 비례항 : 현재 상태에서의 오차 값의 크기에 비례한 제어작용   
        (현재 상태와 목표 상태까지의 차이만큼 힘을 싣는다는 의미라고 생각한다.)
        - 적분항 : 정상 상태에서의 오차를 없애는 작용   
        (필자 눈으로는 오차를 없앤다기 보다는 원하는 지점으로 값이 수렴하게 만드는 것으로 보인다.)
        - 미분항 : 출력값의 급격한 변화에 제동을 걸어 오버 슛을 줄이고 안정성을 향상   
        (필자 눈으로는 오히려 이것이 오차를 없애는 것으로 보인다;)
    - <img src="https://user-images.githubusercontent.com/19484971/188306477-f674529b-3650-4da8-8e0b-653d8d7ba673.png" width=400> 
    > 출처 : https://en.wikipedia.org/wiki/PID_controller 의 Controller theory

    - <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/PID_Compensation_Animated.gif" width=400>
    > 출처 : https://en.wikipedia.org/wiki/PID_controller
    

