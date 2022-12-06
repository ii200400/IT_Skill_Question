# Tutorial 5 : A Textured Cube

여기서는 다양한 내용을 배우게 되는데 간단하게 요약하면 아래와 같다.

- UV 좌표란?
- 텍스처를 직접 로드하는 방법
- 텍스처를 OpenGL에서 사용하는 방법
- filtering 및 mipmapping 정의와 사용방법
- GLFW로 텍스처를 더 강력하게 로드하는 방법
- alpha channel이란

## UV coordinates

openGL의 모델을 텍스처링할 때 삼각형의 어느 부분을 사용해야할지 알려줄 방법이 필요한데 이 때 사용하는 좌표 데이터가 UV 좌표이다.

각 정점이 가지고 있는 float 형의 숫자데이터로 u와 v를 가지고 이 데이터를 사용하여 아래와 같은 방식으로 텍스처에 접근하는데 사용된다.

<img src="https://user-images.githubusercontent.com/19484971/197407862-d8cd231b-370a-419c-93cc-c324f5978cbf.png" width=600>

## BMP 이미지 로드

BMP 파일 로더를 처음부터 작성하여 작동 방식을 알고! 다시는 사용하지 않는다고 하였다. 이유는 단순하다. 모델에는 BMP라는 이미지 형식이 아니라 압축 텍스처(compressed textures)라는 모델에 사용하기 적합한 이미지 형식을 사용하기 때문이다.

그래서 자습서에는 BMP에 대한 내용이 있지만, 필자는 텍스처를 사용할 것이고 BMP이미지는 사용할 생각도 없기 때문에 생략한다.

## 텍스처 적용

먼저 프래그먼트 셰이더를 보면 아래와 같다.
```
#version 330 core

// Interpolated values from the vertex shaders
// vertex shaders에서 삽입된 값
in vec2 UV;

// Ouput data
// 출력값
out vec3 color;

// Values that stay constant for the whole mesh.
// 폴리곤 전체에 저장된 상수 값..?
uniform sampler2D myTextureSampler;

void main(){

	// Output color = color of the texture at the specified UV
	// 지정된 UV에서 텍스처의 색상을 출력값으로 한다.
	color = texture( myTextureSampler, UV ).rgb;
}
```

크게 세 가지 과정으로 나뉘어진다.

- 프래그먼트 셰이더에는 UV 좌표 데이터를 입력받는다.
- 접근할 텍스처를 알기 위해 "sampler2D"를 선언한다.
- 마지막으로 텍스처 액세스는 (R,G,B,A) vec4를 반환하는 texture()함수로 수행된다.

정점 셰이더는 UV를 프래그먼트 셰이더에 전달하기만 하면 된다.
```
#version 330 core

// Input vertex data, different for all executions of this shader.
// 셰이더가 실행될 때마다 입력받는 버텍스 데이터
layout(location = 0) in vec3 vertexPosition_modelspace;
layout(location = 1) in vec2 vertexUV;

// Output data ; will be interpolated for each fragment.
// 각 순간(fragment)마다 출력될 데이터
out vec2 UV;

// Values that stay constant for the whole mesh.
uniform mat4 MVP;

void main(){

	// Output position of the vertex, in clip space : MVP * position
	gl_Position =  MVP * vec4(vertexPosition_modelspace,1);
	
	// UV of the vertex. No special space for this one.
	// 이 예제에서는 특별한 공간(좌표계?)가 없다.
	UV = vertexUV;
}

```

