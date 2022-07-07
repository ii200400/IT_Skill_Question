# JavaScript

단순히 보면 다양한 코딩 언어 중 하나지만, 웹에서는 변칙적인 사용자들의 입력에 대응하여 웹 페이지가 다양한 반응을 보일 수 있도록 만들어준다.

## 개요

프로토타입 기반의 스크립트 프로그래밍 언어이자 인터프리터 언어

+ 기본적으로 ECMA(European Computer Manufacturers Association) Script 라는 유럽의 컴퓨터 제조 연합..?에서 채택한 기술 규격을 기본으로 한다.
	+ ES6이전과 이후의 자바스크립트 기능이 많이 달라졌다. ex) const, let
+ 웹 브라우저에서 동작하는 유일한 프로그래밍 언어
+ 객체지향 등의 여러 프로그래밍 패러다임을 지원
	+ 명령형, 함수형 프로그래밍도 지원하는 멀티 패러다임 프로그래밍 언어
+ 별도의 컴파일 작업을 수행하지 않는다.
	+ 각 브라우저는 인터프리터와 컴파일러의 장점을 결합하여 비교적 느린 인터프리터의 단점을 해결한다.

HTML, CSS와 더불어 웹을 구성하는 요소 중 하나로 접하는 경우가 많으며 필자는 웹을 공부하면서 자바스크립트를 공부하고 정리할 것이기 때문에 바닐라 자바스크립트 보다는 웹에서의 자바스크립트 기준으로 서술할 것이다.

## JavaScript 선언

크게 아래의 두 가지 방법이 있다.

+ 1. `script` 태그를 이용해서 HTML문서 내부에 js를 넣는 방법
+ 2. `script` 태그의 src 속성을 활용하여 외부 파일의 js를 불러오는 방법 
		
	<script src="hello.js" type="text/javascript">
		console.log("1, " + x);
		...
	</script>

+ 두 가지 방법을 혼용한다면 외부 파일이 HTML 내부에서 작성한 js를 덮어쓰게 된다. 
+ `script`태그는 HTML문서 어디든 선언이 가능하다. 
	+ 일반적으로 `head`나 `body` 내부에 작성한다. 
	+ js로 인해 로딩이 늦게 되는 상황을 미연에 방지하기 위해 `body` 태그 내의 가장 끝부분에 작성하는 경우가 일반적이다.
	+ 이 때문에 화면 로딩이 끝나면 호출되는 함수인 window.onload를 자주 사용하기도 한다.

## 주석

코드에 대한 부연설명을 작성하는 부분으로 한 줄 주석과 블록 주석이 있다.   
전자는 `//`로 후자는 `/* */`로 표기한다.

일반적으로 에디터에서는 `ctrl + /`으로 주석을 추가할 수 있는데 이것을 활용하는 것이 좋다.

## 자료형

js에는 자료형을 크게 원시 타입(primitive type)과 객체 타입(object type)으로 분류한다. 원시 타입은 아래의 표에 적힌 5가지 자료형이고 이를 제외한 자료형들은 모두 객체 타입으로 분류된다.

| 자료형 | typeof 출력 값 | 설명 | 
|--------|-----|-----|
| 숫자형 | number | 정수 또는 실수형 |
| 문자열형 | string | 말 그대로 문자열, `'` 혹은 `"`으로 감싸 표기 | 
| boolean형 | boolean | 참/거짓 |
| undefined | undefined | 변수가 선언되었지만 초기화가 되지 않은 경우 | 
| null | object | 값이 존재하지 않는 경우 |

_왜.. null 자료형은 typeof 출력값이 object 인 것이냐.._

<hr>

+ 숫자형
	+ js는 정수만 표현하는 자료형은 존재하지 않는다, 무조건 8byte의 실수이다.   
	+ 다른 언어와 다르게 0으로 나누는 연산에 대해 에러를 내뿜지 않는 대신 특별한 상수(Infinity)를 반환한다.  
	+ parseInt('1A')와 같이 숫자가 섞여 있다면 문자가 나오기전까지의 숫자만을 변환한다. 이 예시에서는 1이 반환된다.
	+ parseInt('1A')와 같이 문자만 들어가 있다면 NaN(Not A Number)를 반환한다.
	+ 다른 언어와 같이 특정 소수점을 정확하게 표현하지 못한다.

