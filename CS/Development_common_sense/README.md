# 1-6 개발상식

`목차`

* [객체 지향 프로그래밍 (Object Oriented Programming - OOP)](#객체-지향-프로그래밍-object-oriented-programming---oop)
  + [객체 지향 프로그래밍의 특징](#객체-지향-프로그래밍의-특징)
  + [객체지향의 장점](#객체지향의-장점)
  + [객체 지향 설계 5원칙](#객체-지향-설계-5원칙)
    - [1. 단일 책임 원칙 (SRP - Single Responsibility Principle)](#1-단일-책임-원칙-srp---single-responsibility-principle)
    - [2. 개방 폐쇄 원칙(OCP - Open-Closed Principle)](#2-개방-폐쇄-원칙ocp---open-closed-principle)
    - [3. 리스코프 치환 원칙(LSP - Liskov Substitution Principle)](#3-리스코프-치환-원칙lsp---liskov-substitution-principle)
    - [4. 인터페이스 분리 원칙(ISP - Interface Segregation Principle)](#4-인터페이스-분리-원칙isp---interface-segregation-principle)
    - [5. 의존 역전 원칙(DIP - Dependency Inversion Principle)](#5-의존-역전-원칙dip---dependency-inversion-principle)
  + [절차 지향 프로그래밍](#절차-지향-프로그래밍)
  + [객체 지향 프로그래밍 vs 절차 지향 프로그래밍](#객체-지향-프로그래밍-vs-절차-지향-프로그래밍)
    - [객체지향과 절차지향 도형 그리기 예제](#객체지향과-절차지향-도형-그리기-예제)
* [RESTful API](#restful-api)
  + [REST (REpresentational State Transfer)](#rest-representational-state-transfer)
    - [REST 구성 요소](#rest-구성-요소)
      * [1. 자원(Resource): URI](#1-자원resource-uri)
      * [2. 행위(Verb): HTTP Method](#2-행위verb-http-method)
      * [3. 표현(Representation of Resource)](#3-표현representation-of-resource)
  + [REST 특징](#rest-특징)
    - [1. Server-Client (서버-클라이언트 구조)](#1-server-client-서버-클라이언트-구조)
    - [2. Stateless (무상태성)](#2-stateless-무상태성)
    - [3. Cacheable (캐시 가능)](#3-cacheable-캐시-가능)
    - [4. Layered System (계층형 구조)](#4-layered-system-계층형-구조)
    - [5. Uniform Interface(인터페이스 일관성)](#5-uniform-interface-인터페이스-일관성)
    - [6. Self-descriptiveness (자체 표현 구조)](#6-self-descriptiveness-자체-표현-구조)
  + [API - Application Programming Interface](#api---application-programming-interface)
  + [REST API 설계 규칙](#rest-api-설계-규칙)
    - [유의사항](#유의사항)
    - [HTTP 응답 상태 코드](#http-응답-상태-코드)
* [MVC(Model-View-Controller) 패턴](#mvcmodel-view-controller-패턴)
* [함수형 프로그래밍](#함수형-프로그래밍)
* [High-order functions (고차함수)](#high-order-functions-고차함수)
* [First-class function (일급함수)](#first-class-function-일급함수)
* [VCS(Version Control System)](#vcsversion-control-system)
  + [Git](#git)
    - [Git WorkFlow](#git-workflow)
    - [Git 명령어](#git-명령어)
    - [Git branch](#git-branch)
    - [git merge](#git-merge)
  + [Git Strategy](#git-strategy)
* [Package와 Import](#package와-import)
  + [Package](#package)
  + [Import](#import)
* [CI/CD](#cicd)

## 객체 지향 프로그래밍 (Object Oriented Programming - OOP)

우리가 실생활에서 쓰는 모든 것을 객체로 취급하고 이러한 객체를 중점으로 프로그래밍하는 방식을 의미한다. 구현에 필요한 객체를 파악하고 각각의 객체들의 역할이 무엇인지를 단순화, 추상화하여 객체들 간의 상호작용을 중점으로 프로그램을 만드는 방식으로 프로그래밍을 하는 것에 중점을 둔다.

- 객체 지향 프로그래밍의 장점!
  - 기능과 데이터를 모듈화하여 신뢰성 높인다.
  - 추가/수정/삭제가 편한 코드를 작성할 수 있다.
  - 코드의 재 사용성을 높일 수 있다.

객체 지향 프로그래밍에서는 현실의 객체를 추상화하여 클래스로 정의하고 클래스를 통해 객체를 만들어 직접 사용한다. 이때 클래스는 설계도, 객체는 설계도를 기반으로 만든 실제 객체라고 많이 비유한다.

- 클래스(class)  
  현실의 객체를 추상화하여 속성(attribute)과 행위(behavior)를 변수와 메서드로 정의한 것.  
  단순히 설계도나 틀, 타입(Type)으로 간주하며 프로그램이 객체를 생성할 때만 사용한다.
- 객체(instance, object)  
  클래스의 정의를 토대로 메모리를 할당받은 데이터와 메소드의 집합으로 프로그램에서 직접 사용한다.  
  이때 클래스는 만든 객체의 **타입(Type)**이 된다.

### 추가설명

이전에는 단순히 계산이 빠르고 특정 값을 대입하면 결과 값을 반환하는 함수를 사용할 수 있는 정도만을 컴퓨터에게 요구했다고 한다.  
하지만, 사람들이 많은 일을 처리해야 하는 상황에 직면하면서 현실세계의 일을 컴퓨터 연산을 활용하기 시작했고 이러한 이유로 현실세계의 객체를 추상화하여 프로그래밍하는 객체 지향 프로그래밍이 대두되었다고 한다. 단순히 사람들이 현실세계를 기준으로 프로그래밍하는 것이 조금 더 직관적이고 편하기 때문인 것도 있다.

<br/>

### 객체 지향 프로그래밍의 특징

객체 지향 프로그래밍의 특징은 매우 많지만 그 중에서도 가장 유명하고 대표적인 4가지를 소개하면 다음과 같다.

1. 추상화(Abstraction)

   - 불필요한 정보는 숨기고 필요한 정보들만을 표현함으로써 공통의 속성이나 기능을 묶어 이름을 붙이는 것
   - 객체지향적 관점에서는 클래스를 정의하는 것을 추상화라고 할 수 있다.

2. 캡슐화(Encapsulation)
   - 실제로 구현되는 부분을 외부에 드러나지 않도록 하여 정보를 은닉하는 것
   - 데이터와 기능을 하나로 묶어(클래스로 만들어) 관리하여 객체가 독립적으로 역할을 수행할 수 있도록 한다.
   - 다른 객체가 임의로 변수나 기능을 바꿀 수 없어 오류 방생 확률을 낮춘다.
     - 만일 한 객체를 바꾸어 다른 객체에 영향을 끼치면 side effect(사이드이펙트/부작용)라고 한다.
   - 내부의 데이터는 외부에서 직접 접근할 수 없도록(private) 하고 메소드를 통하도록(setter/getter) 만드는 것이 더 안전하다.
3. 상속성(Inheritance)

   - 하나의 클래스가 가진 특징(함수, 데이터)을 다른 클래스가 그대로 물려받는 것  
     이때, 상속한 클래스는 상위 클래스 혹은 부모 클래스가 되고 상속받은 클래스는 하위 클래스 혹은 자식 클래스가 된다.
   - 코드의 재활용성이 높아지며 객체지향 방법의 중요한 기능 중 하나에 속한다.

4. 다형성(Polymorphism)
   - 같은 이름을 가진 객체나 메소드, 클래스 등이 여러 방식으로 접근하거나 정의될 수 있다.
   - 오버라이딩(Overriding), 오버로딩(Overloading)이 대표적이다.
     - 오버라이딩(Overriding)  
       자식 클래스에서 부모 클래스의 함수를 재정의하는 것
     - 오버로딩(Overloading)  
       같은 이름의 함수를 매개변수를 다르게 하여 여러 개 정의하여 사용하는 것  
       아주 대표적인 메서드 오버로딩으로는 print문이 있다. ex) print(String) / print(Int)...  
       작성 방법은 [이곳](https://steady-coding.tistory.com/446)을 참고하자.

각 특징에 대해서는 [실습자료 3,4,5]()를 확인하는 것이 더 좋다.

<br/>

### 객체지향의 장점

위의 특징으로 인한 객체지향 프로그래밍의 장점은 아래와 같다.

- 모듈화된 프로그래밍이 용이하다.
- 신뢰성이 높은 프로그래밍이 가능하다.
- 코드의 추가/수정/삭제가 용이하다.
- 코드의 재사용성이 높다.

이러한 장점을 적극적으로 활용하기 위해서는 아래의 5원칙을 대체적으로 지키는 것이 좋다.

<br/>

### 객체 지향 설계 5원칙

이름 그대로 객체 지향 프로그래밍 설계 방법 5가지를 의미한다, 5개 원칙의 머리글자를 따서 'SOLID' 라고도 한다.  
원칙을 지키면서 설계하면, 그 프로그램은 이해하기 쉽고 유지보수 하기 용이하며 논리적일 가능성이 높다.

#### 1. 단일 책임 원칙 (SRP - Single Responsibility Principle)

단일 책임 원칙은 하나의 클래스는 하나의 책임과 역할만 갖도록 한다는 것이다.  
쉽게 말하면 클래스의 추상화를 명확히 하여 기능을 명료하게 정하라는 의미이다.

이를 지키지 않게 되면 객체에 대한 설계를 잘 하지 못했다는 의미로  
어느 클래스에 어느 기능이 있는지 알 수 없어 유지보수가 어렵고 프로그램 분석이 어려워진다.

#### 2. 개방 폐쇄 원칙(OCP - Open-Closed Principle)

확장에는 열려 있어야 하고 변경에는 닫혀 있어야 한다.  
상속성을 활용하여 클래스 확장은 용이하게, 하지만 클래스의 캡슐화는 확실하게 하라는 의미이다.  
조금 더 간단하게 쓰면 상속이나 기능이 많아질 때마다 변경할 점이 너무 많은 코드는 지양하라는 것

개인적으로는 이해하기 가장 어려운 원칙인데, 가벼운 예시를 글로만 간단히 써보겠다.  
car라는 클래스를 만드는데 wheel은 필수적으로 필요한 변수이다.  
때문에 wheel 변수를 car에 넣겠지만 wheel은 3가지 종류가 있다.  
어떤 wheel이 와도 차는 move 기능을 원활히 수행할 수 있어야 하며 wheel 종류가 더 많아져도 car 클래스의 변경점은 없어야 한다.

여기서 wheel 종류가 많아진다고 car의 기능을 수정해야 한다면 추상화 혹은 캡슐화가 잘 되지 않을 것으로 볼 수도 있다.

#### 3. 리스코프 치환 원칙(LSP - Liskov Substitution Principle)

상위 타입의 객체를 하위 타입의 객체로 치환해도 상위 타입을 사용하는 프로그램은 정상적으로 동작해야 한다.  
여기서 상위 타입 객체는 부모 클래스, 하위 타입 객체는 자식 클래스를 의미하며  
상속성을 생각하면 당연한 원칙이기도 하다.

개인적으로는 어떻게 이 원칙이 깨질 수 있는지 궁금하다. 복잡한 객체를 사용한 경험이 없어서 인듯 하다.

#### 4. 인터페이스 분리 원칙(ISP - Interface Segregation Principle)

자신이 사용하지 않는 함수와 의존 관계를 맺지 않는다.  
쉽게 서술하면 기능들을 세분화하여 관리해서 사용하지 않는 기능을 가지지 않도록 해야한다는 의미이다.

간단히 예시를 들어보자면, move라는 클래스에는 fly와 drive라는 기능이 있다고 하자.  
그리고 비행기와 자동차 객체를 의미하는 airPlane 클래스와 car 클래스를 생성할 예정이다.  
airPlane 이라는 클래스를 만들 때, move라는 클래스를 상속받으면 활주로운행 기능과 비행기능을 쉽게 넣을 수 있다.  
또한, car 라는 클래스를 만들 때도 move의 drive 기능을 사용하면 편해보인다. 하지만!  
그대로 상속하면 자동차는 날 수 없기 때문에 fly라는 의미없는 기능이 추가되고 만다.

그러면 어떻게하면 될까?  
간단히 move라는 클래스를 사용하지 않고 fly와 drive 클래스를 따로 만들어서  
airPlane 클래스는 fly와 drive 클래스를 상속하도록 만들고 car 클래스는 drive 클래스만을 상속하도록 만들면 된다.

자연스럽게 기능별로 클래스나 인터페이스가 분리되어 상속이 많아지는 결과로 이어진다.  
이전에 객체지향이 상속의 상속의 상속... 이 겹겹이 쌓여 결국에는 복잡해지는 문제점이 생긴다는 글을 봤는데 이 원칙이 원인인 것 같다.

#### 5. 의존 역전 원칙(DIP - Dependency Inversion Principle)

고수준 모듈은 저수준 모듈의 구현에 의존해서는 안된다.  
모듈이 무엇인지 정확히 모르겠지만, 풀이해보면  
잘 바뀌지 않는 객체가 자주 바뀌는 객체를 참고하면 안 된다. 혹은 구체적인 객체가 추상적인 객체에 의존하면 안 된다. 라고 해석된다.

개방 폐쇄 원칙에서 사용하였던 예시와 유사하게 설명하겠다.  
car라는 클래스는 commnWheel이라는 클래스를 가진(의존한)다.  
겨울이 되어 car는 commnWheel 대신 snowWheel이라는 클래스로 바꾸고 싶어졌다.  
그러면 기존 commnWheel에 대한 코드에 snowWheel에 대한 코드를 추가해야 하는가? 하지만 그렇게 되면 개방 폐쇄 원칙에 위배된다.  
대신 wheel이라는 상위 추상 클래스를 만들어 commnWheel 과 snowWheel에게 상속하여 기본적인 내용을 구성하고  
car 클래스는 wheel이라는 클래스를 변수로 가지도록 만들면 commnWheel 과 snowWheel 어떤 것이 와도 문제가 없다.

의존 역전 원칙에 위배되면 필연적으로 개방 폐쇄 원칙도 위배되는 경우가 많아 의도치 않게 두 원칙의 예시가 같아졌다.  
해당 설명은 필자가 직접 위배한 경험이 있기 때문에 뼈 아프게 다가왔다.

<br/>

5가지 원칙에 대해서 정리를 간결하게 해보겠다.

단일 책임 원칙으로 객체의 역할과 기능을 분명히 하고  
개방 폐쇄 원칙으로 객체의 기능 확장에 추가적인 코드가 최소한이 되도록 하며  
리스코프 치환 원칙으로 자식 클래스는 상위 클래스에 대하여 호환성이 있어야 하며  
인터페이스 분리 원칙으로 클래스가 필요한 기능만을 가질 수 있도록 기능을 작게 나눠 관리하며  
의존 역전 원칙으로 객체 간의 관계 혹은 의존이 적절한지 살펴야 한다.

<br/>

5가지 원칙을 이해하는 대로 적어보았다.  
원칙들과 원칙을 지키지 않는 예시를 살펴보면서 객체지향에 대해서 더 많이 이해할 수 있었던 것 같다.  
그래도 이론을 먼저 보는 사람들이 보기에는 잘 와닿지 않을 것이다, 스스로 위배를 하면서 언칙을 생각하면 금방 이해할 것이라 생각한다.  
또한, **원칙을 지키는 것이 좋지만 객체지향이 모든 방면에서 모든 일을 완벽하게 적용시킬 수는 없는 것 또한 알게 되었다.**

<br/>

### 절차 지향 프로그래밍

객체 지향 프로그래밍은 절차 지향 프로그램과 많이 비교를 하는데 이를 위해 절차 지향 프로그래밍을 가볍게 살펴보겠다.

절차 지향 프로그래밍은 기능을 중점으로 두는 프로그래밍 방식이다. 즉, 어떤 기능을 어떤 순서로 처리하는가에 초점을 맞춘다.  
상대적으로 단순한 절차 지향 프로그래밍의 특징은 다음과 같다.

- 특징
  - 하나의 큰 기능을 처리하기 위해 작은 단위의 기능들로 나누어 처리하는 **Top-Down** 방식으로 설계한다.
  - 객체지향 프로그래밍과의 가장 큰 차이점으로 데이터와 함수를 별개로 취급한다.  
    단순히 객체를 사용하지 않는다고 생각하면 된다...
  - 비교적 작은 규모의 작업을 수행하는 함수(function)를 생성한다.
  - 인수(parameter)와 반환값(value)으로 명령을 전달하고 수행한다.
  - 특정 기능을 수행하려면 단순히 그 일을 해주는 메소드를 직접 호출하면 된다.

### 객체 지향 프로그래밍 vs 절차 지향 프로그래밍

| `객체 지향 프로그래밍`                                              | `절차 지향 프로그래밍`                                                                  |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 다양한 기능이 들어가는 대형 프로젝트에 적합하다.                    | 소형 프로젝트에 적합하다. 작은 기능을 객체별로 나눌면 오히려 복잡해질 수 있기 때문이다. |
| 유지보수가 쉽다. 문제가 되는 객체만 살펴보면 되기 때문이다.         | 유지보수가 어렵다.                                                                      |
| 상대적으로 사람이 이해하기 쉽게 객체로 구별이 되어 분석이 쉽다.     | 프로젝트가 크면 클수록 분석이 어렵다.                                                   |
| 객체를 계획하고 설계하기 위해서 초기에 들어가는 시간과 노력이 많다. | 단순히 일의 과정만을 순차적으로 구현하면 되기 때문에 초기 비용이 적다.                  |
| 처리속도가 느리다.                                                  | 처리속도가 빠르다.                                                                      |

객체 지향 프로그래밍과 반대되는 개념으로 생각하는 경우가 있지만 어디까지나 중점이 되는 개념이 다른 것 뿐이며  
객체 지향 또한 절차 지향과 같이 코드가 순차적으로 진행된다.  
개인적으로는 절차 지향으로 코딩을 하다가 너무 복잡해진 코드를 점점 감당하기 어려워져서  
사람이 조금 더 이해하기 쉬운 방식으로 프로그래밍 방식을 고안한 것이 객체지향으로 생각하고 있다.

#### 객체지향과 절차지향 도형 그리기 예제

한 블로그에서 도형 그리기 예시로 객체지향과 절차지향의 수행 방식의 차이를 보여주었는데 좋은 예시라고 생각해서 남긴다.

1. 절차 지향 프로그래밍 도형 그리기 함수
   - void drawLine(Position, Color);
   - void drawCircle(Position, Color);
   - void drawRectangle(Position, Color);
   - 위에 정의된 함수에 위치와 색상 인수를 전달해 원하는 도형 그리기를 실행한다.  
     ex) drawLine(PositionData, ColorData)
2. 객체 지향 프로그래밍에서의 객체 선언
   - "Shape" 인터페이스(interface) 선언
     - 속성 : Position, Color, Width, Style ...
     - 메소드 : draw(); move(); ...
   - "Shape" 인터페이스를 상속받은 "Line", "Circle", "Rectangle" 클래스 구현
   - 객체화된 인스턴스의 draw() 메소드를 호출해 각 인스턴스의 도형 그리기를 수행  
     ex) LineObject.draw()

<br/>

#### 참고

- [객체 지향](http://www.incodom.kr/%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5)
- [절차 지향](http://www.incodom.kr/%EC%A0%88%EC%B0%A8_%EC%A7%80%ED%96%A5)
- [다형성(Polymorphism)이란?](https://steady-coding.tistory.com/446)
- [객체지향 설계원칙 이해하기](https://western-sky.tistory.com/77)
- [단일 책임 원칙(SRP)이란?](https://steady-coding.tistory.com/370)
- [개방 폐쇄 원칙(OCP)이란?](https://steady-coding.tistory.com/378)

<br/>

## RESTful API

“REpresentational State Transfer” 의 약자인 REST에 ~ful 이라는 형용사형 어미를 붙여 이름이 만들어졌다.  
즉, REST의 기본 원칙을 잘 지킨 api를 RESTful API 이라고 부른다.

본격적으로 RESTful API를 설명하기 앞서 REST와 API에 대한 설명을 먼저 진행하고 하겠다.

### REST (REpresentational State Transfer)

월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식으로  
설계의 중심에 자원(Resource)이 있고 HTTP Method 를 통해 자원을 처리하도록 하는 설계(ROA - Resource Oriented Architecture)를 말한다.  
기본적으로 자원의 이름(자원의 표현)으로 처리 방식을 구분하여 해당 자원의 상태(정보)를 주고 받으며  
웹의 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있다.

#### REST 구성 요소

##### 1. 자원(Resource): URI

모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재한다.  
자원을 구별하는 ID는 ‘/groups/:group_id’와 같이 HTTP URI에 포함되어 사용될 수 있다.  
Client는 URI를 이용해서 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 Server에 요청한다.

##### 2. 행위(Verb): HTTP Method

HTTP 프로토콜의 Method를 사용한다.  
HTTP 프로토콜은 GET, POST, PUT, PATCH, DELETE 와 같은 메서드를 제공한다.

##### 3. 표현(Representation of Resource)

Client가 자원의 상태(정보)에 대한 조작을 요청하면 Server는 이에 적절한 응답(Representation)을 보낸다.  
REST에서 하나의 자원은 JSON, XML, TEXT, RSS 등 여러 형태의 데이터 형식으로 표현될 수 있다.  
JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.

즉, HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고  
HTTP Method(POST, GET, PUT, PATCH, DELETE)를 통해 해당 자원을 처리(CRUD Operation)하는 것을 의미한다.

- CRUD Operation
  - Create : 생성(POST)
  - Read : 조회(GET)
  - Update : 수정(PUT, PATCH)
  - Delete : 삭제(DELETE)
  - HEAD: header 정보 조회(HEAD)

<br/>

### REST 특징

#### 1. Server-Client (서버-클라이언트 구조)

자원(정보)을 가지고 있는 쪽이 서버(Server), 자원을 요청하는 쪽이 클라이언트(Client)가 되어  
서로의 역할을 분명히 하고 의존성을 낮춘다.

- Server: API를 제공하며 데이터 처리와 저장을 책임진다.
- Client: 사용자 인증이나 context(세션, 로그인 정보) 등을 직접 관리하고 책임진다.  
  (라는데.. 세션은 서버에 저장되며 쿠키가 클라이언트에 저장되는 것으로 알고 있고  
  로그인 정보도 클라이언트에서 가지고 있으면 보안 상의 문제가 되는 것으로 안다.  
  내가.. 잘못 알고 있는 걸까?)

#### 2. Stateless (무상태성)

HTTP 프로토콜은 Stateless Protocol이므로 REST 역시 무상태성을 갖는다.  
서버는 작업을 위한 상태정보를 따로 저장하거나 관리하지 않고 클라이언트의 요청만을 단순 처리한다는 것이다.  
서버의 처리 방식에 일관성을 부여하고 부담이 줄어들며, 서비스의 자유도가 높아진다.

- 무상태성이란 요청한 클라이언트와 연결을 유지하지 않으며, 클라이언트의 정보를 저장하지 않는다는 의미이다.

#### 3. Cacheable (캐시 가능)

웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기본적인 기능을 그대로 활용할 수 있다.  
즉, HTTP가 가진 가장 강력한 특징 중 하나인 캐싱 기능을 적용하여 전체 응답시간, 성능, 서버의 자원 이용률을 향상시킬 수 있다.

#### 4. Layered System (계층형 구조)

REST 서버는 다중 계층으로 구성될 수 있다.  
서버는 기본적으로 자원을 처리하면서도,  
앞단에 보안, 로드밸런싱, 암호화, 사용자 인증, 공유 캐시 등을 추가하여 확장성과 보안성을 향상시킬 수 있다.  
PROXY, 게이트웨이 같은 네트워크 기반의 중간 매체를 사용할 수 있다.

#### 5. Uniform Interface(인터페이스 일관성)

URI로 지정한 자원에 대한 조작을 통일되고 한정적인 인터페이스로 수행한다.  
HTTP 표준 프로토콜이 적용 가능한 모든 플랫폼에서 사용이 가능하여 특정 언어나 기술에 종속되지 않는다.  
때문에 한 번 사용한 경험이 있다면 다른 플렛폼과 언어에서도 구조를 빠르게 파악하고 쉽게 적용시킬 수 있다.

#### 6. Self-descriptiveness (자체 표현 구조)

REST API 메시지만 보고도 이를 쉽게 이해 할 수 있는 자체 표현 구조로 되어 있다는 것 이다.  
이는 'REST 구성 요소'와'REST API 설계 규칙'을 보면 확실하게 와 닿는다.

정리하자면  
**REST는 플렛폼과 언어가 다른 클라이언트라도 HTTP 프로토콜이 적용 가능하다면,  
표현이 쉽고 일관된 클라이언트의 요청과 서버의 응답에 따라 빠르고 안전한 통신을 쉽게 구현할 수 있는 구조(아키텍쳐)를 제시한다.**

<br/>

### API - Application Programming Interface

    응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.
    -wikipedia-

api는 여러곳에서 쓰고 있기 때문에 기본적으로는 위의 정의가 더 정확하나,  
RESTful API에서의 api는 '애플리케이션 소프트웨어를 구축하고 통합하기 위한 정의 및 프로토콜 세트'라고 생각하면 된다.  
여기서 '애플리케이션 소프트웨어'는 PC 앱도, 웹도, 핸드폰 앱도 될 수 있으며  
'프로토콜'은 카메라나 진동 센서 같은 기능에 관한 것일수도, 통신을 위한 것일 수도 있다.

즉, 프로그래밍할 때, 일관적인 결과를 얻을 수 있도록 큰 틀이나 기둥(인터페이스)을 만들어주는 역할을 한다.

<br/>

여기서 나는 아키텍쳐와 인터페이스를 햇갈려했는데 아키텍쳐는 설계도, 인터페이스는 실재가 있는 기둥으로 생각하였다.
설계도는 실재로 구현된 것이 없어서 바꾸고 싶다면 지우개로 지우고 다시 그리면 되지만...  
기둥은 한 번 만들고 바꾸려면 위층(자식 클래스)을 다 부수어야 한다. 물론 일단 부수고 윗층이 가라 앉는 것(뻐-그)을 구경해도 된다. ^ㅠ^

<br/>

### REST API 설계 규칙

기본적으로 REST의 설계와 특징을 기본 전제로 가지며 이를 기준으로 규칙을 상세히 정리하겠다.
대표적이고도 기본적인 규칙은 2가지로 아래와 같다.

- 도큐먼트 : 객체 인스턴스나 문서들의 집합
- 컬렉션 : 서버에서 관리하는 디렉터리(파일) 리소스(자원)
- 스토어 : 클라이언트에서 관리하는 리소스 저장소

1. URI는 정보의 자원을 표현해야 한다.

   - 리소스(resource 혹은 자원)는 동사보다는 명사를, 대문자보다는 소문자를 사용한다.
     Ex) GET /GetMembers/1 -> GET /members/1
   - 리소스의 도큐먼트 이름으로는 단수 명사를 사용해야 한다.
   - 리소스의 컬렉션 이름으로는 복수 명사를 사용해야 한다.
   - 리소스의 스토어 이름으로는 복수 명사를 사용해야 한다.
     Ex) GET /member/1 -> GET /members/1

2. 리소스에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.
   - URI에 HTTP Method가 들어가면 안된다.  
     Ex) GET /members/delete/1 -> DELETE /members/1  
     Ex) GET /members/insert/2 -> POST /members/2
   - URI에 행위에 대한 동사 표현이 들어가면 안된다.  
     즉, CRUD 기능을 나타내는 것은 URI에 사용하지 않는다.  
     Ex) GET /members/show/1 -> GET /members/1  
     Ex) GET /members/insert/2 -> POST /members/2
   - URL의 모든 단어는 유일한 식별자(대표적으로 id)만이 들어간다.  
     URI가 다르다는 것은 처리할 자원이 다르거나 처리 방법이 다르다는 의미이고 리소스가 다르면 URL도 다르다.
     Ex) student를 생성하는 route: POST /students  
     Ex) id=12인 student를 삭제하는 route: DELETE /students/12

<br/>

#### 유의사항

RESTful 한 설계를 돕고 가독성을 높여주는 사항을 기술하겠다.

1. 슬래시 구분자(/)는 계층 관계를 나타내는 데 사용한다.
   - '경기도 고양시 덕양구'라고 쓸 것을 '덕양구 고양시 경기도'라고 쓰지 말자.
   - http://restapi.example.com/houses/apartments
   - http://restapi.example.com/animals/mammals/whales
2. URI 마지막 문자로 슬래시(/)를 포함하지 않는다.

   - http://restapi.example.com/houses/apartments/ (X)  
     http://restapi.example.com/houses/apartments (0)

3. 가독성을 위하여 하이픈(-)을 권장하며 밑줄(\_)은 지양한다.

   - 불가피하게 긴 URI경로를 사용하게 된다면 가독성과 원활한 해석을 위해 하이픈을 사용하는 것을 권장한다.
   - 일반적으로 밑줄은 보기 어렵거나 문자가 가려지는 경우가 있기도 하므로 사용을 지양한다.

4. URI 경로에는 소문자가 적합하다.
   - URI 경로는 대소문자에 따라 다른 리소스로 인식하게 되기 때문에 대문자 사용은 피한다.
   - RFC 3986(URI 문법 형식)은 URI 스키마와 호스트를 제외하고는 대소문자를 구별하도록 규정하기 때문이다.
     - RFC 3986 : the URI (Unified Resource Identifier) Syntax document
5. 파일 확장자는 URI에 포함시키지 않는다.

   - REST API에서는 바디(body) 메시지의 형식은 URI 안에 포함시키지 않고 Accept header를 사용하여 저장한다.
   - http://restapi.example.com/members/soccer/345/photo.jpg (X)  
     GET /members/soccer/345/photo HTTP/1.1 Host: restapi.example.com Accept: image/jpg (0)

6. 리소스 간에는 연관 관계가 있는 경우
   - 일반적으로 URL에 동사를 사용하지 않지만 리소스 간의 관계를 보여주기 위해서 쓰기도 한다.  
     해당 부분은 서버와 클라이언트의 협의로 구성되는 부분이 많으므로 꼭 혼자 만들지 말자.
   - GET : /users/{userid}/devices (일반적으로 소유 ‘has’의 관계를 표현할 때)
   - GET : /users/{userid}/likes/devices (관계명이 애매하거나 구체적 표현이 필요할 때)

<br/>

#### HTTP 응답 상태 코드

대표적인 상태코드만 표로 정리한 것이다.

| 상태코드               | 내용                                                                                                                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 2XX                    | 서버가 클라이언트의 요청을 성공적으로 처리하였다.                                                                                              |
| 200 OK                 | 클라이언트의 요청을 정상적으로 수행하였다.                                                                                                     |
| 201 Created            | 클라이언트가 어떠한 리소스 생성을 요청하였고 해당 리소스가 성공적으로 생성되었다. (POST를 통한 리소스 생성 작업 시)                            |
| 204 No Content         | 클라이언트의 요청은 정상적이다. 하지만 컨텐츠를 제공하지 않는다. (일반적으로 PUT이나 PATCH, DELETE로 리소스 처리 시)                           |
| 4XX                    | 클라이언트의 요청이 유효하지 않아 서버가 해당 요청을 수행하지 못했다.                                                                          |
| 400 Bad Request        | 클라이언트의 요청이 유효하지 않아 작업을 진행하지 못했다.                                                                                      |
| 401 Unauthorized       | 클라이언트가 권한이 없기 때문에 작업을 진행하지 못했다. (로그인 하지 않은 유저가 로그인 했을 때, 요청 가능한 리소스를 요청했을 때)             |
| 403 Forbidden          | 클라이언트가 권한이 없기 때문에 작업을 진행할 수 없는 경우 (403 메시지는 리소스가 존재한다는 의미를 내포하므로 400이나 404를 사용할 것을 권고) |
| 404 Not Found          | 클라이언트가 요청한 자원(혹은 경로)이 존재하지 않는다.                                                                                         |
| 405 Method Not Allowed | 클라이언트가 요청한 리소스에서는 사용 불가능한 Method를 사용하였다.                                                                            |
| 301 Moved Permanently  | 클라이언트가 요청한 리소스에 대한 URI가 변경된 경우 (응답 시 Location header에 변경된 URI를 보내준다.)                                         |
| 5XX Server errors      | 서버 오류로 인해 요청을 수행할 수 없다.                                                                                                        |

#### 참고

- [[Network] REST란? REST API란? RESTful이란?](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)
- [REST API 제대로 알고 사용하기](https://meetup.toast.com/posts/92)
- [REST API 관점에서 바라보는 HTTP 상태 코드(HTTP status code)](https://sanghaklee.tistory.com/61)

<br/>

## MVC(Model-View-Controller) 패턴

디자인 패턴이란, 소프트웨어 설계에서 자주 발생하는 문제들을 피하기 위해 사용되는 형식이나 방법을 말한다.  
디자인 패턴 중 MVC 패턴은 다양한 플렛폼에서 기본적으로 쓰이는 패턴 중 하나이기 때문에 해당 카테고리에 넣었다.

이름 그대로 Model, View, Controller 세 가지 형태로 역할을 나누어 개발하는 방법론이다.

### 구성

- Model : 데이터를 저장하고 관리하는 역할, DB와 상호작용 하기도 한다.
- View : 사용자에게 다양한 정보(모델의 데이터)를 표시해주는 역할
- Controller : 뷰를 통하여 사용자 입력을 받아 작업을 수행하는 역할

<br/>

#### 주의점

MVC 패턴을 검색하면 나오는 블로그의 정리된 글들과 사진을 보면  
컨트롤러가 직접 사용자의 입력을 받는 내용이 있는데 필자는 상당히 혼란스러웠다.  
_(아니, 앱이나 웹이나 뷰를 통해서 UI를 처리할텐데 어떻게 사용자 입력이 컨트롤러로 직접가지????)_

알고보니 사용자 입력이 컨트롤러로 직접 전송되는 프로그램들(아마도 서버..?)에 맞춘 내용을 읽은 것 뿐이며  
사용자 입력이 뷰에서 전송되든, 컨트롤러로 직접 입력되든 MVC패턴에 대한 이야기라는 것을 알았다.  
이 글을 읽는 사람들은 필자처럼 햇갈리지 않기를 희망하는 마음으로 도움이 되는 사진을 남기겠다.

<img src="../image/1.6%20MVC1.png" width="70%" height="70%">

왼쪽 - 사용자 입력을 컨트롤러가 직접 받는다.  
오른쪽 - 사용자 입력이 뷰를 통해서 컨트롤러로 전송된다.  
하지만 둘 모두 MVC 패턴이 맞다.

<br/>

### 동작 순서

1. 사용자 입력이 Controller에 들어온다.
2. Controller는 사용자의 입력에 맞게 Model에게 작업을 요청한다.
3. Model이 작업을 완료한 후 결과물을 Controller에게 반환한다.
4. Controller는 Model의 결과물을 표시할 View를 선택한다.
5. View는 Model의 결과물을 화면에 표시한다.
   - 방법1 : View가 Model을 직접 이용하여 업데이트 하는 방법
   - 방법2 : Model에서 View를 호출(Notify)하여 업데이트 하는 방법
   - 방법3 : View가 주기적으로 Model의 변경을 감지(Polling)하여 업데이트 하는 방법

### 특징

- 가장 단순하고 직관적인 디자인 패턴이다.
- 컨트롤러는 여러 개의 뷰를 선택할 수 있는 1:n의 구조이다.
- 컨트롤러는 뷰와 모델사이에서 중개인 역할을 한다.
  - 컨트롤러에게 너무 많은 작업이 몰릴수록 유지보수가 어려워질 수 있다. (이미지 참고)
- 뷰와 모델은 의존성이 없다.
  - 만일 의존성이 있는 코드를 작성해다면, 이 또한 유지보수가 어려워진다.

<br/>

<img src="../image/1.6%20MVC2.png" width="60%" height="60%">

<br/>

#### 참고

- [[IT 기술면접 준비자료] MVC패턴과 모델1, 모델2](https://preamtree.tistory.com/11)
- [[아키텍처 패턴] MVC 패턴이란?](https://medium.com/@jang.wangsu/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4-mvc-%ED%8C%A8%ED%84%B4%EC%9D%B4%EB%9E%80-1d74fac6e256)
- [디자인 패턴 MVC, MVVM 비교](https://donggyu9410.medium.com/%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-mvc-mvvm-%EB%B9%84%EA%B5%90-1a4e6c1c860a)
- [MVC Explained in 4 Minutes (유튜브 동영상)](https://www.youtube.com/watch?v=DUg2SWWK18I&ab_channel=WebDevSimplified)  
  서버 기준으로 클라이언트로부터 요청을 받았을 때 MVC패턴 흐름을 설명하는 동영상이다.  
  한글번역은 없지만 쉬운 영어로 되어있으며 예시도 자세하게 설명하여 볼만 하다.

<br/>

## 함수형 프로그래밍

주어진 인수들을 사용하여 결과값을 일관적으로 반환하는 프로그래밍을 의미한다.  
이름이 `함수형` 이라고 붙인 것도 중/고등학교에서 배운 f(x) = y와같은 함수와 같은 특징을 가지기 때문이다.

관련 내용 : 스코프, call-by-name, 모나드

## High-order functions (고차함수)

## First-class function (일급함수)

간단히는 다른 함수의 매개변수로 넣어줄 수 있는 함수를 의미한다.  
프로그래밍 언어가 함수를 일급시민으로 대우한다면 일급 함수를 가진다고 말한다.

### 참고

- (함수형 프로그래밍이 뭔가요?)[https://www.youtube.com/watch?v=jVG5jvOzu9Y&ab_channel=%EC%96%84%ED%8C%8D%ED%95%9C%EC%BD%94%EB%94%A9%EC%82%AC%EC%A0%84]

## VCS(Version Control System)

컴퓨터에 있는 대부분의 파일들을 저장하여 버전관리를 돕는 시스템을 말한다.  
이러한 시스템이 없었을 때에는 폴더별로 이름에 버전을 붙여서 수동으로 관리했다고 한다...  
(최종.zip, 마지막 최종.zip, 진짜 마지막 최종.zip...)

크게 2가지 형식의 VCS가 있는데 아래와 같다.

- Centralized Version Control

  - 서버에 파일을 업로드하고 버전을 관리하는 방식
  - 각 개발자들이 서버의 파일을 업데이트하며 즉시 동기화가 된다.
  - 네트워크를 통해 서버에 접속해야만하기 때문에 네트워크나 서버에 문제가 있으면 작업을 못한다.
  - CVS, SubVersion, Perferce 등이 해당된다.

- Distributed Version Control
  - 각 개발자들이 개별적으로 버전관리(로컬 저장소)를 진행하고 원할때 서버와 버전 동기화를 진행해주는 방식
  - 즉시 동기화가 되지는 않지만 오프라인 환경에서도 사용 가능하며 서버가 다운되도 안전하다.
  - Git, Mercurial, Darce 등이 해당된다.
  - 대표적인 클라우드 서버로 GitHub와 BitBucket가 있다.

### Git

현재 가장 유명하고도 대표적인 VCS 중 하나이다.  
Git의 특징을 나열해보면 다음과 같다.

- 대표적인 무료 VCS
  - 사용하는 사람이 많으면 사용법이나 해결책을 찾기 쉽다.
- 오픈소스
- 스냅샷(Snapshot) 기술을 활용하여 다른 VCS에 비해 빠르고 가벼움
  - 스냅샷(Snapshot)  
    마치 사진 찍듯이 특정 시점에 스토리지의 파일 시스템을 포착해 보관하는 기술  
    변경점이 있는 파일만을 그때마다 정리하고 변경점이 없는 파일은 이전의 링크를 그대로 가져와 파일 관리속도를 크게 향상시켰다.  
    깃에서는 스냅샷 데이터를 기반으로 고유한 해시코드를 부여하고 버전정보를 빠르게 참조할 수 있도록 한다.
- 오프라인 환경에서도 작동
- 되돌리기(Undo) 기능
- branchd와 merge를 활용한 쉽고 빠른 협업

#### 참고

- [깃, 깃허브 이건 알고 사용하자](https://www.youtube.com/watch?v=lPrxhA4PLoA&t=0s&ab_channel=%EB%93%9C%EB%A6%BC%EC%BD%94%EB%94%A9by%EC%97%98%EB%A6%AC)
- [깃, 깃허브 제대로 배우기 (기본 마스터편, 실무에서 꿀리지 말자)](https://www.youtube.com/watch?v=Z9dvM7qgN9s&ab_channel=%EB%93%9C%EB%A6%BC%EC%BD%94%EB%94%A9by%EC%97%98%EB%A6%AC)
- [누구나 쉽게 이해할 수 있는 Git](https://backlog.com/git-tutorial/kr/)
- [git 공식홈페이지](https://git-scm.com/book/en/v2)

#### Git WorkFlow

깃을 사용하기 위해서는 파일 상태와 저장소(레포지토리)에 대한 용어를 알고 넘어가는 것이 좋다고 생각하여  
깃 작업 흐름에 따라서 간단하게 해당 용어들을 설명하는

- Working Directory : 프로젝트를 작업하고 파일들을 수정하는 장소
  - Untracked : 깃에 저장된 적이 없는 파일 상태를 의미, 보통 새로운 파일을 만든경우의 파일 상태이다.
  - Tracked : 깃에 이미 저장된 적이 있는 파일 상태를 의미
    - Unmodified : tracked 상태의 파일이 특별한 변경점이 없는 상태
    - Modified : tracked 상태의 파일이 수정되었을 때의 상태
    - Deleted : tracked 상태의 파일이 삭제되었을 때의 상태
  - .gitignore  
    로컬 환경의 정보나 빌드 정보 등 저장소에서 관리할 필요가 없는 파일들을 track하지 않도록 설정하는 파일
- Staging Area  
  버전 히스토리(이력)에 저장할 준비가 되어있는 파일들이 있는 영역  
  변경점이 없는 파일은 스냅샷을 할 이유가 없기 때문에, Modified 상태의 파일들만 이 영역으로 들어올 수 있다.
- Local Repository (로컬 저장소)  
  버전 히스토리를 저장하고 관리하는 개인 컴퓨터 내의 저장소  
  commit 명령어를 통해서 Staging Area의 파일들을 로컬 저장소에 저장할 수 있다.
- Remote Repository (원격 저장소)  
  버전 히스토리를 저장하고 관리하는 서버의 저장소  
  push 명령어를 통해서 로컬 저장소의 히스토리를 원격 저장소로 업로드할 수 있다.  
  반대로 pull 명령어를 이용하여 원격 저장소의 히스토리를 로컬 저장소로 다운로드할 수 있다.

#### Git 명령어

Git을 실재로 사용하기 위해서는 다양한 명령어들을 숙지할 필요가 있다. (터미널 명령어들을 알고있다면 조금 더 쉽다.)  
하지만 모든 명령어를 적어놓기에는 너무 많고 가장 자주 쓰이는 명령어들을 위주로 설명을 적어 놓겠다.  
더 많은 명령어들을 확인하기 위해서는 [Documentation - Git SCM](https://git-scm.com/docs)을 확인바란다.

Git은 기본적으로 'git command [-option]' 의 형식을 가진다.  
command에는 add, status, config 등의 명령어가 필수적으로 입력되고  
option에는 command에 맞는 옵션들이 선택사항으로 들어갈 수 있다.

- git --version  
  git이 설치되어있는지 확인하기 위해서 가장 자주 쓰이는, 깃 버전 확인 명령어
- git config --global alias.[지정명령어] [명령어] (ex. git config --global alias.st status)  
  명령어(status) 대신 지정한 명령어(st)를 적어도 컴퓨터가 해당 명령어(status)로 인식한다.
- git [명령어] --h  
  명령어에 대한 옵션들을 간단하게 확인할 수 있다.
- git status  
  현재 작업 브랜치(branch), pull 할 로컬 저장소의 commit의 수, untracked/tracked 파일 등  
  버전 관리에 대해 작업 중인 파일과 저장소 상태를 간단히 볼 수 있다.
  - git status -s  
    위의 명령어보다 더 간결한 형태로 작업 상황을 볼 수 있다.
- git add [파일명]  
  파일이 untracked나 modified 상태라면 Staging Area 영역으로 옮겨준다.
  - git add _ , git add _.css 등..  
    현재 파일 내의 **존재하는** 지정한 파일들을 모두 Staging Area로 옮긴다.
  - git add .  
    현재 파일 내의 모든 파일과 **deleted된 파일을 까지** 모두 Staging Area로 옮긴다.
    - 'git add -A' 'git add .' 'git add -u' 등 다양한 옵션이 있지만 개인적으로 'git add .'을 가장 많이 썼다.  
       버전마다 조금씩 기능에 차이가 있는데 [스택오버플로](https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add)를 참고하자.
- git diff  
  현재 파일 내용과 staging된 파일 내용을 비교한다.
  - gif diff --staged  
    staging된 파일 내용과 최근 commit의 파일 내용을 비교한다.
- git commit  
  staged된 파일들을 레포지토리로 옮겨준다.
  - git commit -m "메시지"  
    "메시지"를 타이틀로하는 commit을 실행한다.
  - git commit -a -m "메시지" , git commit -am "메시지"  
    git add -a과 git commit -m "메시지"를 모두 실행시킨 것과 같다.
- git log  
  깃 커밋에 대한 로그를 확인한다.
  - git log --oneline  
    깃 커밋에 대한 로그를 한 줄로 간단히 확인한다.
  - git log --all
    깃 커밋에 대한 모든 브랜치의 로그를 확인한다.
  - git log --graph
    깃 커밋에 대한 로그를 간단한 UI를 통해 확인한다.
- git push origin 브랜치명

#### Git branch

- 각자 독립적인 작업 영역(저장소) 안에서 여러 개발자들이 동시에 다양한 작업을 할 수 있게 만들어 주는 기능

각 브랜치마다 고유한 역할을 두어 사용하는데 개발시에 공통적으로 사용하는 브랜치는 아래와 같다.

- master  
  배포에 사용하는 브랜치, 사용자에게 직접 영향이 가는 브랜치이기 때문에 신중하게 커밋해야 한다.
- develop
- feature

git branch 명령어

- git branch  
  브랜치 목록을 확인한다.
- git branch 브랜치명  
  새로운 브랜치를 생성한다.
  - git branch -d 브랜치명  
    해당 브랜치를 삭제한다, 단 브랜치는 병합(merge)되어 있어야 가능하다.
  - git branch -D 브랜치명  
    해당 브랜치를 강제 삭제한다.
- git switch 브랜치명  
  다른 브랜치로 이동한다.
  - git switch -c 브랜치명  
    브랜치를 생성과 동시에 이동한다.

참고로 이전에는 checkout이라는 명령어를 사용하였으나 switch, restore 등으로 명령어가 최근(2022년 7월 기준) 나뉘었다고 한다.

#### git merge

- git merge 브랜치명  
  해당 브랜치 부모 브랜치와 병합한다, merge 하기 전에 부모 브랜치로 이동한 후 명령 가능하다.

병합에는 3 종류가 있는데 아래와 같다.

- fast-forward  
  단순히 병합할 브랜치가 부모 브랜치의 최신 커밋 직후인 상태이고 이것을 병합한다면 부모 브랜치는 단순히 커밋을 한 번 한것과 같은 상황인데 이러한 상황을 의미한다. 병합으로 인한 새로운 버전이 생기지 않는다는 것이 특징이다.
- 3-way merge (merge commit)  
  부모 브랜치와 자식 브랜치의 최신 공통 커밋, 부모 브랜치의 최신 커밋, 자식 브랜치의 최신 커밋 3가지를 기준으로 병합하는 특징으로 위와 같은 이름이 붙였다.
  병합 후 커밋이 생기는 특징이 있다.
- merge conflict  
  병합할 두 브랜치의 같은 파일의 같은 내용을 수정하면 동시에 수정한 경우 git은 해당 부분을 자동으로 merge하지 못해서(conflict) 생기는 상황, 같은 파일이라도 다른 내용일 수정하면 merge commit 이 된다.
  - Vim
    충돌 후 머지할 때 사용하는, 리눅스에서 자주 사용되는 택스트 에디터  
    입력모드와 명령모드가 있는데 esc를 눌러 `:wq`(저장후 종료)를 해주면 기본 내용으로 충돌에 대한 새 커밋이 자동으로 생성된다.

### Git Strategy

깃을 활용하여 버전 관리를 어떻게 해야할지에 대하여 다양한 전략(strategy)들이 존재한다.  
기본적으로는 버전 관리를 위하여 적당한 수준의 기능별로 커밋을 진행해 나간다.

해당 부분은 필자가 제대로 사용해본 경험이 없어서 정리를 늦게 진행할 예정이다.

## Package와 Import

### Package

PC가 파일을 관리하기 위해서 폴더를 사용하는 것처럼 클래스를 관리하기 위해서 패키지를 사용한다. 패키지는 .으로 계층적인 구조를 취하지만 기본적으로는 클래스 파일을 담고있는 폴더들이다.

package 선언은 아래와 같이 한다.  
package package_name;

모든 클래스는 반드시 하나의 패키지에 속해야 하며 주석과 공백을 제외한 첫 문장에 하나의 패키지를 작성해주어야 한다.  
생략하면 default package라고 하는데 바탕화면과 같은 위치라 사용하지 않는 것이 일반적이라고 한다.

소속.프로젝트.용도 로 패키지명을 정하는 것이 일반적이다.  
com.ssa . day . extend 같은 실습명들이 그 예시이다.

### Import

다른 패키지에 선언된 클래스를 사용하기 위한 키워드  
패키지와 클래스 선언 사이에 위치하며 여러개 선언이 가능하다.

선언은 아래와 같이 한다.
import 패키지명.class명  
import 패키지명.\* (해당 패키지의 모든 클래스를 대상으로 import, 하위 패키지는 제외한다.)

임포트한 패키지의 클래스명이 동일하여 명확히 해야할 때는  
java.util.List list = new java.util.ArrayList();  
라고 작성하기도 한다.

임포트를 하지 않아도 기본적으로 추가되는 패키지가 하나 있다.  
java.lang.\*

## CI/CD

지속적인 통합(Continuous Integration)과 Continuous Delivery(지속적인 서비스제공) 혹은 Continuous Deployment(지속적인 배포)의 약자.

애플리케이션 개발 단계를 자동화하여 개발 주기를 보다 짧게, 서비스를 고객에게 빠르게 제공하는 방법으로 새로운 코드 통합으로 인해 개발 및 운영팀에서 발생하는 일명 통합지옥(Integration hell)을 해결하는 솔루션 중 하나이다.

CI/CD은 애플리케이션 통합, 테스트, 제공, 배포 과정을 가지는 라이프사이클 전체에 걸쳐서 지속적인 자동화와 모니터링을 제공하는데 이러한 구축사례를 CI/CD 파이프라인이라고 부른다.

이러한 CI/CD 툴로 실무에서 가장 널리 쓰이는 Jenkins를 Doker로 설치하고 사용하는 시간을 가졌는데..
설치때문에 머리가 아프다.. 설치하고 다시 작성하겠다;

추가로 공부할 리스트

- 소켓
- MVP(디자인패턴 말고)
- ISP(인터넷 서비스 제공자(Internet service provider; ISP) 말고!)
- 어플리케이션 서비스, 인프라(AWS EC2, Ubuntu, bublic Net, MiddleWare)
