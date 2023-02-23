# BootStrap

`목차`

* [개요](#개요)
* [Container](#container)
* [Grid System](#grid-system)

## 개요

+ 빠르고 쉽게 웹 개발을 위한 무료 프론트엔드 프레임워크
  + 반응형 웹을 쉡게 만들기 위한 기능들을 제공
  + Bootstrap 4 이후 버전은 최신 브라우저들과 모바일 호환
  + HTML 및 CSS 기반의 디자인 템플릿과 JS 플러그인들이 포함된다.
    + forms, buttons, tables 등등..
  + 반응형 웹
    + 웹 표준을 지원하는 모든 스마트 기기에서 접속가능
    + 크게에 맞춰 레이아웃이 적절하게 변화
    + 사이트 유지 및 관리의 용이
    + Html과 CSS로만 구성되어 복잡하지 않다.
  + 뷰 포트(viewport)
    + 스마트 기기 화면에서 실제 내용이 표시되는 영역
    + 픽셀 표현 방식(해상도)이 다른 화면들에 맞추어 글이나 사직을 확대 또는 축소하여 표시하는 가능을 제공한다.

+ Bootstrap CDN은 아래와 같이 적용하였다.
  + 위에서부터 CSS, jQuery, Popper Js, JS에 대한 CDN이다.
  + 물론 w3schools에 있는 CDN을 써도 무방하다. (아마 업데이트를 자주 하는 곳이니 더 좋을 것이다.)
```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
```

가장 중요한 Container와 Grid System 둘의 예시 코드만 남기고 **나머지는 작성하지 않을 것이다.**  
웹에 대한 기술 중에서도 특히 bootstrap은 [w3schools-bootstrap](https://www.w3schools.com/bootstrap/bootstrap_ver.asp) 등의 사이트에서 **원하는 기능을 찾고 복사/붙여넣기 후 적절하게 바꾸는 것이 훨씬 빠르기 때문**이다. 그러니 이 곳에 정리를 하는 것은 특히나 의미가 없다고 판단하였다.

## Container

+ 컨테이너는 내용을 담을 때 사용되는 가장 기본적인 클래스로 아래의 두 종류가 있다.
  + `.container` 클래스는 반응형 고정 너비의 컨테이너를 제공
  + `.container-fluid` 클래스는 뷰포트 기준 최대 너비 컨테이너를 제공

```
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Bootstrap</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
	<div class="container" style="background: skyblue;">
		<h1>container</h1>
	  	<p>class : container</p>
	</div>
	<div class="container-fluid" style="background: pink;">
	  	<h1>container-fluid</h1>
	  	<p>class : container-fluid</p>
	</div>
</body>
</html>
```
![image](https://user-images.githubusercontent.com/19484971/178116686-8d055ccc-688c-456c-be3f-f462959a4d40.png)

## Grid System

+ 페이지에 최대 12개의 열을 활용하여 반응형 웹을 위한 레이아웃을 만드는데 도움이 되는 시스템
  + flexbox라는 것으로 구축되었다고 한다.
  + 화면 크기에 따라 열을 재정렬시켜 반응형 웹을 구현한다.

```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Bootstrap</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
	<div class="container">
		<div class="row">
			<div class="col-sm-4 bg-success">.col-sm-4</div>
			<div class="col-sm-8 bg-primary">.col-sm-8</div>
		</div>
		<div class="row">
			<div class="col-sm-2 bg-success">.col-sm-2</div>
			<div class="col-sm-4 bg-primary">.col-sm-4</div>
			<div class="col-sm-6 bg-warning">.col-sm-6</div>
		</div>
		<div class="row">
			<div class="col-md-2 bg-success">.col-md-2</div>
			<div class="col-md-4 bg-primary">.col-md-4</div>
			<div class="col-md-6 bg-warning">.col-md-6</div>
		</div>

		<div class="row">
			<div class="col bg-success">col</div>
			<div class="col bg-primary">col</div>
			<div class="col bg-warning">col</div>
		</div>
	</div>
</body>
</html>
```
큰 화면에서 
![image](https://user-images.githubusercontent.com/19484971/178117181-3334271d-ba32-4157-8176-a7d181986fc9.png)

좁은 화면에서
![image](https://user-images.githubusercontent.com/19484971/178117204-1b8b13f5-af53-4835-aee4-3524276ee876.png)
