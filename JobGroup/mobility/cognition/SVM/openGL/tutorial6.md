# Tutorial 6 : Keyboard and Mouse

마참내! FPS 게임에서처럼 마우스와 키보드를 사용하여 카메라를 움직이는 방법을 배운다!

## 인터페이스

튜토리얼 전체에서 재사용되는 `common/controls.cpp`라는 별도의 파일에 함수를 선언하고 `tutorial06.cpp`에서 사용할 수 있도록 include를 해주어 사용할 것이다.

이전 튜토리얼과 크게 다르지 않지만, MVP 행렬을 한 번 계산하는 대신 이제 매 프레임마다 수행하는 방식으로 바뀌었다.

```
do{

    // ...

    // Compute the MVP matrix from keyboard and mouse input
    computeMatricesFromInputs();
    glm::mat4 ProjectionMatrix = getProjectionMatrix();
    glm::mat4 ViewMatrix = getViewMatrix();
    glm::mat4 ModelMatrix = glm::mat4(1.0);
    glm::mat4 MVP = ProjectionMatrix * ViewMatrix * ModelMatrix;

    // ...
}
```

이 코드에서는 3가지 함수을 활용한다.

1. computeMatricesFromInputs() : 키보드와 마우스를 읽어 투영(projection) 및 보기(view) 행렬을 계산한다.
2. getProjectionMatrix() : 계산된 투영 행렬을 반환한다.
3. getViewMatrix() : 계산된 View 행렬을 반환한다.

다른 방법이 있다면 그것으로 바꿔도 상관없다고 한다.

## control 파일

controls.cpp 내부를 조금 살펴보면 아래와 같다.

먼저 카메라에 대한 설정을 진행한다. 카메라의 초기 위치, 시야각, 속도 등을 지정한다.
```
// position
// 카메라 위치 초기화
glm::vec3 position = glm::vec3( 0, 0, 5 );
// horizontal angle : toward -Z
// 카메라 수평각 초기화 (-Z 방향으로)
float horizontalAngle = 3.14f;
// vertical angle : 0, look at the horizon
// 카메라 수직각 초기화 (수평선을 보도록)
float verticalAngle = 0.0f;
// Initial Field of View
// 시야각 초기화
float initialFoV = 45.0f;

float speed = 3.0f; // 3 units / second
float mouseSpeed = 0.005f;
```

수평각과 수직각이 햇갈려서 찾은 이미지
<img src="https://user-images.githubusercontent.com/19484971/197906904-97900af1-2639-4fe5-8746-a2eaecd9fe98.png" width=600>

FoV(Field of View)는 시야각이라는 의미로, 값에 따라 확대/축소의 정도가 차이난다. FoV가 작을수록 물체가 가깝게, 클수록 물체는 멀게, 작게 보인다.

80° = 매우 넓은 각도, 큰 변형. 60° - 45°: 표준. 20° : 큰 줌.

먼저 입력에 따라 position, horizontalAngle, verticalAngle 및 FoV를 다시 계산한 다음 position, horizontalAngle, verticalAngle 및 FoV에서 View 및 Projection 행렬을 계산하는 과정을 거친다.

### Orientation

아래의 코드로는 마우스의 위치를 읽어들인다.
```
// Get mouse position
// 마우스 위치 얻기!
int xpos, ypos;
glfwGetCursorPos(&xpos, &ypos);
```

하지만 커서를 움직인후 다시 화면 중앙으로 옮겨주어야 한다. 그렇지 않으면 곧 창 밖으로 이동해서 더 이상 이동할 수 없게 된다.

```
// Reset mouse position for next frame
// 프레임마다 마우스의 위치를 초기화
glfwSetCursorPos(1024/2, 768/2);
```

해당 코드는 창이 1024*768이라고 가정하지만 항상 그런 것은 아니기 때문에 원하는 경우 `glfwGetWindowSize`를 사용하여 윈도우의 가로, 세로 길이를 찾아내어 커서를 옮겨줄 수 있다.

