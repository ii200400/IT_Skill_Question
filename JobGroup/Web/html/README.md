# HTML5 (Hyper Text Markup Language)

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

## 기본 문법

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

## 포맷팅 요소

포맷팅 요소는 개인적으로는 웹 페이지에서 사용하기 보다는.. 깃허브 정리글에 더 자주 썼던 것 같다.

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

## 목록형 요소

unordered list(ul)와 ordered list(ol)이 대표적이다.   

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

## 테이블 요소

본인은 기본적으로 `table`, `tr`, `th`, `td` 만 기억한다, 일반적으로 복붙해서 내용만 넣어 사용하기 때문이다.

`colspan`과 `rowspan` 속성은 항상 어떻게 합치는지 햇갈린다;;   

참고로 table로 만들 수 있는 것은 div로도 만들 수 있다, 둘의 가장 큰 차이는 table의 경우 테이블 내 모든 데이터가 로딩이 되어야 화면에 표시되지만 div의 경우에는 각 데이터가 로딩이 될 때마다 화면에 표시해준다.   
그래서 데이터가 많은 경우에는 div를 사용하는 경우도 있다고 한다.

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

## 이미지 요소

`src` 속성에 상대/절대 경로를 넣어 이미지를 불러오기 위해 사용하는 요소이다.

보통 CSS 함께 사용하여 너비나 높이, float를 지정한다.

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

## 링크 요소

Anchor를 뜻하는 a태그를 이용해서 다른 문서를 연결한다.

+ target 속성
	+ _self : 링크를 새 창이나 탭에서 연다.
	+ _blank : 현재 화면에서 링크를 연다.

```
<h2>관련 사이트</h2>
<a href="http://www.naver.com" target="_self">네이버</a><br>
<a href="http://www.daum.net">다음</a><br>
<a href="http://www.nate.com">네이트</a><br>
<a href="http://www.google.com" target="_blank">구글</a><br>
```
![image](https://user-images.githubusercontent.com/19484971/175974249-4e759dd8-78f2-47ad-953b-18dc26279b50.png)

### bookmark 예시

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

## 폼 요소

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

## 블록/인라인 요소

태그는 크게 block과 inline 형식으로 나눌 수 있다.

+ Block-level Elements
	+ 항상 새 줄에서 시작하고 자동으로 요소 앞뒤에 약간의 공백(여백)을 추가한다.
	+ 대표적으로 `div`태그가 있다.
+ Inline Elements
	+ 새 줄에서 시작하지 않는다.
	+ 대표적으로 `span`태그가 있다.

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

## DTD, Schema

통일된 xml을 만들기 위해 만드는 xml 작성 규칙이나 양식을 적어놓은 문서를 의미한다.
프로젝트마다, 통신마다 다를 수 있으며 원활한 데이터 송수신을 위해 해당 작업을 하는 사람들이 참고하는 문서이다.

이러한 문서를 잘 따른 문서를 valid라고 한다.

[DTD Turotial](https://www.w3schools.com/xml/xml_dtd_intro.asp)을 참고하면 이해가 조금 더 쉽다.