소수점 예시

```
var x = 0.3 - 0.2;
var y = 0.2 - 0.1;
console.log(x == y);	// false
console.log(x);			// 0.09999999999999998
console.log(y);			// 0.1

var a = 0.3;
var b = 0.2;

var result = (a * 10 - b * 10) / 10;
console.log(result);	// 0.1
```

Infinity, Nan 예시

```
// 언더플로우
console.log(0 / 100);		// 0
console.log(-0 / 100);		// -0

// 오버플로우
console.log(100 / 0);		// Infinity
console.log(-100 / 0);		// -Infinity
console.log(Infinity / 0);	// Infinity
console.log(-Infinity / 0);	// -Infinity

console.log(0 / 0);				// Nan
console.log(parseInt('1A'));	// 1
console.log(parseInt('A'));		// NaN

console.log(new Number('1'));	// 1
console.log(new Number('1A'));	// NaN
```

<hr>

+ 문자열
	+ 16비트의 유니코드 문자를 사용한다.
	+ 문자 하나를 나타내는 자료형은 없다.   
	+ `'`와 `"`를 구분하지 않고 사용이 가능하다.
		+ 단, 혼용은 불가능
	+ 이스케이프 시퀸스`\` 사용이 가능하다.
		+ `'`을 출력하려면 `\'`이라고 작성하면 된다.
	+ 백틱 `\``을 활용한 문자열 표현이 가능하다.

문자열 예시

```
console.log('문자열 안에 포함된 \'작은따옴표\' 표현');	
// 문자열 안에 포함된 '작은따옴표' 표현
console.log("특수문자 사용\n줄바꿈 했다.");			
// 특수문자 사용
// 줄바꿈 했다.

// 당신의 이름은 임영선(26)입니다.
var name = "임영선";
var age = 26;
var str1 = "당신의 이름은 " + name + "(" + age + ")입니다.";
console.log(str1);

// 당신의 이름은 임영선(26)입니다.
var str2 = `당신의 이름은 ${name}(${age})입니다.`;
console.log(str2);
```

<hr>

+ boolean
	+ 비교 연산에서 null, ''(빈 문자열), undefined, 0은 모두 false 취급을 받는다.
		+ null과 undefined는 분명하게 다르므로 구분을 잘하자.

### 자동 형 변환

+ Java나 C++과는 다르게 매우 느슨한 형 변환 규칙이 적용된다.
+ 함수에 어떤 자료형이라도 전달할 수 있고 그 값을 필요에 따라 변환한다.
	+ 정확히는 모르겠지만 숫자 연산보다 문자 연산이 우선인 것 같다.
+ 서로 다른 자료형의 연산이 가능하다.
+ 모든 자료형을 var로만 선언하고 별도의 구분이 없기 때문에 혼란이 야기된다.

```
console.log("message : " + msg);		// undefined
var msg = 40;

console.log("message : " + msg);		// message 40
msg = "hello javascript";	
console.log(msg);						// hello javascript

console.log("The message is " + 40);	// The message is 40
console.log(40 + " is The message");	// 40 is The message

console.log("40" - 5);					// 35
console.log("40" + 5);					// 405
console.log(5 + "40");					// 540

console.log(parseInt("123.45") + 1);	// 124
console.log(parseFloat("123.45") + 1);	// 124.45

console.log("1.1" + "1.1");				// 1.11.1
console.log((+"1.1") + (+"1.1"));		// 2.2
```

## 변수

자바 스크립트는 변수와 함수 이름이 혼동되지 않도록 변수에는 형용사/명사를, 함수에는 동사를 사용하도록 권장한다. 예를 들어 isSelected/getCount는 함수명으로 selected/count는 변수명으로 사용한다.   

키워드, 공백 문자를 포함하지 않고 숫자로 시작하지 않고, \_와 \$을 포함이 가능한 이름이 가능하다. 또한 낙타 표기법(영어 소문자를 기본으로 작성하되 두번째 단어부터는 첫 알파벳을 대문자로 표기하는 방식)을 기본으로 사용한다. 

### var keyword & Dynamic Typing

자바 스크립트는 변수를 선언할 때 타입을 명시하지 않으면서 어떤 타입이라도 사용 가능한 var 키워드가 (왜인지) 기본적으로 사용되며 다른 자료형으로 재선언 및 중복 선언이 가능하다.