이제 카메라 각을 계산하는 코드를 만들자.
```
// glfwGetTime is called only once, the first time this function is called
// C++ 에서 static 초기화하는 줄은 1번만 실행되며 다음에 이 줄에 도달했을 때는 무시된다.
// https://boycoding.tistory.com/169
static double lastTime = glfwGetTime();

// Compute time difference between current and last frame
// 이전 프레임과 지금 프레임의 시간차를 구한다.
double currentTime = glfwGetTime();
float deltaTime = float(currentTime - lastTime);

// Compute new orientation
horizontalAngle += mouseSpeed * deltaTime * float(1024/2 - xpos );
verticalAngle   += mouseSpeed * deltaTime * float( 768/2 - ypos );
```

위의 코드를 해석하면 다음과 같다.

- 1024/2-xpos : 마우스를 많이 움직일수록 회전이 크게된다.
- float : C++은 형변환을 자동으로 해주기는 한다.
- mouseSpeed : 마우스 이동에 따른 회전 속도를 높이거나 낮추기 위한 것입니다. 게임에서의 민감도를 의미한다.
- += : 마우스를 움직이지 않으면 1024/2-xpos는 0이 되고(커서가 매 프레임마다 중앙으로 강제이동되고 있기 때문), horizontalAngle+=0은 horizontalAngle을 변경하지 않는다. 
- `deltaTime` : 컴퓨터 성능마다 60fps, 20fps 등 속도가 다르다. 이를 보완하기 위해서 사용한다. 의미는 마지막 프레임 이후의 시간.

이제 월드 좌표계에서 카메라가 보고 있는 방향을 나타내는 벡터를 계산할 수 있다! 정확히 이해는 잘 못하겠지만, 정면에 대한 단위 벡터인 것 같다.
```
// Direction : Spherical coordinates to Cartesian coordinates conversion
// 구면 좌표계를 데카르트 좌표계(월드 좌표계)로 변환
glm::vec3 direction(
    cos(verticalAngle) * sin(horizontalAngle),
    sin(verticalAngle),
    cos(verticalAngle) * cos(horizontalAngle)
);
```

아래는 이해를 돕기 위한 코사인과 사인에 대한 이미지이다.

<img src="https://user-images.githubusercontent.com/19484971/197813731-d76f4c90-f77d-46b7-bd2e-cd0d069a9d62.png" width=200>

lookat 함수의 "up" 벡터를 계산해 넣자. "위"가 항상 +Y를 향하는 것은 아니라는 것을 기억하자. +Y와 같을수도 있지만 수평과 평행할 수 있다. 

아래는 같은 위치에서 다른 "up" 벡터를 가지는 카메라 사진이다.

<img src="https://user-images.githubusercontent.com/19484971/197816592-3e1f0354-0be8-447a-b90b-66bf01886a4d.png" width=600>

자습서의.. 설명이 너무 난해하다; 코드를 해석하면.. 카메라의 오른쪽 방향의 단위벡터를 하나 구한다. 이때 아래는 코사인과 사인을 활용한다.

```
// Right vector
// 카메라의 오른쪽 방향 벡터
glm::vec3 right = glm::vec3(
    sin(horizontalAngle - 3.14f/2.0f),
    0,
    cos(horizontalAngle - 3.14f/2.0f)
);
```

위와 비슷하게 카메라 좌표계의 윗 방향 단위벡터를 구하려는데 이미 정방과 측면은 구했으므로 두 방향의 모두에게 90도인 방향을 구하면 된다. 즉, 외적을 활용하면 쉽게 구할 수 있다.

```
// Up vector : perpendicular to both direction and right
// 카메라의 위쪽 방향 벡터 
// 앞쪽 방향 벡터와 오른쪽 방향 벡터를 외적하여 구한다.
glm::vec3 up = glm::cross( right, direction );
```

### 위치

글로벌하게 쓰이는 화살표 키보드를 활용해서 카메라를 움직일 수 있도록 만든다.

```
// Move forward
if (glfwGetKey( GLFW_KEY_UP ) == GLFW_PRESS){
    position += direction * deltaTime * speed;
}
// Move backward
if (glfwGetKey( GLFW_KEY_DOWN ) == GLFW_PRESS){
    position -= direction * deltaTime * speed;
}
// Strafe right
if (glfwGetKey( GLFW_KEY_RIGHT ) == GLFW_PRESS){
    position += right * deltaTime * speed;
}
// Strafe left
if (glfwGetKey( GLFW_KEY_LEFT ) == GLFW_PRESS){
    position -= right * deltaTime * speed;
}
```

위에서 방향을 모두 계산해두었기 때문에 참으로 간단하다.

### 시야

