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
	
## JavaScript

단순히 보면 다양한 코딩 언어 중 하나지만, 웹에서는 변칙적인 사용자들의 입력에 대응하여 웹 페이지가 다양한 반응을 보일 수 있도록 만들어준다.

### 1. 개요

프로토타입 기반의 스크립트 프로그래밍 언어이자 인터프리터 언어

+ 기본적으로 ECMA(European Computer Manufacturers Association) Script 라는 유럽의 컴퓨터 제조 연합..?에서 채택한 기술 규격을 기본으로 한다.
+ 특징
	+ 객체지향 등의 여러 프로그래밍 패러다임을 지원

HTML, CSS와 더불어 웹을 구성하는 요소 중 하나로 접하는 경우가 많으며 필자는 웹을 공부하면서 자바스크립트를 공부하고 정리할 것이기 때문에 바닐라 자바스크립트 보다는 웹에서의 자바스크립트 기준으로 서술할 것이다.

### 2-1. JavaScript 선언

크게 아래의 두 가지 방법이 있다.

+ 1. `script` 태그를 이용해서 HTML문서 내부에 js를 넣는 방법
+ 2. `script` 태그의 src 속성을 활용하여 외부 파일의 js를 불러오는 방법

두 가지 방법을 모두 사용하는 경우에는 외부 파일이 HTML 내부에서 작성한 js를 덮어쓰게 되므로 꼭 하나의 방법만을 사용하여야 한다. 아래와 같이 사용하면 script 내부의 코드는 무시된다.   
		
	<script src="hello.js" type="text/javascript">
		console.log("1, " + x);
		...
	</script>

`script`태그는 HTML문서 어디든 선언이 가능하나, 일반적으로 `head`나 `body` 내부에 작성한다. js로 인해 로딩이 늦게 되는 상황을 미연에 방지하기 위해 `body` 태그 내의 가장 끝부분에 작성하는 경우도 있다.

[2-1, 2-2 코드 링크 추가 요망]()

### 3-1. 주석

코드에 대한 부연설명을 작성하는 부분으로 한 줄 주석과 블록 주석이 있다.   
전자는 `//`로 후자는 `/* */`로 표기한다.

일반적으로 에디터에서는 `ctrl + /`으로 주석을 추가할 수 있다는 것이 더 좋은 정보이다.

### 3-2. 변수

자바 스크립트는 변수와 함수 이름이 혼동되지 않도록 변수에는 형용사/명사를, 함수에는 동사를 사용하도록 권장한다. 예를 들어 isSelected/getCount는 함수명으로 selected/count는 변수명으로 사용한다.   

키워드, 공백 문자를 포함하지 않고 숫자로 시작하지 않고, \_와 \$을 포함이 가능한 이름이 가능하다. 또한 낙타 표기법(영어 소문자를 기본으로 작성하되 두번째 단어부터는 첫 알파벳을 대문자로 표기하는 방식)을 기본으로 사용한다. 

#### var keyword & Dynamic Typing

자바 스크립트는 변수를 선언할 때 타입을 명시하지 않으면서 어떤 타입이라도 사용 가능한 var 키워드가 (왜인지) 기본적으로 사용되며 다른 형의 자료형까지도 재선언 및 중복 선언이 가능하다.

또한 동적 타이핑을 통해 서로 다른 형 끼리의 형 변환이 자유롭고 서로 다른 형끼리의 연산도 가능하므로 사용하고 있는 변수에 대한 숙지가 필수적이다.

_때문에 무슨 타입인지 개발자도 모르는 경우가 발생한다._

#### Variable Hoisting (변수 호이스팅)

js에는 모든 선언(변수와 함수 선언)이 해당 Scope의 처음에 위치한 것 처럼 작동을 하는 특성을 의미한다.

즉, 아래줄에 선언이 되어있어도 윗줄에서 출력이 가능하다, 물론 초기화가 되어있지 않기 때문에 undefined가 출력된다.

[ 3-6 링크 추가 요망]()

### 3-3 자료형

