# 2-1. Kotlin

+ JVM과 GC 원리
+ Collection
+ Mutable vs Immutable
+ Annotation
+ Generic
+ final keyword
+ KeyWords
+ Overriding vs Overloading
+ Visibility Modifier (Access Modifier in Java)

> JetBrain에서 공식적으로 만든 [프로그래밍 학습 사이트 Hyperskill](https://hyperskill.org/knowledge-map/361?track=18)를 찾았다. 현재 몇 가지 강의를 확인 중에 있다.
> 기대 이하이다, 아무리 초심자를 대상으로 했다지만 너무 쉽다. 정말 최소 한도의 정보만 알려주고 진행하는 방식에 서양권 특유의 정의 방식이 이해하기 난해하게 만든다.

## Kotlin 개요

모바일, 서버 측 및 데스크톱 애플리케이션을 개발하는 개발자들이 사용하는 언어로 JetBrains에서 개발하였다.   
2016년 첫 번째 공식 버전이 출시되고 Google I/O 2017 컨퍼런스에서 Google이 Android에서 Kotlin에 대한 최고 수준의 지원을 발표했다.   
때문에 현재 코틀린은 안드로이드에서 특히 많이 쓰인다.

자바와 완전호환을 내세우며 등장하였으며 자바와 견주어도 괜찮은 성능과 사용자 편의성으로 사용자들을 대거 유입하였다.   
안드로이드 공식 홈페이지에서도 오랫동안 사용했던 Java보다 Kotlin을 장려를 하고있다.

</br>

### Kotlin 특징

1. 자바와의 완전 호환   
  이미 광범위한 곳에 쓰이고 있는 자바와 호환이 된다는 것은 큰 장점이다.   
  즉, 이미 존재하는 자바 라이브러리를 그대로 이용할 수 있다는 의미이다.

2. 다중 플렛폼 언어   
  JVM, Android, JS, 다양한 PC OS 에서 작동이 가능하다.   
  때문에 안드로이드 앱부터 웹개발까지 가능하다.
  
3. 다양한 프로그래밍 패러다임 지원   
  명령형 프로그래밍, 객체 지향 프로그래밍, 일반 프로그래밍, 함수형 프로그래밍 등 여러 프로그래밍 패러다임을 지원한다.
  
4. 정적 타입 언어   
  기본적으로 컴파일 시 변수의 자료형(Type)이 결정된다.   
  자료형을 명시하지 않아도 자료형 추론이 가능하며 스마트 캐스트 기능까지 갖고 있다.

5. Null Safety  
  널이 가능한 자료형(Nullable Type)과 불가능한 자료형(Non-Null Type)을 구분한다.   
  두 자료형은 따로 명시하며 null이 불가능한 자료형은 따로 null check가 들어가지 않는다.
  
이밖에도...   
코루틴(Coroutine), 간결성(Concise), 확장함수(Extension Functions) 등등 많은 특징을 가진다.

참고: https://velog.io/@beargu2/Kotlin-%ED%8A%B9%EC%A7%95

</br>

## JVM과 GC 원리



</br>

## Collection