튜토리얼에서 `layout(location = 1) in vec2 vertexUV`를 사용한 것과 같이 적용한다, 하지만 (R, G, B) 가 아닌 (U, V) 쌍의 버퍼를 지정한다.
```
// Two UV coordinatesfor each vertex. They were created with Blender.
// 각 정점에 대한 두 개의 UV 좌표로 블렌더로 만들었다고 한다.
static const GLfloat g_uv_buffer_data[] = { 
    0.000059f, 1.0f-0.000004f, 
    0.000103f, 1.0f-0.336048f, 
    0.335973f, 1.0f-0.335903f, 
    1.000023f, 1.0f-0.000013f, 
    0.667979f, 1.0f-0.335851f, 
    0.999958f, 1.0f-0.336064f, 
    0.667979f, 1.0f-0.335851f, 
    0.336024f, 1.0f-0.671877f, 
    0.667969f, 1.0f-0.671889f, 
    1.000023f, 1.0f-0.000013f, 
    0.668104f, 1.0f-0.000013f, 
    0.667979f, 1.0f-0.335851f, 
    0.000059f, 1.0f-0.000004f, 
    0.335973f, 1.0f-0.335903f, 
    0.336098f, 1.0f-0.000071f, 
    0.667979f, 1.0f-0.335851f, 
    0.335973f, 1.0f-0.335903f, 
    0.336024f, 1.0f-0.671877f, 
    1.000004f, 1.0f-0.671847f, 
    0.999958f, 1.0f-0.336064f, 
    0.667979f, 1.0f-0.335851f, 
    0.668104f, 1.0f-0.000013f, 
    0.335973f, 1.0f-0.335903f, 
    0.667979f, 1.0f-0.335851f, 
    0.335973f, 1.0f-0.335903f, 
    0.668104f, 1.0f-0.000013f, 
    0.336098f, 1.0f-0.000071f, 
    0.000103f, 1.0f-0.336048f, 
    0.000004f, 1.0f-0.671870f, 
    0.336024f, 1.0f-0.671877f, 
    0.000103f, 1.0f-0.336048f, 
    0.336024f, 1.0f-0.671877f, 
    0.335973f, 1.0f-0.335903f, 
    0.667969f, 1.0f-0.671889f, 
    1.000004f, 1.0f-0.671847f, 
    0.667979f, 1.0f-0.335851f
};
```

버텍스 버퍼와 똑같이 생성하고, 바인딩하고, 입력해주면 된다. 단, U와 V 정보만 있으므로 size는 2로 바꾸는 것을 잊지말자.
```
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
```

<img src="https://user-images.githubusercontent.com/19484971/197652563-681b79df-533f-4f3b-8c5a-8308789874a4.png" width=400>

## 필터링(filtering)과 밉맵(mipmapping)

<img src="https://user-images.githubusercontent.com/19484971/197652987-6c3348a2-c957-41d0-befd-c86577c4c235.png" width=400>

위의 스크린샷에서 볼 수 있듯이 텍스처 품질은 그다지 좋지 않다. 이는 loadBMP_custom에서 다음과 같은 코드가 있기 때문이다.

```
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
```

프래그먼트 셰이더에서 texture()가 (U,V) 좌표에 있는 값을 그대로 사용한다는 의미이다, 아래의 사진을 참고하자.

<img src="https://user-images.githubusercontent.com/19484971/197653437-0432e0f9-6fa7-42fa-bdb2-bb1ae2fec2c9.png" width=400>

이를 해결하기 위해 색을 보정하는 몇 가지 방법이 있는데 이것을 필터링이라고 부른다.

### 선형 필터링(Linear filtering)

주변의 다른 셀의 색상을 살펴보고 그것들의 중간값을 계산하여 넣어주는 방식이다. 이렇게 하면 위에서 본 잘리는 듯한 가장자리를 피할 수 있다.

<img src="https://user-images.githubusercontent.com/19484971/197655193-fd0b42e2-5851-4142-bbf2-18139c7d57a5.png" width=400>

이 방식은 많이 활용하기는 하지만 고품질을 원한다면 조금은 느린 등방성 필터링을 사용할 수도 있다.

### 이방성 필터링(Anisotropic filtering)

실제로 보이는 이미지의 일부에 가깝다고.. 한다.. 예를 들어 텍스처가 측면에서 보이고 약간 회전된 경우 이방성 필터링은 해당 방향을 따라 고정된 수의 샘플("비등방성 수준"..?)을 취하여 파란색 직사각형에 포함된 색상을 계산한다.

<img src="https://user-images.githubusercontent.com/19484971/197655197-54d1ec9d-55a8-452a-87af-97d4317757e0.png" width=400>

### 밉맵(Mipmaps)

밉맵은 렌더링 속도를 향상시키기 위한 목적으로 텍스처와 이를 연속적으로 미리 축소시킨 텍스처들로 이루어진 비트맵 이미지의 집합.. 이라고 한다.

위의 필터링 방법으로는 4개의 텍셀(텍스처의 셀)로는 부족하다고 한다. 특히 모델이 멀리 떨어져 있어서 아주 작게 보이는 경우 특히 문제가 되는데 그렇다고 모든 셀을 평균화하기는 어렵다. 이럴 때 밉맵을 사용한다!

밉맵에 대해서는 아래와 같다.

