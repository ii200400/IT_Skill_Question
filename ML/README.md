- AI, 머신 러닝, 딥러닝 차이점?
AI는 인공지능의 약자로, 사람에 준하는 지능을 가진 기계를 만들기 위한 기술을 의미합니다.
AI를 만들기 위한 여러 기술 중에는 기계학습이 있으며 기계가 학습을 하는 듯한 알고리즘이 특징으로 이러한 이름이 붙여졌다고 합니다
기계학습을 구현하는 대표적인 방법으로 딥러닝이 있습니다. 사람 뇌의 뉴런을 모방하는 듯한 알고리즘인 뉴런네트워크를 활용하여 구현할 수 있습니다.

- 딥러닝이 각광받는 이유?
많은 양의 데이터가 쌓이면서 그 데이터를 효율적으로 분석하고 정리할 필요가 생겼는데 딥러닝을 이용하여 만든 AI가 이러한 데이터를 빠르게 분석하고 활용하는데 큰 도움이 되고 있다고 생각하기 때문입니다.

- Likelihood와 probability의 차이점?
일반적으로는 단순히 가능성, 확률이라고 부릅니다. 어떠한 분포도가 주어졌을 때, 범위 내에 데이터가 있을 확률을 의미합니다. 
우도 또는 가능도라 불립니다. x값이 주어졌을 때, 가정한 분포도(매개변수)가 실재와 부합하는 정도라고 이해했습니다.
참고 - https://www.youtube.com/watch?v=mxCmB1WE3R8

- Maximum Likelihood estimation과 Maximum A Posteriori estimation의 차이?
MLE는 가지고 있는 데이터들이 가장 잘 설명되는 형태의 분포도(매개변수)를 찾는 것입니다.
MAP는 MLE와 비슷하지만 베이즈 정리(Bayes’ theorem)에 근거한 사전 확률을 고려합니다.

- Logistic Regression(로지스틱 회귀)이란?

 
- Linear Regression이란? 푸는 방법 2가지 - 선형대수적 방법, Gradient Descent
 
- SVD란?
 
- SVD의 차원 축소에 쓰이는 3가지 방법?
 
 
- Bayesian Rule?
 
 
- SVM이란?
 
 
- Conditional Random Field가 뭔지?
 
- Hidden Markov Model?
 
- KL divergence?
 
- Validation set과 Test set을 나누는 이유?
val set은  평가할 때 사용하는 데이터 집합이고 test set은 실재로 모델이 새로운 정보에도 잘 적용되는지를 확인할 때 사용되는 데이터 집합입니다.
val set은 데이터가 잘 인식하는지 평가하는데 사용되고 모델은 val set에서의 평가가 높아지도록 파라미터들을 수정하기 때문에 실질적으로는 훈련에 영향을 미치지만 test set은 그렇지 않습니다.
 
- Generative model과 Discriminative model의 차이?
 
 
- Bayesian Inference?
 
- Dropout?
과적합을 방지하기 위한 정귀화 기법 중 하나입니다. 레이어의 유닛(노드, 뉴런)을 얼마나 무시할지 정하는 것 만으로 과적합이 방지된다는 점이 인상적입니다.

- Normalization 아는 것?


- Dilated CNN?

- Attention이란?

- Memory Network?

- Transformer?

- Self Attention을 활용한 다른 논문들을 아는지?

- 인상 깊었던 논문?

- Highway network?

- Elmo?

- World model?

- 요즘 Sigmoid 보다 ReLU를 많이 쓰는데 그 이유는?
https://gaussian37.github.io/math-question-q2/ ,  https://saintbinary.tistory.com/8
+ Non-Linearity라는 말의 의미와 그 필요성은?
분류 또는 회귀를 할 때, 데이터 분포에 맞는 함수나 그래프를 찾으면 모델링을 잘 했다고 평가할 수 있습니다. 보통 현실의 문제는 직선 형태를 띄는 linear한 문제보다는 non-linear한 문제가 많습니다. 
때문에 더 평가를 잘하는 모델을 만들기 위해서는 비선형을 이해하는 것이 중요합니다.
 
