# vue

`목차`

* [개요](#개요)
* [Vue.js](#vuejs)
* [MVVM Pattern](#mvvm-pattern)
* [vue instance](#vue-instance)
  + [Life Cycle](#life-cycle)
  + [템플릿](#템플릿)
* [보간법(Interplation)](#보간법interplation)
* [디렉티브(Directives)](#디렉티브directives)
* [Component](#component)
* [Router](#router)
* [NodeJS](#nodejs)
* [NPM (Node Package Manager)](#npm-node-package-manager)
* [SFC (Single File Component)](#sfc-single-file-component)
* [@vue/cil (Command Line Interface)](#vuecil-command-line-interface)
  + [prettier 에러 해결 과정](#prettier-에러-해결-과정)
  + [vue-cil 프로젝트 구조](#vue-cil-프로젝트-구조)
* [Vuex](#vuex)
  + [State](#state)
  + [Actions](#actions)
  + [Mustations](#mustations)
  + [Getters](#getters)
  + [Devtools](#devtools)
* [Bootstrap Vue](#bootstrap-vue)

```
나중에 더 공부할 내용

DOM, 가상 DOM

DOM (리얼 DOM) : 실제 html 태그들 (view)
가상 DOM : vue에서 가상 돔을 만들고, 리얼 DOM에 매핑해준다. (view model)

div에 데이터를 주입할 때, server단에서 이 기능을 수행해주는지, client단에서 이 기능을 수행해 주는지에 따라 방식이 나뉜다.
SSR(server side rendering) CSR(client side rendering), sfc(single file conponent) 은 다음에 정리하자.

html(dom) 해석해서 화면에 뿌려주는 작업
```

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

<img src = "https://v2.ko.vuejs.org/images/lifecycle.png" width="400">

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

뷰 컴포넌트를 구성하는 template, logic, style을 한 파일에 구현하는 특정한 형식의 파일이다.   
SPA(Single Page Application)를 제작하는데 필요한 요소(컴포넌트)이다.

SPA는 웹 사이트의 전체 페이지를 하나의 페이지에 담아 동적으로 화면을 바꿔가며 표현하는 애플리케이션을 의미한다.

+ 확장자가 `.vue`인 파일
+ `.vue` = template(html) + script + style 세 가지의 파일을 하나의 파일로 관리한다.
  + template : html을 기본 언어로 하며 vue 파일 마다 최대 하나의 template 블록을 가진다.
    + template 태그 내에는 단 하나의 태그만 사용해야만 한다.
  + script : js를 기본언어로 하며 vue 파일 마다 최대 하나의 script 블록을 가진다.
    + js는 ES6를 지원하며 import와 export를 사용할 수 있다.
  + style : css를 기본 언어로 하며 vue 파일마다 여러 개의 style 블록을 가질 수 있다.
    + 해당 파일에만 적용되는 style을 만들고 싶다면 scoped를 사용해야 한다.
  + .vue 파일들은 실행시 모여 index.html 파일 하나로 변환된다.
  + 위의 이유로 SPA(Single Page Application) 구현이 가능하게 된다.
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

### prettier 에러 해결 과정

+ Vue는 컴포넌트 이름에 합성어를 사용해야 한다
  + 단순히 Login.vue라고 하면 안되고 LoginView.vue의 최소 두 단어를 포함한 이름을 사용한다.
+ Vue는 end line CRLF를 지원하지 않는다. LF 사용하기 (윈도우)
  + package.json → eslineConfig → rule 추가
    ``` 
    "rules": {
      "prettier/prettier": ["error", { "endOfLine": "auto"}]
    } 
    ```
  + 싱글쿼테이션? 에러가 생기는 경우도 있다는데 필자는 생기지 않아서 잘 모르겠다;   
    위의 경우에는 'quotes': \['off', 'single'\]을 사용하면 된다는 말을 들었다.
+ vue는 tab space size 2만 지원한다.
  + vscode 설정에서 (ctrl + ,) prettier Tab Width : 2 로 바꾼다.
  + 에러가 생기는 파일로 가서 우클릭 - Fromat Document With.. - Prettier 로 정렬해준다.
    + 이후 Alt+Shift+F를 사용하면 prettier 포맷으로 정렬된다.
    + 설정의 Editer: Format On Save를 활용하면 위의 단축키 없어 저장할 때마다 정렬된다.
  + 필자는 Extension에서 ExtionPrettier - Code formatter 를 사용하고 있는데 영향이 있는지 모르겠다;
+ 프로젝트를 껐다가 다시 켜준다. (npm run serve)

### vue-cil 프로젝트 구조

정확히는 모르겠으므로 아는대로 작성해보겠다.

+ node_modules : 설치한 라이브러리들이 있는 파일
+ public
  + favicon.ico : 브라우저의 탭에 나타나는 이미지
  + index.html : SPA의 결과물이 되는 html 파일   
    기본적으로 app을 id로 하는 div 하나를 포함하고 있다.
+ scr
  + assets : 정적 파일들이 저장되는 파일
  + components : 컴포넌트(.vue)가 들어가는 파일
    + HelloWorld.vue : 기본적으로 제공되는 컴포넌트
  + router : vue 생성시 features에서 Router를 선택했다면 존재하는 파일
    + index.js : 라우터 역할을 하는 js 파일   
      경로에 대해 어떤 컴포넌트들을 활용하여 화면을 표시할지 결정한다. (.. 맞나..?)
      맞지 않는 경로를 요청받아도 에러가 생기지는 않는다;
  + store : vue 생성시 features에서 vuex를 선택했다면 존재하는 파일
    + index.js : vuex를 적용시키는 js 파일, vuex 설명은 해당 주제 바로 다음에 있다.
  + views
  + App.vue : 가장 먼저 불리는 컴포넌트, components 파일 내의 컴포넌트 파일을 활용(import)한다.
  + main.js : App.vue에 사용될 기본 객체를 정의한다.   
    객체는 mount시에 app을 id로 하는 태그에 등록되어 화면이 구현된다.   
    참고로 $mount("#app")는 el: "#app"와 같은 효과라고 한다.
+ jsconfig.json : 
+ babel.config.js : 
+ package-lock.json : 
+ package.json : 해당 프로젝트의 정보(이름, 버전, 활용 라이브러리 등)를 담고있는 파일
  뷰와 부트스트랩이 충돌하는지 잘 작동하지 않는 기능이 있다면 4.5.3으로 다운그래이드 하라고 하였다.
+ .gitignore : git 버전관리에 해당 파일들이 포함되지 않게된다.
  

음.. App.vue가 components들을 import 하고     
main.js가 App.vue를 import해서 화면이 구현된다.

여러 컴포넌트들을 잘 조합하여 화면(Dom)으로 표현해 주는 역할이 render라고 한다. (잘 모르겠다;)


router/index.js에 없는 라우팅을 요구해도 에러는 나지 않는다.

package.json의 파일내 아래의 줄 정도는 이해하는것이 좋을 것 같다.

"serve": "vue-cli-service serve",
"build": "vue-cli-service build",
"lint": "vue-cli-service lint"

[dependency 버전 설정](https://blog.outsider.ne.kr/1041)
[package.json과 package-lock.json의 차이점](https://velog.io/@songyouhyun/Package.json%EA%B3%BC-Package-lock.json%EC%9D%98-%EC%B0%A8%EC%9D%B4)

## Vuex

+ Vue.js 애플리케이션에 대한 상태관리패턴 + 라이브러리
+ 애플리케이션의 모든 컴포넌트들의 중앙 저장소와 데이터 관리의 역할을 가진다.
  + 상위(부모)와 하위(자식)의 컴포넌트의 관계가 복잡해지고 애플리케이션의 구성요소가 더욱 다양해지면서 데이터 전달과 공유 부분이 너무 복잡해지는 문제가 발생함에 따라 등장하였다.
+ 컴포넌트들은 vuex에 접근하여 데이터에 접근이 가능하도록 한다.
  + 컴포넌트가 직접 상태(데이터)를 바꾸는 것은 지양한다.
  + 하나의 저장소에 여러 컴포넌트들이 직접 연결된 단일 상태 트리 (Single State Tree)가 된다.
+ State, Actions, Mutation, Getter 로 나뉘어 데이터 관리를 한다.

작동 과정
1. 뷰의 컴포넌트에서 dispatch를 통해 vuex의 Actions를 호출한다.
2. Actions는 가지고 있는 메서드들 중에서 적절한 것을 사용한다. 
  + 메서드들은 대부분 서버 통신을 처리하기 위해 비동기로 작동된다.
3. 작업이 완료되면 commit을 통해 Mutation을 호출한다.
4. Mutations는 가지고 있는 메서드들 중에서 적절한 것을 사용한다. 
  + 메서드들은 State의 상태를 변경시키는 작업을 하기 때문에 동기로 작동된다.
  + 모든 메서드는 state를 인자로 가진다.
6. State의 상태가 변경되고 Render가 진행되어 

[공식 vuex 3.0 홈페이지](https://v3.vuex.vuejs.org/)

![image](https://user-images.githubusercontent.com/19484971/168512579-75c46e16-c106-4a5b-b9f9-d38e514c56ea.png)   
vuex 홈페이지에 있던 Vuex 작동 방식(State Management Pattern)

### State

+ 중앙에서 관리하는 모든 상태정보(data)를 관리
  + 상태정보는 여러 컴포넌트 내부에 있는 특정 데이터를 의미한다.
  + Vuex를 사용하기 이전에는 각 컴포넌트에서 데이터를 직접 확인했었다.
  + Vuex를 사용하면 Vuex Stroe에서 컴포넌트들이 사용하는 state를 한 눈에 파악할 수 있다.
+ Mutations의 method에 의해 변경됨
+ State가 변경되면 해당 state를 공유하는 모든 컴포넌트의 DOM이 자동 렌더링됨
+ 모든 Vue 컴포넌트는 Vuex Store에서 state 정보를 참조하여 사용

### Actions

+ 컴포넌트에서 dispatch() 메소드에 의해 호출됨
+ 주로 백엔드 API와 통신하여 Data Fetching 등의 작업을 수행
  + 때문에 메서드들은 대부분은 서버 통신을 처리하기 위해 비동기로 작동된다.
+ 항상 context가 인자로 넘어온다.
  + store.js 파일 내에 있는 모든 요소의 변경 및 호출 가능..
  + 하지만 state를 직접 변경하는 것은 권장하지 않는다.
+ Mutations에 정의되어있는 메서드들을 context.commit() 메서드를 통해 호출 가능
  + Mustaions의 메서드에서만 State를 변경하도록 조작한다.

### Mustations

+ Actions의 commit() 메서드에 의해 호출된다.
+ Actions의 메서드의 첫 번째 인자는 state이다.
  + 주로 state를 변경하는 작업을 하기 때문이다.
  + state의 변화 시점을 명확히 하기 위해 동기 작업만을 한다.

### Getters

+ Computed 와 유사하다.
  + State를 변경하지 않고 활용하여 계산을 수행하는 특징이 있기 때문
  + Getter 자체는 state를 변경시키지 않는다!

### Devtools

개발자가 제작한 프로그램이 생성, 테스트, 디버깅이 용이하도록 돕는 소프트웨어이다.

브라우저에서 F12키를 누르고 Vue탭에서 vuex의 작동을 자세히 확인할 수 있는데, 어느 시점에 어떤 함수가 불려 어떻게 값이 바뀌었는지 한 눈에 볼 수 있어 작업 흐름을 확인하거나 디버깅에 용이하다.

Vuex에 포함된 부분은 아니지만, 사용을 권장하는지 Vuex 공식 홈페이지에서도 Vuex가 해당 툴과 통합되어 있다는 언급이 있다.

## Bootstrap Vue

뷰에서 부트스트랩을 사용하는 실습을 해보았다.

터미널을 통해 프로젝트에 `npm install vue bootstrap bootstrap-vue` 명령어로 3가지 종류의 패키지들을 설치하고 app.js 혹은 main.js에 특정 코드를 추가해주어야지 사용이 가능하다고 했다. 내용은 공식 홈페이지를 참고하자!

[공식 홈페이지](https://bootstrap-vue.org/)

[template 페이지](https://bootstrap-vue.org/docs/reference/starter-templates)
