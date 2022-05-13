# vue

+ vue.js

도데체 최ㅅㄹ님은 어떻게 들으면서 작성하시는 것인지..
FE부터 밀렸는데 언제 정리하냐..
ssr(server side rendering) csr(client side rendering), sfc(single file conponent)?

## 개요

준비 항목

+ VSCode
+ Live Server
+ 필수 Extention - vuter, vue 3 snippets
+ Chrome 웹스토어 - Vue.js devtools
  + vue 사용시 f12 개발자도구를 통해 vue 탭에 들어가면 data를 바꿀 수 있게 된다.

Vue.js 참고문서
+ [가이드 문서](https://kr.vuejs.org/v2/guide/)
+ [API 문서](https://kr.vuejs.org/v2/api/)

추가 사항

DOM, 가상 DOM

DOM (리얼 DOM) : 실제 html 태그들 (view)
가상 DOM : vue에서 가상 돔을 만들고, 리얼 DOM에 매핑해준다. (view model)
SSR, CSR

server side rendering
client side rendering
div에 데이터를 주입할 때, server단에서 이 기능을 수행해주는지, client단에서 이 기능을 수행해 주는지에 따라 방식이 나뉜다.
렌더링

html(dom) 해석해서 화면에 뿌려주는 작업
나중에 더 공부해보기

## Vue.js

정의?

[가이드문서 - 설치방법](https://kr.vuejs.org/v2/guide/installation.html)

1. CDN
2. npm
3. vue-cli

+ CDN으로 사용하기

```
<!-- 개발버전, 도움되는 콘솔 경고를 포함. -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<!-- 상용버전, 속도와 용량이 최적화됨. -->
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<div id="app">
    <h2>{{message}}</h2>
</div>
```

```
// 인스턴스 생성
new Vue({
    el: "#app",
    // data: {
    //     message: "안녕 Vue!!!!"
    // }
    data() {
        return {
            message: "안녕 Vue"
        }
    },
})
```

## MVVM Pattern

양방향 데이터 렌더링 기능이 특징인 vue에서 사용하는 디자인 패턴   
웹에서만 사용되는 디자인 패턴은 아니다.

+ Model + View + ViewModel
  + Model : 순수 자바스크립트 객체, 데이터를 저장하는 역할
  + View : 웹 페이지의 Dom/Html, 화면에 데이터를 표현하는 역할
  + ViewModel : Vue 객체, model과 view를 연결시키는 양방향 데이터 바인딩을 해주는 역할

## vue instance

Vue 인스턴스
[가이드 문서 - 인스턴스](https://kr.vuejs.org/v2/guide/instance.html)

el - element
data - data
template - 화면에 표시할 속성
methods - 로직 제어, 이벤트 처리 등
created - init이랑 똑같은것, Life Cycle Hook
유효범위 → el 태그 범위 내에서만 적용됨

+ vue 객체가 created 이후 element와 연결된다.
+ life cycle은 크게 생성, 부착, 갱신, 소멸로 나뉜다.
  + 데이터를 관리에 필수적으로 쓰인다.
  + 몇 가지 더 있지만 꼭 필요한 것은 아니다.

### Life Cycle

[가이드문서 - 라이프사이클 다이어그램](https://kr.vuejs.org/v2/guide/instance.html#%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8)

<img src = "https://kr.vuejs.org/images/lifecycle.png" width="400">

+ created - 변수 초기화, 보통 여기에서 통신이 이루어진다. (back-end와 뭔가 처리)
+ mounted - el, dom, data 연결!
+ updated - data나 화면이 바뀔때 호출
+ destroyed - 끝낼때.

인스턴스를 만들고 실행시켜보자.

```
// 각 라이프 사이클에서 데이터가 어떻게 변하는지 관찰해보자.
// 라이프 사이클 후킹
new Vue({
  data: {
      a: 1
  },
  created: function () {
      // `this` 는 vm 인스턴스를 가리킵니다.
      console.log('a is: ' + this.a)
  },
})
// => "a is: 1"
```

### 템플릿

[가이드 문서 - 템플릿 문법](https://kr.vuejs.org/v2/guide/syntax.html)

## 보간법(Interplation)

[가이드 문서 - 뷰 보간법](https://kr.vuejs.org/v2/guide/syntax.html#%EB%B3%B4%EA%B0%84%EB%B2%95-Interpolation)

문자열
+ 데이터 바인딩의 가장 기본 형태는 "Mustache" 구문(이중중괄호)를 사용하여 텍스트 보간법을 사용한다.


{{ ~~~~ }} : 데이터 바인딩
```
<div id="app">{{message}}</div>
```


## 디렉티브(Directives)

+ vue에서의 `v-`접두사가 있는 특수 속성
+ 디렉티브의 속성 값은 단일 javaScript 표현식이 된다. (v-for는 예외)
+ 디렉티브는 표현식의 값이 변경될 때 추가적인 효과를 실시간(반응형)으로 DOM에 적용시키는 역할을 가진다.

+ v-model
  + 양방향 바인딩 처리를 위해서 사용
+ v-bind
  + 엘리먼트의 속성에 비인딩 처리를 위해 사용
  + 속성과 같이 쓰이는 특징이 있다.
  + `:`로 대체 가능
+ v-show
  + 조건에 따라 엘리먼트를 화면에 렌더링 
  + style의 display를 조정하여 보이지 않기 때문에 보이지만 않을 뿐 크기는 가지고 있다.
+ v-if, v-if-else, v-else
  + 조건에 따라 엘리먼트를 화면에 렌더링
  + v-for="(item, index) in items" :key="index
  + v-for="item in items" :key="index
  + 위의 문법을 따르며 key는 꼭 같이 사용해주어야 작동한다.

![image](https://user-images.githubusercontent.com/19484971/166411232-21ae4a55-84e9-49e3-b9d7-a8e54b7c8e27.png)

+ v-for
  + 배열이나 객체의 반복에 사용
  + 2.x 버전에서는 v-for 구문이 더 높은 우선순위를 가지고
    3.x 버전에서는 v-if 구문이 항상 더 높은 우선순위를 가진다.
    때문에 2버전은 모든 데이터를 불러오고 if문으로 걸러주기 때문에 조금 더 느리다고 한다.
+ v-clock
  + Vue instance가 준비될 때 까지 mustache를 숨기는데 사용
  + 잘 안 쓰인다고 한다.

+ v-once :  화면에 한번 뿌리면 data가 변해도 화면이 안바뀐다.
```
<h2>{{message}}</h2>
<h2 v-once>변하지 않는것 : {{message}}</h2>
```
v-html : message가 html 문법이면 변환해서 뿌려준다.
```<div id="app">{{message}}</div> <!-- 일반 텍스트 -->
<div id="app" v-html>{{message}}</div> <!-- html 문서 -->
```
```
message: "<h2>안녕 vue</h2>"
```
v-text="message" : el 안에  message를 뿌려준다. el 안에 있던 다른 내용은 무시
```
<!-- 같은 표현 -->
<span v-text="msg">무시됩니다.</span>
<span>{{msg}}</span>
```

{{  javascript 문법 사용 가능 }}

## Component

아파서 정리 못했다;;

## Router

위와 동문;

## NodeJS

자바 스크립트를 브라우저 밖에서 application처럼 실행시킬 수 있게 만들어주는 툴

NodeJS 를 설치하면서 NPM을 같이 설치하고 NPM을 통해서 @vue/cil를 설치할 예정이다.

[NodeJS LTS](https://nodejs.org/ko/)를 설치하여서 필자는 NodeJS(v16.15.0)과 NPM(8.5.5)을 설치하고 진행하였다.


## NPM (Node Package Manager)

+ Command 에서 써드파티 모듈을 설치하고 관리하는 툴
+ 패키지 매니저, 스프링의 maven, 파이썬의 pip 과 비슷한 역할을 수행한다.
+ [npm 사이트](https://www.npmjs.com/)에서 모튤 검색이 가능하다.
  + $ npm init   
    새로운 프로젝트나 패키지를 만들 때 사용 (package.json 생성)
  + $ npm install package   
    생성되는 위치에서만 사용 가능한 패키지로 설치
  + $ npm install -g package   
    글로벌 패키지에 추가, 모든 프로젝트에서 사용 가능한 패키지로 설치
  + 일반적으로 npm 모듈 소개 페이지에서 추천하는 방식으로 사용한다.   
    -g을 추천하면 넣고 사용하지 않으면 넣지 않고 설치한다.

## SFC (Single File Component)

+ 확장자가 `.vue`인 파일
+ `.vue` = template(html) + script + style 세 가지의 파일을 하나의 파일로 관리한다.
  + template : html을 기본 언어로 하며 vue 파일 마다 최대 하나의 template 블록을 가진다.
  + script : js를 기본언어로 하며 vue 파일 마다 최대 하나의 script 블록을 가진다.
    s는 ES6를 지원하며 import와 export를 사용할 수 있다.
  + style : css를 기본 언어로 하며 vue 파일마다 여러개의 style 블록을 가질 수 있다.
  + .vue 파일들은 실행시 모여 index.html 파일 하나로 변환된다.
+ 구문 강조가 가능
+ 컴포넌트에만 CSS의 범위를 제한할 수 있음
+ 전처리기를 사용해 기능의 확장이 가능

## @vue/cil (Command Line Interface)

+ vue 개발을 위해 공식적으로 제공되는 CLI 기반의 스캐폴딩 도구
  + 스캐폴딩 : 개발을 쉽게 시작할 수 있도록 기본 구조(인터페이스 등)를 미리 만들어 제공해주는 것
+ [vue cli 공식 사이트](https://cli.vuejs.org/)

설치 및 실행
+ $ npm install -g @vue/cli 으로 npm을 통해 설치한다.
+ $ vue create project-name 으로 @vue/cil 프로젝트를 생성한다.
+ 원하는 설정을 고르고 진행한다, 필자의 설정은 아래의 그림을 참고하자.
+ 터미널 창에서 프로젝트가 생성된 폴더로 이동하고 npm run serve를 실행시킨다.
+ localhost:8080에서 결과를 확인한다.
  
강의를 따라 아래와 같이 설정하였다.

![image](https://user-images.githubusercontent.com/19484971/167975026-cebd3f16-59f1-4cf7-aa8a-ed3aba2d41b1.png)

prettier 에러 해결 과정

+ Vue는 컴포넌트 이름에 합성어를 사용해야 한다
  + 단순히 Login.vue라고 하면 안되고 LoginView.vue의 최소 두 단어를 포함한 이름을 사용한다.
+ Vue는 end line CRLF를 지원하지 않는다. LF 사용하기 (윈도우)
  + package.json → eslineConfig → rule 추가
    ``` 
    "rules": {
      "prettier/prettier": ["error", { "endOfLine": "auto" }]
    } 
    ```
+ vue는 tab space size 2만 지원한다.
  + vscode → ctrl + , → prettier Tab Width : 2
  + 에러가 생기는 파일로 가서 우클릭 - Fromat Document With.. - Prettier 로 정렬해준다.
  + 필자는 Extension에서 ExtionPrettier - Code formatter 를 사용하고 있는데 영향이 있는지 모르겠다;
+ 프로젝트를 껐다가 다시 켜준다. (npm run serve)

### 프로젝트 구조



[dependency 버전 설정](https://blog.outsider.ne.kr/1041)
[package.json과 package-lock.json의 차이점](https://velog.io/@songyouhyun/Package.json%EA%B3%BC-Package-lock.json%EC%9D%98-%EC%B0%A8%EC%9D%B4)