- 1x1 이미지(이는 이미지의 모든 텍셀의 평균임)만 남을 때까지 이미지를 연속적으로 2씩 축소하여 초기화한다.
- 메쉬를 그릴 때 텍셀이 얼마나 큰지에 따라 어떤 밉맵을 사용하는 것이 더 적합한지 선택한다.
- 가장 가까운 선형 또는 이방성 필터링을 사용하여 이 밉맵을 샘플링한다.
- 추가 품질을 위해 두 개의 밉맵을 샘플링하고 결과를 혼합할 수도 있다.

와.. 무슨말인지 모르겠다.. 색상 선택을 아주 고급스럽게 해준다는 의미간다. 그래도 확실히 아는 것은  OpenGL에게 잘 부탁하면 모든 것을 해 준다는 것이다.

```
// When MAGnifying the image (no bigger mipmap available), use LINEAR filtering
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
// When MINifying the image, use a LINEAR blend of two mipmaps, each filtered LINEARLY too
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
// Generate mipmaps, by the way.
glGenerateMipmap(GL_TEXTURE_2D);
```

하지만 필자는 아직 사용하지 않았다, 적용하고 싶은 이미지가 있는데 필요하다면 활용해볼 예정이다.

## GLFW로 텍스처를 로드하는 방법

전용 라이브러리를 사용하면 쉽게 텍스처를 로드할 수 있다. 

문제는 GLFW2에서 TGA 파일에만 가능하고 현재 사용 중인 GLFW3에서는 해당 기능이 제거되었다고 한다...

아니 왜 튜토리얼에서 굳이 소개한걸까..?

## 압축 텍스처

이쯤되면 TGA 대신 JPEG 파일을 로드하는 방법이 궁금한데, 자습서에서 하지 말라고 즉답하였다;

GPU는 JPEG를 이해할 수 없다. 그래서 원본 이미지를 JPEG로 압축하고 GPU가 이해할 수 있도록 압축을 해제하는 대신 이미지 품질이 떨어지는 문제가 있다고 한다. 그래서 다른 방법으로 텍스처를 만든다.

## 더 많은 내용

음.. 이 아래에서부터는 텍스처를 만드는 방법이 기술되어있다. 그런데 내가 만들 프로젝트에서는 텍스처를 만드는 것이 아니라 카메라에서 받은 이미지를 투영해서 만드는 것이다.

즉, 해당 방식을 사용할 수 없다. 그래서 이 아래 내용은 생략하겠다!

