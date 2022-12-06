# Tutorial 4 : A Colored Cube

이번 튜토리얼에서는 조금 더.. 입체적인 모델(정육면체✨)과 모델에 색상을 추가하고 Z버퍼에 대해서 알아볼 것이다.

## 큐브 그리기

기본적으로 openGL은 삼각형이 기본이기 때문에 큐브를 그리기 위해서는 삼각형 2개의 빗변을 맞대어 사각형을 만들고 그 사각형을 6개 똑같이 만들어 정육각형으로 만들면 된다.

튜토리얼에서는 아래와 같은 정육면채를 만들었다.
```
// Our vertices. Tree consecutive floats give a 3D vertex; Three consecutive vertices give a triangle.
// A cube has 6 faces with 2 triangles each, so this makes 6*2=12 triangles, and 12*3 vertices
// 정육면체에는 6개의 정사각형 면이 있고 OpenGL은 삼각형으로 면을 만드는 것이 기본이기 때문에,
// 각 면에 대해 2개씩 12개의 삼각형을 그려야 한다;;
static const GLfloat g_vertex_buffer_data[] = { 
    -1.0f,-1.0f,-1.0f,
    -1.0f,-1.0f, 1.0f,
    -1.0f, 1.0f, 1.0f,
    1.0f, 1.0f,-1.0f,
    -1.0f,-1.0f,-1.0f,
    -1.0f, 1.0f,-1.0f,
    1.0f,-1.0f, 1.0f,
    -1.0f,-1.0f,-1.0f,
    1.0f,-1.0f,-1.0f,
    1.0f, 1.0f,-1.0f,
    1.0f,-1.0f,-1.0f,
    -1.0f,-1.0f,-1.0f,
    -1.0f,-1.0f,-1.0f,
    -1.0f, 1.0f, 1.0f,
    -1.0f, 1.0f,-1.0f,
    1.0f,-1.0f, 1.0f,
    -1.0f,-1.0f, 1.0f,
    -1.0f,-1.0f,-1.0f,
    -1.0f, 1.0f, 1.0f,
    -1.0f,-1.0f, 1.0f,
    1.0f,-1.0f, 1.0f,
    1.0f, 1.0f, 1.0f,
    1.0f,-1.0f,-1.0f,
    1.0f, 1.0f,-1.0f,
    1.0f,-1.0f,-1.0f,
    1.0f, 1.0f, 1.0f,
    1.0f,-1.0f, 1.0f,
    1.0f, 1.0f, 1.0f,
    1.0f, 1.0f,-1.0f,
    -1.0f, 1.0f,-1.0f,
    1.0f, 1.0f, 1.0f,
    -1.0f, 1.0f,-1.0f,
    -1.0f, 1.0f, 1.0f,
    1.0f, 1.0f, 1.0f,
    -1.0f, 1.0f, 1.0f,
    1.0f,-1.0f, 1.0f
};
```

튜토리얼 2에서처럼 표준함수들(glGenBuffers, glBindBuffer, glBufferData, glVertexAttribPointer)로 버퍼를 생성, 바인딩, 할당하면 된다. 조금 다른점이 하나 있는데 그려야하는 삼각형의 개수이다.

```
// Draw the triangle !
// 각 정점들을 그려서 12개의 삼각형을 그린다.
glDrawArrays(GL_TRIANGLES, 0, 12*3); // 12*3 indices starting at 0 -> 12 triangles
```

현재는 정점을 3번씩 작성하게 되는데 이는 큰 메모리 낭비이다. 튜토리얼 9에서 이러한 낭비를 줄이는 방법을 알게된다고 한다.

## 색상 추가

셰이더에 정점 데이터를 보내던 것처럼 색상 데이터를 보내면 된다.