js에는 자료형을 크게 원시 타입(primitive type)과 객체 타입(object type)으로 분류한다. 원시 타입은 아래의 표에 적힌 5가지 자료형이고 이를 제외한 자료형들은 모두 객체 타입으로 분류된다.

| 자료형 | typeof 출력 값 | 설명 | 
|--------|-----|-----|
| 숫자형 | number | 정수 또는 실수형 |
| 문자열형 | string | 말 그대로 문자열, `'` 혹은 `"`으로 감싸 표기 | 
| boolean형 | boolean | 참/거짓 |
| undefined | undefined | 변수가 선언되었지만 초기화가 되지 않은 경우 | 
| null | object | 값이 존재하지 않는 경우 |

_왜.. null 자료형은 typeof 출력값이 object 인 것이냐.._

+ 숫자형   
	js는 정수만 표현하는 자료형은 존재하지 않는다, 무조건 실수이다.   
	다른 언어와 다르게 0으로 나누는 연산에 대해 에러를 내뿜지 않는 대신 특별한 상수(Infinity, NaN)를 반환한다.   

+ 문자열   
	문자 하나를 나타내는 자료형은 없다.   
	`'`와 `"`를 구분하지 않고 사용이 가능하다.

+ boolean
  비교 연산에서 null, ''(빈 문자열), undefined, 0은 모두 false 취급을 받는다.
	
null과 undefined는 분명하게 다르므로 구분을 잘하자.

[3-2 ~ 3-5  링크 추가 요망]()

### 3-4. const & let

ECMA Script6부터 const와 let 키워드가 추가되어 상수를 사용할 수 있다고 한다.   

const의 경우에는 상수이기 때문에 당연히 초기화 이후 읽기만 가능하다.   
또한, 모든 문자를 대문자로 작성하고 단어 사이에는 `_`을 사용하는 변수와는 다른 명명 규칙이 있다.

let은.. 명명 규칙은 var과 같고 여타 다른 언어의 변수와 같다.   
개인적으로는 let을 알게된 이후로는 var은 안 쓰고 let만 사용한다.

차이점을 표로 정리하면 다음과 같다.

| 키워드 | 구분 | 선언위치 | 재선언 |
|---|----|----|----|
| var | 변수 | 전역 스코프 | 가능 |
| let | 변수 | 해당 스코프 | 불가능 |
| const | 상수 | 해당 스코프 | 불가능 | 

참고로 필자는 전역 스코프는 전역 변수,  해당 스코프는 지역 변수로 이해하고 넘어갔다. 

[3-7, 3-8  링크 추가 요망]()

### 3-5. 연산자

코틀린과 비슷한 부분이 많아서 본인은 쉽게 기억할 것 같다.

for, if, switch 문은 생략한다.

### 3-8 객체

객체는 이름과 값으로 구성된 프로퍼티의 집합
일급 객체

객체 생성 3가지 방법
객체 리터럴로 객체를 생성
Object로 객체를 생성후 프로퍼티를 추가
객체 생성 함수 구현

객체의 속성은 dot`.`이나 대괄호`[]`를 사용해서 접근한다.

객체의 종류가 많은데
가장 중요한 것은 DOM이라고 한다.

3-9 함수

var과 비슷하게 함수도 함수 호이스팅 기능이 있다.
정확히 말하자면 자바 스크립트는 모든 선언에 대해서 호이스팅 기능을 제공한다고 한다.

일급객체
var 변수에 함수

콜백함수는 특정 이벤트가 발생했을 때 시스템에 의해 호출되는 함수를 의미한다.
일반적으로는 콜백함수는 매개변수를 통해서 전달되고 이벤트에 따라 특정 시점에 실행된다.
주로 비동기 처리에서 사용되는데, 콜백의 콜백이 사용되는 구조로 인해 콜백지옥이라는 말이 있다고 한다. 본인은 2중까지밖에 안해서 지옥까지 보지는 않았다.

4-2 window 객체

브라우저에서 창을 띄우는 방법이 있지만 요즘에는 모달 창을 더 많이 이용한다고 한다.

4-3 새 창 열기

창 

5-2 문서 객체 만들기

아따 진짜 설명 엄청 많네..
6-4 이벤트 핸들러 등록

