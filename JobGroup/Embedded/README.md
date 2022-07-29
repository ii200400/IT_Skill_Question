# Embedded

그 강의에서 한 첫번째 프로젝트가 상상 놀이터라는 소아병동 IOT 프로젝트였는데, 이 때 겪었던 배운 내용, 버그나 오류를 지라에 정리하기는 하였으나 학기 끝나면 사라질 예정인 페이지라 이곳에 정리하기로 하였다.

강의를 듣고 정리한 내용은 아니므로 잘 정리하지는 못할 것 같다.

- [경험한 에러를 정리한 페이지](./problems/README.md)

## Raspberry pi

## GPIO(General Purpose Input/Output)

```
다용도 입출력(general-purpose input/output, GPIO)은 입력이나 출력을 포함한 동작이 런타임 시에 사용자에 의해 제어될 수 있는, 집적 회로나 전기 회로 기판의 디지털 신호 핀이다.

-위키백과-
```

필자는 단순하게 핀과 GPIO에 대해 아래와 같이 알고 있다.

- 라즈베리파이에는 전력이 공급되는 핀(Power), 전력이 나가는 핀(Ground) 등 다양한 핀이 있다.
- 개발자가 입출력에 사용할 수 있는 핀은 GPIO라고 불린다.
  - 입출력 외에도 다양한 역할을 가지는 경우가 있다. 핀 맵의 괄호의 내용을 보면 알 수 있다.
  - 필자의 기억으로는 특별한 역할을 가진 센서의 핀은 라즈베리파이의 적절한 GPIO에 넣어야지만 작동했던 것 같다. (불확실)

![image](https://user-images.githubusercontent.com/19484971/181657619-1490b328-0a19-4bc7-82bc-157616ac25bf.png)

참고

- [라즈베리파이 GPIO 핀 번호](https://fishpoint.tistory.com/6181)

## SSH

## get-apt와 apt의 차이

### pip와 apt-get의 차이

## JS에서 Python 파일 실행하기

프로젝트 중 라즈베리파이 센서의 값을 웹으로 송신해야하는 경우가 생겨 컨선턴트님께 여쭤보았더니 방법이 있으시다고 하셔서 검색해서 아래와 같이 실습을 해보았다.

잘 작동해서 놀랐다..

test.js 파일

```
var spawn = require("child_process").spawn;

// 2. spawn을 통해 "python 파이썬파일.py" 명령어 실행
const result = spawn("python", ["./hello.py"]);

// 3. stdout의 'data'이벤트리스너로 실행결과를 받는다.
result.stdout.on("data", function (data) {
  console.log("111", data.toString());
});

// 4. 에러 발생 시, stderr의 'data'이벤트리스너로 실행결과를 받는다.
result.stderr.on("data", function (data) {
  console.log("222", data.toString());
});
```

hello.py

```
def getValue():
    print ("value")

if __name__ == '__main__':
  a='a'
  a.toInt()
  getValue()
```

결과 (정상 작동시)

```
[Running] node "c:\Users\IM\Desktop\test.js"
111 value


[Done] exited with code=0 in 0.806 seconds
```

결과 (에러 발생시)

```
[Running] node "c:\Users\IM\Desktop\test.js"
222 Traceback (most recent call last):
  File "./hello.py", line 7, in <module>
    a.toInt()
AttributeError: 'str' object has no attribute 'toInt'


[Done] exited with code=0 in 1.013 seconds
```

참고

- [[Node.js] 자바스크립트로 파이썬 연동 실행 방법(함수 매개변수 전달 호출 : child-process)](https://curryyou.tistory.com/225)
- [자바스크립트에서 Python 파일 실행하기](https://doongdoongeee.tistory.com/148)
