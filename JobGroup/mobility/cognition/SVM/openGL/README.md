# openGL

SVM을 제작하면서 3D 그래픽을 구현하기 위해서 openGL을 공부하게 되었다.

openGL이 무엇인지 찾아보았더니 아래와 같은 문구를 볼 수 있었다.

> 오픈 그래픽 라이브러리은 1992년 실리콘 그래픽스사에서 만든 2차원 및 3차원 그래픽스 표준 API 규격으로, 프로그래밍 언어 간 플랫폼 간의 교차 응용 프로그래밍을 지원한다.   
-위키백과-

간단하게 openGL은 `Open Graphics Library`의 약자로 그래픽 처리를 위한 API이다. API를 실재로 개발하는 사람들은 그래픽 카드 제조업체이고 필자같은 일반 학생은 openGL에서 지원하는 응용 프로그래밍을 사용하는 정도에 그치기 때문에 API를 알기보다는 openGL에서 사용하는 함수와 객체를 이해하고 어떻게 활용하는지를 잘 파악하는 것이 중점이 된다. 

모든 OpenGL 버전에 대한 사양 및 확장에 대한 정보는 [이곳](https://registry.khronos.org/OpenGL/index_gl.php)에서 확인할 수 있다.

평소에는 오픈소스를 자주보고 사용하는데 오픈 **그래픽** 라이브러리를 사용하게 되어서 꽤 신선하다. 잘 공부해두면 하드웨어 그래픽에 대한 기초를 쌓을 수 있을 것 같다!

## openGL 튜토리얼

기본적으로는 [opengl-tutorial](http://www.opengl-tutorial.org/)를 참고하여 진행하였으며 여기에 필자가 모르는 내용을 추가하면서 실습하였다.

[openGL을 잘 번역해주시고 설명도 친절하게 잘한 블로그](https://heinleinsgame.tistory.com/18?category=757483)도 많이 참고하였다.

사실 객체에 대한 내용을 먼저 작성할까 고민도 하였지만.. 너무 정보가 많아서 이해가 잘 되지 않는다;; 튜토리얼을 기준으로 보이는 코드를 조금씩 이해하는 방향으로 바꾸었다.

- [Tutorial 1 : Opening a window](./tutorial1.md)
- [Tutorial 2 : The first triangle](./tutorial2.md)
- [Tutorial 3 : Matrices](./tutorial3.md)
- [Tutorial 4 : A Colored Cube](./tutorial4.md)
- [Tutorial 5 : A Textured Cube](./tutorial5.md)
- [Tutorial 6 : Keyboard and Mouse](./tutorial6.md)
- [Tutorial 7 : Model loading](./tutorial7.md)
- [Tutorial 8 : Basic shading](./tutorial8.md)