마우스 휠을 Field Of View에 바인딩하여 간단한 줌을 사용할 수도 있다.
```
float FoV = initialFoV; // - 5 * glfwGetMouseWheel();
```

그런데.. GLFW 3에서는 이에 대한 콜백 설정이 필요하다. 자습서에서는 너무 복잡하므로 비활성화되어 있다.

### 행렬 계산

위에서 이미 위치, 각 방향 벡터를 계산해놓았기 때문에 가지고 있는 변수를 lookat함수에 넣기만 하면 된다!
```
// Projection matrix : 45&deg; Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
// 45도의 시야각, 4:3비율, 0.1~100 거리 내의 물체에 대한 투영행렬
ProjectionMatrix = glm::perspective(glm::radians(FoV), 4.0f / 3.0f, 0.1f, 100.0f);
// Camera matrix
ViewMatrix = glm::lookAt(
    position,           // Camera is here
    position+direction, // and looks here : at the same position, plus "direction"
    up                  // Head is up (set to 0,-1,0 to look upside-down)
);
```

## 결과

<img src="https://user-images.githubusercontent.com/19484971/197899930-28b59ccc-bdb2-48b3-9fd7-a01c7dd03ba5.gif" width=300>

### 뒷면 컬링

이제 자유롭게 이동할 수 있다! 이동해서 큐브 내부로 들어가면 다각형이 계속 표시되는 것을 확인할 수 있는데 이는 괜찮아 보이지만.. 이를 생략하여 최적화를 생각해볼 수도 있다. 보통 일반적인 응용 프로그램에서 큐브 안으로 들어가지는 않기 때문이다.

카메라가 삼각형의 뒤에 있는지 또는 앞에 있는지 GPU가 확인하여 앞에 있으 때만 삼각형을 표시하도록 만든다. 평균적으로 2배 적은 삼각형을 이용하여 속도는 더 빨라지면서 겉으로 보기에 기능상의 문제는 생기지 않기 때문에 간단하면서 좋은 최적화 방법이다!

적용하기도 매우 쉽다. GPU는 삼각형의 법선을 계산하고(외적을 사용한다.) 이 법선이 카메라를 향하고 있는지 여부만을 확인하면 된다.

법선을 계산하는데 비용이 들기 때문에 단순히 3D 모델러에서 "법선 반전" 기능을 클릭하여 적용시키는 방법도 있다. 그러면 굳이 법선을 계산하지 않아도 좋다.

openGL에서 뒷면을 없애는(뒷면 컬링) 기능을 활성화하는 것은 아래와 같이 간단하다.
```
// Cull triangles which normal is not towards the camera
// 법선이 카메라를 향하지 않는 삼각형은 지운다.
glEnable(GL_CULL_FACE);
```

## 전체코드