정점을 선언하는 것처럼 색상을 선언한다, 0~1사이의 float형으로 빨강, 초록, 파랑의 세 색상의 값을 작성해주면 된다.
```
// One color for each vertex. They were generated randomly.
static const GLfloat g_color_buffer_data[] = { 
    0.583f,  0.771f,  0.014f,
    0.609f,  0.115f,  0.436f,
    0.327f,  0.483f,  0.844f,
    0.822f,  0.569f,  0.201f,
    0.435f,  0.602f,  0.223f,
    0.310f,  0.747f,  0.185f,
    0.597f,  0.770f,  0.761f,
    0.559f,  0.436f,  0.730f,
    0.359f,  0.583f,  0.152f,
    0.483f,  0.596f,  0.789f,
    0.559f,  0.861f,  0.639f,
    0.195f,  0.548f,  0.859f,
    0.014f,  0.184f,  0.576f,
    0.771f,  0.328f,  0.970f,
    0.406f,  0.615f,  0.116f,
    0.676f,  0.977f,  0.133f,
    0.971f,  0.572f,  0.833f,
    0.140f,  0.616f,  0.489f,
    0.997f,  0.513f,  0.064f,
    0.945f,  0.719f,  0.592f,
    0.543f,  0.021f,  0.978f,
    0.279f,  0.317f,  0.505f,
    0.167f,  0.620f,  0.077f,
    0.347f,  0.857f,  0.137f,
    0.055f,  0.953f,  0.042f,
    0.714f,  0.505f,  0.345f,
    0.783f,  0.290f,  0.734f,
    0.722f,  0.645f,  0.174f,
    0.302f,  0.455f,  0.848f,
    0.225f,  0.587f,  0.040f,
    0.517f,  0.713f,  0.338f,
    0.053f,  0.959f,  0.120f,
    0.393f,  0.621f,  0.362f,
    0.673f,  0.211f,  0.457f,
    0.820f,  0.883f,  0.371f,
    0.982f,  0.099f,  0.879f
};
```

버퍼는 정점 데이터와 비슷하게 진행하면 된다.
```
// 위와 똑같은 방법으로, 위치 대신 색상 데이터를 색상을 담당할 버퍼에 입력해준다.
GLuint colorbuffer;
glGenBuffers(1, &colorbuffer);
glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
glBufferData(GL_ARRAY_BUFFER, sizeof(g_color_buffer_data), g_color_buffer_data, GL_STATIC_DRAW);
```

GLSL에 넘겨줄 때도 같다.
```
// 2nd attribute buffer : colors
// 두번째 속성 버퍼로 색상 데이터를 넣어준다.
glEnableVertexAttribArray(1);
glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
glVertexAttribPointer(
    1,                                // attribute. No particular reason for 1, but must match the layout in the shader.
    3,                                // size
    GL_FLOAT,                         // type
    GL_FALSE,                         // normalized?
    0,                                // stride
    (void*)0                          // array buffer offset
);
```

버텍스셰이더에서 위의 버퍼에 접근할 수 있게 되었으니 사용한다.
```
layout(location = 1) in vec3 vertexColor;

// Output data ; will be interpolated for each fragment.
// 출력 데이터, 각 fragment에 따라서.. 보간..?
out vec3 fragmentColor;

void main(){

    [...]

    // The color of each vertex will be interpolated
    // to produce the color of each fragment
    fragmentColor = vertexColor;
}
```

프레그먼트 셰이더에서 변수를 하나 선언하여 최종 출력 색상으로 지정해준다.
```
in vec3 fragmentColor;

void main(){

	// Output color = color specified in the vertex shader, 
	// interpolated between all 3 surrounding vertices
	// 딱히 추가 작업하는 것 없이 최종 출력할 색상으로 한다.
	color = fragmentColor;

}
```

## 중간결과

필자는 완성된 코드를 모두 복붙하여 아래와 같은 튜브는 보지 못했지만 Z 버퍼를 사용하지 않아서 일어난 현상이라고 한다.

<img src="https://user-images.githubusercontent.com/19484971/197397359-8f4298c1-fc50-4963-8cd6-29e15f76cf67.png" width=500>

Z-Buffer를 사용하지 않으면 아래 사진처럼 가까운 삼각형을 멀리있는 삼각형이 덮어 씌워버리는 경우가 있기 때문에 꼭 사용해주어야 한다.

<img src="https://user-images.githubusercontent.com/19484971/197397467-bcfb5087-2e07-401d-a082-1c8ee703899e.png" width=100>

## Z Buffer

각 fragment의 깊이 데이터를 저장하고 먼저 로딩해주어야 하는지 판단하여 위의 문제를 해결할 수 있다.