인라인 이벤트 핸들러 방식은 점차 사용하지 않는 추세였지만, 간단한 이벤트의 경우에는 아직 해당 방식으로 처리하고 있다고 한다.

7 web storage (웹 스토리지)

데이터를 사용자 로컬에 보존하는 방식으로, 자바스크립트만을 통해서 조작이 가능하다.
기본적으로 key-value 세트로 저장이 되며 도메인과 브라우저 별로 문자열 형식으로 저장이 된다.

쿠키와 다른점은..   
유효기간이 없고 영구적으로 이용이 가능하며   
브라우저에 따라 다르지만 5MB까지 사용이 가능하다.   
또한 네트워크 요청 시 서버로 전송이 되지 않으며.. 어쩌구

localStorage는..

sessionStorage는
저장되는 위치만 달라질 뿐 위와 같은데 같은 세션에서만 사용가능하다.   
여기서 세션은 아마.. 서버와 통신할 때 사용하는 무언가로 기억한다, 통신 때마다 값이 달라져서 현재 통신 때만 사용이 가능하다는 의미 같다.

## DB (데이터 베이스)

자세한 DB이론은 [이곳에서](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database) 다룰 것이고 여기에서는 웹에서 디비가 어떤 역할을 맡고 어떻게 활용되고 있는지를 중점으로 서술하겠다.

웹에서는 요청에 대한 응답에 필요한 데이터나 사용자가 작성한 데이터를 저장하기 위해 사용한다.

jdbc를 어디에 넣어야 할지 모르겠네;; 아이고난;;
자바로 디비를 컨트롤하는 기능..? 이라고 생각하고 있다.

## Back End

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

### Servlet

백엔드에서 사용하는 자바파일의 일종, 해당 파일만으로는 웹 페이지를 구현하기 크게 힘들어서 아래의 jsp와 같이 활용한다.

#### Servlet LifeCycle

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

### JSP (Java Server Pages)

HTML 내에 자바코드를 삽입하여 웹 서버가 동적 페이지를 만들 수 있도록 하는 `언어`이다.   

java EE 기능 중 일부로 웹 애플리케이션 서버에서 동작이 가능하며 자바 **서블릿으로 변환된 후 실행**된다는 특징이 있다. 하지만, 서블릿과는 다르게 HTML 표준에서 작성되기 때문에 웹 페이지를 디자인하기 훨씬 편리하다는 장점이 있다.   
Html에 자바코드가 삽입되는 형식이므로 Html보다 더 코드가 길며 삽입되는 자바코드가 없다면 파일 형식을 html로 바꿔도 그대로 작동된다.

JSTL등의 JSP 태그 라이브러리를 같이 사용하는 경우에는 자바 코딩없이 태그만으로 간략하게 작성이 가능해지므로 생산성을 더욱 높일 수 있다.

1999년 썬 마이크로시스템즈에서 배포하였으며 이와 유사한 구조로는 PHP, ASP, ASP.NET등이 있다. 



#### JSP 동작 흐름

[사진 추가 요망]()

jsp로 생성되는 서블릿은 컨테이너가 기본적으로 생성해주는 9개의 객체들이 있다는 점이 특징이다. 이 객체들을 jsp의 `기본객체` 또는 `내장객체`라고 한다.

jsp는 Scriptlet 기반 언어이지만 서블릿으로 한번 변환되면 서블릿은 Compile 기반 언어이기 때문에 Compile 언어의 특징도 가지고 있다고 말할 수 있다. jsp는 두 가지 방식의 장점을 활용하기 때문에 서블릿으로 변환되기는 하나 서블릿과 크게 속도차이는 나지 않는다고 한다.

+ 더 알아보기
	+ Compile 기반 언어(서블릿)와 Scriptlet 기반 언어

#### JSP 기본객체

[JSP 9개의 기본객체 서술 요망]()

+ JSP 기본객체 scope
[JSP 4개의 기본객체 scope 서술 요망]()

### JSP Scripting Element (JSP 스크립팅 요소)