+ ReLU로 어떻게 곡선 함수를 근사하나?
활성함수로 ReLU를 학습에 사용하면 선형적인 부분이 여러개 이어져 전체적으로는 비선형적인 성질을 가지는 함수를 만들 수 있습니다. 이 함수의 장점이 gradient가 출력층까지 잘 전달된다는 것인데 이것 때문에 점점 곡선 함수에 근사하게 바뀝니다.

+ ReLU의 문제점은?
입력값은 0을 중심으로 분포하는데 sigmoid도 relu도 

+ Bias는 왜 있는걸까?
모든 그래프가 원점을 지나지는 않습니다. 그래프를 평행이동시키는 역할을 하고 있습니다.
학습에서는 이 값이 높아질 수록 뉴런이 활성화 하기 쉽습니다.

+ sigmoid의 문제점
특정 범위 이외는 0이나 1로만 수렴하는 값을 반환하고 이것이 반복되면 gradient 또한 0이 되어 학습이 제대로 되지 않습니다.
0이하의 입력값에 대해서 처리를 하지 못합니다.
ReLU와 비교할 때, 연산이 조금 더 복잡합니다.

- Gradient Descent에 대해서 쉽게 설명한다면?
+ 왜 꼭 Gradient를 써야 할까?
 
+ 그 그래프에서 가로축과 세로축 각각은 무엇인가?
 
+ 실제 상황에서는 그 그래프가 어떻게 그려질까?
 
+ GD 중에 때때로 Loss가 증가하는 이유는?
 
+ 중학생이 이해할 수 있게 더 쉽게 설명 한다면?
 
+ Back Propagation에 대해서 쉽게 설명 한다면?
 
 
 
- Local Minima 문제에도 불구하고 딥러닝이 잘 되는 이유는?
+ GD가 Local Minima 문제를 피하는 방법은?
 
+ 찾은 해가 Global Minimum인지 아닌지 알 수 있는 방법은?
- CNN에 대해서 아는대로 얘기하라
+ CNN이 MLP보다 좋은 이유는?
 
+ 어떤 CNN의 파라메터 개수를 계산해 본다면?
 
+ 주어진 CNN과 똑같은 MLP를 만들 수 있나?
 
+ 풀링시에 만약 Max를 사용한다면 그 이유는?
 
+ 시퀀스 데이터에 CNN을 적용하는 것이 가능할까?
 
- Word2Vec의 원리는?
+ 그 그림에서 왼쪽 파라메터들을 임베딩으로 쓰는 이유는?
 
+ 그 그림에서 오른쪽 파라메터들의 의미는 무엇일까?
 
+ 남자와 여자가 가까울까? 남자와 자동차가 가까울까?
 
+ 번역을 Unsupervised로 할 수 있을까?
 
 
- Auto Encoder에 대해서 아는대로 얘기하라
+ MNIST AE를 TF나 Keras등으로 만든다면 몇줄일까?
 
+ MNIST에 대해서 임베딩 차원을 1로 해도 학습이 될까?
 
+ 임베딩 차원을 늘렸을 때의 장단점은?
 
+ AE 학습시 항상 Loss를 0으로 만들수 있을까?
 
+ VAE는 무엇인가?
 
 
- Training 세트와 Test 세트를 분리하는 이유는?

+ Validation 세트가 따로 있는 이유는?
 
+ Test 세트가 오염되었다는 말의 뜻은?
 
+ Regularization이란 무엇인가?
 
 
 
- Batch Normalization의 효과는?
+ Dropout의 효과는?
 
+ BN 적용해서 학습 이후 실제 사용시에 주의할 점은? 코드로는?
 
+ GAN에서 Generator 쪽에도 BN을 적용해도 될까?
 
 
- SGD, RMSprop, Adam에 대해서 아는대로 설명한다면?
+ SGD에서 Stochastic의 의미는?
 