또한 동적 타이핑을 통해 서로 다른 형 끼리의 형 변환이 자유롭고 서로 다른 형끼리의 연산도 가능하므로 사용하고 있는 변수에 대한 숙지가 필수적이다.

_때문에 무슨 타입인지 개발자도 모르는 경우가 발생하기도 한다._

### Variable Hoisting (변수 호이스팅)

js에는 모든 선언(변수와 함수 선언)이 해당 Scope의 처음에 위치한 것 처럼 작동을 하는 특성을 의미한다.

즉, 아래줄에 선언이 되어있어도 윗줄에서 출력이 가능하다, 물론 초기화가 되어있지 않기 때문에 undefined가 출력된다.

예시는 아래 const와 let과 같이 작성

## const & let

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

+ 예시

```
console.log(`vr: ${vr}`); // vr: undefined
// console.log(`vl: ${vl}`); // 에러
// console.log(`con: ${con}`); // 에러

var vr = "vr";
let vl = "vl";
const con = "con";
console.log(`vr: ${vr}`); // vr: vr
console.log(`vl: ${vl}`); // vl: vl
console.log(`con: ${con}`); // con: con

{
	// 블록 사용
	var vr = "vr2";
	let vl = "vl2";
	const con = "con2";
	console.log(`vr: ${vr}`); // vr: vr2
	console.log(`vl: ${vl}`); // vl: vl2
	console.log(`con: ${con}`); // con: con2
}

console.log(`vr: ${vr}`); // vr: vr2
console.log(`vl: ${vl}`); // vl: vl
console.log(`con: ${con}`); // con: con

var vr = 1;
console.log(`vr: ${vr}`); // vr: 1

function test() {
	// 지역(함수) 스코프
	var vr = "vr3";
	let vl = "vl3";
	const con = "con3";
	console.log(`vr: ${vr}`); // vr: vr3
	console.log(`vl: ${vl}`); // vl: vl3
	console.log(`con: ${con}`); // con: con3
}
test();

// 모두 변화 없음
console.log(`vr: ${vr}`); // vr: 1
console.log(`vl: ${vl}`); // vl: vl
console.log(`con: ${con}`); // con: con
```

참고로 필자는 전역 스코프는 전역 변수,  해당 스코프는 지역 변수로 이해하고 넘어갔다. 

## 연산자

코틀린과 비슷한 부분이 많아서 본인은 쉽게 기억할 것 같다.

+ 예시

```
var num1 = 10;
var num2 = 20;
var bool = true;		

console.log('num1++ : ' + num1++);				// 10
console.log('num1 : ' + num1);					// 11
console.log('--num1 : ' + --num1);				// 10
console.log('!bool : ' + !bool);				// false

console.log('typeof bool : ' + typeof bool);	// boolean
console.log('typeof num1 : ' + typeof num1);	// number

var num = 10;
var str = "10";
// 값 비교
console.log('num == str : ' + (num == str));		// true
// 타입을 포함하여 값 비교
console.log('num === str : ' + (num === str));		// false
```

