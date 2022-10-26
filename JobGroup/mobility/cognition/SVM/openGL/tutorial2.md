# Tutorial 2 : The first triangle

간단한 삼각형을 그리는 튜토리얼이다. 커스텀한 쉐이더를 적용시키기도 한다!

아래는 이번 튜토리얼에서 알아두면 좋은 개념들이다. 어렵지 않으니 한번 쓱 읽어보자.

- VAO(Vertex Array Object)
	- 많은 양의 정점들을 GPU 메모리에 저장하기 위해 사용하는 객체
    - openGL에서 사용하는 객체 중 하나로 창이 생성되면(= OpenGL 컨텍스트 생성 후) 다른 OpenGL 호출 전에 해당 객체에 대한 작업을 먼저 진행한다.
    - 다른 튜토리얼에서 자세히 다루므로 이 튜토리얼에서는 단순히 정점을 배열로 저장하는 객체라고 생각하고 넘어가자.
- 화면좌표(Screen Coordinates)
    - openGL에서 가장 기본이 되는 물체인 삼각형을 만들 때 세 점(points)으로 정의할 수 있다.
    - 3D 그래픽에서 점은 버텍스(vertex, 정점)라고 말한다.
    - 3D 그래픽이기 때문에 버텍스는 X, Y 및 Z의 3가지 좌표가 있다.
    - 컴퓨터를 바라보고 사용하고 있는 사람을 기준으로 X는 오른쪽, Y 는 위쪽, Z는 뒤쪽이다.
        - 편하게 오른손 법칙을 활용하면 X는 엄지손가락, Y는 검지손가락, Z는 가운데 손가락이라고 생각하자.
    - 화면의 중앙은 (0, 0, 0)이다.
        - 위에서 바라볼 때(z축 정보를 무시할 때), (-1,-1)은 화면의 왼쪽 하단 모서리이고 (1,-1)은 오른쪽 하단이고 (0,1)은 중간 상단이다.
- 그래픽 파이프라인(graphics pipeline)
	- 3D 좌표를 2D 좌표로 변환하는 작업과 2D 좌표를 색이 들어간 픽셀로 변환하는 작업을 한다.
	- 여러 단계(작업)로 나뉘어 병렬로 실행될 수 있다.
		- GPU를 통해 실행된다.
		- 데이터를 빠르게 처리할 수 있고 수천 개의 작은 프로그램으로 나뉘기도 한다.
		- 이 작은 프로그램들이라는 것은 **shaders**라고 불린다.
		- 쉐이더는 OpenGL Shading Language (GLSL) 로 작성된다.
	- 해당 작업은 커스텀이 가능하다.

아래 사진은 그래픽 파이프라인의 모든 단계가 추상화된 모형이다. 파란색으로 칠해진 부분은 커스텀할 수 있는 쉐이더이다.

<img src="https://user-images.githubusercontent.com/19484971/197345065-602c59c2-4fb5-4531-9469-0b6870386829.png" width=500>

현대 OpenGL에서 최소한 vertex shader와 fragment shader는 직접 작성할 것을 요구하는데, 이는 GPU에 기본 vertex/fragment shader가 존재하지 않기 때문이라고 한다; 때문에 해당 튜토리얼은 시작하기 전에 알아두어야 할 것이 많은 것이다.