+ 미니배치를 작게 할때의 장단점은?
 
+ 모멘텀의 수식을 적어 본다면?
 
 
- 간단한 MNIST 분류기를 MLP+CPU 버전으로 numpy로 만든다면 몇줄일까?
+ 어느 정도 돌아가는 녀석을 작성하기까지 몇시간 정도 걸릴까?
 
+ Back Propagation은 몇줄인가?
 
+ CNN으로 바꾼다면 얼마나 추가될까?
 
 
- 간단한 MNIST 분류기를 TF나 Keras 등으로 작성하는데 몇시간이 필요한가?
+ CNN이 아닌 MLP로 해도 잘 될까?
 
+ 마지막 레이어 부분에 대해서 설명 한다면?
 
+ 학습은 BCE loss로 하되 상황을 MSE loss로 보고 싶다면?
 
+ 만약 한글 (인쇄물) OCR을 만든다면 데이터 수집은 어떻게 할 수 있을까?
 
 
 
- 간단한 MNIST DCGAN을 작성한다면 TF 등으로 몇줄 정도 될까?
+ GAN의 Loss를 적어보면?
 
+ D를 학습할때 G의 Weight을 고정해야 한다. 방법은?
 
+ 학습이 잘 안될때 시도해 볼 수 있는 방법들은?
 
 
- 딥러닝할 때 GPU를 쓰면 좋은 이유는?
+ 학습 중인데 GPU를 100% 사용하지 않고 있다. 이유는?
 
+ GPU를 두개 다 쓰고 싶다. 방법은?
 
+ 학습시 필요한 GPU 메모리는 어떻게 계산하는가?
 
 
 
- TF 또는 Keras 등을 사용할 때 디버깅 노하우는?
 
- Collaborative Filtering에 대해 설명한다면?
 
- AutoML이 뭐하는 걸까?
 
 
 
nn 정의
gradient descent 의 정의와 식
stochastic gradient descent 정의 그리고 장점
regression의 정의와 예시 알고리즘(linear regression 말함)
linear regression의 정의와 장점 단점, 업데이트 방법, optimal을 찾는법 (least square)
classification의 정의와 예시 (logistic regression 말함)
logistic regression의 정의와 장단점
supervised, unsupervised, semi-supervised 정의
semi-supervised가 중요한 이유
clustering 정의
clustering 예시 (k means 말함)
kmeans가 뭔지 어떻게 업데이트하는지 설명, k는 어떻게 설정하는지
kmeans의 장점과 단점(단점은 구분할 수 있는 데이터 분포가 정해져있음, 클래스 2개가 일직선으로 떨어져 있으면 kmeans로 구분 못함)
cross validation이 뭔지 (k-fold cross validation이 말하고 그걸 쓰는 이유 말함 데이터가 limit 하니까)
reinforcement learning의 정의 (reward, state, action, policy, state transition)
rl 업데이트 방법 (q-function)
q-learning이 off-policy인지 on-policy인지
non bayesian과 bayesian의 차이
non parametric learnin의 정의와 예시 (원래는 binomial이라고 했는데 이거 틀림 왜냐면 p가 필요하기 때문에. 정답은 histogram). sequential data를 표현하는 모델의 예시 (hidden markov, bayes, rnn)
rnn의 정의와 식
rnn의 장점과 단점 (vanishing gradient) 해결방법 lstm.
rnn과 hidden markov의 장단점 비교 (rnn은 파라미터 쉐어해서 표현력이 떨어지지만 end-to-end 모델이라 gradeint descent해서 optimal 찾긴 찾음)
neural network 업데이트 방법 (backpropagation)
rnn의 업데이트 방법 (time delayed backpropagation)
big one black box 모델과 neural net같은 모델 (이 두 모델을 정의하는 term이 있는데 기억이 안남)을 비교했을때 nn같은 module화된 모델의 장단점 (장점은 모델 expresivity 가 훨 좋음, 단점은 각각의 모듈과 그 모듈들의 condition을 배워야 해서 오래 걸림)
 

