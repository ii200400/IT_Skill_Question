# Tutorial 1 : Opening a window

## 설치 및 환경

설치를 진행하고 무사히 검은색(혹은 파란색) 창이 만들어지는지 확인하는 튜토리얼이다. 튜토리얼을 보고 그대로 따라했는데 에러가 조금 있었지만 구글링으로 쉽게 해결되었다!

필자의 환경은 아래와 같다.

- 드라이버 : NVIDIA GeForce TRX 2070 Super with Max-Q Design
- 코드 편집기 : MS Visual Studio Express 2017
- 언어 : C++
- openCV 3.3
- CMake 3.24.2

openCV의 최신버전은 4.5버전이나 3.3버전을 기준으로 튜토리얼이 진행된다. 그 이유는 3.3 이후의 버전은 openGL의 핵심 기능에 대한 변경없이 최적화 작업이나 편리한 기능이 추가되었을 뿐이라 최신 OpenGL 버전과 동일하게 유지되기 때문에 개념과 기술을 배우는데 문제가 없고 상대적으로 호환성도 좋기 때문이라고 한다.

## 윈도우 열어보기

먼저 C++의 기본적인 라이브러리를 include 한다.
```
// Include standard headers
#include <stdio.h>
#include <stdlib.h>
```

다음으로 openGL에서 열심히 사용할 GLEW를 Include 한다. 
GLEW(OpenGL Extension Wrangler)은 플랫폼(운영체제) 마다 사용 방법이 다르고 복잡한 OpenGL을 손쉽게 사용할 수 있게 해주는 확장 라이브러리이다.
```
// Include GLEW. Always include it before gl.h and glfw3.h, since it's a bit magic.
// 아래의 라이브러리보다 꼭 먼저 include 해주어야 한다.
#include <GL/glew.h>

// Include GLFW
// GLFW가 창과 키보드를 조작할 수 있도록 한다.
#include <GLFW/glfw3.h>
```

```
// Include GLM
// 3D 계산을 위한 라이브러리
#include <glm/glm.hpp>
//  “glm::vec3”(“vec3” )을 입력하는 것을 강제한다. 
using namespace glm;
```

C++ 이 처음 코드를 읽으려고 하는 함수(main 함수)이다. 우선은 GLFW라는 것을 초기화(인수턴스화)한다.
```
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

```

OpenGL 창을 만들어보자!
```
// OpenGL 윈도우를 생성
glfwWindowHint(GLFW_SAMPLES, 4);	// 4x 안티에일리어싱
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);	// OpenGL 3.3 을 쓸것이라는 내용
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);	//옛날 버전 OpenGL은 사용하지 않는다는 의미

// Open a window and create its OpenGL context
// OpenGL 컨텍스트를 생성하고 지금 생성하는 윈도우를 openGL의 기본 윈도우 컨덱스트로 지정, "Tutorial 01"은 단순히 윈도우 이름이다.
window = glfwCreateWindow( 1024, 768, "Tutorial 01", NULL, NULL);
if( window == NULL ){
    // GLFW 윈도우를 여는데 실패했습니다. Intel GPU 를 사용한다면, 3.3 지원을 하지 않습니다. 2.1 버전용 튜토리얼을 시도하세요.
    fprintf( stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n" );
    getchar();
    // GLFW 종료 및 프로그램 종료
    glfwTerminate();
    return -1;
}
```

사용자가 Escape 키를 누를 때까지 기다리도록하는 코드도 추가하고 무사히 openGL이 종료되도록 한다.
```
// Ensure we can capture the escape key being pressed below
// 밑에서 Escape 키가 눌러지는 것을 감지할 수 있도록 할 것
glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

// Dark blue background
// 배경 색상 설정
glClearColor(0.0f, 0.0f, 0.4f, 0.0f);

// 렌더링 루프
// 렌더링 : 3차원 공간에 객체(Object)를 2차원 화면인 하나의 장면(Scene)에 바꾸어 표현하는 것
// 즉, 화면을 로딩한다는 것
do{
    // Clear the screen. It's not mentioned before Tutorial 02, but it can cause flickering, so it's there nonetheless.
    // 이전 루프의 결과 이미지들이 화면에 계속 남아 있기 때문에 지워준다.
    glClear( GL_COLOR_BUFFER_BIT );

    // Draw nothing, see you in tutorial 2 !

    
    // Swap buffers
    // 버퍼들을 교체
    glfwSwapBuffers(window);
    glfwPollEvents();

} // Check if the ESC key was pressed or the window was closed
// ESC 키가 눌러졌는지 혹은 창이 닫혔는지 체크 및 
while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
        glfwWindowShouldClose(window) == 0 );

// Close OpenGL window and terminate GLFW
// OpenGL 창을 닫고 GLFW 종료
glfwTerminate();
```

[다음은 삼각형을 배우는 튜토리얼](./tutorial2.md)이라고 한다!

## 전체 코드

```
// Include standard headers
#include <stdio.h>
#include <stdlib.h>

// Include GLEW. Always include it before gl.h and glfw3.h, since it's a bit magic.
#include <GL/glew.h>

// Include GLFW
// GLFW가 창과 키보드를 조작할 수 있도록 한다.
#include <GLFW/glfw3.h>
GLFWwindow* window;

// Include GLM
// 3D 계산을 위한 라이브러리
#include <glm/glm.hpp>
//  “glm::vec3”(“vec3” )을 입력하는 것을 강제한다. 
using namespace glm;

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
	// OpenGL 컨텍스트를 생성하고 지금 생성하는 윈도우를 openGL의 기본 윈도우 컨덱스트로 지정, "Tutorial 01"은 단순히 윈도우 이름이다.
	window = glfwCreateWindow( 1024, 768, "Tutorial 01", NULL, NULL);
	if( window == NULL ){
		// GLFW 윈도우를 여는데 실패했습니다. Intel GPU 를 사용한다면, 3.3 지원을 하지 않습니다. 2.1 버전용 튜토리얼을 시도하세요.
		fprintf( stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n" );
		getchar();
		// GLFW 종료 및 프로그램 종료
		glfwTerminate();
		return -1;
	}

	// Initialize GLEW
	// GLEW 초기화
	glfwMakeContextCurrent(window);
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

	// 렌더링 루프
	// 렌더링 : 3차원 공간에 객체(Object)를 2차원 화면인 하나의 장면(Scene)에 바꾸어 표현하는 것
	// 즉, 화면을 로딩한다는 것
	do{
		// Clear the screen. It's not mentioned before Tutorial 02, but it can cause flickering, so it's there nonetheless.
		// 이전 루프의 결과 이미지들이 화면에 계속 남아 있기 때문에 지워준다.
		// 현재는 컬러 값만 생각하므로 컬러 버퍼만 지운다.
		glClear( GL_COLOR_BUFFER_BIT );

		// Draw nothing, see you in tutorial 2 !

		
		// Swap buffers
		// 버퍼들을 교체
		glfwSwapBuffers(window);
		glfwPollEvents();

	} // Check if the ESC key was pressed or the window was closed
	// ESC 키가 눌러졌는지 혹은 창이 닫혔는지 체크
	while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
		   glfwWindowShouldClose(window) == 0 );

	// Close OpenGL window and terminate GLFW
	// OpenGL 창을 닫고 GLFW 종료
	glfwTerminate();

	return 0;
}
```