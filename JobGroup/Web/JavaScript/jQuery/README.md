# jQuery

## 개요

+ John Resig이 2006년 발표한 크로스 플랫홈을 지원하는 경량 javascript library.
+ 복잡하고 많은 UI 코드의 관리를 용이하게 만들어준다.
  + 어떠한 브라우저에서도 동일하게 동작하도록 크로스 플랫폼을 지원한다.
  + 즉, 브라우저 호환성을 고려하여 대체코드 작성할 필요가 없다.
  + 네이티브 DOM API(DOM 쿼리나 조작 등)보다 직관적이고 편리한 API 제공
    + DOM 탐색을 위해 사용하는 Selector 표현 방식은 CSS에서의 Selector와 같다.
  + 이벤트, Ajax, 매니메이션 효과를 간편하게 사용
  + 다양한 Effect 함수를 제공하여 동적인 페이지 간편하게 구현
  + jQuery 선택자는 래퍼세트(WrapperSet) 객체를 반환하여 `메소드 체인`이 가능하게 한다.
    + ex) $(selector).func1().func2().func3()...
+ [공식사이트](https://jquery.com/)에서 다운로드를 받아 사용하던가, CDN(Content Delivery Network)을 사용하여 적용한다.
  + CDN은 `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.x.x/jquery.min.js"></script>`와 같이 작성하여 적용시킨다. 필자는 3.5.1버전을 사용하였다.
  + CDN은 지리적 제약 없이 전 세계 사용자에게 빠르고 안전하게 콘텐츠를 전송할 수 있는 콘텐츠 전송 기술을 의미한다는데.. 아직 잘 모르겠고 클라우드 공부시에 같이 해야겠다;
  + [w3schools](https://www.w3schools.com/jquery/default.asp)에도 jQuery에 대한 설명이 있으니 참고하자.

## 기본 구문

### DOM 요소 선택

+ Selector를 사용하여 DOM 객체를 탐색하고, 반환된 래퍼런스 세트를 통해 함수를 수행한다.
  + ex) $(selector).action();
  + jQuery로 DOM을 탐색하기 전에, 웹 브라우저에 문서가 모두 로드되어 있어야 한다!
+ jQuery는 Document Ready 이후 작업을 처리할 수 있는 두 가지 방법을 제공한다.

```
// 첫 번째 방법
$(document).ready(function () {
  // TODO
});

// 두 번째 방법
$(function () {
  // TODO
});
```

+  예시

위는 기존의 DOM 객체를 가져오는 방법 아래는 jQuery로 DOM 객체를 가져오는 방법이다.
```
<script type="text/javascript">
	var element1 = document.getElementById("div1");
	var element2 = document.getElementsByTagName("div")[0];
	var element3 = document.getElementsByName("div3")[0];
	var element4 = document.getElementsByClassName("div4")[0];
	
	console.log(element1.innerHTML);
	console.log(element2.innerHTML);
	console.log(element3.innerHTML);
	console.log(element4.innerHTML);
  
  var element1 = $("#div1");
	var element2 = $("div").eq(0);
	var element3 = $("[name=div3]").eq(0);
	var element4 = $(".div4").eq(0);
	
	console.log(element1.html());
	console.log(element2.html());
	console.log(element3.html());
	console.log(element4.html());
</script>
```

<hr>

선택자는 대부분 CSS와 작성 방법이 같으므로 요소 선택자, DOM 계층 선택자는 생략한다.   
역시 더 많은 정보는 [w3schools](https://www.w3schools.com/jquery/jquery_selectors.asp)에서 확인 하는 것이 좋다.

<hr>

### 속성 선택자

+ CSS의 선택자와 같은 표현을 활용하여 선택자를 작성하면 된다.

```
<head>
	<meta charset="UTF-8">
	<title>jquery</title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function () {
			$(function () {
				$("#button1").click(function () {
					clear(); $("input[name]").css("background", "silver");
				});
				$("#button2").click(function () {
					clear(); $("input[value='jQuery']").css("background", "silver");
				});
				$("#button3").click(function () {
					clear(); $("#targets > input[value!='jQuery']").css("background", "silver");
				});
				$("#button4").click(function () {
					clear(); $("input[value~='셀렉터']").css("background", "silver");
				});
				$("#button5").click(function () {
					clear(); $("#targets > input[value*='셀렉터']").css("background", "silver");
				});
				$("#button6").click(function () {
					clear(); $("input[value^='셀렉터']").css("background", "silver");
				});
				$("#button7").click(function () {
					clear(); $("input[value$='셀렉터']").css("background", "silver");
				});
				$("#btn_clear").click(function () {
					clear();
				});
			});
			function clear() {
				$("input[type='text']").css("background", "white");
			}
		});
	</script>
</head>

<body>
	<h2>jQuery Attribute Selector</h2>
	<div id="targets">
		<input type="text" name="case1" value="jQuery" /><br />
		<input type="text" name="case2" value="jQuery셀렉터" /><br />
		<input type="text" name="case3" value="jQuery셀렉터 테스트" /><br />
		<input type="text" name="case4" value="셀렉터 테스트" /><br />
		<input type="text" name="case5" value="셀렉터테스트" /><br />
		<input type="text" name="case6" value="테스트" /><br />
	</div>
	<div>
		<input type="button" id="button1" value="name속성을 가짐" />
		<input type="button" id="button2" value="'jQuery' 일치" />
		<input type="button" id="button3" value="'jQuery' 미일치" />
		<input type="button" id="button4" value="'셀렉터' 단어 포함" />
		<input type="button" id="button5" value="'셀렉터' 포함" />
		<input type="button" id="button6" value="'셀렉터'로 시작" />
		<input type="button" id="button7" value="'셀렉터'로 끝남" />
		<input type="button" id="btn_clear" value="clear" />
	</div>
</body>
```

### 필터 선택자

+ DOM 요소 탐색 결과에서 원하는 요소만을 걸러내기 위해 사용
+ 크게 입력 폼 유형을 선택하는 필터 선택자, 요소 특성을 선택하는 필터 선택자 등의 여러 선택자들이 있다.
  + ex) el:button, el:hidden 등
  + CSS와는 다른 함수 형태의 필터 선택자도 있다.
    + ex) el:contains(str), el:nth-child(n), el:eq(n)