등등 다양한 연산자가 있지만 생략한다. 더 많은 연산자를 확인하려면 역시 [w3schools_js_operator](https://www.w3schools.com/js/js_operators.asp)를 참고하자.

for, if, switch, while, do-while 문은 Java나 C++과 너무 유사하여 생략한다.   
그래도 for-of와 for-in은 한 번 살펴보자.

## 객체

+ 객체는 키(key)와 값(value)로 구성된 프로퍼티(property)의 집합
+ 문자열, 숫자, boolean, null, undefined를 제외한 모든 값은 객체
+ 전역 객체를 제외하고 객체에는 동적으로 프로퍼티를 추가하거나 삭제가 가능하다.
+ 프로토타입(prototype)이라는 특별한 프로퍼티를 포함한다.
+ 자바스크립트에서 함수는 일급 객체(first-class object)이므로 값으로 취급할 수 있다.
	+ 눼..? 라고 생각한다면 [얄코동영상 링크](https://www.youtube.com/watch?v=jVG5jvOzu9Y&t=7s)를 넣을테니 참고하자.

+ 객체 생성 3가지 방법
	+ 가장 보편적인 방법, 객체 리터럴`{}`로 객체를 생성
	+ Object 생성자 함수(new Object)로 빈 객체를 생성 후 프로퍼티를 추가
	+ 생성자 함수를 사용하여 동일한 프로퍼티를 가지는 객체 생성
+ 객체의 속성은 dot`.`이나 대괄호`[]`를 사용해서 접근한다.
	+ 객체의 속성은 변경이 가능하다, Mutable 하다고 한다.
+ 객체의 종류
	+ 크게 사용자가 정의한 객체와 웹에서 미리 정의한 객체로 나뉘는데 이중에서 후자에 들어가는 DOM(Document Object Model) 객체가 가장 중요하다.

```
// 1. 객체 리터럴
var student = {
	name: '김씨',
	area: '서울',
	classNum: 7,
	info: function () {
		console.log(this.name + '은 ' + this.area + this.classNum + '반');
	},
};

// 2. Object 생성자 함수
var student = new Object(); // empty obejct
// property 추가
student.name = '김씨';
student.area = '서울';
student.classNum = 7;
student.info = function () {
	console.log(this.name + '는 ' + this.area + this.classNum + '반');
};

// 3. 생성자 함수
function Student(name, area, classNum) {
	this.name = name;
	this.area = area;
	this.classNum = classNum;
	this.info = function () {
		console.log(this.name + '은 ' + this.area + this.classNum + '반');
	};
}

// 생성자 함수로 객체 생성.
var student = new Student('김씨', '서울', 7);

console.log(typeof student); // object
console.log(student); // {name: "김씨", area: "서울", classNum: 7, info: f}
student.info(); // 김씨는 서울7반

var member = {
		"user-name" : "홍길동",
		age : 20,
		city : "서울"
};

// 객체의 속성 접근
console.log(member.age);			// 1. dot 표기법
console.log(member["age"]);			// 2. [] 표기법

// 속성명에 연산자가 포함된 경우 [] 표기법만 접근 가능.
// - 를 감산 연산자로 취급해버리기 때문;
console.log(member["user-name"]);	// 홍길동
console.log(member.user-name);		// NaN
```

## 함수

+ 일급 객체(first-class object)로 취급한다.
	+ 함수를 런타임 중 동적으로 생성 가능하고 콜백함수로 만들거나 리턴 값이 될 수 있다.
		+ 콜백함수는 특정 이벤트가 발생했을 때 시스템에 의해 호출되는 함수
	+ [얄코동영상 링크](https://www.youtube.com/watch?v=jVG5jvOzu9Y&t=7s) 참고..
+ 함수도 3가지의 정의 방법이 있다.
	+ 함수 선언문, 함수 표현식, Function 생성자
+ var과 비슷하게 함수도 함수 호이스팅 기능이 있다. 
	+ 자바 스크립트는 모든 선언에 대해서 호이스팅 기능을 제공한다고 한다.
	+ 스크립트가 로딩이 되는 시점에 함수를 변수 객체에 저장하기 때문에 함수의 선언/초기화/할당이 한 번에 일어난다.
+ 함수를 호출할 때 정의된 매개변수와 전달인자의 수가 일치하지 않더라도 에러가 생기지 않는다.

```
// 1. 함수 선언문
function sum1(num) {
	var sum = 0;
	for(var i=1;i<=num;i++) {
		sum += i;
	}
	console.log(sum);	// 55
}
sum1(10);

// 3. 함수 표현식
var sum2 = function(num) {
	var sum = 0;
	for(var i=1;i<=num;i++) {
		sum += i;
	}
	console.log(sum);	// 55
}
sum2(10);

// 3. Function 생성자 함수
var sum3 = new Function("num",
	"var sum = 0;" + 
	"for(var i=1;i<=num;i++) {" +
	"	sum += i;" + 
	"} " +
	"console.log(sum);" );
sum3(10);

// 호이스팅
var result = plus(5, 7);
console.log(result); // 12

function plus(num1, num2) {
	return num1 + num2;
}

// 변수 호이스팅이 발생하여 에러가 생긴다.
var result = plus(5, 7); // TypeError
console.log(result);

var plus = function (num1, num2) {
	return num1 + num2;
};
```

### 콜백함수

+ 특정 이벤트가 발생했을 때 시스템에 의해 호출되는 함수
+ 일반적으로는 매개변수를 통해서 전달되고 이벤트에 따라 특정 시점에 실행된다.
+ 주로 비동기 처리에서 사용된다. 
	+ 콜백에서 콜백이 사용되는 구조로 인해 콜백지옥이라는 말이 있다.

```
// 이벤트 콜백함수1
<button id="btn">click!!</button>
<script type="text/javascript">
	// id가 btn인 요소를
	var btn = document.getElementById('btn');
	// 클릭하면 로그가 찍히도록 만든다.
	btn.addEventListener('click', function () {
		console.log('안녕하세요 여러분!!');
	});
</script>

// 이벤트 콜백함수2
<script type="text/javascript">
	setTimeout(function () {
		console.log('3초후 실행됩니다.');
	}, 3000);
</script>
```

콜백함수를 매개변수로 넘겨줄 때 주의할 코딩!

```
// 버그
<input type="text" id="test" value="테스트" />
<button id="btn">click!!</button>
<script type="text/javascript">
	// 이벤트 등록시에 바로 함수가 작동되고 이벤트 매개변수로 null이 들어간다..
	btn.addEventListener('click', view(document.getElementById("test").value));
	function view(val) {
		console.log('안녕하세요!!');
	}
</script>

// 해결
<input type="text" id="test" value="테스트" />
<button id="btn">click!!</button>
<script type="text/javascript">
	// 함수를 가리키는 변수를 만들어서 넣어준다.
	// 위의 예시처럼 바로 function() { ... }를 넣어주어도 된다.
	var callback = function view() {
		console.log(document.getElementById("test").value);
	};
	btn.addEventListener("click", callback);
</script>
```

## window 객체

+ 웹 브라우저에서 작동하는 JS의 최상위 전역객체
	+ 브라우저와 관련된 다양한 객체와 속성, 함수가 구비되어있다.
	+ 기본으로 제공되는 자료형(Number 등)이나 함수(setInterval() 등)가 여기에 포함된다.
+ BOM(Browser Object Model)로 불리기도 한다.
+ 자세히 알고 싶다면 역시 [w3schools](https://www.w3schools.com/jsref/obj_window.asp)

![image](https://user-images.githubusercontent.com/19484971/176583820-778383fa-23c9-41b3-9e09-50592f9847bd.png)

브라우저 내장객체 (출처 : https://kssong.tistory.com/29)

### alert, confirm, prompt(새 창 열기)

+ 브라우저에서 기본적으로 제공하는 창을 여는 함수가 있다.
	+ alert(), confirm(), prompt()가 대표적
	+ 하지만 요즘에는 모달 창을 더 많이 이용한다고 한다.

```
...
<script type="text/javascript">

function openAlert() {
	alert("알림창입니다.");
}

function openConfirm() {
	if(confirm("확인입니까?")) {
		console.log("확인 눌렀네요.");
	} else {
		console.log("취소 눌렀네요.");
	}
}

function openPrompt() {
	var txt = prompt("문자열 입력", "사용자입력");
	console.log(txt);
}

</script>
</head>
<body>
<input type="button" value="알림창" onclick="javascript:openAlert();">
<input type="button" value="확인창" onclick="javascript:openConfirm();">
<input type="button" value="입력창" onclick="javascript:openPrompt();">
</body>
...
```
![image](https://user-images.githubusercontent.com/19484971/176585248-2f4ac0ab-319f-482c-b7bc-e920a6253687.png)
![image](https://user-images.githubusercontent.com/19484971/176585271-b55b9a45-d513-4690-bea2-824622479b9a.png)
![image](https://user-images.githubusercontent.com/19484971/176585304-ec557eb6-ade6-4ad3-90c2-272c980348f0.png)

### navigator

+ 브라우저의 정보가 내장된 객체
	+ 브라우저 별로 다르게 처리하고 싶은 작업이 있을 때 사용한다.
	+ html5에서는 위치정보를 알려주는 역할로서 기능하기도 한다.

```
<script type="text/javascript">

console.log("Browser CodeName 	: " + navigator.appCodeName);
console.log("Browser Name 		: " + navigator.appName);
console.log("Browser Version 	: " + navigator.appVersion);
console.log("Browser Enabled 	: " + navigator.cookieEnabled);
console.log("Platform 		: " + navigator.platform);
console.log("User-Agent header 	: " + navigator.userAgent);

</script>
```
![image](https://user-images.githubusercontent.com/19484971/176585848-f557db83-11d5-4e65-bef7-c2da201345f1.png)

### location

+ 현재 페이지 주소(URL)과 관련된 정보를 알 수 있다.
	+ location.href : 프로퍼티에 값을 할당하면 해당 URL로 이동, 그렇지 않으면 현재 URL 반환
	+ location.reload() : 현재 페이지를 새로고침

```
console.log(location);
console.log(location.href);
// location.href = "http://www.naver.com";
```
![image](https://user-images.githubusercontent.com/19484971/176586449-53d912c4-71b1-4957-ab10-e0d66435767e.png)

### history

+ 현재 페이지 주소(URL)과 관련된 정보를 알 수 있다.
	+ history.back() / history.forward() : 뒤로가기 / 앞으로 가기 버튼과 같은 기능

### open, close

+ 새 창을 열고 현재 창을 닫게 하는 함수

```
// 4-4.html
<button onclick="javascript:windowOpen();">
	버튼 창열기
</button>
<a href="javascript:windowOpen();">링크 창열기</a>
<script>
	function windowOpen() {
		// 이름을 설정해주지 않으면 같은 창이 클릭할 때마다 계속 생성된다.
		window.open('./4-5.html', 'winname', 'width=300,height=500,top=100,left=100');
	}
</script>
```

```
// 4-5.html
<button onclick="javascript:windowClose();">
	함수 이용해서 닫기
</button>
<a href="javascript:window.close();">
	메소드 이용해서 닫기
</a>
<script>
	function windowClose() {
		// window.close();
		self.close();
	}
</script>

<input type="text" name="test" id="test">
<button onclick="send();">전송</button>
<script>
	function send() {
		// 부모 창(해당 창을 호출한 화면)으로 메시지를 보낼 수 있다.
		var msg = document.getElementById("test").value;
		opener.document.getElementById("view").innerHTML = msg;
		// 입력한 내용을 네이버 검색창에 검색한 화면이 부모 창에 뜨도록 만들 수 있다.
		// opener.location.href = "https://search.naver.com/search.naver?query=" + msg;
		self.close();
	}
</script>
```

### onload

+ html 문서의 로딩이 끝나면 호출된다.
+ 일반적으로 script가 요소보다 먼저 작성되어있는데 요소를 참조하는 경우 많이 사용한다.

## DOM(Document Object Model)

+ HTML과 xml문서의 구조를 정의하는 API를 제공
	+ 문서 요소(element) 집합을 트리 형태의 계층구조로 HTML을 표현한다.
	+ HTML 태그나 요소들을 표현하는 노드와 문자열을 표현하는 노드가 있다.
	+ HTML에 접근하여 페이지를 조작할 때 사용한다.
	+ DOM의 다양한 함수는 역시 [w3schools](https://www.w3schools.com/js/js_htmldom_document.asp)에서 확인하자.

![image](https://user-images.githubusercontent.com/19484971/176592604-a088ed95-8930-4e8e-8f8b-af68546e8e94.png)

(출처: https://en.wikipedia.org/wiki/Document_Object_Model)

```
// JS 만을 활용하여 웹 페이지에 텍스트를 추가할 수 있다.
<script type="text/javascript">
	window.onload = function () {
		// 변수를 선언하고 element node와 text node 생성.
		var title = document.createElement('h2');
		var msg = document.createTextNode('Hello!!!');

		// text node를 element node에 추가.
		title.appendChild(msg);
		document.body.appendChild(title);
	};
</script>
```

### 문서 객체 만들기

+ DOM 구조를 파악하고 적절한 함수를 통해서 문서의 구조(요소)와 속성를 수정할 수 있다.
	+ 다양한 함수가 많이 있으니 꼭 [w3schools](https://www.w3schools.com/js/js_htmldom_document.asp)참고 하는 것을 잊지말자.

요소를 만들고 요소의 속성을 지정한 후 문서에 추가하는 방법
```
// 방법 1
<script type="text/javascript">
	window.onload = function () {
		var profile = document.createElement("img");
		// 작성은 편하지만, 웹 브라우저가 지원하는 속성만 설정 가능
		profile.src = "profile.png";
		profile.width = 150;
		profile.height = 200;

		document.body.appendChild(profile);
	};
</script>

// 방법 2
<script type="text/javascript">
	window.onload = function () {
		var profile = document.createElement("img");
		// 작성은 불편하지만, 웹 브라우저가 지원하는 속성이 아닌것도 설정가능
		profile.setAttribute("src", "profile.png");
		profile.setAttribute("width", 150);
		profile.setAttribute("height", 200);

		profile.setAttribute("data-content", "내사진");

		document.body.appendChild(profile);
	};
</script>
```
아.. 사진을 삭제해서 깨진화면만 나와서 캡쳐를 못하겠다 ^ㅠ^;

### 문서 객체 가져오기

+ 문서의 객체에서 원하는 조건의 요소를 가져올 수 있도록 하는 함수가 많이 있다.
	+ 함수명에 Element이 포함되면 요소 하나를, Elements가 포함되면 요소들의 배열을 반환한다는 공통점이 있다.
	+ querySelector, querySelectorAll은 선택자를 매개변수로 넣어주어야 한다. ex) ".id", "#class"

문자열로 요소를 만들고 Id를 통해 문서의 요소를 찾아 해당 요소에 내용을 추가하는 방법
```
 // 1. id 속성으로 찾기
document.getElementById("idName");
// 2. tagName으로 찾기 (배열 반환)
document.getElementsByTagName("tagName");
// 3. name 속성으로 찾기 (배열 반환)
document.getElementsByName("idName");
// 4. className으로 찾기 (배열 반환)
document.getElementsByClassName("className");
// 5. 선택자로 찾기
document.querySelector("selector");
// 6. 선택자로 찾기 (배열 반환)
document.querySelectorAll("selector");
// 등등..
```
![image](https://user-images.githubusercontent.com/19484971/176619117-54aff8f8-57eb-4a0f-800c-16288187496b.png)

## Event

+ 웹 페이지에서 여러 종류의 상호작용이 있을 때 마다 하는 작업을 위해서 사용
	+ 마우스를 누를 때, 눌렀다가 때었을 때, 키보드를 누를 때 등등 다양한 이벤트 처리 가능
	+ DOM에서 발생하는 이벤트를 감지하여 여러 작업을 수행
+ 특정 이벤트로 불리는 콜백 함수를 이벤트 핸들러 또는 이벤트 리스너라고 부른다.
+ 자주 쓰이는 이벤트 정보는 [w3schools](https://www.w3schools.com/js/js_events.asp)에서 확인할 수 있다.

+ 키보드 이벤트
	+ 운영체제에 영향을 받아 특정 키가 이벤트 핸들러에게 전달되지 않을 수 있다.
	+ `onkeypress`은 아스키 코드를 기준으로, `onkeydown`은 키 코드 기준으로 호출되는데 키 코드는 항상 있지만 아스키 코드는 키보드와 매칭되는 것이 없을 수도 있다.
+ 폼 이벤트
	+ 웹 초기부터 지원되어 여러 웹 브라우저에서 가장 안정적으로 동작하는 이벤트
	+ 대표적으로 `onsubmit`이 있다.

### 이벤트 핸들러

1. 인라인 이벤트 핸들러
	+ 화면의 구조를 담당하는 `html`에 동적인 요소를 만들어주는 `JS`가 침범한다는 문제가 있다.
	+ CBD(Component Based Development) 방식의 Anglar / React / Vue.js 등의 프래임워크나 라이브러리에서는 해당 방식으로 이벤트를 처리한다. (MVC 등의 관점으로 html, css, js 를 묶어 View로 취급하기 때문)

```
<head>
	<meta charset="UTF-8" />
	<title>Insert title here</title>
	<script type="text/javascript">
		var msg1 = function () {
			alert("안녕하세요!!");
		};
		var msg2 = function () {
			var msg = document.querySelector("#div1");
			msg.style.color = "purple";
			msg.style.fontSize = "30px";
			msg.style.fontWeight = "bold";
		};
	</script>
</head>
<body>
	<!-- 인라인 이벤트 방식 1 -->
  <div onclick="alert('안녕하세요');">클릭해보세요</div>
	
	<!-- 인라인 이벤트 방식 2 -->
	<div id="div1" onclick="msg1(); msg2();">클릭해보세요</div>
</body>
```

2. 이벤트 핸들러 프로퍼티
	+ JS에서 이벤트 핸들러를 등록하는 방식
	+ 이벤트 핸들러를 여러 개 설정하고 싶다면 addEventListener를 활용하자.
		+ addEventListener는 캡쳐린과 버블링을 지원하며 모든 DOM(HTML, XML, SVG)에 대해서도 동작한다.

```
<!-- 이벤트 핸들러가 하나만 등록된다. -->
<button id="btn">클릭해보세요</button>
<script type="text/javascript">
	const btn = document.querySelector('#btn');
	// 첫번째 바인딩된 이벤트 핸들러 ==> 실행되지 않는다.
	btn.onclick = function () {
		alert('안녕하세요!!');
	};
	// 두번째 바인딩된 이벤트 핸들러
	btn.onclick = function () {
		btn.style.color = 'purple';
		btn.style.fontSize = '30px';
		btn.style.fontWeight = 'bold';
	};
</script>

<!-- 이벤트 핸들러를 여러 개 등록한다. -->
<button id="btn">클릭해보세요</button>
<script type="text/javascript">
	const btn = document.querySelector('#btn');
	// 첫번째 바인딩된 이벤트 핸들러
	btn.addEventListener('click', function () {
		alert('안녕하세요!!');
	});
	// 두번째 바인딩된 이벤트 핸들러
	btn.addEventListener('click', function () {
		btn.style.color = 'purple';
		btn.style.fontSize = '30px';
		btn.style.fontWeight = 'bold';
	});
</script>
```

+ 추가 (이벤트 핸들러 내부에 인수를 전달하고 싶은 경우)

```
const MIN_ID_LENGTH = 8;
const input = document.querySelector('input[type=text]');
const msg = document.querySelector('.message');

function checkVal(len) {
	if (input.value.length < len) {
		msg.innerHTML = '값은 ' + len + '자 이상 입력해 주세요';
	} else {
		msg.innerHTML = '';
	}
}

input.addEventListener('blur', function () {
	// 이벤트 핸들러 내부에서 함수를 호출하면서 인수를 전달.
	// 예시로 상수를 사용하였지만 변수인 경우에도 사용 가능
	checkVal(MIN_ID_LENGTH);
});
```

## Web Storage (웹 스토리지)

+ 영구으로 데이터를 저장하기 위해 사용하는 저장소
+ key-value 세트로 저장이 되며 도메인과 브라우저 별로 문자열 형식으로 저장이 된다.
+ 웹 스토리지에 대한 함수는 [w3schools](https://www.w3schools.com/js/js_api_web_storage.asp)를 참고하자.

+ Local Storage
	+ 데이터를 사용자 로컬에 보존하는 방식
	+ JS로 기본적인 데이터 저장, 삭제 등의 조작 가능 (모바일에서도 사용 가능)
	+ 쿠키와 다르게   
		+ 유효기간이 없고 영구적으로 이용이 가능
		+ 쿠키에 비해 많은 데이터 저장 가능 (storage는 5mb 정도, cookie는 4kb 정도)
		+ 네트워크 요청 시 서버로 전송이 되지 않아 서버가 조작 불가함
		+ origin(프로토콜, 도메인, 포트)가 다르면 접근 불가
+ Session Storage
	+ 저장되는 위치만 달라질 뿐 위와 같은데 같은 세션에서만 사용가능하다. (사용하는 함수도 같다.)   
	+ 즉, 현재 탭에서만 데이터가 유지되고 새로고침 등의 이유로 탭에서 벗어나면(새로운 응답을 받으면) 사라진다.

```
function init() {
	//localStorage 데이터 추가 방법 3가지
	localStorage.Test = 'Sample';
	// localStorage["Test"] = "Sample";
	// localStorage.setItem("Test", "Sample");
	
	//LocalStorage 데이터 취득 방법 3가지
	var val = localStorage.Test;
	// var val = localStorage["Test"];
	// var val = localStorage.getItem("Test");
	
	//localStorage 데이터 삭제
	localStorage.removeItem("Test");
	
	//localStorage 모든 데이터 삭제
	localStorage.clear();
}
```

F12(개발자 모드)의 로컬/세션 스토리지에서 저장된 데이터를 확인할 수 있다.