하드웨어에 직접 하도록 요청하는 방법이 있는데 아래와 같다.
```
/ Enable depth test
// Z버퍼를 사용할 것을 알린다.
glEnable(GL_DEPTH_TEST);
// Accept fragment if it closer to the camera than the former one
// Z 값(깊이값)을 버퍼에 저장했다가 카메라와의 거리에 따라 먼저 불러올 대상인지 파악해주는 역할을 한다.
glDepthFunc(GL_LESS); 
```

그리고 색상과 각 프레임의 깊이 데이터를 지워준다.
```
// Clear the screen
// 앞의 내용은 색상버퍼를 뒤의 내용은 Z버퍼를 비워준다는 의미같다.
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
```

그러면 깔끔하게 큐브가 출력된다!

<img src="https://user-images.githubusercontent.com/19484971/197398627-cf937e1b-deca-4668-bae4-2a59fe765471.png" width=600>

[다음 튜토리얼](./tutorial5.md)은 이번에 만든 큐브에 색상대신 텍스쳐(이미지 집합체)를 적용하는 방법을 배울 것이다!

## 전체 코드

`tutorial04.cpp`
```
// 정육면체를 그리고 그라데이션 색상도 입혀보고 Z버퍼.. 도 알아보는 튜토리얼

// Include standard headers
#include <stdio.h>
#include <stdlib.h>

// Include GLEW
#include <GL/glew.h>

// Include GLFW
#include <GLFW/glfw3.h>
GLFWwindow* window;

// Include GLM
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
using namespace glm;

#include <common/shader.hpp>

int main( void )
{
	// Initialise GLFW
	if( !glfwInit() )
	{
		fprintf( stderr, "Failed to initialize GLFW\n" );
		getchar();
		return -1;
	}

	glfwWindowHint(GLFW_SAMPLES, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	// Open a window and create its OpenGL context
	window = glfwCreateWindow( 1024, 768, "Tutorial 04 - Colored Cube", NULL, NULL);
	if( window == NULL ){
		fprintf( stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n" );
		getchar();
		glfwTerminate();
		return -1;
	}
	glfwMakeContextCurrent(window);

	// Initialize GLEW
	glewExperimental = true; // Needed for core profile
	if (glewInit() != GLEW_OK) {
		fprintf(stderr, "Failed to initialize GLEW\n");
		getchar();
		glfwTerminate();
		return -1;
	}

	// Ensure we can capture the escape key being pressed below
	glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

	// Dark blue background
	glClearColor(0.0f, 0.0f, 0.4f, 0.0f);

	// Z 버퍼가 없으면.. http://www.opengl-tutorial.org/beginners-tutorials/tutorial-4-a-colored-cube/
	// 위의 페이지의 중간쯤에 있는 이상한 큐브처럼 된다.

	// Enable depth test
	// Z버퍼를 사용할 것을 알린다.
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	// Z 값(깊이값)을 버퍼에 저장했다가 카메라와의 거리에 따라 먼저 불러올 대상인지 파악해주는 역할을 한다.
	glDepthFunc(GL_LESS); 

	GLuint VertexArrayID;
	glGenVertexArrays(1, &VertexArrayID);
	glBindVertexArray(VertexArrayID);

	// Create and compile our GLSL program from the shaders
	GLuint programID = LoadShaders( "TransformVertexShader.vertexshader", "ColorFragmentShader.fragmentshader" );

	// Get a handle for our "MVP" uniform
	GLuint MatrixID = glGetUniformLocation(programID, "MVP");

	// Projection matrix : 45?Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
	glm::mat4 Projection = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);
	// Camera matrix
	glm::mat4 View       = glm::lookAt(
								glm::vec3(4,3,-3), // Camera is at (4,3,-3), in World Space
								glm::vec3(0,0,0), // and looks at the origin
								glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
						   );
	// Model matrix : an identity matrix (model will be at the origin)
	glm::mat4 Model      = glm::mat4(1.0f);
	// Our ModelViewProjection : multiplication of our 3 matrices
	glm::mat4 MVP        = Projection * View * Model; // Remember, matrix multiplication is the other way around

	// Our vertices. Tree consecutive floats give a 3D vertex; Three consecutive vertices give a triangle.
	// A cube has 6 faces with 2 triangles each, so this makes 6*2=12 triangles, and 12*3 vertices
	// 정육면체에는 6개의 정사각형 면이 있고 OpenGL은 삼각형으로 면을 만드는 것이 기본이기 때문에,
	// 각 면에 대해 2개씩 12개의 삼각형을 그려야 한다;;
	static const GLfloat g_vertex_buffer_data[] = { 
		-1.0f,-1.0f,-1.0f,
		-1.0f,-1.0f, 1.0f,
		-1.0f, 1.0f, 1.0f,
		 1.0f, 1.0f,-1.0f,
		-1.0f,-1.0f,-1.0f,
		-1.0f, 1.0f,-1.0f,
		 1.0f,-1.0f, 1.0f,
		-1.0f,-1.0f,-1.0f,
		 1.0f,-1.0f,-1.0f,
		 1.0f, 1.0f,-1.0f,
		 1.0f,-1.0f,-1.0f,
		-1.0f,-1.0f,-1.0f,
		-1.0f,-1.0f,-1.0f,
		-1.0f, 1.0f, 1.0f,
		-1.0f, 1.0f,-1.0f,
		 1.0f,-1.0f, 1.0f,
		-1.0f,-1.0f, 1.0f,
		-1.0f,-1.0f,-1.0f,
		-1.0f, 1.0f, 1.0f,
		-1.0f,-1.0f, 1.0f,
		 1.0f,-1.0f, 1.0f,
		 1.0f, 1.0f, 1.0f,
		 1.0f,-1.0f,-1.0f,
		 1.0f, 1.0f,-1.0f,
		 1.0f,-1.0f,-1.0f,
		 1.0f, 1.0f, 1.0f,
		 1.0f,-1.0f, 1.0f,
		 1.0f, 1.0f, 1.0f,
		 1.0f, 1.0f,-1.0f,
		-1.0f, 1.0f,-1.0f,
		 1.0f, 1.0f, 1.0f,
		-1.0f, 1.0f,-1.0f,
		-1.0f, 1.0f, 1.0f,
		 1.0f, 1.0f, 1.0f,
		-1.0f, 1.0f, 1.0f,
		 1.0f,-1.0f, 1.0f
	};

	// One color for each vertex. They were generated randomly.
	static const GLfloat g_color_buffer_data[] = { 
		0.583f,  0.771f,  0.014f,
		0.609f,  0.115f,  0.436f,
		0.327f,  0.483f,  0.844f,
		0.822f,  0.569f,  0.201f,
		0.435f,  0.602f,  0.223f,
		0.310f,  0.747f,  0.185f,
		0.597f,  0.770f,  0.761f,
		0.559f,  0.436f,  0.730f,
		0.359f,  0.583f,  0.152f,
		0.483f,  0.596f,  0.789f,
		0.559f,  0.861f,  0.639f,
		0.195f,  0.548f,  0.859f,
		0.014f,  0.184f,  0.576f,
		0.771f,  0.328f,  0.970f,
		0.406f,  0.615f,  0.116f,
		0.676f,  0.977f,  0.133f,
		0.971f,  0.572f,  0.833f,
		0.140f,  0.616f,  0.489f,
		0.997f,  0.513f,  0.064f,
		0.945f,  0.719f,  0.592f,
		0.543f,  0.021f,  0.978f,
		0.279f,  0.317f,  0.505f,
		0.167f,  0.620f,  0.077f,
		0.347f,  0.857f,  0.137f,
		0.055f,  0.953f,  0.042f,
		0.714f,  0.505f,  0.345f,
		0.783f,  0.290f,  0.734f,
		0.722f,  0.645f,  0.174f,
		0.302f,  0.455f,  0.848f,
		0.225f,  0.587f,  0.040f,
		0.517f,  0.713f,  0.338f,
		0.053f,  0.959f,  0.120f,
		0.393f,  0.621f,  0.362f,
		0.673f,  0.211f,  0.457f,
		0.820f,  0.883f,  0.371f,
		0.982f,  0.099f,  0.879f
	};

	// 버퍼를 표준 함수(glGenBuffers, glBindBuffer, glBufferData, glVertexAttribPointer)로 생성, 바인딩, 초기화(?)해주기!
	// 위에서 각 정점은 실제로 최소 3번 작성되는데 이는 메모리 낭비이다, 튜토리얼 9에서 이것을 다루는 방법을 배운다고 한다.
	GLuint vertexbuffer;
	glGenBuffers(1, &vertexbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);

	// 위와 똑같은 방법으로, 위치 대신 색상 데이터를 색상을 담당할 버퍼에 입력해준다.
	GLuint colorbuffer;
	glGenBuffers(1, &colorbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_color_buffer_data), g_color_buffer_data, GL_STATIC_DRAW);

	do{

		// Clear the screen
		// 앞의 내용은 색상버퍼를 뒤의 내용은 Z버퍼를 비워준다는 의미같다.
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// Use our shader
		glUseProgram(programID);

		// Send our transformation to the currently bound shader, 
		// in the "MVP" uniform
		glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);

		// 1rst attribute buffer : vertices
		// 첫번째 속성으로 위치 데이터를 넣어준다.
		glEnableVertexAttribArray(0);
		glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
		glVertexAttribPointer(
			0,                  // attribute. No particular reason for 0, but must match the layout in the shader.
			3,                  // size
			GL_FLOAT,           // type
			GL_FALSE,           // normalized?
			0,                  // stride
			(void*)0            // array buffer offset
		);

		// 2nd attribute buffer : colors
		// 두번째 속성 버퍼로 색상 데이터를 넣어준다.
		glEnableVertexAttribArray(1);
		glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
		glVertexAttribPointer(
			1,                                // attribute. No particular reason for 1, but must match the layout in the shader.
			3,                                // size
			GL_FLOAT,                         // type
			GL_FALSE,                         // normalized?
			0,                                // stride
			(void*)0                          // array buffer offset
		);

		// Draw the triangle !
		// 각 정점들을 그려서 12개의 삼각형을 그린다.
		glDrawArrays(GL_TRIANGLES, 0, 12*3); // 12*3 indices starting at 0 -> 12 triangles

		glDisableVertexAttribArray(0);
		glDisableVertexAttribArray(1);

		// Swap buffers
		glfwSwapBuffers(window);
		glfwPollEvents();

	} // Check if the ESC key was pressed or the window was closed
	while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
		   glfwWindowShouldClose(window) == 0 );

	// Cleanup VBO and shader
	glDeleteBuffers(1, &vertexbuffer);
	glDeleteBuffers(1, &colorbuffer);
	glDeleteProgram(programID);
	glDeleteVertexArrays(1, &VertexArrayID);

	// Close OpenGL window and terminate GLFW
	glfwTerminate();

	return 0;
}
```

