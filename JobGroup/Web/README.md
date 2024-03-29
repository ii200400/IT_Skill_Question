`목차`

* [개요](#개요)
* [cookie session](#cookie-session)
  + [쿠키](#쿠키)
  + [Session](#session)
* [Web Architecture](#web-architecture)
* [Get vs Post](#get-vs-post)
* [URL(Uniform Resource Locator)](#url-uniform-resource-locator-)

`관련 내용`

1. [HTML](./html)
2. [CSS](./css)
3. [JavaScript](./JavaScript)
4. [BootStrap](./bootstrap)
5. [DB](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database)
6. [Servlet & JSP](./JSP)
7. [Spring](./spring)
8. [Vue](./vue)

# 3-3 Web

## 개요

기본적으로 사용되는 HTML5 웹 문서는 3가지 구성요소가 있다.

+ HTML5(Hyper Text Markup Language)   
  기본적인 Markup Language 에 링크의 기능을 추가한 마크업 언어.
  웹 페이지의 문서 구조 담당
+ CSS(Cascading Style Sheets)   
  웹 페이지의 디자인(표현)을 담당
+ JS(JavaScript)   
  웹 페이지의 이벤트 담당

jdbc를 어디에 넣어야 할지 모르겠네;; 아이고난;;
자바로 디비를 컨트롤하는 기능이라고 생각하고 있다.

## cookie session

쿠키와 세션에 대해 이해하려면 우선 이들의 기반이 되는 http의 특징을 알아야 한다.

+ http 특징
  + 클라이언트의 요청에 대한 서버의 응답 직후 연결이 끊어진다. (stateless)
  + 같은 클라이언트가 요청을 해도 서버는 현재 요청을 한 클라이언트가 방금 전 요청을 한 클라이언트인지 알 수 없다. 
    + 로그인 했다고 연결이 되어있다는 것이 아니라 request를 보내고 response를 받을 때까지만 연결을 유지한다.
    + 웹은 세계의 모든 사람들이 접근 가능한데, 한 번 연결했다고 계속 연결이 유지되면 메모리 자원이 빠르게 고갈되기 때문
  
이와 같은 상황에서 클라이언트를 구별해야하는 문제를 해결하기 위해 Cookie와 Session을 사용한다.

+ 참고
  + [javadocs](https://javaee.github.io/javaee-spec/javadocs/)에서 `HttpServletRequest`를 통해 cookie와 session을 관리하는 메소드들을 볼 수 있다.

### 쿠키

서버와 통신하는 **클라이언트에 저장**되는 자그마한 데이터이다.   
클라이언트에 텍스트 파일형식으로 **key와 value 쌍의 문자열(String) 형태**로 저장된다.

브라우저(IE, 크롬, 파이어폭스..)가 클라이언트의 별도 설정없이도 요청을 보낼 때 항상 Request Header에 쿠키를 넣어 서버로 전송한다.   
브라우저마다 쿠키를 따로 관리하기 때문에 브라우저가 다르면 쿠키도 다르고 서버는 다른 클라이언트라고 인식한다. 

쿠키에는 다음과 같은 요소가 있다.
+ 이름 : 쿠키 구별을 위한 이름
+ 값 : 쿠키 매핑 값
+ 유효기간 : 쿠키가 유효한 기간
+ 도메인 : 쿠키를 전송할 도메인
+ 경로 : 쿠키를 전송할 요청 경로(클라이언트 uri)

쿠키를 사용하는 이유는 아래와 같다.
+ 서버가 알아야할 정보(세션관리 정보 등)를 저장
+ 사용자 편의를 위해 (ID 저장, 일주일간 다시보지 않기)
+ 사용자마다 적절한 페이지 표시 (최근 검색한 상품 목록, 광고, 테마 스킨)
+ 트래킹(사용자의 행동과 패턴을 분석하고 기록)

동작순서
1. 클라이언트가 페이지를 요청
2. WAS가 쿠키를 생성
3. HTTP Header에 쿠키를 넣어 응답 (이 때 만료가 된 쿠키는 제외)
4. 브라우저는 받은 쿠키를 PC에 저장하고 다시 WAS에게 요청할 때 쿠키도 함께 전송
5. 브라우저가 종료되어도 쿠키의 만료기간이 남아있다면 클라이언트는 계속 보관
6. 동일 사이트 재방문시 클라이언트의 PC에 쿠키가 있는 경우 요청할 때 쿠키를 함께 전송

참고로 쿠키는 브라우저마다 다르지만 특정한 개수의 쿠키 개수만을 가질 수 있다.

### Session

클라이언트가 웹 서버에 연결되어 있는 상태를 의미한다.   
WAS는 메모리에 **객체 형태**로 세션을 관리하며 메모리가 허용되는한 제한없이 저장이 가능하다.

일반적으로는 **서버에서** 클라이언트의 정보를 일정기간 저장하기 위해 사용한다, 대표적으로 아래의 기능에 세션을 활용한다.
+ 로그인 유지
+ 장바구니 품목 관리

동작순서
1. 클라이언트가 페이지를 요청
2. 서버는 접근한 클라이언트의 Request Header 필드인 Cookie를 확인하여, 클라이언트가 해당 session id를 보냈는지 확인한다.
3. session id가 존재하지 않는다면, 서버는 session id를 생성해 클라이언트에게 돌려준다.
4. 서버에서 클라이언트로 돌려준 session-id를 쿠키를 저장해 서버에 저장.
5. 클라이언트는 재접속 시, 이 쿠키를 이용하여 session id값을 서버에 전달

특징
+ 웹 서버에 웹 컨테이너의 상태를 유지하기 위한 정보 저장
+ 웹 서버에 저장되는 쿠키
  + 브라우저를 닫거나, 서버에서 세션을 삭제했을 때만 삭제
  + 서버에서 관리하므로 비교적 쿠키보다 보안이 좋음
+ 저장 데이터에 제한 없음
+ 각 클라이언트 별로 고유 Session id가 존재
  + Session id로 클라이언트를 구분하여 각 클라이언트 요구에 맞는 서비스 제공

쿠키 개념은 많은데 왜 세션 개념은 없는지;; 필자는 `웹 서버에 연결되어 있는 상태`를 `웹 서버에 저장된 클라이언트 정보`라고 생각하고 있다.

이유는 세션은 세션 id를 활용하여 구별하고 세션에는 클라이언트의 정보가 저장되어 있는데 그 정보는 보통 클라이언트의 정보(연결 상태나 장바구니 정보 등)이기 때문.

## Web Architecture

사용자와 직접 상호작용하지는 않지만 프론트 엔드에서 보낸 정보(요청)를 토대로 적적한 정보를 반환(응답)하는 서버 역할을 가진다. 이 때 종종 DB의 데이터를 활용하기도 한다.

백엔드 서버는 크게 3가지로 나눌 수 있다.

+ 클라이언트의 접속을 확인하고 응답을 처리해주는 Web Server(웹 서버)
+ 클라이언트의 요청에 따른 로직을 처리하는 Application Server(어플리케이션 서버)
+ 응답에 사용될 데이터들을 저장하고 관리하는 DBMS(데이터 베이스 관리 시스템 이하 디비)

요청이 들어왔을 때 위의 서버들이 응답을 하기 까지의 과정은 간단하게는 아래와 같다.

1. 어플리케이션 서버는 기본적으로 클라이언트가 입력한 정보를 받고   
2. 로직을 처리한 후
3. 응답 페이지를 만든다. (html) 

로직은 크게 2가지로 나눌 수 있으며 일반적으로 아래와 같다.
디비를 사용하지 않는 로직은 모두 비즈니스 로직이라고 생각하라고 하셨다.
1. Business Logic (비즈니스 로직) - Service.java
2. DB Logic (디비 로직) - Dao.java

![image](https://user-images.githubusercontent.com/19484971/178147676-51b16d81-ac5e-43c6-97df-2453a741515e.png)   
(model 1 architecture)

웹 서버는 언어를 이해할 수 없기 때문에 어플리케이션 서버에게 로직을 맡기곤 했는데 요즘의 백엔드는 두 기능을 모두 가지는 서버인 Web Application Server(WAS 일명 와스)를 가지는 경우도 있다고 많다.

필자의 경우 교육과정에 따라 이클립스에서 Dymamic Web Project로 프로젝트(웹 어플리케이션)를 생성하고 무료 WAS인 Tomecat(톰캣) 9.0.60 버전을 사용하게 되었다.

중간에 Dto(data transfer object)와 Vo(value of)에 대해서 추가로 설명해주셨는데, DTO는 작업을 처리하기 위해서 사용자로부터 받는 데이터 객체(일반적으로 DB 테이블 중 하나와 같은 것)이고 VO는 응답 데이터를 반환하기 위해서 DB로부터 받은 데이터 객체(DTO와 같을 수도 있고 JOIN을 통해 DB 테이블에 없는 객체일 수 있는 것)라고 설명해주셨다.

조금 더 자세한 내용은 [JSP의 MVC](https://github.com/ii200400/IT_Skill_Question/tree/master/JobGroup/Web/JSP#%EC%9B%B9-%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4)에 정리되어있다.

## Get vs Post

|  | Get | Post |
| -| -- | -- |
| 특징 | 전송되는 데이터가 URL 뒤에 Query String으로 전달<br>입력값이 적은 경우나 데이터 노출에 문제가 없는 경우에 사용한다. | URL과 별도로 HTTP header 뒤 body에 입력 스트림 데이터로 전송 |
| 장점 | 간단한 데이터를 빠르게 전송.<br>form tag 뿐만 아니라 직접 URL에 입력하여 전송 가능. | 데이터의 제한이 없다.<br>최소한의 보안 유지 효과를 볼 수 있다. |
| 단점 | URL에 쿼리 스트링 형식으로 전송할 수 있는 데이터 양에 제한이 있다. | 전달 데이터의 양이 같을 경우 GET 방식보다 느리다. |

## URL(Uniform Resource Locator)

+ 네트워크 상에서 자원이 어디 있는지를 알려주기 위한 참조값을 의미한다.

![image](https://user-images.githubusercontent.com/19484971/178305428-018036ac-b14f-4f83-953a-dbe1cfbb2a05.png)   
(참조 [velog.io/@keywookim](https://velog.io/@keywookim/We.TIL-30-Django-%EC%BF%BC%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%A7%81-%EA%B0%84%EB%8B%A8-%EC%82%AC%EC%9A%A9%EB%B2%95))

추가로 정리
+ 프록시 서버
+ url에 주소를 입력했을 때 생기는 일
+ ![image](https://user-images.githubusercontent.com/19484971/178859256-4bd684fd-95fc-45a7-9761-fbd790a63500.png)
+ AWS
