# 개요

(member functions 링크 추가 요망, 프로퍼티 설명 확인, primitive values 링크 추가 요망)
코틀린에서는 변수에 맴버 함수`member functions`와 프로퍼티`properties`를 호출할 수 있다는 점에서 모든 것이 객체이다. 특정 타입(`numbers`, `characters`, `booleans`)들은 `primitive values`로 표현되기도 하지만 보통은 일반적인 클래스와 같이 사용된다.

코틀린의 기본적인 자료형 `numbers`, `booleans`, `characters`, `strings`, 그리고 `arrays`에 대해서 알아보도록 하겠다.

## Numbers

### Integer types

코틀린은 정수를 표현하기 위해 네 가지의 숫자 자료형이 있다. 크기와 표현 가능한 수에 따라 나뉘는데 다음과 같다.

| Type | Size (bits) | Min value | Max value |
|---|---|---|---|
| `Byte` | 8 | -128 | 127 |
| `Short` | 16 | -32768 | 32767 |
| `Int` | 32 | -2,147,483,648 (-231) | 2,147,483,647 (231 - 1) |
| `Long` | 64 | -9,223,372,036,854,775,808 (-2^63) | 9,223,372,036,854,775,807 (2^63 - 1) |

정수를 담는 변수들은 따로 자료형을 명시하지 않아도 `Int` 자료형으로 유추하고 `Int`로 표현할 수 있는 값을 넘는 값이 저장된다면 `Long` 자료형으로 유추한다. 만일 따로 명시하고 싶다면 접미사 `L`을 사용하거나 자료형을 명시해주면 된다.

    val one = 1 // Int
    val threeBillion = 3000000000 // Long
    val oneLong = 1L // Long
    val oneByte: Byte = 1
    
### Floating-point types

나, 멈춰!
