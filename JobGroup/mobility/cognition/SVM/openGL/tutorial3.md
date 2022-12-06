# Tutorial 3 : Matrices

코드에 대한 설명은 없고 행렬에 대한 정보만 많다. 가장 중요한 튜토리얼이라는데 개인적으로는 튜토리얼 2가 더 중요해보인다. (행렬 변환은 다른 프로그램에서도 쓰일 수 있지만 튜토리얼 2는 openGL에서만 쓰이는 코드가 많아서)

그래도 행렬은 그래픽에서 너무나도 중요하게, 유용하게 쓰이므로 해당 튜토리얼 또한 중요한 튜토리얼임에는 확실하다!

## 행렬(Matrices)

행렬 자체는 알고있고 행렬의 곱셈도 알고있다고 가정하고 진행하겠다. 자세한 내용을 바란다면 [이곳](https://heinleinsgame.tistory.com/10?category=757483)을 참고하자.

이때 GLM을 사용하는데 이것은 OpenGL Mathematics의 약자이며 행렬의 연산을 위해서 사용하는 헤더 파일만 있는 라이브러리이다.

3차원 행렬을 C++에서 GLM을 활용하였을 때는 아래와 같이 사용하고
```
glm::mat4 myMatrix;
glm::vec4 myVector;
// fill myMatrix and myVector somehow
glm::vec4 transformedVector = myMatrix * myVector; // Again, in this order ! this is important.
```

셰이더를 사용할 때 사용하는 언어인 GLSL에서는 아래와 같이 사용한다.
```
mat4 myMatrix;
vec4 myVector;
// fill myMatrix and myVector somehow
vec4 transformedVector = myMatrix * myVector; // Yeah, it's pretty much the same than GLM
```

C++에서 행렬 연산은 많이 사용해서 아래에서 다양한 행렬 함수를 볼 수 있는데 GLSL에서는 결과를 받는 경우가 많아서 상대적으로 행렬을 계산하는 함수가 적은 것 같다.

### 동차좌표(Homogeneous coordinates)

n차원 좌표정보를 n+1개의 좌표로 나타내는 좌표계

- 3차원 좌표의 동차좌표를 (x,y,z,w)와 같이 표현하면
    - w == 1인 벡터 (x,y,z,1)은 위치를 의미한다.
    - w == 0인 벡터(x,y,z,0)는 방향을 의미한다.

동차좌표를 이용하여 아래의 회전, 이동행렬을 동시에, 간단하게 처리할 수 있다. 아래에서 소개할 행렬은 모두 동차행렬로 표시할 것이기 때문에 잘 기억하는 것이 좋다.

### 단위행렬(Identity matrix)

단위행렬 혹은 항등행렬이라고 불리는 주대각선의 원소가 모두 1이며 나머지 원소는 모두 0인 정사각 행렬을 의미한다.

<img src="https://user-images.githubusercontent.com/19484971/197367415-b08b2bf3-5fbd-4670-b925-df5f756065f9.png" width=700>

행렬 A에 단위행렬을 곱하면 항상 행렬 A가 나온다는 특징이 있다.

C++
```
glm::mat4 myIdentityMatrix = glm::mat4(1.0f);
```

### Scaling matrices

내가 못 찾는 건가..? 한국어로 부르는 이름이 없다; 비례행렬이라고 부르는 블로그를 보긴하였지만.. 위키가.. 없다. 학교에서 배울때는 스칼라(Scalar) 행렬이라고 배웠다.

각 방향별로 배수를 취하는 행렬로 주대각선의 원소 외에는 모두 0이다.

<img src="https://user-images.githubusercontent.com/19484971/197367762-94bf694f-696d-4fb9-8856-b9ab65af3af2.png" width=100>

아래는 각 벡터의 모든 방향으로 크기를 2배로 곱하는 행렬이다.

<img src="https://user-images.githubusercontent.com/19484971/197367769-aac096fd-dc28-400a-9ebf-66bc2abf9e61.png" width=700>

단위행렬은  (X,Y,Z) = (1,1,1)인 Scaling 행렬의 특수한 경우이고 (X,Y,Z)=(0,0,0)도 마찬가지이다.

C++
```
// Use #include <glm/gtc/matrix_transform.hpp> and #include <glm/gtx/transform.hpp>
// 위의.. 라이브러리가 필요하다고 한다.
glm::mat4 myScalingMatrix = glm::scale(2.0f, 2.0f ,2.0f);
```

### 변환행렬(Transformation matrices)

각 방향마다 옮기고 싶은 위치만큼 옮겨주는 행렬, 동차행렬로 아래와 같이 표현한다.

<img src="https://user-images.githubusercontent.com/19484971/197368062-9f44dcca-6cf1-4ad5-b5b9-822e93fe7690.png" width=100>

벡터(10,10,10,1)를 x축 방향으로 10만큼 옮기는 행렬과 연산은 다음과 같다.

<img src="https://user-images.githubusercontent.com/19484971/197368073-8fd1273a-f13c-48c3-b492-55b50db6d9c3.png" width=700>

(20,10,10,1)를 얻을 수 있다, 여기서 1은 (20,10,10)가 의미하는 것이 위치라는 것을 표현하는 숫자임을 잊지말자.

벡터(0,0,-1,0)를 x축 방향으로 10만큼 옮기는 연산을 하면 벡터(0,0,-1)라는 `방향`을 옮기는 것이므로 연산 이후에도 달라지는 점이 없다.

<img src="https://user-images.githubusercontent.com/19484971/197368514-7ab990a9-90dd-4b82-a91d-5cf640d8ded0.png" width=700>

C++의 GLM
```
#include <glm/gtx/transform.hpp> // after <glm/glm.hpp>
 
glm::mat4 myMatrix = glm::translate(glm::mat4(), glm::vec3(10.0f, 0.0f, 0.0f));
glm::vec4 myVector(10.0f, 10.0f, 10.0f, 0.0f);
glm::vec4 transformedVector = myMatrix * myVector; // guess the result
```

셰이더의 GLSL
```
vec4 transformedVector = myMatrix * myVector;
```

### 회전행렬(Rotation matrices)

이름 그대로 벡터를 회전하는 행렬, 간단한 사용을 위해서 정확한 내용을 알 필요는 없어서 자습서에서는 설명을 생략하였다; [튜토리얼 17](http://www.opengl-tutorial.org/intermediate-tutorials/tutorial-17-quaternions/)에서 자세히 볼 수 있다고 한다.

C++
```
// Use #include <glm/gtc/matrix_transform.hpp> and #include <glm/gtx/transform.hpp>
glm::vec3 myRotationAxis( ??, ??, ??);
glm::rotate( angle_in_degrees, myRotationAxis );
```

### 행렬곱

위에서 알게된 행렬들을 곱하으로써 여러가지의 행렬을 동시에 적용할 수 있다.

아래와 같이 이동, 회전, 스케일링 행렬을 한번에 적용이 가능하다.
```
TransformedVector = TranslationMatrix * RotationMatrix * ScaleMatrix * OriginalVector;
```

여기서 주의할 점은.. 회전행렬과 변환행렬은 순서에 따라서 다른 결과를 불러오는 경우가 일반적이기 때문에 주의해주어야 한다. 자습서에서는 아래와 같이 설명하였다.

- 한 걸음 나아가고 좌회전
- 좌회전하고 한 걸음 전진

때문에 회전행렬과 변환행렬을 같이 쓴다면 잘 고려하고 사용하자!

C++에서 GLM 사용:
```
glm::mat4 myModelMatrix = myTranslationMatrix * myRotationMatrix * myScaleMatrix;
glm::vec4 myTransformedVector = myModelMatrix * myOriginalVector;
```

GLSL에서 :
```
mat4 transform = mat2 * mat1;
vec4 out_vec = transform * in_vec;
```

## The Model, View and Projection matrices

아오.. 서양에서는 동양과는 다르게 화면을 대하는 점 때문인지 필자가 이해를 못하는 것인지 설명을 이해할 수가 없다;;

대충.. 월드, 모델, 카메라 좌표계를 설명하려는 것 같은데, 이해하는 만큼만 작성해보겠다.

### Model matrix

모델의 예시는 블렌더(Blender)라는 툴에서 유명한 모델인 `the monkey Suzanne`로 진행한다!

<img src="https://user-images.githubusercontent.com/19484971/197369232-b6acf211-ac98-4271-b5e6-1f4d431b1874.png" width=400>

우리가 관찰하고자하는 이 모델은 다양한 정점으로 이루어져 있는데 이 모델이 월드 좌표계 어디에 위치하는지 파악할 필요가 있다.

<img src="https://user-images.githubusercontent.com/19484971/197369253-2b05f377-a0b6-438a-aed7-34616b494a71.png" width=600>

월드 좌표계의 중심점과 모델간에 검은색 선 만큼의 이동이 있다는 것을 볼 수 있다. 

<img src="https://user-images.githubusercontent.com/19484971/197369438-9ef823ae-b8ad-4482-9d7c-f8a19b31df89.png" width=600>

그러므로 모델의 정점을 월드 좌표계로 이동시키기 위해서는 `Model Matrix`를 적용시켜주어야 한다.

<img src="https://user-images.githubusercontent.com/19484971/197369443-596ae015-f736-4984-bcba-67fbb5d3eec4.png" width=200>

### View matrix

위의 모델을 볼 때는 카메라의 시점을 통해 보게된다. 카메라를 통해서 모델을 보게되면 어떻게 모델이 보일까?

일단 아래와 같이 카메라를 추가해보자.

<img src="https://user-images.githubusercontent.com/19484971/197372497-a267bfdd-34b9-467f-a5a7-a4b4586f7bbd.png" width=600>

월드좌표계의 모델의 정점들이 카메라의 시점을 기준으로 보게되므로 아래와 같이 모델 정점을 월드좌표계로 바꿔주고 다시 그것을 카메라 좌표계로 바꾸어주는 작업이 필요하다.

<img src="https://user-images.githubusercontent.com/19484971/197372501-66a370b8-679c-44ab-a6ba-faa34de958af.png" width=600>

openGL에서 카메라 설정하기 위해서는 GLM의 glm::lookAt 기능을 활용하면 된다.

```
glm::mat4 CameraMatrix = glm::lookAt(
    cameraPosition, // the position of your camera, in world space
    cameraTarget,   // where you want to look at, in world space
    upVector        // probably glm::vec3(0,1,0), but (0,-1,0) would make you looking upside-down, which can be great too
);
```

다이어그램으로 표현하면 다음과 같다.

<img src="https://user-images.githubusercontent.com/19484971/197372530-ca663de2-e203-4397-8561-c4547a46baed.png" width=200>

### Projection matrix

카메라가 모델 기준(카메라 좌표계에서)으로 보았을 때 정점이 어떻게 변환하는지는 위에서 간단히 보았다. 하지만 아직 끝이 아니다!

카메라의 시점이 넓은지 좁은지에 따라서 거리가 같은 물체라도 더 작고 멀게 혹은 더 크고 가깝게 보일 수 있는데 이를 원근 투영이라고 한다.

<img src="https://user-images.githubusercontent.com/19484971/197375510-5cbc199e-85a1-437e-968a-032a0ffe64a2.png" width=600>

C++에서 4x4 행렬로 이 투영법을 나타내면 아래와 같다.
```
// Generates a really hard-to-read matrix, but a normal, standard 4x4 matrix nonetheless
glm::mat4 projectionMatrix = glm::perspective(
    glm::radians(FoV), // The vertical Field of View, in radians: the amount of "zoom". Think "camera lens". Usually between 90° (extra wide) and 30° (quite zoomed in)
    4.0f / 3.0f,       // Aspect Ratio. Depends on the size of your window. Notice that 4/3 == 800/600 == 1280/960, sounds familiar ?
    0.1f,              // Near clipping plane. Keep as big as possible, or you'll get precision issues.
    100.0f             // Far clipping plane. Keep as little as possible.
);
```

그러면 결과적으로 모델의 정점을 모델 좌표계 -> 월드 좌표계 -> 카메라 좌표계 -> 동차 좌표계(homogeneous Coordinates)로 바꿀 수 있다.

<img src="https://user-images.githubusercontent.com/19484971/197375951-d3454691-fa31-4afb-8e27-274afac1d7b1.png" width=200>

동차공간(Homogeneous Space) 이란 모든 정점이 작은 큐브에 정의되는 것으로 말보다는 아래의 사진으로 이해하는 것이 편하다.

원래 카메라 좌표계에서 아래의 붉은 공간내의 물체를 본다면 아래와 같다.

<img src="https://user-images.githubusercontent.com/19484971/197376052-496558bb-6a33-405d-97fb-3d8a560f4edd.png" width=600>

위의 사진을 동차 좌표계로 바꾸면 아래와 같이 보인다.

<img src="https://user-images.githubusercontent.com/19484971/197376057-24a46b0e-e7f6-4ba2-87d8-c73af9233244.png" width=600>

우리 컴퓨터 모니터는 카메라같은 시야를 가진 것이 아니라서 동차 좌표계 기준의 물체를 보여주게 된다.

<img src="https://user-images.githubusercontent.com/19484971/197377501-00ada511-d76b-4253-9912-43c905e00c03.png" width=600>

여기에 모니터의 화면비율까지 고려하면 아래와 같이 된다. 이것은 셰이더에서 작동으로 변환이 된다고 한다.

<img src="https://user-images.githubusercontent.com/19484971/197377505-4f3b2295-f7bd-4bc9-90d2-c3c638244ea0.png" width=600>

월드좌표계, 카메라좌표계, 동차좌표계 각각에서의 카메라의 시야에 따른 물체의 표현을 잘 표현한 사이트가 있어서 가져와보았다.

<img src="https://user-images.githubusercontent.com/19484971/197377301-4d31a538-14ff-4acd-b73b-34d491c3689f.gif" width=600>

> 출처 : https://jsantell.com/model-view-projection/

아무리봐도.. 예시 엄청 좋다 발표 ppt에도 사용하는 것이 좋겠다.

### Cumulating Model View Projection matrix

위의 행렬을.. openGL에서 직접 적용해야 사용하는 모델의 원하는 모습으로 볼 수 있다. 기본적으로는 아래와 같이 작성하여 적용한다.

C++
```
// C++ : compute the matrix
glm::mat4 MVPmatrix = projection * view * model; // Remember : inverted !
```

GLSL
```
// GLSL : apply it
transformed_vertex = MVP * in_vertex;
```

## 실습

250줄 만에 튜토리얼 실습을 진행해보자!

우선 행렬 연산을 위한 라이브러리를 가장 윗줄에 넣는다!
```
#include <glm/gtc/matrix_transform.hpp>
```

GLSL에게 결과값을 넘겨주기 위한 객체의 ID를 먼저 저장해둔다.
```
// Get a handle for our "MVP" uniform
// programID에서 "MVP"이라는 단어로 찾은 uniform 객체의 ID를 저장한다.
GLuint MatrixID = glGetUniformLocation(programID, "MVP");
```

각 모델에 대한 MVP 매트릭스를 생성한다.
```
// 첫번째 파라미터는 카메라의 시야각, 여기서는 45라디안으로 설정하였다. 
// 해당 수치는 원근감에 크게 영향을 준다. 보통은 30~90도 사이로 지정한다.
// 두번째는 화면비(Aspect Ratio)로 평소말하는 4:3, 16:9 같은 것들이다.
// 세번째와 네번째는 near clipping plane, far clipping plane(전방 절단면, 후방 절단면)이라는 것을 정의하는데 이것은..
// 장면의 일부 형상을 제외하고, 장면의 특정 부분만 렌더링하는데에 쓰이는 가상의 평면을 말한다고 한다.
// (참고 : http://pertinency.blogspot.com/2019/12/clipping-planes.html)
// Projection matrix : 45?Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
// 아래의 코드는 시야각 45라디안에 4:3비율의 화변비, 0.1~100거리의 물체를 화면에 보여주는 투영이다.
glm::mat4 Projection = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);

// Or, for an ortho camera :
// 아래는 직교투영..?이라고 한다. 위에서 사용한 것은 원근투영이다.
//glm::mat4 Projection = glm::ortho(-10.0f,10.0f,-10.0f,10.0f,0.0f,100.0f); // In world coordinates

// Camera matrix
// 단순히 openGL의 카메라를 월드 좌표계의 (4, 3, 3)에 위치시키고 (0, 0, 0)을 바라보게 한 상태를 의미한다.
// 마지막 파라미터는 upvector라고 하는데 검색해보니 카메라의 위를 정의해주는 벡터를 정의해주는 것이다.
// 한 위치에서 다른 위치를 바라본다고 해도 고개를 90로 돌려서 볼 수 있고, 안 돌리고 볼 수 있고, -90로 돌려서 볼 수 있는데 그것을 정의해주는 것
glm::mat4 View = glm::lookAt(
    glm::vec3(4,3,3), // Camera is at (4,3,3), in World Space
    glm::vec3(0,0,0), // and looks at the origin
    glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
);

// Model matrix : an identity matrix (model will be at the origin)
glm::mat4 Model = glm::mat4(1.0f);

// Our ModelViewProjection : multiplication of our 3 matrices
// 위의 ModelViewProjection 세 행렬을 곱해준다. 순서는 꼭 지켜주어야 한다.
// Remember, matrix multiplication is the other way around
glm::mat4 MVP = Projection * View * Model; 
```

위에서 찾았던 MatrixID 변수를 통해 GLSL에게 계산 결과를 넘겨준다. 
```
// Send our transformation to the currently bound shader, in the "MVP" uniform
// 사용중인 쉐이더 내의 uniform "MVP"에 programID의 데이터를 보낸다.
glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);
```

`SimpleVertexShader`, `vertexshader`에서 
정점을 변환하기 위해 위에서 받은 정보를 사용한다.
```
// Input vertex data, different for all executions of this shader.
layout(location = 0) in vec3 vertexPosition_modelspace;
  
// Values that stay constant for the whole mesh.
// 전체.. opengl의 mesh에 대해서 일정하게 유지되는 값?
uniform mat4 MVP;
  
void main(){
    // Output position of the vertex, in clip space : MVP * position
    // clip 공간에서의 정점의 출력 위치
    // clip space라는 것이 시야범위 내에서 보이는 물체들만 존재하는 좌표계라고 한다.
    // 즉, 절단면에 의해 걸러지지 않는 물체이면서 시야범위에 있는 물체들만이 존재하는 좌표계
    // 참고 : http://rapapa.net/?p=3531
    gl_Position =  MVP * vec4(vertexPosition_modelspace,1);
}
```

찾아보니.. openGL에서는 모니터에 표현하기까지 다양한 좌표계를 거치게 되는데 그 중 clip 공간은 모니터에서 표현되기 바로 직전의 공간임을 알 수 있었다. 더 자세한 내용은 [이곳](https://heinleinsgame.tistory.com/11?category=757483)에서 확인할 수 있다.

<img src="https://user-images.githubusercontent.com/19484971/197383952-c623aa05-a51a-478f-a99f-8c6195532c2d.png" width=600>

끝났다! 튜토리얼 2에서 만든 같은 삼각형을 다른 시점에서 보는 화면이 출력된다.

<img src="https://user-images.githubusercontent.com/19484971/197380634-c7eb158f-b133-46a2-8bec-0a81f99328c9.png" width=400>

아직은 고정된 시점이지만 튜토리얼 6에서는 키보드와 마우스를 사용하여 이러한 값을 동적으로 수정하여 게임에서 사용하는 것 같은 카메라를 만드는 방법을 배운다고 한다.

하지만 그 전에 [3D 모델에 색상을 넣는 방법(튜토리얼 4)](./tutorial4.md)과 [텍스처를 입히는 방법(튜토리얼 5)](./tutorial5.md)을 살펴볼 것이다.

## 전체코드

`tutorial03.cpp`
```
// Include standard headers
#include <stdio.h>
#include <stdlib.h>

// Include GLEW
#include <GL/glew.h>

// Include GLFW
// 3D 계산을 위한 라이브러리
#include <GLFW/glfw3.h>
GLFWwindow* window;

// Include GLM
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
// “glm::vec3”(“vec3” )을 입력하는 것을 강제한다. 
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
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); //We don't want the old OpenGL 

	// Open a window and create its OpenGL context
	window = glfwCreateWindow( 1024, 768, "Tutorial 03 - Matrices", NULL, NULL);
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

	GLuint VertexArrayID;
	glGenVertexArrays(1, &VertexArrayID);
	glBindVertexArray(VertexArrayID);

	// Create and compile our GLSL program from the shaders
	GLuint programID = LoadShaders( "SimpleTransform.vertexshader", "SingleColor.fragmentshader" );

	// Send our transformation to the currently bound shader, in the "MVP" uniform
	// 사용중인 쉐이더 내의 uniform "MVP"에 programID의 데이터를 보낸다.
	GLuint MatrixID = glGetUniformLocation(programID, "MVP");

	
	// 첫번째 파라미터는 카메라의 시야각, 여기서는 45라디안으로 설정하였다. 
	// 해당 수치는 원근감에 크게 영향을 준다. 보통은 30~90도 사이로 둔다고 한다.
	// 두번째는 화면비(Aspect Ratio)로 평소말하는 4:3, 16:9 같은 것들이다.
	// 세번째와 네번째는 near clipping plane, far clipping plane(전방 절단면, 후방 절단면)이라는 것을 정의하는데 이것은..
	// 장면의 일부 형상을 제외하고, 장면의 특정 부분만 렌더링하는데에 쓰이는 가상의 평면을 말한다고 한다.
	// (참고 : http://pertinency.blogspot.com/2019/12/clipping-planes.html)
	// openGL에도 같은 설명이 있지만 절두체..;;라고 번역되고 시야범위 색을 빨간색으로 통일하는 바람에 이해를 못했다;
	// Projection matrix : 45?Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
	// 아래의 코드는 시야각 45라디안에 4:3비율의 화변비, 0.1~100거리의 물체를 화면에 보여주는 투영(맞나..)이다.
	glm::mat4 Projection = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);
	
	// Or, for an ortho camera :
	// 아래는 직교투영..?이라고 한다. 위에서 사용한 것은 원근투영이다.
	//glm::mat4 Projection = glm::ortho(-10.0f,10.0f,-10.0f,10.0f,0.0f,100.0f); // In world coordinates
	
	// Camera matrix
	// 단순히 openGL의 카메라를 월드 좌표계의 (4, 3, 3)에 위치시키고 (0, 0, 0)을 바라보게 한 상태를 의미한다.
	// 마지막 파라미터는 upvector라고 하는데 검색해보니 카메라의 위를 정의해주는 벡터를 정의해주는 것이다.
	// 한 위치에서 다른 위치를 바라본다고 해도 고개를 90로 돌려서 볼 수 있고, 안돌리고 볼 수 있고, -90로 돌려서 볼 수 있는데 그것을 정의해주는 것
	glm::mat4 View       = glm::lookAt(
								glm::vec3(4,3,3), // Camera is at (4,3,3), in World Space
								glm::vec3(0,0,0), // and looks at the origin
								glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
						   );
	// Model matrix : an identity matrix (model will be at the origin)
	glm::mat4 Model = glm::mat4(1.0f);
	// Our ModelViewProjection : multiplication of our 3 matrices
	// 위의 ModelViewProjection 세 행렬을 곱해준다. 순서는 꼭 지켜주어야 한다.
	glm::mat4 MVP = Projection * View * Model; // Remember, matrix multiplication is the other way around

	static const GLfloat g_vertex_buffer_data[] = { 
		-1.0f, -1.0f, 0.0f,
		 1.0f, -1.0f, 0.0f,
		 0.0f,  1.0f, 0.0f,
	};

	GLuint vertexbuffer;
	glGenBuffers(1, &vertexbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);

	do{

		// Clear the screen
		glClear( GL_COLOR_BUFFER_BIT );

		// Use our shader
		glUseProgram(programID);

		// Send our transformation to the currently bound shader, 
		// in the "MVP" uniform
		// 사용중인 쉐이더 내의 uniform "MVP"에 programID의 데이터를 보낸다.
		glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);

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

		// Draw the triangle !
		glDrawArrays(GL_TRIANGLES, 0, 3); // 3 indices starting at 0 -> 1 triangle

		glDisableVertexAttribArray(0);

		// Swap buffers
		glfwSwapBuffers(window);
		glfwPollEvents();

	} // Check if the ESC key was pressed or the window was closed
	while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
		   glfwWindowShouldClose(window) == 0 );

	// Cleanup VBO and shader
	glDeleteBuffers(1, &vertexbuffer);
	glDeleteProgram(programID);
	glDeleteVertexArrays(1, &VertexArrayID);

	// Close OpenGL window and terminate GLFW
	glfwTerminate();

	return 0;
}


```

`SimpleTransform.vertexshader`
```
#version 330 core

// Input vertex data, different for all executions of this shader.
layout(location = 0) in vec3 vertexPosition_modelspace;

// Values that stay constant for the whole mesh.
// 전체.. opengl의 mesh에 대해서 일정하게 유지되는 값..이요?
uniform mat4 MVP;

void main(){

	// Output position of the vertex, in clip space : MVP * position
	// clip 공간에서의 정점의 출력 위치
	// clip space라는 것이 시야범위 내에서 보이는 물체들만 존재하는 좌표계라고 한다.
	// 즉, 절단면에 의해 걸러지지 않는 물체이면서 시야범위에 있는 물체들만이 존재하는 좌표계
	// 참고 : http://rapapa.net/?p=3531
	gl_Position =  MVP * vec4(vertexPosition_modelspace,1);
}
```

`SingleColor.fragmentshader`
```
#version 330 core

// Output data
out vec3 color;

void main()
{
	// Output color = red 
	color = vec3(1,0,0);

}
```