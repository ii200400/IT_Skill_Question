CS에서 보이는 이미지들을 모아놓음

파일의 이름은
'(분류 숫자). (소분류 이름)(몇번째).파일형식'
ex)1-1. List2.png

이미지를 상대적 경로를 이용해서 올리려고 할 때
```
![test image](1.1%20Array1.png)
```
![test image](1.1%20Array1.png)

+이미지 크기를 조절하고 싶을 때
```
<img src="1.1%20Array1.png" width="40%" height="40%">
```
<img src="1.1%20Array1.png" width="40%" height="40%">

이미지를 절대적 경로를 이용해서 올리려고 할 때
```
![test image](https://github.com/ii200400/IT_Skill_Question/blob/master/CS/image/1.1%20Array1.png)</code>
```
![test image](https://github.com/ii200400/IT_Skill_Question/blob/master/CS/image/1.1%20Array1.png)

참고로 ../는 상위 파일 ./는 현재파일 (때문에 1.1%20Array1.png 과 ./1.1%20Array1.png 은 같다.)

**참고로 빈칸(스페이스 바)은 %20으로 채워주어야 한다. \
위의 1.1%20Array1.jpg는 원래 1.1 Array1.jpg이다.**