```
<head>
  <meta charset="UTF-8" />
  <title>jquery</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script type="text/javascript">
    $(document).ready(function () {
      $("tr:eq(0)").css("background", "black").css("color", "white");
      $("td:nth-child(3n)").css("background", "red");
      $("td:nth-child(3n+1)").css("background", "blue");
      $("td:nth-child(3n+2)").css("background", "green");
    });
  </script>
</head>
<body>
  <h2>jQuery필터 셀렉터</h2>
  <p>jQuery필터 셀렉터의 종류를 나열하였습니다.</p>
  <div>
    <table>
      <tr>
        <th>이름</th>
        <th>표현식</th>
        <th>설명</th>
      </tr>
      <tr>
        <td>button 필터</td>
        <td>:button</td>
        <td>모든 버튼 선택</td>
      </tr>
      <tr>
        <td>checkbox 필터</td>
        <td>:checkbox</td>
        <td>체크박스 엘리먼트 선택</td>
      </tr>
      <tr>
        <td>체크상태 필터</td>
        <td>:checked</td>
        <td>선택된 체크박스</td>
      </tr>
      <tr>
        <td>비활성화 필터</td>
        <td>:disabled</td>
        <td>비활성화 엘리먼트 선택</td>
      </tr>
      <tr>
        <td>활성화 필터</td>
        <td>:enabled</td>
        <td>활성화 엘리먼트 선택</td>
      </tr>
      <tr>
        <td>파일 필터</td>
        <td>:file</td>
        <td>파일 엘리먼트 선택</td>
      </tr>
    </table>
  </div>
</body>
```
![image](https://user-images.githubusercontent.com/19484971/177815161-a218e83e-1eea-42c7-9f79-50298211da61.png)

### jQuery method

+ jQuery는 선택자를 통해 탐색한 DOM 객체들을 래퍼세트라는 특별한 배열 객체에 담아 반환한다.
  + 선택된 DOM 객체가 업슨 경우에도 빈 래퍼세트를 반환
  + 래퍼세트에는 내포된 DOM 객체를 처리하는 다양한 메소드가 존재
  + 메소드는 플러그-인 확장을 통해 추가 가능

+ 요소 반복
  + `$.each` 함수는 배열이나 객체를 반복적으로 처리할 때 사용한다.
    + 첫번째 인자는 JS 배열이나 래퍼세트 객체
    + 두번째 인자는 각 요소를 반복하면서 호출할 콜백함수 정의
    + 콜백함수는 두 개의 매개변수(index: 배열 인덱스, item: 반복 요소 객체)f를 가진다.

```
<head>
	<meta charset="UTF-8">
	<title>jquery</title>
	<style type="text/css">
		.high-light-0 {
			background: yellow;
		}

		.high-light-1 {
			background: orange;
		}

		.high-light-2 {
			background: blue;
		}

		.high-light-3 {
			background: green;
		}

		.high-light-4 {
			background: red;
		}
	</style>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function () {
			// h2 태그마다 high-light-0~4 클래스로 CSS 적용
			$("h2").each(function (index, item) {
				// item 대신 this 사용 가능
				$(item).addClass("high-light-" + index);
			});
		});
	</script>
</head>

<body>
	<h2>첫번째</h2>
	<h2>두번째</h2>
	<h2>세번째</h2>
	<h2>네번째</h2>
	<h2>다섯번째</h2>
</body>
```
![image](https://user-images.githubusercontent.com/19484971/177820704-bc90c1ea-e14a-4a65-b43f-5d20db08fcfa.png)

+ 필터 함수

```
<head>
	<meta charset="UTF-8">
	<title>jquery</title>
	<script 
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
	$(document).ready(function() {
		/*
		$("h2:even").css({
			background: "black",
			color: "white"
		});
		*/
		// h2 태그의 홀수 또는 짝수에 CSS 색상 적용 (filter selector)
		$("h2").filter(":even").css({
			background: "black",
			color: "white"
		});
    // 아래 코드로 대체 가능 (filter method)
    // $("h2")
    //   .filter(function (index) {
    //     return index % 2 == 0;
    //   })
    //   .css({
    //     background: "black",
    //     color: "white",
    //   });
	});
	</script>
</head>
<body>
	<h2>첫번째</h2>
	<h2>두번째</h2>
	<h2>세번째</h2>
	<h2>네번째</h2>
	<h2>다섯번째</h2>
	<h2>여섯번째</h2>
</body>
</html>
```
![image](https://user-images.githubusercontent.com/19484971/177820877-1a398641-9cb6-4bea-b019-8951134b6421.png)

+ 위치기반 함수
  + DOM 객체의 특정 위치를 선택하는 함수
```
<head>
	<meta charset="UTF-8">
	<title>jquery</title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function () {
			// first() 함수를 사용하여 첫번째 h2 태그 색상 변경
			// last() 함수를 사용하여 마지막 h2 태그 색상 변경
			// eq() 함수를 사용하여 세번째 h2 태그 색상 변경
			$("h2").first().css("background", "blue")
				.css("color", "white");
			$("h2").last().css("background", "black");
			$("h2").eq(2).css("background", "silver");
			$("h2").eq(-1).css("color", "white");
		});
	</script>
</head>

<body>
	<h2>첫번째</h2>
	<h2>두번째</h2>
	<h2>세번째</h2>
	<h2>네번째</h2>
	<h2>다섯번째</h2>
	<h2>여섯번째</h2>
</body>
```
![image](https://user-images.githubusercontent.com/19484971/177822496-0e5d1da7-413e-4395-9434-23b3263ddde2.png)

+ 래퍼세트 요소 추가/삭제
  + add()와 not() 메소드로 래퍼세트에 주어진 조건에 해당하는 요소를 추가/제거한 래퍼 세트를 반환한다.

+ DOM 요소 판별
  + is() 메서드는 기존 래퍼세트가 주어진 선택자와 일치하는지 여부 반환
  + 즉, 래퍼세트가 아닌 boolean을 반환
  + 비교 조건을 선택자로 표현하기 어려운 경우, 함수 사용 가능

+ 자손 요소 탐색
  + find() 메소드는 래퍼세트의 모든 요소에 대하여 주어진 선택자를 만족하는 모든 자손 요소를 선택한다.








