# 2-1. Kotlin

+ 개념
  + 자료형
    + 기본 자료형
    + 자료형 확인 & 캐스트
+ Iterable
+ Collection
+ Annotation
+ Generic
+ KeyWords
  + final
  + inline
+ Overriding vs Overloading
+ Visibility Modifier (Access Modifier in Java)
+ JVM과 GC 원리

> 정리하고 싶은 내용들을 목차로 적어놓은 것이며 아직 대부분의 내용을 정리하지는 못했다.

## Kotlin 개요

모바일, 서버 측 및 데스크톱 애플리케이션을 개발하는 개발자들이 사용할 수 있는 언어로 JetBrains에서 개발하였다.   
2016년 첫 번째 공식 버전이 출시되고 Google I/O 2017 컨퍼런스에서 Google이 Android에서 Kotlin에 대한 최고 수준의 지원을 발표했다고 한다.   
때문에 현재 코틀린은 안드로이드에서 특히 많이 쓰인다.

자바와 완전호환을 내세우며 등장하였으며 자바와 견주어도 괜찮은 성능과 사용자 편의성으로 사용자들을 대거 유입하였다.   
안드로이드 공식 홈페이지에서도 오랫동안 사용했던 Java보다 Kotlin을 장려를 하고있다.

자바의 구조와 기능들을 갖추고있어 자바 카테고리로 만들까도 생각하였지만, 대부분의 특징은 같아도 엄연히 다른 언어이고 코틀린만의 특징도 있기 때문에 자바와 겹치는 내용이 많을 것을 알면서도 코틀린 카테고리로 만들어 정리를 하게 되었다.   
물론 자바와의 비교는 어느정도 추가로 들어갈 예정이다.

해당 글은 다양한 블로그들과 <https://kotlinlang.org/>을 참고하여 작성되었음을 밝힌다.

</br>

### Kotlin 특징

1. 자바와의 완전 호환   
  이미 광범위한 곳에 쓰이고 있는 자바와 호환이 된다는 것은 큰 장점이다.   
  즉, 이미 존재하는 자바 라이브러리를 그대로 이용할 수 있다는 의미이다.

