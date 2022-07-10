# Back End

사용자와 직접 상호작용하지는 않지만 프론트 엔드에서 보낸 정보(요청)를 토대로 적적한 정보를 반환(응답)하는 서버 역할을 가진다. 이 때 종종 DB의 데이터를 활용하기도 한다.

백엔드 서버는 크게 3가지로 나눌 수 있다.

+ 클라이언트의 접속을 확인하고 응답을 처리해주는 Web Server(웹 서버)
+ 클라이언트의 요청에 따른 로직을 처리하는 Application Server(어플리케이션 서버)
+ 응답에 사용될 데이터들을 저장하고 관리하는 DBMS(데이터 베이스 관리 시스템 이하 디비)

요청이 들어왔을 때 위의 서버들이 응답을 하기 까지의 과정은 간단하게는 아래와 같다.

첫번째로 어플리케이션 서버는 기본적으로 클라이언트가 입력한 정보를 받고   
두번째로 로직을 처리한다.   
로직은 크게 2가지로 나눌 수 있으며 일반적으로 사용하는 네이밍은 아래와 같다.
디비를 사용하지 않는 로직은 모두 비즈니스 로직이라고 생각하라고 하셨다.
1. Business Logic (비즈니스 로직) - Service.java
2. DB Logic (디비 로직) - Dao.java

[사진 추가 요망]()

마지막으로 위의 로직을 통해서 응답을 할 준비가 되었다면 클라이언트가 해석할 수 있는 html 형식으로 응답을 보낸다.

중간에 Dto(data transfer object)와 Vo(value of)라는 것이 같다고 생각하지만 다른 용어라고 추가로 언급해주셨는데.. 무슨 말인지 모르겠다; 애초에 Vo가 무엇인지 설명을 안해주셨다;

[사진 추가 요망]()

웹 서버는 언어를 이해할 수 없기 때문에 어플리케이션 서버에게 로직을 맡기곤 했는데 요즘의 백엔드는 두 기능을 모두 가지는 서버인 Web Application Server(WAS 일명 와스)를 가지는 경우도 있다고 많다고 한다.

필자의 경우 교육과정에 따라 이클립스에서 Dymamic Web Project로 프로젝트(웹 어플리케이션)를 생성하고 무료 WAS인 Tomecat(톰캣) 9.0.60 버전을 사용하게 되었다.

## Servlet

백엔드에서 사용하는 자바파일의 일종, 해당 파일만으로는 웹 페이지를 구현하기 크게 힘들어서 아래의 jsp와 같이 활용한다.

## Servlet LifeCycle

라이프 사이클이란 한 객체가 생성되어서 실행되고 소멸되기까지의 과정을 의미한다. 즉, 서블릿에 관한 해당 과정을 의미한다.

한 **종류**의 서블릿은 반드시 1개만 서버에 존재하고 서블릿은 ServletContainer(서블릿 컨테이너)가 관리한다. 때문에 서블릿의 라이프 사이클도 서블릿 컨테이너에 의해 관리된다.   

서블릿은 컨테이너에 의해   
객체가 생성(단 한번)되고 초기화(단 한번)되며   
요청에 대한 처리를 요청시마다 반복해서 진행하다가   
제거(단 한번)된다.

