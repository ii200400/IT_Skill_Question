# 2-1. Kotlin

+ Iterable
+ Collection
+ Mutable vs Immutable
+ Annotation
+ Generic
+ final keyword
+ KeyWords
+ Overriding vs Overloading
+ Visibility Modifier (Access Modifier in Java)
+ JVM과 GC 원리

> 정리하고 싶은 내용들을 목차로 적어놓은 것이며 아직 대부분의 내용을 정리하지는 못했다.

## Kotlin 개요

모바일, 서버 측 및 데스크톱 애플리케이션을 개발하는 개발자들이 사용하는 언어로 JetBrains에서 개발하였다.   
2016년 첫 번째 공식 버전이 출시되고 Google I/O 2017 컨퍼런스에서 Google이 Android에서 Kotlin에 대한 최고 수준의 지원을 발표했다.   
때문에 현재 코틀린은 안드로이드에서 특히 많이 쓰인다.

자바와 완전호환을 내세우며 등장하였으며 자바와 견주어도 괜찮은 성능과 사용자 편의성으로 사용자들을 대거 유입하였다.   
안드로이드 공식 홈페이지에서도 오랫동안 사용했던 Java보다 Kotlin을 장려를 하고있다.

자바의 구조와 기능들을 갖추고있어 자바 카테고리로 만들까도 생각하였지만,   
대부분의 특징은 같아도 엄연히 다른 언어이고 코틀린만의 특징도 있기 때문에   
자바와 겹치는 내용이 많을 것을 알면서도 코틀린 카테고리로 만들어 정리를 하게 되었다.

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

## Iterator

컬렉션(Collection)이나 순차적인 데이터를 가지고 있는 자료형의 데이터를 순서대로 접근하기 위해 사용하는 코틀린의 표준 라이브러리 중 하나이다.   
자료형의 모든 데이터를 하나씩 불러올 때 자주 사용되며 Iterable<T> 인터페이스를 상속한 자료형이라면 Iterator를 호출하여 구현할 수 있다.

Iterator는 다양한 자료형에 상속되어있는데 아래의 그림과 같다.
  
<img src="../image/2.1%20Iterator1.png" width="50%" height="50%">

  
<br/>
  
Iterator에는 Iterator.next와 Iterator.hasNext. 단 2개의 함수만 있다.   
Iterator.hasNext은 다음 데이터가 존재하는지 확인하여 true/false(Boolean)를 반환하는 함수이고   
Iterator.next는 다음 데이터를 탐색하고 해당 데이터를 반환하는 함수이다. 

위의 두 함수를 사용하여 모든 데이터를 살펴볼 수 있는데 다음과 같다.
  
    val numbers = listOf("one", "two", "three", "four")
    val numbersIterator = numbers.iterator()
    while (numbersIterator.hasNext()) {
        println(numbersIterator.next())
    }
    ----------
    one
    two
    three
    four

또 다른 방법으로도 위의 결과를 확인할 수 있는데 아마 다들 사용해본 경험이 있는 for문이다.

    val numbers = listOf("one", "two", "three", "four")
    for (item in numbers) {
        println(item)
    }
    ----------
    one
    two
    three
    four
  
forEach문 또한 같은 결과를 보이는 것을 확인할 수 있다.
  
    val numbers = listOf("one", "two", "three", "four")
    numbers.forEach {
        println(it)
    }
    ----------
    one
    two
    three
    four

<br/>

이터레이터는 이와같이 모든 데이터를 살펴볼 수 있는 라이브러리이다.   
이러한 이터레이터는 `MutableIterator`, `ListIterator`, `MutableListIterator` 세 종류가 파생되어 나왔다.   
각각의 차이점을 간단히 살펴보겠다.
  
#### 1. MutableIterator
  
##### 참고

+ [kotlinlang.org/docs](https://kotlinlang.org/docs/iterators.html)

<br/>
  
## Collection

Collection(콜렉션)은 대부분의 프로그래밍 언어에 있는 라이브러리이며 코틀린 또한 기본적으로 제공하는 라이브러리이다.   
순차적인 데이터(element 나 item)를 가지고 있는 자료구조들을 관리하는 유용한 도구로 사용된다.   
코틀린에서는 대표적으로 List, Set, Map 3개의 자료형이 콜렉션에 포함된다.

+ List   
  인덱스(Index)를 통해 특정 위치의 데이터(element)에 빠르게 접근하는 순서가 있는 자료형   
  데이터의 중복이 가능하다.
  
+ Set   
  중복을 허용하지 않는 데이터 집합을 나타내는 자료형   
  데이터의 순서보다 데이터의 존재 유무를 중점으로 둔다.
  
+ Map   
  키(key)와 값(value)이라고 불리는 데이터를 하나의 집합으로 저장하고 키를 활용하여 값을 빠르게 찾는 자료형   
  키는 중복이 불가능하지만 값은 중복이 가능하고 순서보다는 키와 값 데이터의 매핑(연관성)을 중점으로 본다.

### Collection types

콜렉션은 크게 Mutable(가변, read/write)과 Immutable(불변, only-read)두 가지 유형으로 나눌 수 있다.


##### 참고

+ [kotlinlang.org/docs](https://kotlinlang.org/docs/collections-overview.html)