2. 다중 플렛폼 언어   
  JVM, Android, JS, 다양한 PC OS 에서 작동이 가능하다.   
  즉, 안드로이드 앱부터 웹개발까지 가능하다.
  
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
코틀린이 어떻게 쓰이는 언어이고 어떤 기능이 있는 언어인지 간결하게 확인하기 위해서는 [kotlinlang.org 다큐먼트의 Basics](https://kotlinlang.org/docs/basic-syntax.html)를 둘러보는 것을 추천한다. 물론 영어로 쓰여있기는 하나 친절하고 간결하게 쓰여있어 필자는 잘 이해하였다.

##### 참고

+ https://velog.io/@beargu2/Kotlin-%ED%8A%B9%EC%A7%95

</br>

## Iterator

코틀린에서 유용하게 사용되는 표준 라이브러리 중 하나이다.   
[컬렉션(Collection)](https://github.com/ii200400/IT_Skill_Question/tree/master/Language/Kotlin#collection)이나 순차적인 데이터를 가지고 있는 자료형의 데이터를 순서대로 접근하기 위한 기능이다.    
코틀린 내부를 살펴보면 `Iterable<T>` 인터페이스를 상속받은 자료형은 모두(사실 내가 확인한 자료형만) `Iterator` 기능을 담고 있었다.    

Iterator는 다양한 자료형에 상속되어있는데 아래의 그림과 같다.
  
<img src="../image/2.1%20Iterator1.png" width="50%" height="50%">
(출처: kotlinlang.com)

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
이러한 이터레이터는 `MutableIterator`, `ListIterator`, `MutableListIterator` 세 종류가 파생(상속)되어 나왔다.   
각각의 차이점을 간단히 살펴보겠다.

<br/>

#### 1. MutableIterator

가변(mutable)적인 콜렉션을 위한 이터레이터이다.   
데이터를 삭제할 수 있는 기능(`remove`)이 추가된다.   

    val numbers = mutableListOf("one", "two", "three", "four") 
    val mutableIterator = numbers.iterator()

    while (mutableIterator.hasNext()) {
        mutableIterator.next()
        mutableIterator.remove()    
        println("After removal: $numbers")
    }
    -----
    After removal: [two, three, four]
    After removal: [three, four]
    After removal: [four]
    After removal: []

#### 2. ListIterator

라이브러리에는 인덱스를 통하여 데이터에 접근을 지원하는 이터레이터이다.   
*그런데 array는 해당 이터레이터를 사용하지 않고 기본 이터레이터를 사용한다. 내가 뭔가 array에 대해서 잘 못 이해한 것일까?*

추가되는 기능은 이전 데이터로 돌아가는 기능(`hasPrevious`, `previous`)과   
인덱스를 찾는 기능(`nextIndex`, `previousIndex`)이다.   
조금 놀랍게도 `previousIndex`는 현재 위치의 인덱스를 찾아주는 기능을 하고   
`nextIndex`는 다음 위치의 인덱스를 찾아준다.   

    val numbers = listOf("one", "two", "three", "four")
    val listIterator = numbers.listIterator()
    while (listIterator.hasNext()) listIterator.next()
    println("Iterating backwards:")
    while (listIterator.hasPrevious()) {
        print("Index: ${listIterator.previousIndex()}")
        println(", value: ${listIterator.previous()}")
    }
    ----------
    Iterating backwards:
    Index: 3, value: four
    Index: 2, value: three
    Index: 1, value: two
    Index: 0, value: one

#### 3. MutableListIterator

위의 이터레이터들의 특징을 모두 가지는 동시에 데이터를 추가(`add`)하고 수정(`set`)하는 기능까지 있는 이터레이터이다.

    val numbers = mutableListOf("one", "four", "four") 
    val mutableListIterator = numbers.listIterator()

    mutableListIterator.next()
    mutableListIterator.add("two")
    mutableListIterator.next()
    mutableListIterator.set("three")   
    println(numbers)
    -----
    [one, two, three, four]

### for vs forEach

iterator예시를 통해 for문과 forEach문은 둘 모두 iterator를 활용하여 순차적으로 데이터를 탐색하는 기능을 가진 것을 알 수 있다.   
둘의 차이가 궁금하여 필자가 IntelliJ를 통해 라이브러리 내부를 보았을 때, for문은 iterator와 직접적으로 사용하여 데이터를 탐색하고 forEach문은 for문을 활용하여 데이터를 탐색하는 것을 찾아볼 수 있었다.   

<img src="../image/2.1 Iterator2.png" width="80%" height="80%">

'어... 그러면 뭐가 그렇게 달라서 함수를 따로 만든 걸까?' 하는 생각에 for문과 forEach문의 차이점이라고 검색해보았다.   
일반적으로 특정 자료형에서 for문과 forEach문의 속도 차이를 서술한 글이 대부분이었고 왜 속도가 2배, 3배나 차이나는지, 왜 어떤 자료형에서는 forEach문이 더 빠르고 어떤 자료형에서는 더 느린지에 관한 설명은 나와있지 않았다.   
때문에 해당 내용에 관해 조금 자세하게 서술하려 했으나, 내용을 넣기에는 너무 주제의 글이 커질 것 같아서 두 문법의 차이점을 간단하게 서술하고 속도에 관한 차이점은 다른 주제의 링크[`inline` **링크 추가 요망**]()를 남겨두는 것으로 생략하겠다.

**결과적으로 두 문법의 차이점은 아래와 같다.**

1. forEach문은 기본적으로 람다형식의 함수를 계속 호출하는 형태로 for문 보다 속도가 느리다.
2. forEach문은 람다함수를 사용하는 문제로 break을 사용하면 continue와 같은 
3. 몇몇 자료형의 forEach문은 내부적으로 [`inline` **링크 추가 요망**]() 키워드를 사용하여 for문 보다 속도가 빠르다.

<br/>

#### 자바 Iterator 라이브러리

코틀린의 `MutableIterator` 클래스는 자바에서는 Iterator라는 클래스 명으로 들어가 있으며 코틀린의 Iterator와 대응되는 자바 클래스는 없다.   
코틀린 라이브러리의 Mutable이라는 단어가 들어간 클래스들 중 몇몇은 자바 라이브러리의 일반 클래스와 대응되는 것을 볼 수 있다.   
예를 들어 코틀린의 `MutableListIterator`와 자바의 `ListIterator`, 코틀린의 `MutableCollection`과 자바의 `Collection`가 대응된다.(개인적으로는 같아보인다.)   
하지만 코틀린의 `MutableList`는 자바의 `ArrayList`를 이용하여 클래스를 생성한다. 때문에 자바와 코틀린은 같이 공부해야하고 확실하게 구분해야 한다고 생각한다.

##### 참고

+ [kotlinlang.org/docs](https://kotlinlang.org/docs/iterators.html)
+ [Kotlin] for문 vs foreach문](https://hwan-shell.tistory.com/245)

<br/>
  
## Collection

Collection(콜렉션)은 코틀린 라이브러리 중 하나이며 코틀린 또한 기본적으로 제공하는 라이브러리이다.   
이터레이터를 상속받고 [`Generic` **링크 추가 요망**]()을 활용하여 구현된 콜렉션은 데이터들을 관리하는 유용한 도구로 사용된다.  

콜렉션은 크게 Immutable(불변, only-read)과 Mutable(가변, read/write) 두 가지 유형으로 나눌 수 있다.   

#### Immutable Collection

<img src="../image/2.1 Collection1.PNG" width="80%" height="80%">

라이브러리 내에서의 클래스 명은 Immutable Collection이 아닌 Collection이다.
또한 Iterable은 Iterator을 가지고 있는 클래스로 Iterator라고 생각해도 무방할 정도로 간단한 클래스이다.

가장 기본적인 컬랙션으로 상술했듯이 읽기만 가능하다.   
가지고 있는 데이터들이 비어있는지 확인하는 함수(`isEmpty`) 와 특정 데이터들이 포함되어있는지 확인하는 함수(`contains`, `containsAll`)가 있다.   

#### Mutable Collection

<img src="../image/2.1 Collection1.PNG" width="80%" height="80%">

콜렉션과 MutableIterable(MutableIterator)를 상속받아 데이터를 추가하고 삭제하는 기능이 추가된 콜랙션이다.   
데이터 조작에 대한 함수들(`add`, `remove`, `addAll`, `removeAll`, `retainAll`, `clear`)이 추가된다.

<br/>

코틀린에서 콜렉션이라고 하면 대표적으로 List, Set, Map 3개의 자료형을 언급하게 된다.

+ List   
  인덱스(Index)를 통해 특정 위치의 데이터(element)에 빠르게 접근하는 순서가 있는 자료형   
  데이터의 중복이 가능하다.
  
+ Set   
  중복을 허용하지 않는 데이터 집합을 나타내는 자료형   
  데이터의 순서보다 데이터의 존재 유무를 중점으로 둔다.
  
+ Map   
  키(key)와 값(value)이라고 불리는 데이터를 하나의 집합으로 저장하고 키를 활용하여 값을 빠르게 찾는 자료형   
  키는 중복이 불가능하지만 값은 중복이 가능하고 순서보다는 키와 값 데이터의 매핑(연관성)을 중점으로 본다.

##### 참고

+ [kotlinlang.org/docs](https://kotlinlang.org/docs/collections-overview.html)
+ [Kotlin의 Collection 함수](https://medium.com/hongbeomi-dev/kotlin-collection-%ED%95%A8%EC%88%98-7a4b1290bce4)
+ 코틀린 내부 라이브러리 주석들
