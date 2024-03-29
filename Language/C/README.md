# 2-3 C

[모두의 코드](https://modoocode.com/231)에서 배운 내용을 기초로 작성하였음을 밝힌다. C++을 공부하기 전에 기반을 닦아두기 위해서 진행한다.

잘 정리되어있어서 행복하다. 알고 있는 내용은 생략하거나 합쳐서 조금씩 바꾸어 작성하였다.

- [1. C언어란?](./1.md)
- [2-1. C 언어 본격 맛보기](./2-1.md)
- 2-2. 주석(Comment)에 대한 이해 (생략)
- [2-3. 수를 표현하는 방법(기수법)](./2-1.md)
- [3. 변수가 뭐지?](./3.md)
- [4-2. 컴퓨터가 음수를 표현하는 방법 (2의 보수)](./4-2.md)
- [5. 문자 입력 받기](./5.md)
- [6. 만약에...(if 문)](./6.md)
- 7.뱅글 뱅글 (for, while) (생략)
- [8. 우분투 리눅스에서 C 프로그래밍 하기](./8.md)
  - 다시보기
- [9. 만약에... 2탄 (switch 문)](./9.md)
- [10. 연예인 캐스팅(?) (C 언어에서의 형 변환)](./10.md)
  - 실직적으로는 컴퓨터의 실수 표현 방법을 더 많이 설명
- [11-1. C 언어의 아파트 (배열), 상수](./11-1.md)
- [11-2. C 언어의 아파트2 (고차원의 배열)](./11-2.md)
- [12-1. 포인터는 영희이다! (포인터)](./12-1.md)
- [12-2. 포인터는 영희이다! (포인터)](./12-2.md)
- [12-3. 포인터는 영희이다! (포인터)](./12-3.md)
- [13-1. 마술 상자 함수(function)](./13-1.md)
- [13-2. 마술 상자 함수 2 (function)](./13-2.md)
- [13-3. 마술 상자 함수 3 (function)](./13-3.md)
- [13-4. 마술 상자 함수 (생각해볼 문제에 대한 아이디어)](./13-4.md)
  - 13-3 강의 과제에 대한 아이디어
  - 문제 5만 풀이
- [14. 컴퓨터의 머리로 따라가보자 - 디버깅(debugging)](./14.md)
- [15-1. 일로와봐, 문자열(string)](./15-1.md)
- [15-2. 일로와봐, 문자열(string)](./15-2.md)
  - 문자열보다는 버퍼에 대한 설명이 더 많음
- [15-3. 일로와봐, 문자열(string) - 문자열 지지고 볶기 & 리터럴](./15-3.md)
- [16-1. 모아 모아 구조체(struct)](./16-1.md)
- [16-2. 모아 모아 구조체(struct) - 구조체 인자로 가진 함수](./16-2.md)
  - C언어의 주요 내용은 여기까지
  - 다시보기 [과제](./16-2.project.md)
- [16-3. 구조체와 친구들(공용체(union), 열거형(enum))](./16-3.md)
- [17. 변수의 생존 조건 및 데이터 세그먼트의 구조](./17.md)
  - 배운 개념을 환기하는 정도
- [18-1. 파일 뽀개기 (헤더파일과 #include)](./18-1.md)
  - 도서관리 프로젝트를 헤더파일로 정리하는 내용도 있지만 구조체를 사용하지 않은 내용이다.
- [18-2. 파일 뽀개기 (# 친구들, 라이브러리)](./18-2.md)
- [19. main 함수의 인자, 텅 빈 void 형](./19.md)
- [20-1. 동동동 메모리 동적할당(Dynamic Memory Allocation)](./20-1.md)
- [20-2. 메모리 동적할당 + 메모리 갖고 놀기](./20-2.md)
- [21. 매크로 함수, 인라인 함수](./21.md)

- 기타
  - [C 레퍼런스](https://modoocode.com/category/C%20Reference)

## 개요

### C언어에 대해

C언어는 배우기 힘들다. 이유는..

- 무려 50년(1972년)에 출시한 언어
- 새로 출시된 언어들에 비해 편의성이 상대적으로 낮음
- 유닉스 운영체제를 작성하기 위해서 만들어져 시스템 프로그래밍이 주 목적이라 시스템 관련 배경지식과 긴밀함
  - 몰라도 되지만, 모른다면 더욱 까다로움
- 제공하는 기능이 적고 배울 내용은 적고 구현할 것은 많음

### 컴퓨터에 대해

컴퓨터란? **일련의 연산을 수행하는 계산기**

일반 계산기나 데스크탑 컴퓨터이나 같은 계산기에 불과하다.

차이점은..

- 명령어를 읽고 명령에 따라 연산을 수행
- 명령어를 통해 사람의 노동이나 작업의 자동화가 가능

계속해서 컴퓨터에 대해 알아보기 위해서 아래의 내용을 살펴볼 것이다.

- 명령어를 처리하는 장소
- 명령어를 저장하는 장소
- 프로그램과 명령어 작성

### 명령어를 처리하는 장소

중앙처리장치 CPU이라는 반도체에 의해서 명령어가 처리된다.

CPU(Central Processing Unit)

- 1초에 약 10억개의 연산을 처리
- 엄청난 열을 발생하여 보통 쿨러(냉각장치) 아래에 배치

GPU(Graphics Processing Unit)

- 그래픽 관련 연산(행렬 연산) 전문 처리 장치
- CPU에 비해 특수한 명령어만 처리

### 명령어를 저장하는 장소

CPU에 의해 처리된 결과를 CPU에 저장하면 좋겠으나, CPU는 연산의 처리에만 특화된 장치여서 저장 공간이 매우 부족하다.

때문에 데이터를 저장하는 공간은 레지스터(Register)를 사용한다.

레지스터

- CPU 연산 결과를 저장하는 장소
- CPU의 구조(아키텍쳐)에 따라서 사용되는 수와 비트가 다름
  - 64비트 컴퓨터의 경우 레지스터는 8바이트
- CPU 내부에 존재하는 메모리

레지스터는 용량이 적은 편이기 때문에 많은 데이터를 저장하기 위해서 램을 같이 사용한다.

RAM(램 / Random Access Memory)

- CPU 밖에 존재하는 메모리
- 8GB 이상의 크기
- 휘발성 메모리의 특징으로 전원이 없다면 데이터 소실

메모리

- 휘발성 메모리는 레지스터와 RAM이 존재
- 전원이 꺼져도 저장하기 위한 메모리는 하드디스크(HDD)나 SSD 등이 존재
- 레지스터와 렘 사이의 메모리 접근을 돕기 위해 캐시(Cache)를 사용
  - 캐시는 계층별로 L1, L2.. 가 존재
  - 숫자가 작을수록 크기가 작고 CPU가 읽는 속도가 빨라 더 중요한 데이터 순으로 저장됨
  - 캐시에 저장될 데이터는 예측 알고리즘을 적용하여 최대한 적중률을 높이는 방향으로 저장
  - 요청한 데이터가 캐시에 없는 경우 캐시미스(Cache miss)라고 부름
- 보통 저장용량이 클수록 데이터를 가져오는 것이 느리므로 각자의 특성을 살려 사용처가 결정
  - 프로그램은 하드디스크가 저장
  - CPU에서 사용할 프로그램은 하드디스크에서 RAM으로 복제하여 사용

### 명령어 작성

위와 같이 CPU는 메모리와 같이 연산을 진행한다. 그럼 메모리의 어느 위치에 저장할까? (램 기준으로 설명을 진행한다.)

램의 모든 공간는 1바이트 단위로 0번을 시작으로 고유의 주소(address)가 부여되어있다.

주소를 활용하여 램에 데이터를 관리하는데 아래와 같은 방식으로 진행된다.

1. CPU는 램에게 어디에서 데이터를 읽을지 알려주면 램은 해당 위치의 데이터를 즉시 전달한다.
2. 저장도 위와 마찬가지로 진행한다. (이미 데이터가 있다면 덮어 씌워진다.)
3. 저장한 주소값과 얼만큼의 데이터를 읽을지를 지정해준다. (램은 데이터의 끝 주소를 모른다.)

어셈블리(Assembly)

- CPU가 직접 해석하는 명령어
- 어셈블리어(명령어)와 실제 CPU가 이해할 수 있는 명령어가 1대1로 대응
- 메모리의 주소값에 해당하는 데이터는 꼭 값을 레지스터(변수)에 저장하고 레지스터를 통해 참조하는 방식으로 작동
  - 레지스터는 변수가 아니나, 이해하기 힘들어 나에게 맞게 작성
  - 어셈블리어는 따로 공부하는 것을 추천..

#### CPU가 명령어를 읽는 방법

CPU는 렘에 데이터를 주소값을 통해 접근하는데, 이때 사용되는 명령어는 어디에 저장되어있을까? 바로 프로그램이다.

즉, CPU가 명령어를 실행하는 것을 **프로그램을 실행한다**고 말한다. 프로그램은 단순하게 생각하면 **실행할 명령어와 데이터의 집합**으로 볼 수 있다.

프로그램의 실행은 아래와 같이 진행된다.

1. 운영체제가 CPU에게 램에 위치한 프로그램이 저장된 주소값을 알려준다.
2. 해당 주소값은 `RIP`이라는 특별한 레지스터에 저장한다.
3. CPU가 `RIP`에 명령어 주소를 업데이트하면서 작성된 명령어를 순차적으로 진행시켜나간다.

```
여기서 CPU는 데이터를 명령어인지, 숫자인지 구별하지 않고 읽는다. 실제로 해킹 기법 중에서 사용자 (해커가) 입력한 데이터를 마치 명령어로 착각하게 해서 해커가 원하는 프로그램을 실행시키는 공격 기법이 있다고 한다.
```

### 가상 메모리와 물리 메모리

CPU가 참조하는 메모리 주소값과 실재 램의 메모리 주소값은 다르다. 전자는 가상 메모리(virtual memory) 라고 하고, 후자는 물리 메모리(physical memory) 라고 한다.

당연히 메모리를 원활히 사용하기 위해 가상 메모리와 물리 메모리를 매핑해주는 변환법이 존재한다. 방법에 따라 **페이징(Paging)**과 **세그멘테이션(Segmentation)**으로 나뉜다.

두 방식은 조금은 다르지만 공통된 부분이 있다.

1. 두 메모리의 매핑을 위해 존재하는 테이블이 있다. 테이블은 프로그램이 추가될 때마다 생겨난다.
2. 메모리에 데이터를 분할하여 저장하기 위한 불연속 메모리 관리 기법이다.
3. 메모리 관리 방식에 따라 사용되지 못하고 빈 메모리가 생기게 된다.
4. 경우에 따라서는 실재 프로그램이 필요로 하는 메모리의 총량이 물리 메모리의 용량보다 더 큰 경우도 해결가능하다. (대신 하드디스크까지 동원되며 속도가 느려진다.)

### 정리

내용을 정리하면 아래와 같다.

- 모든 연산은 CPU 에서 수행된다.
  - 정확히는, CPU 의 자그마한 레지스터 상에서 수행된다.
  - 64 비트 CPU 의 경우 레지스터의 크기는 8 바이트 이다.
- CPU 는 무슨 연산을 할 지 알려주는 명령어와 명령어를 실행하기 위해 필요로 하는 데이터를 메모리 (램) 에서 읽는다.
- 프로그램을 실행한다는 것은 하드 디스크에 작성된 명령어들과 데이터를 메모리에 쓰는 것이다.
  - 운영체제가 CPU 에 처음으로 실행해야 할 명령어의 주소값을 전달함으로써 프로그램이 시작된다.
- CPU 에는 캐시가 있어서 메모리 접근 횟수를 줄일 수 있다.
- CPU 에서 참조하는 주소값은 실제 물리 메모리 주소값이 아니라 가상 메모리 주소값이다.
  - 덕분에 각 프로그램들은 마치 자신이 방대한 메모리 공간 전체를 사용하는 것 처럼 생각하며 작동한다.
  - 가상 메모리 주소값은 각 프로그램의 매핑 테이블을 통해서 실제 메모리 주소값으로 변환된다.

### 후기

컴퓨터 구조론을 다시 공부하고 있는 기분이 든다. 내가 아는 내용을 추가하고 상대적으로 어려워서 이해를 못한 어셈블리어는 제외하였다.