만약 보고 싶다면 [이곳](http://www.opengl-tutorial.org/beginners-tutorials/tutorial-5-a-textured-cube/)을 읽자!

그런데.. 자습서 가장 아래부분까지 왔어도 `alpha channel`이라는 단어는 안 보이는데.. 내용을 넣다가 만건지.. 내가 이해 못한건지..

## 전체코드

`tutorial5.cpp`
```
// 이 튜토리얼에서는 아래의 내용을 배운다고 한다.

//UV 좌표란 ?
// 메쉬에 텍스쳐링 할 때 각 삼각형에 대해 이미지의 어느 부분을 사용해야 하는지 OpenGL에 알려주는 방법이 필요하다. 
// 이때 사용하는 것이 UV 좌표이다.
// 텍스쳐링 : 텍스처 매핑(texture mapping)은 컴퓨터 그래픽스 분야에서 가상의 3차원 물체의 표면에 세부적인 질감의 묘사를 하거나 색을 칠하는 기법
//텍스처를 직접 로드하는 방법
//OpenGL에서 사용하는 방법
//필터링 및 밉매핑이란 무엇이며 사용 방법
//GLFW로 텍스처를 더 강력하게 로드하는 방법
//알파 채널이란

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

int main( void )
{
	// Initialise GLFW
	if( !glfwInit() )
	{
		fprintf( stderr, "Failed to initialize GLFW\n" );
		return -1;
	}

	glfwWindowHint(GLFW_SAMPLES, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	// Open a window and create its OpenGL context
	window = glfwCreateWindow( 1024, 768, "Tutorial 05 - Textured Cube", NULL, NULL);
	if( window == NULL ){
		fprintf( stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n" );
		glfwTerminate();
		return -1;
	}
	glfwMakeContextCurrent(window);

	// Initialize GLEW
	glewExperimental = true; // Needed for core profile
	if (glewInit() != GLEW_OK) {
		fprintf(stderr, "Failed to initialize GLEW\n");
		return -1;
	}

	// Ensure we can capture the escape key being pressed below
	glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

	// Dark blue background
	glClearColor(0.0f, 0.0f, 0.4f, 0.0f);

	// Enable depth test
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	glDepthFunc(GL_LESS); 

	GLuint VertexArrayID;
	glGenVertexArrays(1, &VertexArrayID);
	glBindVertexArray(VertexArrayID);

	// Create and compile our GLSL program from the shaders
	GLuint programID = LoadShaders( "TransformVertexShader.vertexshader", "TextureFragmentShader.fragmentshader" );

	// Get a handle for our "MVP" uniform
	GLuint MatrixID = glGetUniformLocation(programID, "MVP");

	// Projection matrix : 45?Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
	glm::mat4 Projection = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);
	// Camera matrix
	glm::mat4 View       = glm::lookAt(
								glm::vec3(4,3,3), // Camera is at (4,3,3), in World Space
								glm::vec3(0,0,0), // and looks at the origin
								glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
						   );
	// Model matrix : an identity matrix (model will be at the origin)
	glm::mat4 Model      = glm::mat4(1.0f);
	// Our ModelViewProjection : multiplication of our 3 matrices
	glm::mat4 MVP        = Projection * View * Model; // Remember, matrix multiplication is the other way around

	// Load the texture using any two methods
	//GLuint Texture = loadBMP_custom("uvtemplate.bmp");
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
	// 각 정점에 대한 두 개의 UV 좌표로 블렌더로 만들었다고 한다.
	static const GLfloat g_uv_buffer_data[] = { 
		0.000059f, 1.0f-0.000004f, 
		0.000103f, 1.0f-0.336048f, 
		0.335973f, 1.0f-0.335903f, 
		1.000023f, 1.0f-0.000013f, 
		0.667979f, 1.0f-0.335851f, 
		0.999958f, 1.0f-0.336064f, 
		0.667979f, 1.0f-0.335851f, 
		0.336024f, 1.0f-0.671877f, 
		0.667969f, 1.0f-0.671889f, 
		1.000023f, 1.0f-0.000013f, 
		0.668104f, 1.0f-0.000013f, 
		0.667979f, 1.0f-0.335851f, 
		0.000059f, 1.0f-0.000004f, 
		0.335973f, 1.0f-0.335903f, 
		0.336098f, 1.0f-0.000071f, 
		0.667979f, 1.0f-0.335851f, 
		0.335973f, 1.0f-0.335903f, 
		0.336024f, 1.0f-0.671877f, 
		1.000004f, 1.0f-0.671847f, 
		0.999958f, 1.0f-0.336064f, 
		0.667979f, 1.0f-0.335851f, 
		0.668104f, 1.0f-0.000013f, 
		0.335973f, 1.0f-0.335903f, 
		0.667979f, 1.0f-0.335851f, 
		0.335973f, 1.0f-0.335903f, 
		0.668104f, 1.0f-0.000013f, 
		0.336098f, 1.0f-0.000071f, 
		0.000103f, 1.0f-0.336048f, 
		0.000004f, 1.0f-0.671870f, 
		0.336024f, 1.0f-0.671877f, 
		0.000103f, 1.0f-0.336048f, 
		0.336024f, 1.0f-0.671877f, 
		0.335973f, 1.0f-0.335903f, 
		0.667969f, 1.0f-0.671889f, 
		1.000004f, 1.0f-0.671847f, 
		0.667979f, 1.0f-0.335851f
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
	glDeleteTextures(1, &Texture);
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
// 셰이더가 실행될 때마다 입력받는 버텍스 데이터
layout(location = 0) in vec3 vertexPosition_modelspace;
layout(location = 1) in vec2 vertexUV;

// Output data ; will be interpolated for each fragment.
// 각 순간(fragment)마다 출력될 데이터
out vec2 UV;

// Values that stay constant for the whole mesh.
uniform mat4 MVP;

void main(){

	// Output position of the vertex, in clip space : MVP * position
	gl_Position =  MVP * vec4(vertexPosition_modelspace,1);
	
	// UV of the vertex. No special space for this one.
	// 이 예제에서는 특별한 공간(좌표계?)가 없다.
	UV = vertexUV;
}
```

`TextureFragmentShader.fragmentshader`
```
#version 330 core

// Interpolated values from the vertex shaders
// vertex shaders에서 삽입된 값
in vec2 UV;

// Ouput data
// 출력값
out vec3 color;

// Values that stay constant for the whole mesh.
// 폴리곤 전체에 저장된 상수 값..?
uniform sampler2D myTextureSampler;

void main(){

	// Output color = color of the texture at the specified UV
	// 지정된 UV에서 텍스처의 색상을 출력값으로 한다.
	color = texture( myTextureSampler, UV ).rgb;
}
```