위의 내용은.. 대부분의 내용을 생략한 것이고 자세한 과정을 알고 싶다면 [Learn OpenGL 번역] 2-4. 시작하기 - Hello Triangle](https://heinleinsgame.tistory.com/7?category=757483)를 참고하자.

## 삼각형 그리기

삼각형을 그리기 위해서는 이 예제에서 처럼 간단한 세 가지 좌표를 가진 세가의 버텍스가 필요하다.
```
static const GLfloat g_vertex_buffer_data[] = { 
    -1.0f, -1.0f, 0.0f,
    1.0f, -1.0f, 0.0f,
    0.0f,  1.0f, 0.0f,
};
```

위의 버텍스를 정점으로하고 쉐이더를 적용시킨 삼각형을 만들어볼 것이다.

먼저 버퍼를 생성하여 삼각형 데이터를 넘겨준다.
```
// This will identify our vertex buffer
// vertex buffer 변수 생성
GLuint vertexbuffer;
// Generate 1 buffer, put the resulting identifier in vertexbuffer
// 버퍼 1개를 생성하고 해당 버퍼의 ID(name이라고도 한다.)를 vertexbuffer에 저장한다.
glGenBuffers(1, &vertexbuffer);
// The following commands will talk about our 'vertexbuffer' buffer
// 'vertexbuffer'를 GL_ARRAY_BUFFER라는 유형의 버퍼에 `바인드` 한다. 
// 바인딩(binding) : 프로그램에 사용된 구성 요소의 실제 값 또는 프로퍼티를 결정짓는 행위
glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
// Give our vertices to OpenGL.
// openGL에 vertex 데이터를 전달
// 미리 정의된 정점 데이터(g_vertex_buffer_data)를 버퍼의 메모리에 복사하는 것
glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);
```

```
// 1st attribute buffer : vertices
// 첫번째(0) 버퍼의 속성은 버텍스
glEnableVertexAttribArray(0);
// 위에 같은.. 코드가 있는데 왜 또 있지..?
glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
glVertexAttribPointer(
    0,                  // attribute 0. No particular reason for 0, but must match the layout in the shader. (첫번째 속성 데이터라는 것, 첫번째라는 것에 큰 의미는 없다.)
    3,                  // size (버텍스의 x, y, z 세 개의 정보를 말하는 것 같다.)
    GL_FLOAT,           // type (버텍스가 가진 정보는 float이다.)
    GL_FALSE,           // normalized? (정규화는 되지 않았다.)
    0,                  // stride (?)
    (void*)0            // array buffer offset (오프셋 설정여부같다.)
);

// Draw the triangle !
// 삼각형 그리기
// 인덱스 0부터 2까지의 버텍스를 사용하여 1개의 삼각형을 만든다.
glDrawArrays(GL_TRIANGLES, 0, 3); // 3 indices starting at 0 -> 1 triangle
glDisableVertexAttribArray(0);
```

여기까지하면 흰색 삼각형을 볼 수 있다고 한다. 그런데 필자는 튜토리얼 코드를 전부 복사해서 보지는 못했다.

<img src="https://user-images.githubusercontent.com/19484971/197085915-ddba56d0-1301-4e38-91e0-ab593de8535c.png" width=200>

이 삼각형에 빨간색을 입히기 위해 쉐이더를 사용해보겠다!

## 셰이더(Shaders)

튜토리얼에서는 셰이더 설명도 안하네 아이고난..

> 컴퓨터 그래픽스 분야에서 셰이더(shader)는 소프트웨어 명령의 집합으로 주로 그래픽 하드웨어의 렌더링 효과를 계산하는 데 쓰인다.   
-위키백과-

어.. 그냥 3D 그래픽에서 그려지는 물체에 색상, 질감 등을 입혀 시각적으로 조금 더 실감나게 볼 수 있도록 사용하는 소프트웨어 명령들이라고 생각해야겠다. (게임할 때 렌더링이라는 말은 들었는데 뭐였는지는 정확히 모르겠다.)

- openGL에서의 셰이더
    - 최소 두 개의 셰이더 코드를 사용해서 적용한다.
        - 하나는 정점 셰이더(VertexShader)라고 하는 각 정점에 대해 실행되는 셰이더 
        - 다른 하나는 프래그먼트(FragmentShader) 각 샘플에 대해 실행되는 셰이더
        - 두 셰이더는 일반적으로 별도의 파일에 있는데 이 예제에는 SimpleFragmentShader.fragmentshader 와 SimpleVertexShader.vertexshader로 되어있다. 
    - LoadShaders라는 함수에 두 개의 셰이더 코드 경로를 넣어주면 내부에서 알아서 작동된다.
        - 튜토리얼에서 LoadShaders 함수의 내부도 보여주었지만.. 생략한다..!
	- 확장자는 관련이 없어(늬에..?) .txt 또는 .glsl 로 해도 된다.
	- GLSL(OpenGL Shading Language)은  shader 언어이다, 튜토리얼에서도 사용한다. 
		- C나 C++과 거의 비슷하게 보이는 것도 사실이다.

더 자세한 내용을 바란다면 [이곳](https://heinleinsgame.tistory.com/8?category=757483)을 참고하자.

### 정점 셰이더(Vertex Shader)

먼저 정점 셰이더를 살펴보고 다음에 프레그먼트 셰이더를 보겠다.

첫 번째 줄은 컴파일러에게 OpenGL3을 사용할 것임을 알려주고 두번째 줄은 입력 데이터를 선언한다.

```
// 컴파일러에게 OpenGL 3.3의 구문을 사용할 것임을 알림
#version 330 core

// Input vertex data, different for all executions of this shader.
// 입력 데이터를 선언한다.
layout(location = 0) in vec3 vertexPosition_modelspace;
```

여기서 두 번재 줄이 특히 중요한데 하나하나 뜯어보면 아래와 같..다.

- "vec3"
    - GLSL에서 3개의 구성요소로 구성된 벡터이다.
        - 현 튜토리얼에서 구성요소 개수가.. C++에서 작성한 glVertexAttribPointer의 size와 같아야 하는 것 같다. 마찬가지로 구성요소는 type, 현 튜토리얼에서는 float를 의미하는 것 같다. (더 정확한 설명이 없어 유추하였다.)
    - 확실한 것은 C++ 코드에서 3개의 구성 요소를 사용하는 경우 GLSL에서도 3개의 구성 요소를 사용해야한다는 것
    - C++ 코드에서 삼각형을 선언하는 데 사용한 glm::vec3과 비슷하지만 다르다고 한다.
- "layout(location = 0)"
    - vertexPosition_modelspace 속성(성질이 아닌 객체의 속성)에 값을 제공할 때 사용하는 버퍼를 의미한다.
    - 버퍼가 가진 버텍스의 데이터는 위치, 하나 또는 여러 색상, 하나 또는 여러 텍스처 좌표, 기타 많은 속성 등 수많은 속성(의미)을 가질 수 있다.
    - 값 "0"은 중요하지 않고 단순히 c++ 코드의 glVertexAttribPointer의 첫 번째 매개변수와 동일한 값으로 설정해야 한다.
- "vertexPosition_modelspace"
    - 변수명이다.
- "in"
    - 단순히 입력 데이터임을 의미한다.

저 한 줄 때문에 글이 정말 길었다.. 하지만 셰이더를 작성할 때 꼭 필요하다고 판단하여 확실히 짚고 넘어갔다.

그 다음으로는 각 꼭짓점에 대해 호출되는 함수(main)를 실행한다.

```
void main(){
	// 아래의 코드는 ​버퍼에 저장된 값을 그대로 정점의 위치​으로 설정해주는 기능일뿐이다.
	// gl_Position은 몇 안 되는 내장 변수 중 하나이고 꼭 값을 할당해야만 한다. 다른 것은 선택 사항이여서 생략이 가능하다.
    gl_Position.xyz = vertexPosition_modelspace;
    gl_Position.w = 1.0;

}
```

### 프래그먼트 셰이더(Fragment Shader)

Fragment shader는 픽셀의 출력 컬러 값을 계산하는 것에 관한 쉐이더이다.

다행히도 정점 셰이더와는 다르게 설명할 것이 적다! 각 조각(이 튜토리얼에서는 삼각형)의 색상을 빨간색으로 설정하는 것이 끝이다!

참고로 알파값까지 넣으려면 vec4를 활용하여 네 가지 수를 설정해주면 된다. `vec4(1.0f, 0.5f, 0.2f, 1.0f)` 이런식으로.
```
#version 330 core

// Ouput data
out vec3 color;

void main()
{
	// Output color = red 
	// 색상을 빨간색으로 설정 (0이 최소, 1이 최대)
	// 순서대로 빨강, 초록, 파랑을 의미한다.
	color = vec3(1,0,0);
}
```

## 셰이더 적용하기

커스텀 쉐이더를 사용하기 위해 common/shader.hpp이라는 이름의 파일을 불러와서 LoadShaders 함수를 사용할 것이다.

```
// 버퍼와 마찬가지로 셰이더에는 직접 액세스할 수 없고 ID를 통해 접근이 가능하다.
// 해당 예제에서는 LoadShaders 기능을 활용하기 위해서 아래의 파일을 불러온다.
#include <common/shader.hpp>
```

main 함수가 불리기 전에 LoadShaders 함수를 호출한다.

```
// Create and compile our GLSL program from the shaders
// 셰이더에서 GLSL 프로그램을 생성 및 컴파일한다.
GLuint programID = LoadShaders( "SimpleVertexShader.vertexshader", "SimpleFragmentShader.fragmentshader" );
```


```
// Clear the screen
// 스크린을 clear 한다. 커스텀 쉐이더를 넣기 전에 먼저 하는 것 같다.
// 게다가 이전 glClearColor(0.0f, 0.0f, 0.4f, 0.0f) 호출로 인해 배경색이 진한 파란색으로 된다.
glClear( GL_COLOR_BUFFER_BIT );

// Use our shader
// 위에서 등록한 쉐이더 사용
glUseProgram(programID);
```

그러면 빨간색 삼각형을 볼 수 있다!

<img src="https://user-images.githubusercontent.com/19484971/197103091-0bd48038-8796-4731-859c-a2511d53f5c9.png" width=200>

[다음 튜토리얼에서는 2D 변환](./tutorial3.md)을 배운다. 카메라를 설정하는 방법, 물체를 이동하는 방법이 있다.

## 전체 코드

`tutorial02.cpp`
```
// Include standard headers
#include <stdio.h>
#include <stdlib.h>

// Include GLEW
// 아래의 라이브러리보다 꼭 먼저 include 해주어야 한다.
#include <GL/glew.h>

// Include GLFW
// 3D 계산을 위한 라이브러리
#include <GLFW/glfw3.h>
GLFWwindow* window;

// Include GLM
#include <glm/glm.hpp>
// “glm::vec3”(“vec3” )을 입력하는 것을 강제한다. 
using namespace glm;

// 커스텀 쉐이더를 사용하기 위해 common/shader.hpp이라는 이름의 파일을 불러온다.
// 버퍼와 마찬가지로 셰이더에는 직접 액세스할 수 없고 ID를 통해 접근이 가능하다.
// 해당 예제에서는 LoadShaders 기능을 활용하기 위해서 아래의 파일을 불러온다.
#include <common/shader.hpp>

int main( void )
{
	// Initialise GLFW
	if( !glfwInit() )
	{
		// GLFW를 초기화 실패했다면 아래의 문자 출력
		fprintf( stderr, "Failed to initialize GLFW\n" );
		getchar();
		return -1;
	}

	// OpenGL 윈도우를 생성
	glfwWindowHint(GLFW_SAMPLES, 4);	// 4x 안티에일리어싱
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);	// OpenGL 3.3 을 쓸것이라는 내용
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);	//옛날 OpenGL은 사용하지 않는다는 의미

	// Open a window and create its OpenGL context
	// 새창을 열고, OpenGL 컨텍스트를 생성
	// 후술되는 코드를 보면, 이 변수는 전역(Global) 변수이다.
	window = glfwCreateWindow( 1024, 768, "Tutorial 02 - Red triangle", NULL, NULL);
	if( window == NULL ){
		// GLFW 윈도우를 여는데 실패했습니다. Intel GPU 를 사용한다면, 3.3 지원을 하지 않습니다. 2.1 버전용 튜토리얼을 시도하세요.
		fprintf( stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n" );
		getchar();
		// GLFW 종료 및 프로그램 종료
		glfwTerminate();
		return -1;
	}
	// GLEW 초기화
	// Initialize GLEW
	glfwMakeContextCurrent(window);
	glewExperimental = true; // Needed for core profile 코어 프로파일을 위해 필요함
	if (glewInit() != GLEW_OK) {
		// GLEW 초기화 실패
		fprintf(stderr, "Failed to initialize GLEW\n");
		getchar();
		glfwTerminate();
		return -1;
	}

	// Ensure we can capture the escape key being pressed below
	// 밑에서 Escape 키가 눌러지는 것을 감지할 수 있도록 할 것
	glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

	// Dark blue background
	// 배경 색상 설정
	glClearColor(0.0f, 0.0f, 0.4f, 0.0f);

	//  Vertex Array Object 를 생성
	GLuint VertexArrayID;
	glGenVertexArrays(1, &VertexArrayID);
	glBindVertexArray(VertexArrayID);

	
	// 3 버텍스들을 표현하는 3 벡터들의 배열
	// 최소한 두 개의 셰이더가 필요하다. 
	// 하나는 정점 셰이더(VertexShader)라고 하는데 각 정점에 대해 실행되고 
	// 다른 하나는 프래그먼트(FragmentShader) 셰이더라고 하며 각 샘플에 대해 실행된다.
	
	// 두 셰이더는 일반적으로 별도의 파일에 있는데 이 예제에는 SimpleFragmentShader.fragmentshader 와 SimpleVertexShader.vertexshader로 되어있다. 
	// 확장자는 관련이 없지만 일반적으로는 .txt 또는 .glsl 로 하는 것 같다.

	// 셰이더는 OpenGL의 일부인 GLSL: GL 셰이더 언어라는 언어로 프로그래밍된다. 
	// C 또는 Java와 달리 GLSL은 런타임에 컴파일된다. 
	// 즉, 애플리케이션을 시작할 때마다 모든 셰이더가 다시 컴파일된다.

	// LoadShaders의 내부 코드는 아래의 링크에서 확인할 수 있다. (그런데 무슨소리인지 모르겠다.)
	// http://www.opengl-tutorial.org/beginners-tutorials/tutorial-2-the-first-triangle/#shaders

	// Create and compile our GLSL program from the shaders
	// 셰이더에서 GLSL 프로그램을 생성 및 컴파일한다.
	GLuint programID = LoadShaders( "SimpleVertexShader.vertexshader", "SimpleFragmentShader.fragmentshader" );

	// 컴퓨터를 바라보고 사용하고 있는 사람을 기준으로
	// X는 오른쪽, Y 는 위쪽, Z는 뒤쪽 이라고 한다.
	// 오른손 법칙을 사용해도 좋다고 한다.
	static const GLfloat g_vertex_buffer_data[] = { 
		-1.0f, -1.0f, 0.0f,
		 1.0f, -1.0f, 0.0f,
		 0.0f,  1.0f, 0.0f,
	};

	// (0, 0)이 중앙이고 좌하단이 (-1,-1),  (1,-1)은 오른쪽 하단이고 (0,1)은 중간 상단이다.

	// This will identify our vertex buffer
	// vertex buffer 변수 생성
	GLuint vertexbuffer;
	// Generate 1 buffer, put the resulting identifier in vertexbuffer
	// 버퍼 1개를 생성하고 해당 버퍼의 ID(name이라고도 한다.)를 vertexbuffer에 저장한다.
	glGenBuffers(1, &vertexbuffer);
	// The following commands will talk about our 'vertexbuffer' buffer
	// 'vertexbuffer'를 GL_ARRAY_BUFFER라는 유형의 버퍼에 `바인드` 한다.
	// 바인딩(binding) : 프로그램에 사용된 구성 요소의 실제 값 또는 프로퍼티를 결정짓는 행위
	glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
	// Give our vertices to OpenGL.
	// openGL에 vertex 데이터를 전달
	// 미리 정의된 정점 데이터(g_vertex_buffer_data)를 버퍼의 메모리에 복사하는 것
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);

	do{
		// Clear the screen
		// 스크린을 clear 한다. 커스텀 쉐이더를 넣기 전에 먼저 하는 것 같다.
		// 게다가 이전 glClearColor(0.0f, 0.0f, 0.4f, 0.0f) 호출로 인해 배경색이 진한 파란색으로 된다.
		glClear( GL_COLOR_BUFFER_BIT );

		// Use our shader
		// 위에서 등록한 쉐이더 사용
		glUseProgram(programID);

		// 1st attribute buffer : vertices
		// 첫번째(0) 버퍼의 속성은 버텍스
		glEnableVertexAttribArray(0);
		// 설정을 바꾸면 다시 바인드를 해주어야 설정이 적용된다.
		glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
		glVertexAttribPointer(
			0,                  // attribute 0. No particular reason for 0, but must match the layout in the shader. (첫번째 속성 데이터라는 것, 첫번째라는 것에 큰 의미는 없다.)
			3,                  // size (버텍스의 x, y, z 세 개의 정보를 말하는 것 같다.)
			GL_FLOAT,           // type (버텍스가 가진 정보는 float이다.)
			GL_FALSE,           // normalized? (정규화는 되지 않았다.)
			0,                  // stride (?)
			(void*)0            // array buffer offset (오프셋 설정여부같다.)
		);

		// Draw the triangle !
		// 삼각형 그리기
		// 인덱스 0부터 2까지의 버텍스를 사용하여 1개의 삼각형을 만든다.
		glDrawArrays(GL_TRIANGLES, 0, 3); // 3 indices starting at 0 -> 1 triangle
		glDisableVertexAttribArray(0);

		// Swap buffers
		glfwSwapBuffers(window);
		glfwPollEvents();

	} // Check if the ESC key was pressed or the window was closed
	while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
		   glfwWindowShouldClose(window) == 0 );

	// Cleanup VBO
	glDeleteBuffers(1, &vertexbuffer);
	glDeleteVertexArrays(1, &VertexArrayID);
	glDeleteProgram(programID);

	// Close OpenGL window and terminate GLFW
	glfwTerminate();

	return 0;
}
```

`SimpleVertexShader.vertexshader`
```
// 컴파일러에게 OpenGL 3.3의 구문을 사용할 것임을 알림
#version 330 core

// Input vertex data, different for all executions of this shader.
// 입력 데이터를 선언한다.
layout(location = 0) in vec3 vertexPosition_modelspace;

void main(){

	// 아래의 코드는 정점의 위치를 ​​버퍼의 값으로 설정해주는 기능일뿐이다.
	// gl_Position은 몇 안 되는 내장 변수 중 하나이고 꼭 값을 할당해야 한다. 다른 것은 선택 사항이다.
    gl_Position.xyz = vertexPosition_modelspace;
    gl_Position.w = 1.0;

}
```

`SimpleFragmentShader.fragmentshader`
```
#version 330 core

// Ouput data
out vec3 color;

void main()
{
	// Output color = red 
	// 색상을 빨간색으로 설정 (0이 최소, 1이 최대)
	// 순서대로 빨강, 초록, 파랑을 의미한다.
	color = vec3(1,0,0);
}
```