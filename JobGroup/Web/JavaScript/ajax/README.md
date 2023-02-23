# AJAX(Asynchronous Javascript And XML)

`목차`

- [ajax란?](#ajax란)
- [AJAX(Asynchronous Javascript And XML)](#ajaxasynchronous-javascript-and-xml)
  * [XML HTTP Request](#xml-http-request)

## ajax란?

+ 웹에서 화면을 갱신하지 않고 데이터를 서버로부터 가져와 처리하는 방식을 의미한다.
  + 프레임워크나 라이브러리가 아니다!
  + 화면 갱신이 없으므로 사용자 입장에서는 편리하다. 
  + 동적으로 DOM을 수정해야하므로 구현이 복잡하다.
  + JavaScript의 SMLHttpRequest(XHR) 객체로 데이터를 전달하고 비동기 방식으로 결과를 조회한다.
+ 클라이언트 중심의 개발방식으로 동적 화면구성을 주 관점으로 한다.
  + 참고로 서버 중심의 개발방식은 JSP, PHP, ASP가 있다.

+ Ajax 요청에 대한 응답 과정
  + data 입력 후 event 발생시 서버에 요청을 한다.
  + 서버는 받은 data를 토대로 작업을 한 후 응답 페이지를 만드는 대신 text, XML, Json으로 응답을 한다.
  + 클라이언트는 서버로부터 응답 데이터를 이용하여 화면 전환없이 동적으로 화면을 재구성 한다.

![image](https://user-images.githubusercontent.com/19484971/178088924-d602894c-be86-4a7f-a0c4-0d6344cef5ae.png)

(출처: https://www.w3schools.com/js/js_ajax_intro.asp)

## XML HTTP Request

+ JS가 Ajax 방식으로 통신할 때 사용하는 객체
  + Ajax통신 시 전송방식, 경로 등의 정보를 담는 역할
  + 실제 서버와의 통신은 브라우저의 Ajax 엔진에서 수행
  + Ajax 없이 직접 JS로 프로그래밍한다면 브라우저 별로 다른 통신방식으로 인하여 코드가 복잡해진다.

기본적인 httpRequest 객체를 만드는 코드 (아직 서버로 요청하는 함수만을 구현)
```
<!-- httpRequest.js  -->
<script type="text/javascript">
  var httpRequest = null;

  // 통신시 사용하는 객체 (브라우저 별로 상이)
  function getXMLHttpRequest() {
    if (window.ActiveXObject) {
      // MS IE
      try {
        return new ActiveXObject("Msxml2.XMLHTTP");
      } catch (e1) {
        try {
          return new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e2) {
          return null;
        }
      }
    } else if (window.XMLHttpRequest) {
      // 기타 웹 브라우저
      return new XMLHttpRequest();
    } else {
      return null;
    }
  }

  // 서버에 요청을 하는 함수
  function sendRequest(url, params, callback, method) {
    httpRequest = getXMLHttpRequest();

    // 통신 방식과 url을 설정하고
    var httpMethod = method ? method : 'GET';
    if(httpMethod != 'GET' && httpMethod != 'POST'){
      httpMethod = 'GET';
    }
    var httpParams = (params == null || params == '') ? null : params;
    var httpUrl = url;
    if(httpMethod == 'GET' && httpParams != null){
      httpUrl = httpUrl + "?" + httpParams;
    }

    // 설정한대로 통신을 진행한다.
    //alert("method == " + httpMethod + "\turl == " + httpUrl + "\tparam == " + httpParams);
    httpRequest.open(httpMethod, httpUrl, true);
    httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    // readyState가 바뀌면 호출될 콜백함수를 등록한다.
    httpRequest.onreadystatechange = callback;
    //alert(httpMethod == 'POST' ? httpParams : null);
    httpRequest.send(httpMethod == 'POST' ? httpParams : null);
  }
</script>
```

+ XMLHTTPRequest 객체의 속성값 readyState와 status로 서버로부터 응답이 왔는지, 정상적인 응답인지를 확인한다.
  + readyState
    + 0 Uninitialized 객체만 생성 (open 메소드 호출 전).
    + 1 Loading open 메소드 호출.
    + 2 Loaded send 메소드 호출. status의 헤더가아직 도착되기 전 상태.
    + 3 Interactive 데이터 일부를 받은 상태.
    + 4 Completed 데이터 전부를 받은 상태.
  + status
    + 200 OK 요청 성공.
    + 403 Forbidden 접근 거부.
    + 404 Not Found 페이지 없음.
    + 500 Internal Server Error 서버 오류 발생.
    + 등등..

랜덤 유저 정보를 제공하는 사이트를 통해서 1초마다 랜덤한 유저 정보를 가져오는 코드
```
<script type="text/javascript" src="../js/httpRequest.js"></script>
  <script type="text/javascript">
    // 랜덤 유저 정보 가져오기
    function getUser() {
      sendRequest("https://randomuser.me/api/", null, viewUser, "GET");
    }

    function viewUser() {
      if (httpRequest.readyState == 4) {
        if (httpRequest.status == 200) {
          // 받은 데이터를 일단 text 취급을하여 화면에 넣어본다. (원래는 Json parse 코드를 넣어야한다.)
          var time = httpRequest.responseText;
          var div = document.getElementById("userInfo");
          div.setAttribute("class", "viewUser");
          div.innerHTML = time;
        }
      } else {
        // 로딩중...
      }
    }

    window.onload = function () {
      setInterval(getUser, 1000);
    };
  </script>
</head>
<body>
  <h2>랜덤 인물</h2>
  <div id="userInfo"></div>
</body>
```
![image](https://user-images.githubusercontent.com/19484971/178101682-46aaf0e5-e58d-4117-9d78-5d1fda57629b.png)

### jQuery Ajax 함수

+ jQuery에서 제공하는 $.ajax() 함수로 Ajax를 쉽게 접근할 수 있다.
  + 다른 함수들에 비해 옵션을 쉽고 다양하게 지정할 수 있어 실무에서 자주 사용된다.
  + 옵션은 디폴트 값이 있어 생략이 가능하다.
  + [w3schools](https://www.w3schools.com/jquery/jquery_ajax_intro.asp)에서 간결한 내용을 볼 수 있다.
  + 훨씬 자세한 내용은 [w3schools의 jQuery AJAX 참조](https://www.w3schools.com/jquery/jquery_ref_ajax.asp)에서 확인하자.

개인적으로도 사용이 너무 쉬워서 당황하게 된다.

```
<!-- 1-06.xml -->
<?xml version="1.0" encoding="UTF-8"?>

<students>
	<student>
		<id>20201111</id>
		<name>김</name>
		<class>A</class>
		<grade>90</grade>
	</student>
	<student>
		<id>20201112</id>
		<name>홍</name>
		<class>B</class>
		<grade>92</grade>
	</student>
	<student>
		<id>20201113</id>
		<name>박</name>
		<class>C</class>
		<grade>91</grade>
	</student>
</students>
```

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>CSV</title>
    <style type="text/css">
      table {
        width: 300px;
        height: 100px;
      }
      th,
      td {
        text-align: center;
      }
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
      $(document).ready(function () {
        $("#listBtn").click(function () {
          // server에서 넘어온 data(라고 가정한다.)
          $.ajax({
            url: "1-06.xml",
            type: "GET",
            // json 형식인 경우
            // contentType: 'application/json;charset=utf-8',
            // dataType: 'json',
            dataType: "xml",
            success: function (response) {
              makeList(response);
            },
            error: function (xhr, status, msg) {
              console.log("상태값 : " + status + " Http에러메시지 : " + msg);
            },
          });
        });

        function makeList(data) {
          var studentList = ``;
          $(data)
            .find("student")
            .each(function (index, item) {
              studentList += `
        		<tr>
        			<td>${$(this).find("id").text()}</td>
        			<td>${$(this).find("name").text()}</td>
        			<td>${$(this).find("class").text()}</td>
        			<td>${$(this).find("grade").text()}</td>
        		</tr>
        		`;
              $("#studentinfo").empty().append(studentList);
            });
          $("tr:first").css("background", "darkgray").css("color", "white");
          $("tr:odd").css("background", "lightgray");
        }
      });
    </script>
  </head>
  <body>
    <h3>분반</h3>
    <button id="listBtn">학생정보보기</button>
    <table>
      <tr>
        <th>학번</th>
        <th>이름</th>
        <th>분반</th>
        <th>성적</th>
      </tr>
      <tbody id="studentinfo"></tbody>
    </table>
  </body>
</html>
```
버튼 누르기 전

![image](https://user-images.githubusercontent.com/19484971/178104095-bf5c6e12-b760-4f1f-996f-e7f43bb9f2d5.png)

버튼 누른 후

![image](https://user-images.githubusercontent.com/19484971/178104100-207fd0fc-8237-4fba-a718-0a682ebee191.png)

강의에서 해당내용을 하지 않아서 가장 기본적인 내용만을 정리하였다.

jQuery AJAX 함수인 .load()나 jQuery AJAX 진행 상황을 알기위한 Event 관리에 사용되는 전역변수들에 대한 내용도 있는데 생략한다.