`tutorial06.cpp`
```
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
#include <common/texture.hpp>
#include <common/controls.hpp>

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
	window = glfwCreateWindow( 1024, 768, "Tutorial 0 - Keyboard and Mouse", NULL, NULL);
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
    // Hide the mouse and enable unlimited mouvement
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
    
    // Set the mouse at the center of the screen
    glfwPollEvents();
    glfwSetCursorPos(window, 1024/2, 768/2);

	// Dark blue background
	glClearColor(0.0f, 0.0f, 0.4f, 0.0f);

	// Enable depth test
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	glDepthFunc(GL_LESS); 

	// Cull triangles which normal is not towards the camera
	// 법선이 카메라를 향하지 않는 삼각형은 지운다.
	glEnable(GL_CULL_FACE);

	GLuint VertexArrayID;
	glGenVertexArrays(1, &VertexArrayID);
	glBindVertexArray(VertexArrayID);

	// Create and compile our GLSL program from the shaders
	GLuint programID = LoadShaders( "TransformVertexShader.vertexshader", "TextureFragmentShader.fragmentshader" );

	// Get a handle for our "MVP" uniform
	GLuint MatrixID = glGetUniformLocation(programID, "MVP");

	// Load the texture
	GLuint Texture = loadDDS("uvtemplate.DDS");
	
	// Get a handle for our "myTextureSampler" uniform
	GLuint TextureID  = glGetUniformLocation(programID, "myTextureSampler");

	// Our vertices. Tree consecutive floats give a 3D vertex; Three consecutive vertices give a triangle.
	// A cube has 6 faces with 2 triangles each, so this makes 6*2=12 triangles, and 12*3 vertices
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

	// Two UV coordinatesfor each vertex. They were created with Blender.
	static const GLfloat g_uv_buffer_data[] = { 
		0.000059f, 0.000004f, 
		0.000103f, 0.336048f, 
		0.335973f, 0.335903f, 
		1.000023f, 0.000013f, 
		0.667979f, 0.335851f, 
		0.999958f, 0.336064f, 
		0.667979f, 0.335851f, 
		0.336024f, 0.671877f, 
		0.667969f, 0.671889f, 
		1.000023f, 0.000013f, 
		0.668104f, 0.000013f, 
		0.667979f, 0.335851f, 
		0.000059f, 0.000004f, 
		0.335973f, 0.335903f, 
		0.336098f, 0.000071f, 
		0.667979f, 0.335851f, 
		0.335973f, 0.335903f, 
		0.336024f, 0.671877f, 
		1.000004f, 0.671847f, 
		0.999958f, 0.336064f, 
		0.667979f, 0.335851f, 
		0.668104f, 0.000013f, 
		0.335973f, 0.335903f, 
		0.667979f, 0.335851f, 
		0.335973f, 0.335903f, 
		0.668104f, 0.000013f, 
		0.336098f, 0.000071f, 
		0.000103f, 0.336048f, 
		0.000004f, 0.671870f, 
		0.336024f, 0.671877f, 
		0.000103f, 0.336048f, 
		0.336024f, 0.671877f, 
		0.335973f, 0.335903f, 
		0.667969f, 0.671889f, 
		1.000004f, 0.671847f, 
		0.667979f, 0.335851f
	};

	GLuint vertexbuffer;
	glGenBuffers(1, &vertexbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);

	GLuint uvbuffer;
	glGenBuffers(1, &uvbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, uvbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_uv_buffer_data), g_uv_buffer_data, GL_STATIC_DRAW);

	do{

		// Clear the screen
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// Use our shader
		glUseProgram(programID);

		// Compute the MVP matrix from keyboard and mouse input
		computeMatricesFromInputs();
		glm::mat4 ProjectionMatrix = getProjectionMatrix();
		glm::mat4 ViewMatrix = getViewMatrix();
		glm::mat4 ModelMatrix = glm::mat4(1.0);
		glm::mat4 MVP = ProjectionMatrix * ViewMatrix * ModelMatrix;

		// Send our transformation to the currently bound shader, 
		// in the "MVP" uniform
		glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);

		// Bind our texture in Texture Unit 0
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, Texture);
		// Set our "myTextureSampler" sampler to use Texture Unit 0
		glUniform1i(TextureID, 0);

		// 1rst attribute buffer : vertices
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

		// 2nd attribute buffer : UVs
		glEnableVertexAttribArray(1);
		glBindBuffer(GL_ARRAY_BUFFER, uvbuffer);
		glVertexAttribPointer(
			1,                                // attribute. No particular reason for 1, but must match the layout in the shader.
			2,                                // size : U+V => 2
			GL_FLOAT,                         // type
			GL_FALSE,                         // normalized?
			0,                                // stride
			(void*)0                          // array buffer offset
		);

		// Draw the triangle !
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
	glDeleteBuffers(1, &uvbuffer);
	glDeleteProgram(programID);
	glDeleteTextures(1, &TextureID);
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
layout(location = 0) in vec3 vertexPosition_modelspace;
layout(location = 1) in vec2 vertexUV;

// Output data ; will be interpolated for each fragment.
out vec2 UV;

// Values that stay constant for the whole mesh.
uniform mat4 MVP;

void main(){

	// Output position of the vertex, in clip space : MVP * position
	gl_Position =  MVP * vec4(vertexPosition_modelspace,1);
	
	// UV of the vertex. No special space for this one.
	UV = vertexUV;
}


```

`TextureFragmentShader.fragmentshader`
```
#version 330 core

// Interpolated values from the vertex shaders
in vec2 UV;

// Ouput data
out vec3 color;

// Values that stay constant for the whole mesh.
uniform sampler2D myTextureSampler;

void main(){

	// Output color = color of the texture at the specified UV
	color = texture( myTextureSampler, UV ).rgb;
}
```

