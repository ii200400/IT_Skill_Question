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




