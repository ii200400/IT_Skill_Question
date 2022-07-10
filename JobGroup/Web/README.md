# 3-3 Web

+ 미생성

## 개요

기본적으로 사용되는 HTML5 웹 문서는 3가지 구성요소가 있다.

+ HTML5(Hyper Text Markup Language)   
  기본적인 Markup Language 에 링크의 기능을 추가한 마크업 언어.
  웹 페이지의 문서 구조 담당
+ CSS(Cascading Style Sheets)   
  웹 페이지의 디자인(표현)을 담당
+ JS(JavaScript)   
  웹 페이지의 이벤트 담당

## HTML5 (Hyper Text Markup Language)

마크업 언어(markup language)로 태그(tag)를 사용하여 문서의 구조를 기술한다.

+ 태그(tag)를 기준으로 문서가 작성된다.
	+ 태그는 시작 태그와 종료 태그가 있는데 `/`로 구분한다.
	+ 시작 태그만 있는 경우도 있다. ex)<br/>
+ 각 태그는 속성과 속성 값을 가진다.
	+ <a href="url">link</a> 에서 `href`는 속성이름, `"url"`은 속성 값이 된다.
	+ 글로벌 속성(global attribute)이라는, 어느 태그에나 사용할 수 있는 속성이 있다.
		+ 대표적으로 `class`와 `id`가 있다, `dir`, `style`, `title`등도 있다.
		+ `class`는 중복이 가능한 속성으로 css에서 주로 사용한다.
		+ `id`는 중복이 불가능한 속성으로 JS에서 주로 사용한다.
+ 특수문자는 별도의 표기법이 있다.
	+ 대표적으로 `&`는 `&amp;`를 통해 작성할 수 있다.
		+ `&`는 get방식의 데이터 요청시, 쿼리스트링에서 파라미터 구분자로 쓰이기 때문에 자주 쓰인다고 한다.
	+ `<p>이번 과정의 &apos;교재 &apos;는 &lt;html &amp; css&gt;입니다.</p>`
	+ <p>이번 과정의 &apos;교재 &apos;는 &lt;html &amp; css&gt;입니다.</p>

### 기본 문법

1. 문서는 항상 xml의 버전과 인코딩을 명시하는 아래와 비슷한 코드로 시작해야 한다.   
   ex) <?xml version="1.1" encoding="UTF-8"?>
2. 반드시 root element가 존재해야 한다.   
   나머지 태그들은 Tree 형태로 구성된다.
3. 시작 태그와 종료 태그는 일치해야 한다.   
   ex) <tag> ~~ </tag>
4. 시작 태그는 key-value 구조의 속성(attribute)을 가질 수 있다.    
   값은 "" 또는 ''로 묶어서 표현한다.   
   ex) <tag key="value"> ~~ </tag>
5. 태그는 대소문자를 구별한다.  
6. 주석은 `<!-- -->`으로 작성이 가능하다.   
   웹 페이지에서는 보이지 않지만 '소스보기'에서는 보이므로 주의하자. 

elements(요소)에 대한 내용은 w3schools에 잘 정리되어있어서 자세히 서술하지 않을 예정이다. 아무리 정리해도 저 페이지보다 더 잘 정리 못하고 더 잘 정리 할 필요도 없다.

교수님은 Emmet(에밋)을 활용해서 빠르게 작성하시곤 했는데 익숙하지 않아서 그런가? 잘 사용을 못 했다.

### 포맷팅 요소

포맷팅 요소는 개인적으로는 웹 페이지에서 사용하기 보다는.. 깃허브 정리글에 더 자주 썼던 것 같다.

#### 예시

