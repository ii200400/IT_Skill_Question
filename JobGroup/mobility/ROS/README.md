# ROS(Robot Operation System)

- 로봇을 개발하는데 필수적인 라이브러리 제공하는 소프트웨어 프레임워크
- 노드간 통신을 기반으로 전체 시스템 구동
- Application 부분만 개발하면 되기 때문에 개발 시간, 비용 절약 효과
- 다른 프레임워크와 쉽게 통합될만큼 얇다(thin).
- `Python` , `C++` 및 `Lisp` 등을 통해 개발이 가능
- 메시지 기록, 재생기능으로 반복적인 단위/통합 테스트가 용이
- 확장에 적합
- Unix 기반의 플랫폼에서만 운용이 가능하다.
    - <img src="https://user-images.githubusercontent.com/19484971/188320845-afb42cf0-d10e-4ac6-83a2-339daacc25f1.png" width=600>   
    > 출처 : http://wiki.ros.org/ROS/Introduction
- 등등.. 자세한 내용은 [ros Documentation](http://wiki.ros.org/Documentation)를 참고

- ROS의 시스템 구조 

<img src="https://user-images.githubusercontent.com/19484971/188321035-9255ea14-5ab4-4ec0-85af-537276fce56c.png" width=300>

- 다양한 툴과 노드를 통한 Architecture 구조도

<img src="https://user-images.githubusercontent.com/19484971/188321187-3c532825-4eff-4ec1-a6e2-c2c36603abd1.png" width=600>

- ROS 용어

<img src="https://user-images.githubusercontent.com/19484971/188321327-0c947bb4-e223-40d0-ab5b-e33a1c74eb02.png" width=600>

- ROS 통신

<img src="https://user-images.githubusercontent.com/19484971/188321505-b5869791-e3c3-4bf1-a072-4eb0002e1e42.png" width=600>

필자는 ROS의 용어와 통신의 정확한 이해를 못하여 결국 코드를 보면서 이해하였다.

1. topic이든 service든 시뮬레이션은 한번 명령을 받으면 그 다음 명령을 받을 때 까지 현 명령을 계속 수행한다.
2. 위의 점 때문에 특정 명령을 유지할 시간(rate)를 잘 설정하지 않으면 너무 짧게 수행하거나 너무 오래 수행할 수 있다.

- ROS 패키지 구조

<img src="https://user-images.githubusercontent.com/19484971/188321971-693edcd8-8503-4d19-b2b0-2cb6c3e59058.png" width=600>

- ROS 명령어

<img src="https://user-images.githubusercontent.com/19484971/188322131-dca9cce9-dded-4a69-af47-cf3d7863ed40.png" width=600>

ros 명령어들은 터미널이 어느 위치에 있던지 ros 패키지 기준으로 바로 명령이 가능하다는 장점이 있다.