`TransformVertexShader.vertexshader`
```
#version 330 core

// Input vertex data, different for all executions of this shader.
// C++ 코드의 속성 순서에 맞게 입력 데이터를 받는다.
layout(location = 0) in vec3 vertexPosition_modelspace;
layout(location = 1) in vec3 vertexColor;

// Output data ; will be interpolated for each fragment.
// 출력 데이터, 각 fragment에 따라서.. 보간..? 뭐요?
out vec3 fragmentColor;
// Values that stay constant for the whole mesh.
// 메시(삼각형들의 집합)에 저장된 상수값
uniform mat4 MVP;

void main(){	

	// Output position of the vertex, in clip space : MVP * position
	gl_Position =  MVP * vec4(vertexPosition_modelspace,1);

	// The color of each vertex will be interpolated
	// to produce the color of each fragment
	fragmentColor = vertexColor;
}
```

`ColorFragmentShader.fragmentshader`
```
#version 330 core

// Interpolated values from the vertex shaders
// vertex shaders에서 넘겨받은 데이터를 입력데이터로 받아들인다.
in vec3 fragmentColor;

// Ouput data
out vec3 color;

void main(){

	// Output color = color specified in the vertex shader, 
	// interpolated between all 3 surrounding vertices
	// 딱히 추가 작업하는 것 없이 최종 출력할 색상으로 한다.
	color = fragmentColor;

}
```