```
<blockquote>
	<abbr title="Internet of Things"><mark>IoT</mark></abbr>란 인터넷을 기반으로 모든 사물을 연결하여 정보를
	상호 소통하는 지능형 기술 및 서비스.<br>
	(출처 : <q cite="https://terms.naver.com/alikeMeaning.nhn?query=E00273180">Naver 지식백과</q>)
</blockquote>
<hr>
<strong>의미있는 글자</strong>를 굵게 할 때는 &lt;strong&gt;, <b>단순 글자</b>를 굵게 할 때는 &lt;b&gt;를 씁니다.<br>
<em>의미있는 글자</em>를 비스듬히 할 때는 &lt;em&gt;, <i>단순 글자</i>를 비스듬히 할 때는 &lt;i&gt;를 씁니다.
```

![image](https://user-images.githubusercontent.com/19484971/175944997-4ea587ec-6c0e-4abc-b199-f1f2157383ff.png)

+ 참고
	+ https://www.w3schools.com/html/html_formatting.asp

### 목록형 요소

unordered list(ul)와 ordered list(ol)이 대표적이다.   

#### 예시

```
<ul>
	<li>Oracle</li>
	<li style="list-style-type: circle">Java</li>
	<li style="list-style-type: square">HTML5</li>
	<li style="list-style-type: disc">CSS3</li>
</ul>

<ol>
	<li>Oracle</li>
	<li>Java</li>
	<li>HTML5</li>
	<li>CSS3</li>
</ol>

<ol type="a">
	<li>Oracle</li>
	<li>Java</li>
	<li>HTML5</li>
	<li>CSS3</li>
</ol>
```
![image](https://user-images.githubusercontent.com/19484971/175946078-3c17f84e-8614-4aa3-ae53-86a13283451e.png)

+ 참고
	+ https://www.w3schools.com/html/html_lists.asp

### 테이블 요소

본인은 기본적으로 `table`, `tr`, `th`, `td` 만 기억한다, 일반적으로 복붙해서 내용만 넣어 사용하기 때문이다.

`colspan`과 `rowspan` 속성은 항상 어떻게 합치는지 햇갈린다;;   

참고로 table로 만들 수 있는 것은 div로도 만들 수 있다, 둘의 가장 큰 차이는 table의 경우 테이블 내 모든 데이터가 로딩이 되어야 화면에 표시되지만 div의 경우에는 각 데이터가 로딩이 될 때마다 화면에 표시해준다.   
그래서 데이터가 많은 경우에는 div를 사용하는 경우도 있다고 한다.

#### 예시

```
<table border="1px">
	<caption>
		[[insert Title]]
	</caption>
	<thead>
		<tr>
			<th>title 1</th>
			<th>title 2</th>
			<th>title 3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>data 1</td>
			<td>data 2</td>
			<td>data 3</td>
		</tr>
		<tr>
			<td>data 4</td>
			<td>data 5</td>
			<td>data 6</td>
		</tr>
	</tbody>
</table>
```
![image](https://user-images.githubusercontent.com/19484971/175981955-b43fe2e6-2ab7-45c1-b70e-0ebe2e46e533.png)

+ 참고
	+ [w3schools_html_tables](https://www.w3schools.com/html/html_tables.asp)

### 이미지 요소

`src` 속성에 상대/절대 경로를 넣어 이미지를 불러오기 위해 사용하는 요소이다.

보통 CSS 함께 사용하여 너비나 높이, float를 지정한다.

#### 예시

```
<div align="center">
	<img
		src="https://upload.wikimedia.org/wikipedia/commons/2/29/Data_stack.svg"
		title="스택입니다."
		width="300"
		height="200"
		alt="참 이쁘네요."
	/>
</div>
```
![image](https://user-images.githubusercontent.com/19484971/175970996-ab78c941-04ad-42ba-b23b-3c4e20388ace.png)

+ 참고
	+ [w3schools_html_images](https://www.w3schools.com/html/html_images.asp)

### 링크 요소

Anchor를 뜻하는 a태그를 이용해서 다른 문서를 연결한다.

+ target 속성
	+ _self : 링크를 새 창이나 탭에서 연다.
	+ _blank : 현재 화면에서 링크를 연다.

#### 예시

```
<h2>관련 사이트</h2>
<a href="http://www.naver.com" target="_self">네이버</a><br>
<a href="http://www.daum.net">다음</a><br>
<a href="http://www.nate.com">네이트</a><br>
<a href="http://www.google.com" target="_blank">구글</a><br>
```
![image](https://user-images.githubusercontent.com/19484971/175974249-4e759dd8-78f2-47ad-953b-18dc26279b50.png)

#### bookmark 예시

`#`을 이용하여 특정 id가 있는 위치로 이동시킬 수 있다.   
개인적으로는 깃헙에서 목차를 만들 때 자주 쓴다.

```
<ul id="menu">
	<li><a href="#content1">내용1</a></li>
	<li><a href="#content2">내용2</a></li>
	<li><a href="#content3">내용3</a></li>
</ul>

<h3 id="content1">내용 1</h3>
<p>내용이 상당히 길다.......</p>

<p><a href="#menu">메뉴로이동</a></p>

<h3 id="content2">내용 2</h3>
<p>내용이 상당히 길다.......</p>

<p><a href="#menu">메뉴로이동</a></p>

<h3 id="content3">내용 3</h3>
<p>내용이 상당히 길다.......</p>
```
![image](https://user-images.githubusercontent.com/19484971/175975231-e0bb7998-5d8c-4ec0-b3ae-1b18e70fd5cc.png)


+ 참고
	+ [w3schools_html_links](https://www.w3schools.com/html/html_links.asp)

### 폼 요소

사용자로부터 데이터를 입력받아 서버로 전송하기 위해 사용한다.   
이때 서버로 데이터를 전송하는 것을 submit이라고 한다.

+ method 속성
	+ GET : 주소창에 사용자의 입력데이터가 쿼리스트링으로 전달된다, 길이 제한이 있을 수 있다.
	+ POST : HTTP 메시지의 body에 사용자 입력데이터가 담겨 전송된다, 직접적으로 노출되지 않는다.
+ action 속성
	+ 입력데이터를 처리할 서버의 파일이나 프로그램을 지정한다.
+ name 속성
	+ 클라이언트에서 특정 데이터에 붙이는 이름, 서버에서 데이터를 구별할 때 사용한다.

+ input 태그
	+ 사용자 입력을 받는 대표적인 태그, form 태그가 없어도 사용이 가능하다.
	+ input에는 다양한 type이 있는데 type마다 사용방법을 알아야 원활히 쓸 수 있다.
		+ image type은 submit이 2번 작동되는 문제가 있다고 한다, 굳이 버튼에 이미지를 넣을 생각을 하지 않아서 문제가 일어나는 것은 확인하지 못하였다. 
		+ button 태그에도 위와 같은 문제가 있다고 한다.
		+ file type은 꼭 post method와 enctype="multipart/form-data"를 사용해야 전송이 잘 된다.
	+ w3schools에서 각 타입의 작동 방식을 보는 것을 추천한다.

#### 예시

```
<h2>form control - input</h2>
<form method="post" action="login.jsp">
	<fieldset>
		<label for="userid">아이디 : </label>
		<input type="text" id="userid" name="userid" size="10" maxlength="16" value="아이디입력">
		<label for="pass">비밀번호 : </label>
		<input type="text" id="pass" name="pass" size="10" maxlength="16" placeholder="비밀번호입력">
		<input type="submit" value="로그인">
	</fieldset>
</form>
```
![image](https://user-images.githubusercontent.com/19484971/175980294-4584478e-b221-4707-9e5c-40c27cdeeb29.png)

+ 참고
	+ https://www.w3schools.com/html/html_forms.asp

### 블록/인라인 요소

태그는 크게 block과 inline 형식으로 나눌 수 있다.

+ Block-level Elements
	+ 항상 새 줄에서 시작하고 자동으로 요소 앞뒤에 약간의 공백(여백)을 추가한다.
	+ 대표적으로 `div`태그가 있다.
+ Inline Elements
	+ 새 줄에서 시작하지 않는다.
	+ 대표적으로 `span`태그가 있다.

#### 예시

```
<div class="ssa3">SSA 3기</div>
<div class="ssa4">SSA 4기</div>
<div class="ssa5">SSA 5기</div>

<span class="ssa3">SSA 3기</span>
<span class="ssa4">SSA 4기</span>
<span class="ssa5">SSA 5기</span>
```
![image](https://user-images.githubusercontent.com/19484971/175994078-9bf07233-711f-41b6-94b8-fa96e41989d3.png)

+ 참고
	+ https://www.w3schools.com/html/html_blocks.asp

## XML

태그를 이용해서 문서나 데이터 구조를 명시하는 Markup Language 중 하나이다.

+ 사용자가 태그를 정의해서 작성이 가능하다. 
	+ 위의 특성으로 `Extensible Markup Language` 라고도 한다. 
	+ 단, Html에 비해 정확한 문법을 준수해야만 작동이 된다.

본인은 단순하게 데이터 송수신 문서로 생각하고 있다. 실재로 공공데이터 api에서도 제공하는 파일 형식으로 가장 자주 봤기 때문;

### DTD, Schema

통일된 xml을 만들기 위해 만드는 xml 작성 규칙이나 양식을 적어놓은 문서를 의미한다.
프로젝트마다, 통신마다 다를 수 있으며 원활한 데이터 송수신을 위해 해당 작업을 하는 사람들이 참고하는 문서이다.

이러한 문서를 잘 따른 문서를 valid라고 한다.

[DTD Turotial](https://www.w3schools.com/xml/xml_dtd_intro.asp)을 참고하면 이해가 조금 더 쉽다.

## CSS(Cascading Style Sheets)

단순히 내용을 보여주는 HTML5의 표현 방식을 정하는 부분이다.   
선택자(selector)와 선언(declaration)으로 구성된다.
+ 선택자 : 규칙이 적용되는 요소들
+ 선언 : 선택자에 적용될 스타일

![image](https://www.w3schools.com/css/img_selector.gif)   
출처 : [w3schools_css_syntax](https://www.w3schools.com/css/css_syntax.asp)

+ CSS의 적용 우선순위
	+ 마지막 규칙 < 구체적인 규칙 < !important가 우선 적용.
		+ 적용 우선순위를 잘 알지 못하면 적용이 안되는 상황을 이해하지 못할 수 있다.
		+ 구체적인 규칙이란.. 전체 선택자 < 타입 선택자 < 클래스 선택자 < ID 선택자

내용이 너무 많으므로 선택자만 정리하고 넘어가겠다.

### CSS 적용 방법

3가지 방법으로 CSS를 적용할 수 있다.   
각각 외부 CSS(External CSS), 내부 CSS(Internal CSS), 인라인 CSS(Inline CSS)라고 한다.

참고로 3가지 혼합해서 작성이 가능하다. 한 가지의 방법으로만 사용해야 하는 것은 아니다.

```
<!-- /css 폴더에 .css 파일을 작성하고 로딩하여 css를 적용하는 방법(외부 스타일 시트) -->
<head>
	...
	<link rel="stylesheet" type="text/css" href="../css/4-1.css">
</head>

<!-- style 태그를 사용하여 css을 적용하는 방법(내부 스타일 시트) -->
<head>
	...
	<style type="text/css" media="screen">
		/* 아래와 같이 외부의 파일을 불러올 수도 있다. */
		@import url("../css/4-1.css");	
		/* @import "../css/4-1.css"; */

		/* 이렇게 현재 파일에 직접 style을 작성할 수 있다. */
		h2 {
			background-color: orange;
		}
	</style>
</head>

<!-- style 속성을 직접 사용하여 스타일을 적용하는 방법(인라인 스타일 시트) -->
<body>
	<h2 style="color: magenta;">Inline Style Sheet</h2>
	<p style="background-color: skyblue; color: purple;">Using Inline
		Style Sheet !!!</p>
</body>
```

+ 참고
	+ https://www.w3schools.com/css/css_syntax.asp

### 선택자

위에서 말했던 선언의 스타일이 적용될 요소들을 의미한다.   
설명을 작성하려고는 했는데.. CSS Selector Reference에 너무 잘 정리 되어있어서 예시만 간단하게 추가하겠다;

#### 예시

CSS 우선순위까지 고려해야되어서 조금 복잡하지만 하나씩보면 이해가 간다.

```
<head>
	<meta charset="UTF-8">
	<title>Descendant Selector(하위선택자)</title>

	<style type="text/css">
		div div {
			background: blue;
			color: red;
		}

		div p {
			background: lightgray;
			color: skyblue;
		}

		div>div {
			background: green;
			color: orange;
		}

		div>p {
			background: purple;
			color: pink;
		}
	</style>
</head>

<body>
	<div>div Descendant Selector div
		<p>div > p Descendant Selector p</p>
		<div>div div Descendant Selector
			<span>
				<div>
					<ul>
						<li>
							<p>div p Descendant Selector</p>
						</li>
					</ul>
				</div>
			</span>
		</div>
		<div>div div Descendant Selector2
		</div>
	</div>
</body>
```
![image](https://user-images.githubusercontent.com/19484971/176006370-b770042f-f483-4e95-8ec0-0553a3601c26.png)

으어.. 예시가 복잡하다;;   
어쨋든 위와 같은 느낌으로 마우스가 올라간 태그, 특정 속성을 가진 태그 등의 선택자 지정이 가능하다.
 
+ 참고
	+ https://www.w3schools.com/css/css_selectors.asp
	+ https://www.w3schools.com/cssref/css_selectors.asp

## DB (데이터 베이스)

자세한 DB이론은 [이곳에서](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database) 다룰 것이고 여기에서는 웹에서 디비가 어떤 역할을 맡고 어떻게 활용되고 있는지를 중점으로 서술하겠다.

웹에서는 요청에 대한 응답에 필요한 데이터나 사용자가 작성한 데이터를 저장하기 위해 사용한다.

jdbc를 어디에 넣어야 할지 모르겠네;; 아이고난;;
자바로 디비를 컨트롤하는 기능..? 이라고 생각하고 있다.

## cookie session

클라이언트의 요청에 대한 서버의 응답 직후 연결이 끊어지는 http 특징(stateless)으로 인해 같은 클라이언트가 요청을 해도 서버는 이전과 지금의 클라이언트가 같은지 알 수 있는 방법이 없다. 이와 같은 문제를 해결하기 위해 Cookie와 Session을 사용한다.

로그인 했다고 연결이 되어있다는 것이 아니고 request를 보내고 response를 받을 때까지만 연결을 하는 이유는 웹은 세계의 모든 사람들이 접근 가능한데, 한 번 연결했다고 계속 연결이 유지되면 메모리 자원이 빠르게 고갈되기 때문이라고 한다.

### 쿠키

서버와 통신하는 **클라이언트에 저장**되는 자그마한 데이터이다.   
클라이언트에 텍스트 파일형식으로 key와 value 쌍의 문자열(String) 형태로 저장된다.

브라우저(IE, 크롬, 파이어폭스..)가 클라이언트의 별도 요청 없이도 항상 Request Header에 쿠키를 넣어 서버로 전송하며 브라우저마다 쿠키를 따로 관리하기 때문에 브라우저가 다르면 쿠키도 다르고 서버는 다른 클라이언트라고 인식한다. 

쿠키는 

쿠키를 사용하는 이유는 아래와 같다.
1. 서버가 알아야할 정보(세션관리 정보 등)를 저장
2. 사용자 편의를 위해 (ID 저장, 일주일간 다시보지 않기)
3. 사용자마다 적절한 페이지 표시 (최근 검색한 상품 목록, 광고)
4. 트래킹(사용자의 행동과 패턴을 분석하고 기록)

동작순서

### Session

클라이언트가 웹 서버에 연결되어 있는 상태를 의미한다.   
WAS는 메모리에 객체 형태로 세션을 관리하며 메모리가 허용되는한 제한없이 저장이 가능하다.

일반적으로는 서버에서 클라이언트의 정보를 일정기간 저장하기 위해 사용하며 대표적으로는 로그인 유지나 장바구니 품목 관리에 쓰인다.


## 웹 디자인 패턴

JSP(혹은 서블릿)를 활용하여 구성할 수 있는 Web Application Architecture는 크게 model1과 model2로 나뉜다. 

전자는 JSP(혹은 서블릿)가 클라이언트의 요청에 대한 로직 처리와 응답 페이지(response page/view)에 대한 처리를 모두 하는 것을, 후자는 JSP가 요청에 대한 응답 페이지에 대한 처리만 하는 것을 의미한다.

필자가 이전에 BE에 올려두었던 아키텍쳐 사진들은 모두 모델1 방식의 아키택쳐이다. Servlet이나 JSP가 요청을 받고 (자바 빈즈를 활용하거나) DB의 데이터를 참고해서 응답 페이지를 만들고 응답해주는 형식인 것을 볼 수 있다.

모델1에 대해서는 충분히 알아봤으니 이 아래부터는 MVC 패턴을 웹개발에 도입한 모델2에 대해 정리를 진행할 예정이다.

### 웹의 MVC 패턴 (Model 2)

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

그림을 그리면 아래와 같다.

[바쁘다, 나중에 사진 추가 요망..]()

위 사진의 과정은 다음과 같다.
1. 클라이언트가 데이터를 담아서 요청을 보낸다.
2. 서블릿이 클라이언트의 요청을 받아서 처리가 가능한 모델의 메소드를 호출한다.
3. 모델의 Service가 비즈니스 로직을, DAO가 비즈니스 로직 처리를 위한 DB 로직을, DataBase가 DB로직을 처리하기 위한 SQL문을 처리하고 결과를 (DTO 등으로) 만들어 반환한다.
4. 서블릿은 모델에서 받은 반환값을 토대로 적절한 JSP을 호출한다.
5. JSP는 서블릿에서 받은 데이터를 토대로 화면을 만들어 서블릿에게 반환한다.
6. 서블릿은 JSP에서 받은 화면을 클라이언트에게 전송하여 응답을 마친다.

#### 모델의 장단점

모델 1과 모델2의 장단점은 아래와 같다.

+ 모델 1
	+ 구조가 단순하고 직관적이라서 배우기 쉽다.
	+ 개발 시간이 비교적 짧아 개발 비용이 감소한다.
	+ 화면 출력을 위한 코드(FE)와 로직 처리를 위한 코드(BE)가 섞여있기 때문에 분업이 어렵다.
	+ JSP코드가 복잡해지고 프로젝트 규모가 커지게되면 유지보수가 어려워진다.
	+ 확장성(신기술 도입, 새로운 Framework 적용)이 나쁘다.
+ 모델 2
	+ 화면 출력을 위한 코드와 로직 처리를 위한 코드가 분리되어있기 때문에 분업이 용이하다.
	+ JSP 코드가 모델 1에 비해 덜 복잡하다.
	+ 기능에 따라 코드가 분리되어 유지보수가 쉽고 확장성이 늘어난다.
	+ 구조가 복잡하여 초기 개발이 어렵고 따라서 초기 개발 비용도 증가한다.

### Front Controller

command 디자인패턴이라고도 한다.
controller를 두 역할로 나누어 관리하는 방법을 의미한다
하나는 경로를 지정하는 controller, 다른 하나는 비즈니스 로직을 관리하는 controller로 나뉜다.

### EL (Expression Language)


### JSTL (JSP Standard Tag Library)


