# 2-2 Java

+ JDK(Java Development Kit)

## 개요

나중에 정리

해당 글은 SSAFY 7기 자바 전공반에서 배운 내용을 기초로 작성하였음을 밝힌다.

## JDK (Java Development Kit)

Oracle Corporation 에서 배포한 자바를 통해 응용프로그램을 개발할 때 유용한 소프트웨어들의 집합이다.   

JLS(Java Language Specification ) 및 JVMS(Java Virtual Machine Specification)를 구현하고 Java API(Application Programming Interface)의 Standard Edition(SE)을 제공한다고 하는데...   
필자는 단순히 가상 머신, 컴파일러, 성능 모니터링 도구, 디버거 및 자바의 기본 자료형과 라이브러리 등등을 제공한다고 이해하였다.

## JVM

언어는 소스코드를 번역하는 시점에 따라 크게 컴파일러 언어와 인터프리터 언어로 나뉜다, 이중에서 자바는 둘 모두의 장점을 활용하는 방식을 가진다.

자바의 Write once, Run anywhere의 키워드가 생긴 원인이다.



어떤 OS 이던지 JVM이 설치되어있다면 자바의 컴파일러가 자바의 소스코드를 머신

## Garbage Collection


## 자바의 객체지향 특징

4가지가 있다고 한다.

## 데이터 종류

### Primitive Type (기본형)

자바가 제공하는 8개의 기본 자료형이 있다.

### Numbers

저장에 사용하는 비트 중 가장 앞의 비트는 부호를 나타내는 부호비트(Sign bit)이고 나머지는 실재 값을 저장하는 비트로 쓰인다.

이중 int와 double은 기본형으로 숫자를 쓰면 자동으로 해당 자료형으로 인식한다.

컴파일러는 기본형을 추론하고 선언한 자료형과 맞지 않다면 에러를 뿜어낸다.

기본적으로 실수형은 정수와 소수를 저장하는 부분으로 나뉘어져 있는데 이진법으로는 소수를 정확하게 표현하기 어려워 정확한 계산이 이루어지지 않을 수도 있다.
이때는 BigDecimal을 사용하는 것도 방법이다.

사칙연산을 수행할 때 오버플로우가 발생할 수 있다.
참고로 오버플로우는 논리오류는 아니다, 개발자가 버그를 만드는 원인이 될 수는 있겠지만..

### Reference Type (참조형)

String, int[] 및 사용자가 만든 클래스들 모두 참조형으로 만드는 만큼의 갯수가 있다.

### Type casting (형 변환)

기본적으로는 기본형끼리, 참조형끼리 형 변환이 가능하다.   
하지만 boolean은 다른 타입과 호환되지 않는다.

+ 묵시적 형 변환
  + 타입의 표현 범위가 커지는 방향으로 


+ 암시적 형 변환



## Literal (리터럴)

들은 경험이 없어... 나만..

## 
