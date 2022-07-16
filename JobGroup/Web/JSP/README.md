# Servlet & JSP

+ 웹 서버를 자바 파일로 구현할 때 사용하는 파일들

+ 현재는 많이 사용하는 기술은 아니지만, 현재 널리 사용하는 Spring의 기초가 되는 내용이 있다.
+ 실습 코드가 많이 길어서 해당 파일에는 이론적인 부분만 남길 것이다.

## Servlet

+ 백엔드의 web 환경에서 웹 페이지를 동적으로 생성하기 위한 자바 프로그램 또는 사양(?)을 의미한다.
	+ 자바 클래스의 일종으로 server + applet(어플리케이션과 유사 단어)을 합친 단어
	+ http 프로토콜 상에서 요청에 대해 응답을 해주는 역할
	+ JSP가 HTML 문서에 Java 코드를 포함하고 있다면 서블릿은 자바 코드 안에 HTML을 포함한다는 차이점이 있다.
	+ 해당 파일만으로는 웹 페이지를 구현하기 크게 힘들어서 아래의 jsp와 같이 활용한다.
+ [javaee-spec/javadocs](https://javaee.github.io/javaee-spec/javadocs/)에서 관련 api를 찾아볼 수 있다.
+ 시간이 된다면 servlet의 상속도에 대해서 찾아보자!

### 환경설정

+ 필자의 경우 eclipse를 통해 작업을 진행하였으며 CSS, HTML, JSP encoding을 모두 UTF-8로 설정하고 코딩을 하였다.   
+ Dynamic Web Project을 선택한 후, 프로젝트 명을 작성하고 Apache.org에서 다운로드 받은 Tomcat v9.0을 runtime 환경으로 설정하여 진행하였다.
	+ 서버를 설정할 일이 자주 있지는 않아서 runtime 환경을 다시 설정하려고 하면 어떻게 했는지 까먹었다;
+ context root를 설정하고 마치면 된다.
	+ context root는 특정 주소를 통해 해당 프로젝트를 찾아가는데 사용하는 이름으로 다른 프로젝트와 겹치면 안된다.
	+ 예를 들어 context root를 helloservlet으로 설정하면 프로젝트의 기본 주소는 `http://localhost:8080/helloservlet` 가 된다.
		+ 단순히 주소창에 `http://localhost:8080/helloservlet/`을 치면 `http://localhost:8080/helloservlet/index.html` 에 해당하는 파일을 찾아 반환한다.
	+ content directory는 html, css, js, img등의 정적인 파일들이 들어가는 파일을 의미한다.
	+ Java 파일(Servlet, JSP, 라이브러리 등)은 Java Resource/src에 넣게 된다.
	+ 추후 바꾸고 싶다면 프로젝트 오른 클릭 - properties - web project settings 에서 변경해주면 된다.
	+ 캐시나 서버 버그 등으로 인하여 위의 방법이 안된다면 Servers 파일의 servers.xml 최하단부의 context 태그의 path 속성을 변경하거나 Context 자체를 삭제해주면 확실하다.
+ 이후 Servlet 파일을 생성하여 프로젝트를 진행한다.

필자가 Servlet 작동 테스트를 위해 간단하게 작성한 자바코드
```
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HelloSsafy
 */

/*

이렇게 servlet(서버에서 돌아가는 자바)을 간편하게 생성할 수 있다. 
(아래보면 해당 파일의 클래스가 HttpServlet을 상속받은 것을 볼 수 있다.)
이전에는 따로xml을 만들어서 구현했다고 한다.

본인 프로젝트 기준으로 서버를 키고  http://localhost:8080/helloservlet/hs 라는 주소를 적어주면
doGet 함수가 호출되어 결과를 볼 수 있다.

일반적으로 하이퍼 텍스트의 링크나 주소창에 직접 주소를 적는것, form의 method를 Get으로 작성한 것들은 
(사실상 form의 method를 Post으로 작성한 것들을 제외한 모든 것)
모두 get 방식이므로 doGet이 호출되는 것이다.

doGet(HttpServletRequest request, HttpServletResponse response)의
request는 사용자의 입력 데이터가 저장되어있다. 
response는 request의 데이터를 토대로 응답할 응답할 데이터를 저장한다. 
물론 데이터는 서버에서 로직을 통한 연산 후 넣어준다.
*/

@WebServlet("/hs")

// 서버가 하는 일은 대충 아래와 같다.
// 1. (클라이언트가 보낸) 데이터를 doget(혹은 doPost) 함수로 받아와서 해서
// 2. 비즈니스 로직을 진행하고
// 3. 응답 페이지(적어도 html)를 만들고 응답한다. 
public class HelloSsafy extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
		String name = "임영선";
		// 사용하지 않으면 한글이 깨진다. (인코딩 문제)
		// 텍스트 이지만 html로 인식하고 인코딩은 utf-8로 설정한다는 내용이다.
		response.setContentType("text/html;charset=utf-8");
		// request 인코딩을 설정한 후 PrintWriter를 생성해야 한글이 깨지지 않는다.
		// 위의 코드를 먼저 작성하면 
		PrintWriter out = response.getWriter();
		
		/*
		Servlet으로만 응답페이지를 작성하면 아래와 같이 ""의 저주에 걸릴 수 밖에 없다.
		이러한 불편함 때문에 이후에는 Jsp이 생겨났다.
		
		Jsp는 Servlet처럼 자바파일에 html을 넣는 것이 아니라
		html에 자바를 조금씩 넣는 듯한 형식으로 코딩하게 된다.
		
		 * */ 
		out.println("");
		out.println("<html>");
		out.println("	<body>");
		out.println("		Hello!!!!<br>");
		out.println("		안녕하세요 " + name + "!!!!");
		out.println("	</body>");
		out.println("</html>");
	}
}
```
![image](https://user-images.githubusercontent.com/19484971/178272912-85671e42-f3b2-4e3b-8370-05a0cc8c0147.png)

### Servlet LifeCycle

+ 라이프사이클이란 한 객체가 생성되어서 실행되고 소멸되기까지의 과정을 의미한다. 
  즉, 서블릿에 관한 라이프사이클을 의미한다.
	+ 한 **종류**의 서블릿은 반드시 1개만 서버에 존재하고 서블릿은 ServletContainer(서블릿 컨테이너)가 관리한다.
	+ 서블릿의 관리(라이프사이클)는 서블릿 컨테이너에 의해 일어난다.   

1. 서블릿은 컨테이너에 의해 객체가 생성(단 한번)되고 
2. 초기화(단 한번)되며   
3. 요청에 대한 처리를 요청시마다 반복해서 진행하다가   
4. 제거(단 한번)된다.

![image](https://user-images.githubusercontent.com/19484971/174528543-c4205936-0edc-46a9-b28a-b7451442302a.png)

| method | description |
| --- | --- |
| init() | 서블릿이 메모리에 로드될 때 한 번 호출.<br>코드가 수정되면 새로운 코드 로드를 위해 기존 서블릿을 삭제 후 새로운 서블릿 객체로 해당 메서드 호출 |
| doGet() | Get 방식으로 data를 서버로 전송 시 호출 |
| doPost() | Post 방식으로 data를 서버로 전송 시 호출 |
| service() | 모든 요청이 service()를 통해서 doXX()메소드로 이동 |
| destroy() | 서블릿이 메모리에서 해제될 때(서버를 끄는 경우 등) 호출<br>코드가 수정되었을 때도 새로운 코드 로드를 위해 기존 서블릿 삭제를 위해 호출 |

```
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/*
한 `종류`의 servlet은 반드시 1개만(클라이언트 수와 상관없이) 서버에 존재하고 
서블릿은 ServletContainer(서블릿 컨테이너)가 관리한다.
서블릿 컨테이너는 WAS에서 제공하는 서비스 중 한 종류로 현재 필자가 사용하고 있는 것은 tomecat이니 이것의 서비스가 된다.
서블릿도 자바의 gc에 의해 수거될 수 있지만... 거의 수거되지 않는다.

여러 사용자들의 요청을 받고 응답을 주기 위해서는 서버는 자연스럽게 Thread(쓰레드)를 활용하게 된다고 한다.

어쨋든 서블릿은 컨테이너에 의해 
객체가 생성(단 한번)되고 초기화(단 한번)되며
요청에 대한 처리를 요청시마다 반복해서 진행하다가
제거(단 한번)된다.
이러한 과정을 라이프 사이클이라고 한다.
라이프 사이클이란 한 객체가 생성되어서 실행되고 소멸되기까지의 과정을 의미한다.

위와 같이 서블릿 라이프 사이클은 모두 컨테이너가 관리한다는 점을 기억하는 것이 중요하다.

Servlet 내용 언급 도중 웹 응용 프로그램이라고 하면 filter listener servlet 세 가지를 의미하는 것 이라고 한다.
*/

@WebServlet("/lifecycle")
public class LifeCycle extends HttpServlet {
	private static final long serialVersionUID = 1L;

	@Override
	public void init() throws ServletException {
		System.out.println("init() method call!!!!");
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doGet method call!!!!");
	}

	@Override
	public void destroy() {
		System.out.println("destroy() method call!!!!");
		// 해제 (close) 함수들 넣기
	} 
}
```
최초 요청시, 파일을 수정하고 요청시 init()가, 요청마다 doGet()이, 파일 수정마다 destroy()가 호출되는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/19484971/178307486-f79ccb94-be29-4e57-9a30-eb9da74491cf.png)

### DB Connection

+ JDBC를 활용하여 DB에 연동하는 예시 코드
	+ 필자의 경우 mysql을 연동하였다.
	+ `mysql-connector-java-8.0.24.jar` 과 같은 `jar`파일을 `WEB-INF`의 `lib`에 넣는 것도 잊지말자.

```
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/*

서블렛에서 현재 교육상 사용하고 있는 DB인 mysql을 접근하고 사용할 수 있다는 것을 보여주는 예제
홈페이지 방문마다 cnt를 1씩 증가시키고 해당 cnt를 페이지에 보여주는 간단한 화면을 보여준다.
이때 DB에 연결하기 위해 JDBC를 활용한다.

DML (I U D) : int cnt = pstmt.executeUpdate();
Query (S) : ResultSet rs = pstmt.executeQuery();
위의 의미는 insert, update, delete 작업시에는 executeUpdate를, 
select 작업시에는 executeQuery 함수를 사용하라는 의미이다.

보통은 아래의 작업이 진행된다.
Driver Loading은 초기화시 한번만 작동하면 되므로 init() 내에 있다.
1. data get

2. logic
	2-1. Driver Loading
	2-2. DB Connection (conn 생성)
	2-3. SQL 실행 준비
 		SQL문
		pstmt 생성 (치환변수 값 세팅)
	2-4. SQL 실행
		a. DML (I U D) : int cnt = pstmt.executeUpdate();
		b. Query (S) : 	ResultSet rs = pstmt.executeQuery();
						rs.next() [단독, if, while]
						rs.getXXX("col_name");
	2-5. DB close (역순으로 )
	
3. response page

 */

// 기존에는 web.xml에 해당 파일이 servlet이라는 것을 따로 등록해주었는데
// 아래의 어노테이션을 통해 자동으로 탐색되어 servlet으로 등록해준다. (4.0 이후 버전)
@WebServlet("/counter")
public class CounterServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	@Override
	public void init() throws ServletException {
		try {
//			2-1. Driver Loading
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	//	당신은 XXXXXXXX번째 방문자입니다.
	// 라고 적힌 화면을 응답 페이지로 반환한다.
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		1. data get
		
		int cnt = 0;
		int totalLen = 8;
		int zeroLen = 0;
		
//		DB Logic
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
//			2-2. DB Connection (conn 생성)
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/ssafyweb?serverTimezone=UTC&useUniCode=yes&characterEncoding=UTF-8", "ii200400", "dudtjs972972@");
			
//			2-3. SQL 실행 준비			
			String sql = "select cnt from counter";
			pstmt = conn.prepareStatement(sql);
			
//			2-4. SQL 실행
			rs = pstmt.executeQuery();
			rs.next();
			cnt = rs.getInt(1);
			pstmt.close();
			
			sql = "update counter set cnt = cnt + 1";
			pstmt = conn.prepareStatement(sql);
			pstmt.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
//			2-5. DB close (역순)
			try {
				if(rs != null)
					rs.close();
				if(pstmt != null)
					pstmt.close();
				if(conn != null)
					conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		
//		Business Logic
		String cntStr = cnt + ""; //"138"
		int cntLen = cntStr.length(); // 3
		zeroLen = totalLen - cntLen;
		
//		3. response page
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html>");
		out.println("	<body>");
		out.println("		<div align=\"center\">");
//		out.print("당신은 ");
		for(int i=0;i<zeroLen;i++)
			out.print("<img src=\"/bw/img/img_0.png\" width=\"80\">");
		for(int i=0;i<cntLen;i++)
			out.print("<img src=\"/bw/img/img_" + cntStr.charAt(i) + ".png\" width=\"80\">");
//		out.println("번째 방문자입니다.");
		out.println("		</div>");
		out.println("	</body>");
		out.println("</html>");
	}

}
```

### Servlets Parameter

+ 서블릿에서는 request를 통해서 사용자가 전송한 데이터를 받아온다.
	+ 단일 파라미터라면 `request.getParameter("key")`, 복수 파라미터라면 `request.getParameterValues("key")`를 활용한다.
	+ doPost의 경우에는 body에 데이터가 담겨 오기 때문에 데이터를 읽기 전에 꼭 `request.setCharacterEncoding("utf-8");` 을 작성하여야 한글을 잘 읽을 수 있다.

예시코드는 생략한다.

## JSP (Java Server Pages)

+ HTML 내에 자바코드를 삽입하여 웹 서버가 동적 페이지를 생성할 수 있도록 하는 `서버 사이드 스크립트 언어`이다.
	+ java EE 기능 중 일부로 웹 애플리케이션 서버에서 동작이 가능
	+ 자바 **서블릿으로 변환된 후 실행**된다, 때문에 기본적인 작동 방식은 servlet과 같다.
		+ jsp는 Scriptlet 기반 언어이지만 서블릿으로 한번 변환되면 서블릿은 Compile 기반 언어이기 때문에 Compile 언어의 특징도 가지고 있다. 두 가지 특징을 활용하여 서블릿으로 변환되기는 하나 서블릿과 크게 속도차이는 나지 않는다.
		+ `/.metadata\.plugins\org.eclipse.wst.server.core\tmp0\work\Catalina\localhost\???\org\apache\jsp` 에서 변환된 서블릿 파일을 찾아볼 수 있다.
	+ 서블릿과는 다르게 HTML 표준에서 작성되기 때문에 웹 페이지를 디자인하기 훨씬 편리하다는 장점이 있다.   
	+ JSTL등의 JSP 태그 라이브러리를 같이 사용하는 경우에는 자바 코딩없이 태그만으로 간략하게 작성이 가능해지므로 생산성을 더욱 높일 수 있다.
	+ 1999년 썬 마이크로시스템즈에서 배포하였으며 이와 유사한 구조로는 PHP, ASP, ASP.NET등이 있다. 

[ JSP 동작 흐름 사진 추가 요망]()

+ 더 알아보기
	+ Compile 기반 언어(서블릿)와 Scriptlet 기반 언어

### JSP 기본객체

+ jsp로 생성되는 서블릿은 컨테이너가 기본적으로 생성해주는 9개의 객체들이 있는데 이를 기본객체 또는 내장객체라고 한다.
	+ 이것들과 같이 .java에서 자동으로 생성되는 내장함수나 변수를은 개발자가 사용할 수 있다.

1. 요청(request)
2. 응답(response)
3. 출력(out)
4. 페이지(page)
5. 페이지 컨텍스트(pageContext)
6. 세션(session)
7. 서블릿 환경(config)
8. 어플리케이션(application)
9. 예외(exception)

+ JSP 기본객체 scope
[JSP 4개의 기본객체 scope 서술 요망]()

## JSP Scripting Element (JSP 스크립팅 요소)

jsp에서 자바코드를 삽입할 수 있는 문법을 알아야 작성이 가능하다. 이러한 문법들을 jsp 스크립팅 요소라고 한다.

### 1. 선언 (Declaration)

+ 멤버변수를 선언하거나 메소드를 선언할 때 사용한다.
	+ out 등의 객체가 없기 때문에 `out.println("aa");`와 같은 코드는 선언문에서 사용이 불가능하다.
	+ 이유는 servlet으로 변환되는 파일을 살펴보면 내장 객체보다 먼저 작성되어있기 때문이라는 것을 알 수 있다.

예시

```
<%! 선언 %>
```

예시는 아래와 같다.

```
 <%!
	 // 아래의 코드가 서블릿 자동 생성시, 선언부(전역)에 들어간다.
	 String name = "임영선";
	 private String str;

	 public void init(){
		name = "게으른 너구리";
	 }
 %>
```

### 2. 스크립트릿(Scriptlet)

+ 클라이언트 요청시 반복되어 호출되는 영역으로, 서블렛으로 변환시 service() 메소드에 해당(비즈니스 로직)하는 영역이다. 
  + request와 response를 활용하여 코드를 구현하게 된다.

예시

```
<% 스크립트릿 %>
```

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

+ 데이터 브라우저에 출력시 사용한다. 다른 요소들과는 다르게 세미콜론을 넣지 않는다.

예시

```
<%= 표현식 %>
```

위의 표현은 스크립트릿로도 작성이 가능하다.   
단, 세미콜론을 붙여야 한다는 점을 잊지말자!

`<% out.print(표현식); %>`

예시는 아래와 같다.

```
안녕하세요 <%= name %>

 ```

### 4. 주석 (Comment)

+ 코드 상에 부가 설명을 작성한다.
	+ html의 주석 `<!-- -->`과의 다른 점은 **Jsp의 주석은 서버에서 제외**시켜 클라이언트의 응답 html에는 보이지 않는데 html 주석은 보인다는 것이다.  

`<%-- 주석 --%>`

아래와 같이 html 주석 내에 jsp의 표현식을 넣으면 그대로 실행이 된다는 점도 있다.   
<!-- 이 글은 보이지 않지만.. 오른쪽 글은 보이게 된다. <%= name %> -->

## JSP 지시자 (Directive)

+ 서블릿 컨테이너에게 JSP를 통해 서블릿을 생성할 때 어떻게 생성할지에 관한 설정이나 명령을 의미한다. 

예시

```
<%@ directive_type attr1="value1" attr2="value2" %>
```

### 1. page Directive 

+ 컨테이너에게 현재 JSP 페이지를 어떻게 처리할 것인지에 대한 정보를 제공한다.
	+ 다양한 속성이 있지만 대표적인 것은 contentType, import, session 등이 있다.

`<%@ page attr1="value1" attr2="value2" %>`

+ 이클립스에서 JSP 파일을 생성하면 자동으로 나오는 아래의 코드가 바로 페이지 지시자에 해당한다.

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" %>
```

### 2. include Directive 

+ 특정 JSP 파일을 페이지에 포함시키는 지시자이다.   
+ 여러 JSP 페이지에서 반복적으로 사용되는 부분(일반적으로 header, footer, aside 등)을 jsp file로 만든 후 해당 지시자를 활용하면 반복되는 코드를 줄일 수 있다.

예시

`<%@ page file="/template/header.jsp" %>`

속성이 하나밖에 없다는 점이 개인적으로 편안하다.

### 3. taglib Directive 

+ JSTL 또는 사용자 커스텀 태그(custom tag)를 이용하고자 할 때 사용되며 JSP 페이지 내에 자바 코드를 삽입할 때 조금 더 간결하게 작성할 수 있다.

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

+ 서버에서 페이지를 이동시킬 때 사용하는 forward와 sendRedirect의 차이점
	+ 당연히 페이지를 이동시킨다는 점이 같고 여러 차이점이 존재한다.

이러한 차이점을 표로 정리해보면 아래와 같다.

|  | forward(request, response) | sendRedirect(location) |
| -- | -- | -- |
| 사용 방법 | RequestDispatcher dispatcher = request.getRequestDispatcher(path);<br>dispatcher.forward(request, response); | response.sendRedirect(location); |
| 이동 범위 | 동일 서버(project)내 경로 | 동일 서버 포함, 타 URL 가능. |
| location bar | 기존 URL 유지<br>(실재 이동되는 주소 확인 불가) | 이동하는 page로 주소가 갱신 |
| 객체 | 기존의 request와 response가 그대로 전달 | 기존의 request와 response는 소멸, 새로운 request와 response가 생성. |
| 속도 | 비교적 빠름 (1나노초 정도?) | forward에 비해 느림 |
| 데이터 유지 | request의 setAttribute(name, value)를 통해 전달 | request로는 data 저장 불가능, session이나 cookie를 이용 |

## 웹 디자인 패턴

+ JSP(혹은 서블릿)를 활용하여 구성할 수 있는 Web Application Architecture는 크게 model1과 model2로 나뉜다. 
	+ model1은 JSP(혹은 서블릿)가 클라이언트의 요청에 대한 로직 처리와 응답 페이지(response page/view)에 대한 처리를 모두 하는 구조
	+ Model2는 View는 JSP에서 Controller은 Servlet에서 처리하는 구조

![image](https://user-images.githubusercontent.com/19484971/178997491-5ca6af24-a775-4fd1-83bd-6ac283b659e5.png)

(MVC Model1)

![image](https://user-images.githubusercontent.com/19484971/178997512-290f796f-34c6-4f8a-9f7e-7361048f9a0a.png)

(MVC Model2)

### Model 2

Service/Dao/Java Beans(model), jsp(view), Servlet(controller)에 각 역할을 나누어 웹 프로그램을 만드는 프로그래밍 방법이다.

+ Model
	+ 컨트롤러로부터 데이터를 받아 로직을 처리하고 결과를 반환하는 역할이다.
	+ Service는 비즈니스 로직, DAO는 DB로직, Java Beans는 로직을 처리한 후 반환되는 객체를 저장하는 역할로 또 다시 나눠진다.
		+ DAO는 Data Access Object의 줄임말로 데이터베이스의 data에 접근하기 위한 객체이다.
	+ Java Beans는 DTO나 VO를 만드는데 활용되며 DTO(Data Transfer Object)는 로직을 가지지 않는 순수한 데이터 객체를, VO(Value Object)는.. DTO 객체의 값을 반환할 때 사용되는 객체.. 라고만 들었다. (잘 모르겠다.)
+ View
	+ 화면 처리를 담당한다. 
	+ JSP에서 담당하며 로직 처리는 모델이 해결해주기 때문에 결과 출력을 위한 자바코드만 사용하게 된다.
+ Controller
	+ 클라이언트의 요청을 분석하여 로직처리를 위한 모델을 호출하고 받은 결과를 뷰에 넘겨주며 필요에 따라 데이터를 request나 session에 저장하는 역할
	+ Servlet에서 담당하며 기본적으로 다른 자바파일을 호출하고 데이터를 관리하는 것이 중점이 되어있다.
	+ 상황에 따라 redirect 또는 forward로 JSP를 호출하여 화면을 출력하도록 한다.

Model2 과정은 다음과 같다.
1. 클라이언트가 데이터를 담아서 요청을 보낸다.
2. 서블릿이 클라이언트의 요청을 받아서 처리가 가능한 모델의 메소드를 호출한다.
3. 모델의 Service가 비즈니스 로직을, DAO가 비즈니스 로직 처리를 위한 DB 로직을, DataBase가 DB로직을 처리하기 위한 SQL문을 처리하고 결과를 (DTO 등으로) 만들어 반환한다.
4. 서블릿은 모델에서 받은 반환값을 받아 적절한 JSP을 호출하고 반환값을 넘겨준다.
5. JSP는 서블릿에서 받은 데이터를 토대로 화면을 만들어 서블릿에게 반환한다.
6. 서블릿은 JSP에서 받은 화면을 클라이언트에게 전송하여 응답을 마친다.

참고
+ https://velog.io/@ovan/MVC-Model1%EA%B3%BC-MVC-Model2
	+ 강의에서 설명할 때 사용한 그림은 캡쳐하면 안 될 것 같아 대신 블로그에서 사진을 가져왔다;

### 모델의 장단점

모델 1과 모델2의 장단점은 아래와 같다.

+ 모델 1
	+ 구조가 단순하고 직관적이라서 배우기 쉽다.
	+ 개발 시간이 비교적 짧아 개발 비용이 감소한다.
	+ 화면 출력을 위한 코드(FE)와 로직 처리를 위한 코드(BE)가 섞여있기 때문에 분업이 어렵다.
	+ JSP코드가 복잡해지고 프로젝트 규모가 커지게되면 유지보수가 어려워진다.
		+ 단순히 url 주소 하나를 바꾼다고 가정하면 많은 수정이 필요하다.
	+ 확장성(신기술 도입, 새로운 Framework 적용)이 나쁘다.
+ 모델 2
	+ 화면 출력을 위한 코드와 로직 처리를 위한 코드가 분리되어있기 때문에 분업이 용이하다.
	+ JSP 코드가 모델 1에 비해 덜 복잡하다.
	+ 기능에 따라 코드가 분리되어 유지보수가 쉽고 확장성이 늘어난다.
		+ 단순히 url 주소 하나를 바꾼다고 한다면 담당 Servlet에서 연결된 주소 하나만 바꾸면 된다.
	+ 구조가 복잡하여 초기 개발이 어렵고 따라서 초기 개발 비용도 증가한다.

## Front Controller

+ controller를 두 역할로 나누어 관리하는 방법
	+ 하나는 경로를 지정하는 controller, 다른 하나는 비즈니스 로직을 관리하는 controller로 나뉜다.
+ command 디자인패턴이라고도 한다.

## EL (Expression Language)

+ JSP 스크립트의 표현식`<%= %>`을 대신하여 속성값을 쉽게 출력하도록 고안된 언어
+ `${Map.key}` 혹은 `${Java Bean.property}`로 표현한다.
	+ EL 표현식 도트 연산자 왼쪽은 반드시 java.util.Map 혹은 Java Bean 객체여야 한다.
	+ EL 표현식 도트 연산자 오른쪽은 반드시 맵의 키이거나 Bean 속성명이여야 한다.
	+ 도트 표기법 이외에도 `[]`연산자를 사용하여 객체 값에 접근할 수도 있다.
		+ 일반적으로 `-` 등의 산술연산자 혹은 도트(프로퍼티명이 `student.name`)가 있다면 도트 표기법 대신 `[]`연산자를 사용한다.
		+ 배열이나 리스트의 경우 `[]`연산자 내의 인덱스 값은 문자열이 들어가도 숫자로 자동치환되어 처리된다.   
		  ex) `${array[1]}` 과 `${array["1"]}`은 같은 값을 가리킨다.

EL에서 제공하는 주기능은 아래와 같다.
1. JSP의 네가지 기본 객체가 제공하는 영역의 속성을 편리하게 사용
2. 자바 클래스 메소드 호출 기능
3. 표현 언어만의 기본객체 제공
4. 수지, 관계 논리 연산 제공

+ 참고
	+ [javatpoint.com](https://www.javatpoint.com/EL-expression-in-jsp)

### EL 내장객체

특이하게 pageContext를 제외하고 모두 Map이다.

| category | identifier | type | description |
| -- | -- | -- | -- |
| JSP | pageContext | Java Bean | 현재 페이지의 pageContext instance |
| scope | pageScope | Map | page 스코프에 저장된 객체 | 
| scope | requestScope | Map | request 스코프에 저장된 객체 | 
| scope | sessionScope | Map | session 스코프에 저장된 객체 | 
| scope | applicationScope | Map | application 스코프에 저장된 객체 | 
| 요청 매개변수 | param | Map | ServletRequest.getParameter(String)과 같은 객체 | 
| 요청 매개변수 | paramValues | Map | ServletRequest.getParameterValues(String)과 같은 객체 |
| 요청 헤더 | header | Map | HttpServletRequest.getHeader(String)과 같은 객체 |
| 요청 헤더 | headerValues | Map | HttpServletRequest.getHeaders(String)과 같은 객체 |
| 쿠키 | cookie | Map | HttpServletRequest.getCookies()과 같은 객체 |
| 초기화 매개변수 | initParam | Map | ServletContext.getInitParameter(String)과 같은 객체 |

+ `request.setAttribute("userInfo", "임영선");` 을 JSP에 전송하였을 때 아래의 코드로 불러올 수 있다.
	1. ${requestScope.userinfo}
	2. ${pageContext.request.userinfo}
	3. ${userinfo}
		+ property 명만 작성할 경우 자동으로 pageScope - requestScope - sessionScope - applicationScope 순으로 객체를 찾는다.
+ url?name=임영선&fruit=사과&fruit=바나나
	+ 이름을 가져오는 경우에는 ${param.name}
	+ 과일을 가져오는 경우에는 ${paramValues.fruit[0]}

### EL Operator

대부분은 자바와 같다.

| 카테로리 | 종류 |
| -- | -- |
| 객체 프로퍼티 | [], . |
| 함수 | () |
| 타당성 검사 | not, !, empty |
| 산술 | +, -, \*, /(div), %(mod) |
| 관계형 | <(lt), <=(le), >(gt), >=(ge), ==(eq), !=(ne) |
| 논리 | &&(and), ||(or) |
| 삼항 연산자 | 조건 ? 값1 : 값2 |

+ empty 연산자에서 true를 반환하는 경우는 아래와 같다.
	+ 값이 null인 경우
	+ 빈 문자열 `""`인 경우
	+ 길이가 0인 배열인 경우
	+ 빈 Map 객체인 경우
	+ 빈 Collection 객체인 경우

+ 함수 호출
	+ Java Bean 객체의 함수라면 get과 ()는 생략할 수 있다.
		+ 예를 들어 `user` 객체에 `getName()` 이라는 함수가 있다면 ${user.name} 과 같이 작성하여 데이터를 불러올 수 있다.

## JSTL (JSP Standard Tag Library)

+ Java EE 기반의 웹 애플리케이션 개발 플랫폼을 위한 컴포넌트 모음
+ 개발자가 직접 태그를 작성할 수 있는 기능(custom tag)을 활용하여 만든 것들 중 가장 많이 사용되는 것을 모아 만든 규약 혹은 라이브러리
+ xml 데이터 처리, 조건문, 반복문, 데이터베이스 등의 처리를 할 수 있다.
	+ 스크립트릿을 사용하지 않고 EL과 함께 코드를 더 간결하게 작성할 수 있다.
+ 자바 코드를 직접 사용하지 않고 로직을 내장하는 방법을 제공한다.
	+ 덕분에 코드의 유지보수가 쉬워졌다.
	+ 응용 소프트웨어 코드와 UI 코드를 나누어 관리하기 편해졌다.
+ JSP 2.1~2.2와 호환되는 JSTL 버전은 1.2으로 jstl에 대한 jar파일이 필요하다.
	+ 필자는 [mvnrepository](https://mvnrepository.com/artifact/javax.servlet/jstl/1.2)에서 다운로드하였다.

+ 참고
	+ https://docs.oracle.com/javaee/5/jstl/1.1/docs/tlddocs/
	+ https://www.tutorialspoint.com/jsp/jsp_standard_tag_library.htm

### JSTL Tag 선언

프로젝트에 jstl관련 jar 파일을 넣었다면 파일에 선언을 하고 jstl을 사용할 수 있다.

선언형식은 `<%@ taglib prefix="prefix" uri="uri" %>`이다.

| library | prefix | function | URI | 
| -- | -- | -- | -- |
| core | c | 변수지원, 흐름제어, URL 처리 | http://java.sun.com/jsp/jstl/core |
| XML | x | 변수지원, 흐름제어, URL 처리 | http://java.sun.com/jsp/jstl/core |
| 국제화 | fmt | 변수지원, 흐름제어, URL 처리 | http://java.sun.com/jsp/jstl/core |
| database | sql | 변수지원, 흐름제어, URL 처리 | http://java.sun.com/jsp/jstl/core |
| 함수 |  | 변수지원, 흐름제어, URL 처리 | http://java.sun.com/jsp/jstl/core |

+ 위의 선언에 따라서 core를 선언하여 사용하려면`<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`라고 작성하면 된다.
	+ 필자는 사실 core 밖에 사용하지 않아서 다른 라이브러리는 언급하지 않을 것 이다.
	+ `prefix`에는 꼭 `c`라고 적어야만 하는 것은 아니라서 원하는 값을 넣어도 되나, 통상적으로 `c`를 넣어 사용하기 때문에 가독성을 생각하면 다른 값을 넣는 것은 좋지 않다.

### jstl core Tag

시간이 없어서 정리를;;
커스텀 태그를 액션이라고 서술한다.

+ 변수선언 <c:set>
	+ 변수나 특정 객체의 프로퍼티에 값을 항당할 때 사용한다.
	+ value 속성의 값이나 태그내의 body content로 값을 설정한다.
	+ var 속성은 변수명을, 변수의 생존범위는 scope 속성(디폴트는 page)으로 설정한다.
	+ 특정 객체의 프로퍼티에 값을 할당할 때는 target 속성에 객체를 성정하고 property에 프로퍼티명을 설정한다.

![image](https://user-images.githubusercontent.com/19484971/179339332-68b45db6-9308-4227-8f5f-7171a20989b5.png)

+ 예외 <c:catch>
	+ 기본적으로 JSP 페이지는 예외가 발생하면 지정된 오류페이지를 통해 처리한다.
	+ 해당 액션은 JSP 페이지에서 예외가 발생하면 오류페이지로 넘지기 않고 직접 처리할 수 있도록 한다.
	+ var 속성에는 방생한 예외를 담는 (생존범위가 page인) 변수를 지정한다.
	+ <c:if>와 함께 사용하면 Java 코드의 try-catch와 같은 기능을 구현할 수 있다.

![image](https://user-images.githubusercontent.com/19484971/179339401-4eb057a9-ca77-45fd-8c7a-fdd0eefc9031.png)

+ 조건문 <c:if>, <c:choose> <c:when> <c:otherwise>
	+ test 속성에 지정된 표현식 결과가 true인 경우에 body에 담긴 컨텐츠를 수행한다.
	+ <c:if> 의 var 속성은 표현식의 결과를 담는 변수이다.
	+ <c:choose> <c:when> <c:otherwise>는 if-ifelse-else와 같이 처리할 수 있다.

![image](https://user-images.githubusercontent.com/19484971/179339438-8fbaec68-1b3f-46d7-a76d-cf494de8ece5.png)

+ 반복문 <c:forEach>
	+ java의 for문과 같은 액션이다.
	+ items 속성에는 컬렉션을 지정하는데 이는 Array, Collection, Map 또는 콤마로 분리된 문자열을 의미한다.
	+ var 속성에는 반복에 대한 현재 데이터를 담는 변수를 지정한다.
	+ varStatus 속성을 통해 현재 반복에 대한 상태 정보를 가져올 수 있다.

![image](https://user-images.githubusercontent.com/19484971/179339502-d13a1c08-da9e-4ca3-9fd2-4fbec84d940a.png)

원래 사진을 직접 찍으려고 했는데 생략..! 프로젝트를 위해서 스프링 공부도 해야한다!
