# 3-3 Web

+ 미생성

## 개요

## XML

태그를 이용해서 문서나 데이터 구조를 명시하는 Markup Language 라는 언어 중 하나이다.

사용자가 태그를 정의해서 작성이 가능하기 때문에 Extensible Markup Language라고 하지만,   
Html에 비해 정확한 문법을 준수해야만 작동이 된다.

### 기본 문법

1. 문서는 항상 xml의 버전과 인코딩을 명시하는 아래와 비슷한 코드로 시작해야 한다.   
   ex) <?xml version="1.1" encoding="UTF-8"?>
2. 반드시 root element가 존재해야 한다.
   나머지 태그들은 Tree 형태로 구성된다.
3. 시작 태그와 종료 태그는 일치해야 한다.
   ex) <tag> ~~ </tag>
4. 시작 태그는 key-value 구조의 속성을 가질 수 있다.   
   값은 "" 또는 ''로 묶어서 표현한다.
   ex) <tag key="value"> ~~ </tag>
5. 태그는 대소문자를 구별한다.

### DTD, Schema

통일된 xml을 만들기 위해 만드는 xml 작성 규칙이나 양식을 적어놓은 문서를 의미한다.
프로젝트마다, 통신마다 다를 수 있으며 원활한 데이터 송수신을 위해 해당 작업을 하는 사람들이 참고하는 문서이다.

이러한 문서를 잘 따른 문서를 valid라고 한다.

[DTD Turotial](https://www.w3schools.com/xml/xml_dtd_intro.asp)을 참고하면 이해가 조금 더 쉽다.