![image](https://user-images.githubusercontent.com/19484971/174528543-c4205936-0edc-46a9-b28a-b7451442302a.png)

| method | description |
| --- | --- |
| init() | 서블릿이 메모리에 로드될 때 한 번 호출.<br>코드가 수정되면 새로운 코드 로드를 위해 기존 서블릿을 삭제 후 새로운 서블릿 객체로 해당 메서드 호출 |
| doGet() | Get 방식으로 data 전송 시 호출 |
| doPost() | Post 방식으로 전송시 호출 |
| service() | 모든 요청이 service()를 통해서 doXX()메소드로 이동 |
| destroy() | 서블릿이 메모리에서 해제될 때 호출<br>코드가 수정되었을 때도 새로운 코드 로드를 위해 기존 서블릿 삭제를 위해 호출 |

## JSP (Java Server Pages)

HTML 내에 자바코드를 삽입하여 웹 서버가 동적 페이지를 만들 수 있도록 하는 `언어`이다.   

java EE 기능 중 일부로 웹 애플리케이션 서버에서 동작이 가능하며 자바 **서블릿으로 변환된 후 실행**된다는 특징이 있다. 하지만, 서블릿과는 다르게 HTML 표준에서 작성되기 때문에 웹 페이지를 디자인하기 훨씬 편리하다는 장점이 있다.   
Html에 자바코드가 삽입되는 형식이므로 Html보다 더 코드가 길며 삽입되는 자바코드가 없다면 파일 형식을 html로 바꿔도 그대로 작동된다.

JSTL등의 JSP 태그 라이브러리를 같이 사용하는 경우에는 자바 코딩없이 태그만으로 간략하게 작성이 가능해지므로 생산성을 더욱 높일 수 있다.

1999년 썬 마이크로시스템즈에서 배포하였으며 이와 유사한 구조로는 PHP, ASP, ASP.NET등이 있다. 



### JSP 동작 흐름

[사진 추가 요망]()

jsp로 생성되는 서블릿은 컨테이너가 기본적으로 생성해주는 9개의 객체들이 있다는 점이 특징이다. 이 객체들을 jsp의 `기본객체` 또는 `내장객체`라고 한다.

jsp는 Scriptlet 기반 언어이지만 서블릿으로 한번 변환되면 서블릿은 Compile 기반 언어이기 때문에 Compile 언어의 특징도 가지고 있다고 말할 수 있다. jsp는 두 가지 방식의 장점을 활용하기 때문에 서블릿으로 변환되기는 하나 서블릿과 크게 속도차이는 나지 않는다고 한다.

+ 더 알아보기
	+ Compile 기반 언어(서블릿)와 Scriptlet 기반 언어

### JSP 기본객체

[JSP 9개의 기본객체 서술 요망]()

+ JSP 기본객체 scope
[JSP 4개의 기본객체 scope 서술 요망]()

## JSP Scripting Element (JSP 스크립팅 요소)

jsp에서 자바코드를 삽입할 수 있도록 하는 것(문법? 요소? 영역?)을 알아야 작성이 가능하다. 이러한 문법들을 jsp 스크립팅 요소라고 한다.

### 1. 선언 (Declaration)

멤버변수를 선언하거나 메소드를 선언할 때 사용한다.

`<%! 선언 %>`

예시는 아래와 같다.

```
 <%!
	 // 아래의 코드가 서블릿 자동 생성시, 선언부에 들어간다.
	 String name = "임영선";
	 private String str;

	 public void init(){
		name = "게으른 너구리";
	 }
 %>
```

### 2. 스크립트릿(Scriptlet)

클라이언트 요청시 반복되어 호출되는 영역으로, 서블렛으로 변환시 service() 메소드에 해당(비즈니스 로직)하는 영역이다. request와 response를 활용하여 코드를 구현하게 된다.

`<% 스크립트릿 %>`

예시는 아래와 같다.

```
<%
	// 아래의 코드가 서블릿 자동 생성시, service() 메소드에 들어간다.
	request.setCharacterEncoding("utf-8");
	String userid = request.getParameter("userid");
	String subject = request.getParameter("subject");
	String content = request.getParameter("content");

	System.out.println(subject);
 %>
 ```
 
### 3. 표현식 (Expression)

데이터 출력시 사용한다. 다른 요소들과는 다르게 세미콜론을 넣지 않는다.

`<%= 표현식 %>`

위의 표현은 아래로도 작성이 가능하다.   
단, 세미콜론을 붙여야 한다는 점을 잊지말자!

`<% out.print(표현식); %>`

예시는 아래와 같다.

```
안녕하세요 <%= name %>

 ```

### 4. 주석 (Comment)

코드 상에 부가 설명을 작성한다.

`<%-- 주석 --%>`

html의 주석 `<!-- -->`과의 다른 점은 Jsp의 주석은 서버에서 제외시켜 클라이언트의 응답 html에는 보이지 않는데 html 주석은 보인다는 것이다.   

아래와 같이 html 주석 내에 jsp의 표현식을 넣으면 그대로 실행이 된다는 점도 있다.   
<!-- 이 글은 보이지 않지만.. 왼쪽 글은 보이게 된다. <%= name %> -->

## JSP 지시자 (Directive)

서블릿 컨테이너에게 JSP를 통해 서블릿을 생성할 때 어떻게 생성할지에 관한 설정이나 명령을 의미한다. 기본적인 문법은 아래와 같다.

`<%@ directive_type attr1="value1" attr2="value2" %>`

### 1. page Directive 

컨테이너에게 현재 JSP 페이지를 어떻게 처리할 것인지에 대한 정보를 제공한다.

아래와 같이 작성한다.

`<%@ page attr1="value1" attr2="value2" %>`

이클립스에서 JSP 파일을 생성하면 자동으로 나오는 아래의 코드가 바로 페이지 지시자에 해당한다.

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" %>
```

[jsp 페이지 지시자 속성 정리 요망]()

### 2. include Directive 

특정 JSP 파일을 페이지에 포함시키는 지시자이다.   
여러 JSP 페이지에서 반복적으로 사용되는 부분(일반적으로 header, footer, aside 등)을 jsp file로 만든 후 해당 지시자를 활용하면 반복되는 코드를 줄일 수 있다.

아래와 같이 작성한다.

`<%@ page file="/template/header.jsp" %>`

속성이 하나밖에 없다는 점이 개인적으로 편안하다.

### 3. taglib Directive 

JSTL 또는 사용자 커스텀 태그(custom tag)를 이용하고자 할 때 사용되며 JSP 페이지 내에 자바 코드를 삽입할 때 조금 더 간결하게 작성할 수 있다.

아래와 같이 작성한다.

`<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`

`tagdir` 라는 속성도 있지만 어디에 쓰이는 속성인지 잘 모르겠다.

## Java Beans (자바 빈즈)

JSP에서 사용이 가능한 객체를 지칭하는 용어이다. (빌더 형식의 개발도구에서 재사용이 가능한 소프트웨어 컴포넌트 어쩌구라고 쓰여있는 정의도 있는데 잘 모르겠다.)

자바 빈즈를 사용하는 경우에는 몇 가지 규칙을 따라야 하는데 다음과 같다.
1. 반드시 패키지가 존재해야 한다.
2. 기본 생성자가 존재해야 한다.
3. 멤버변수 접근 제어가는 private 이어야 한다.
4. 멤버변수에 접근할 때는 getter와 setter를 사용한다.

필자의 경우 자바를 배울 때 부터 위의 규칙을 따라서 클래스를 생성했었는데, 자바 클래스와 자바 빈즈의 괴리감이 전혀 없어서 오히려 당혹스러웠다; (교수님 그냥 자바 클래스인데요? 무엇이 빈즈라는..?)

아래는 자바 빈즈를 활용했을 때의 아키택쳐 사진..이다.

[사진 추가..요망..]()

## forward와 sendRedirect

서버에서 페이지를 이동시킬 때 forward와 sendRedirect을 사용하여 이동하는 것이 기본적이다. 하지만, 페이지를 이동시킨다는 점만 같고 개인적으로는 오히려 차이점이 더 많다고 생각한다.   

이러한 차이점을 표로 정리해보면 아래와 같다.

|  | forward(request, response) | sendRedirect(location) |
| -- | -- | -- |
| 사용 방법 | RequestDispatcher dispatcher = request.getRequestDispatcher(path);<br>dispatcher.forward(request, response); | response.sendRedirect(location); |
| 이동 범위 | 동일 서버(project)내 경로 | 동일 서버 포함, 타 URL 가능. |
| location bar | 기존 URL 유지<br>(실재 이동되는 주소 확인 불가) | 이동하는 page로 주소가 갱신 |
| 객체 | 기존의 request와 response가 그대로 전달 | 기존의 request와 response는 소멸, 새로운 request와 response가 생성. |
| 속도 | 비교적 빠름 (1나노초 정도?) | forward에 비해 느림 |
| 데이터 유지 | request의 setAttribute(name, value)를 통해 전달 | request로는 data 저장 불가능, session이나 cookie를 이용 |