jsp에서 자바코드를 삽입할 수 있도록 하는 것(문법? 요소? 영역?)을 알아야 작성이 가능하다. 이러한 문법들을 jsp 스크립팅 요소라고 한다.

#### 1. 선언 (Declaration)

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

#### 2. 스크립트릿(Scriptlet)

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
 
#### 3. 표현식 (Expression)

데이터 출력시 사용한다. 다른 요소들과는 다르게 세미콜론을 넣지 않는다.

`<%= 표현식 %>`

위의 표현은 아래로도 작성이 가능하다.   
단, 세미콜론을 붙여야 한다는 점을 잊지말자!

`<% out.print(표현식); %>`

예시는 아래와 같다.

```
안녕하세요 <%= name %>

 ```

#### 4. 주석 (Comment)

코드 상에 부가 설명을 작성한다.

`<%-- 주석 --%>`

html의 주석 `<!-- -->`과의 다른 점은 Jsp의 주석은 서버에서 제외시켜 클라이언트의 응답 html에는 보이지 않는데 html 주석은 보인다는 것이다.   

아래와 같이 html 주석 내에 jsp의 표현식을 넣으면 그대로 실행이 된다는 점도 있다.   
<!-- 이 글은 보이지 않지만.. 왼쪽 글은 보이게 된다. <%= name %> -->

### JSP 지시자 (Directive)

서블릿 컨테이너에게 JSP를 통해 서블릿을 생성할 때 어떻게 생성할지에 관한 설정이나 명령을 의미한다. 기본적인 문법은 아래와 같다.

`<%@ directive_type attr1="value1" attr2="value2" %>`

#### 1. page Directive 

컨테이너에게 현재 JSP 페이지를 어떻게 처리할 것인지에 대한 정보를 제공한다.

아래와 같이 작성한다.

`<%@ page attr1="value1" attr2="value2" %>`

이클립스에서 JSP 파일을 생성하면 자동으로 나오는 아래의 코드가 바로 페이지 지시자에 해당한다.

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" %>
```

[jsp 페이지 지시자 속성 정리 요망]()

#### 2. include Directive 

특정 JSP 파일을 페이지에 포함시키는 지시자이다.   
여러 JSP 페이지에서 반복적으로 사용되는 부분(일반적으로 header, footer, aside 등)을 jsp file로 만든 후 해당 지시자를 활용하면 반복되는 코드를 줄일 수 있다.

아래와 같이 작성한다.

`<%@ page file="/template/header.jsp" %>`

속성이 하나밖에 없다는 점이 개인적으로 편안하다.

#### 3. taglib Directive 

JSTL 또는 사용자 커스텀 태그(custom tag)를 이용하고자 할 때 사용되며 JSP 페이지 내에 자바 코드를 삽입할 때 조금 더 간결하게 작성할 수 있다.

아래와 같이 작성한다.

`<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`

`tagdir` 라는 속성도 있지만 어디에 쓰이는 속성인지 잘 모르겠다.

### Java Beans (자바 빈즈)

JSP에서 사용이 가능한 객체를 지칭하는 용어이다. (빌더 형식의 개발도구에서 재사용이 가능한 소프트웨어 컴포넌트 어쩌구라고 쓰여있는 정의도 있는데 잘 모르겠다.)

자바 빈즈를 사용하는 경우에는 몇 가지 규칙을 따라야 하는데 다음과 같다.
1. 반드시 패키지가 존재해야 한다.
2. 기본 생성자가 존재해야 한다.
3. 멤버변수 접근 제어가는 private 이어야 한다.
4. 멤버변수에 접근할 때는 getter와 setter를 사용한다.

필자의 경우 자바를 배울 때 부터 위의 규칙을 따라서 클래스를 생성했었는데, 자바 클래스와 자바 빈즈의 괴리감이 전혀 없어서 오히려 당혹스러웠다; (교수님 그냥 자바 클래스인데요? 무엇이 빈즈라는..?)

아래는 자바 빈즈를 활용했을 때의 아키택쳐 사진..이다.

[사진 추가..요망..]()

### forward와 sendRedirect

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

### cookie session (해당부분은 위로 )

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

### session

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