`controls.cpp`
```
// Include GLFW
#include <GLFW/glfw3.h>
extern GLFWwindow* window; // The "extern" keyword here is to access the variable "window" declared in tutorialXXX.cpp. This is a hack to keep the tutorials simple. Please avoid this.

// Include GLM
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
using namespace glm;

#include "controls.hpp"

glm::mat4 ViewMatrix;
glm::mat4 ProjectionMatrix;

glm::mat4 getViewMatrix(){
	return ViewMatrix;
}
glm::mat4 getProjectionMatrix(){
	return ProjectionMatrix;
}


// Initial position : on +Z
// 카메라 위치 초기화 (z축 위로)
glm::vec3 position = glm::vec3( 0, 0, 5 ); 
// Initial horizontal angle : toward -Z
// 카메라 수평각 초기화
float horizontalAngle = 3.14f;
// Initial vertical angle : none
// 카메라 수직각 초기화 (수평선을 보도록)
float verticalAngle = 0.0f;
// Initial Field of View 
// 시야각 초기화
float initialFoV = 45.0f;

float speed = 3.0f; // 3 units / second
float mouseSpeed = 0.005f;



void computeMatricesFromInputs(){

	// glfwGetTime is called only once, the first time this function is called
	// C++ 에서 static 초기화하는 줄은 1번만 실행되며 다음에 이 줄에 도달했을 때는 무시된다.
	// https://boycoding.tistory.com/169
	static double lastTime = glfwGetTime();

	// Compute time difference between current and last frame
	// 이전 프레임과 지금 프레임의 시간차를 구한다.
	double currentTime = glfwGetTime();
	float deltaTime = float(currentTime - lastTime);

	// Get mouse position
	// 마우스 위치 얻기!
	double xpos, ypos;
	glfwGetCursorPos(window, &xpos, &ypos);

	// Reset mouse position for next frame
	glfwSetCursorPos(window, 1024/2, 768/2);

	// Compute new orientation
	horizontalAngle += mouseSpeed * float(1024/2 - xpos );
	verticalAngle   += mouseSpeed * float( 768/2 - ypos );

	// Direction : Spherical coordinates to Cartesian coordinates conversion
	// 구면 좌표계를 데카르트 좌표계(월드 좌표계)로 변환
	glm::vec3 direction(
		cos(verticalAngle) * sin(horizontalAngle), 
		sin(verticalAngle),
		cos(verticalAngle) * cos(horizontalAngle)
	);
	
	// Right vector
	// 카메라의 오른쪽 방향 벡터
	// 앞쪽 방향 벡터와 오른쪽 방향 벡터를 외적하여 구한다.
	glm::vec3 right = glm::vec3(
		sin(horizontalAngle - 3.14f/2.0f), 
		0,
		cos(horizontalAngle - 3.14f/2.0f)
	);
	
	// Up vector
	// 카메라의 위쪽 방향 벡터
	glm::vec3 up = glm::cross( right, direction );

	// Move forward
	if (glfwGetKey( window, GLFW_KEY_UP ) == GLFW_PRESS){
		position += direction * deltaTime * speed;
	}
	// Move backward
	if (glfwGetKey( window, GLFW_KEY_DOWN ) == GLFW_PRESS){
		position -= direction * deltaTime * speed;
	}
	// Strafe right
	if (glfwGetKey( window, GLFW_KEY_RIGHT ) == GLFW_PRESS){
		position += right * deltaTime * speed;
	}
	// Strafe left
	if (glfwGetKey( window, GLFW_KEY_LEFT ) == GLFW_PRESS){
		position -= right * deltaTime * speed;
	}

	float FoV = initialFoV;// - 5 * glfwGetMouseWheel(); // Now GLFW 3 requires setting up a callback for this. It's a bit too complicated for this beginner's tutorial, so it's disabled instead.

	// Projection matrix : 45?Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
	// 45도의 시야각, 4:3비율, 0.1~100 거리 내의 물체에 대한 투영행렬
	ProjectionMatrix = glm::perspective(glm::radians(FoV), 4.0f / 3.0f, 0.1f, 100.0f);
	// Camera matrix
	ViewMatrix = glm::lookAt(
		position,           // Camera is here
		position+direction, // and looks here : at the same position, plus "direction"
		up                  // Head is up (set to 0,-1,0 to look upside-down)
	);

	// For the next frame, the "last time" will be "now"
	lastTime = currentTime;
}
```