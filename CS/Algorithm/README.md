# 1-2 알고리즘

+ Divide & Conquer
+ Brute-Force Search
  + Permutation
  + Combination
  + SubSet
+ Sort
  + Bubble Sort
  + Selection Sort
  + Insert Sort
  + Merge Sort
  + Quick Sort
  + Heap Sort
  + Topological Sort
+ Sieve of Eratosthenes
+ Two Pointer
+ Sliding Window
+ Binary Search
+ Dynamic Programming
  + Knapsack
  + LCS(Longest Common Subsequence)
  + LIS(Longest Increasing Subsequence)
  + Edit Distance
  + Matrix Chain Multiplication
+ Graph Search
  + DFS(Depth-First Search)
  + BFS(Breadth-First Search)
+ Minimum Spanning Tree, MST
  + Prim Algorithm
  + Kruskal Algorithm
+ 그래프 최단 경로 문제
  + Dijkstra Algorithm
  + Bellman-Ford Algorithm
  + Floyd-Warshall Algorithm

## 개요

유한한 단계를 통해 문제를 해결하기 위한 절차나 방법   
스스로는 `컴퓨터 명령문으로 작성하는 문제해결 방법` 이라고 생각한다. 몇 만개가 넘는 문제들이라도 몇 십개의 알고리즘 방법을 통해서 해결하는 경우가 많으며 개인적으로 코딩 테스트에서 가장 자주 등장하는 유형의 알고리즘은 완전탐색, 그리디, 그래프 탐색이었다.

배열, 해시, 재귀함수 등.. 스스로가 생각하기에 알고리즘보다는 컴퓨터 언어 코딩이나 자료구조에 가까운 문제들은 생략하고 작성할 것이다.

기본적인 문제 해결 과정은 다음과 같다.
1. 문제를 읽고 이해한다.   
2. 문제를 익숙한 방식으로 재구현 한다.   
   비슷한 다른 문제를 떠올리거나 그림을 그리는 등..
3. 어떤 알고리즘 혹은 주제로 해결할지 계획을 세운다.   
   똑같은 알고리즘이라도 역순으로 탐색한다던가 정렬 후에 작업하면 좋은 문제도 있다.
4. 계획을 검증한다.   
   보통은 테스트 케이스를 통해서 한다.
5. 프로그램을 구현한다.
6. 풀이를 다시보고 개선점을 찾는다.   
   혼자서는 하기 힘들기 때문에 보통 다른 사람과 스터디를 통해 해결한다.

## 빅-오 표기법

입력 크기 n이 무한대로 커질 때 시간복잡도를 간단히 표현하기 위해 사용하는 표기법으로 가장 큰 영향을 끼치는 n에 대한 계수는 생략한 `최고차항`만을 표시한다.

ex) O(3n+2) -> O(3n) -> O(n)
    O(2n^2 + 10n + 100) -> O(n^2)
    O(4) -> O(1)

일반적으로 알고리즘 문제들은 O(N) ~ O(Nlogn) 의 시간복잡도를 가지는 알고리즘을 주제로 한다.

## Brute-Force Search (완전탐색)

단어 그대로 모든 경우의 수를 탐색해보는 방법

가장 자주 출제되는 문제 유형 중 하나로 종류가 다양하지만 비슷하게 구현한다.   
가장 기본적으로 고려해야 하는 방법으로 해당 방법으로 시간초과가 일어날 것 같으면 다른 알고리즘을 고려하는 것이 알고리즘 문제 해결방법의 순서이다.

[8일차 실습 정리 필요]()

### Permutation (순열)

**서로 다른** 것들 중 몇 개를 **순서를 고려**하여 선택하는 것

서로다른 n개 중 r개를 선택하는 순열을 nPr이라고 표현한다.   
nPn = n! 로 표기하며 Factorial(팩토리얼)이라고 말한다.

n이 10개인 경우 순열의 갯수는 360만, 11인 경우에는 3990만, 12인 경우에는 4억 7천만으로, 시간초과가 생길 수 있음을 고려해서 풀어야 한다.   

일반적으로 순열을 구하는 문제는 11 이하의 수를 나열하라고 주어지는데 그 이상의 수가 주어진다면 다른 알고리즘(DP의 TSP)으로 풀어야 하는 문제이다.

### Combination (조합)

**서로 다른** 것들 중 몇 개를 **순서를 고려하지 않고** 선택하는 것

서로 다른 n개 중 r개를 선택하는 조합을 nCr이라고 표현한다. 서로 다른 n개 중 사용하지 않을 n-r개를 선택하는 것으로도 볼 수 있기 때문에 nCr = nCn-r이라는 특징이 있다!   
알고리즘을 작성할 때는 r이나 n-r 중 더 적은 수를 선택하는 쪽으로 구현하는 것이 더 빠르다!

조합은 위의 특징으로 n개 중 n/2개의 조합을 찾는 것이 가장 조합의 수가 많은데, n = 30 이고 r = 15일 때 1.5억 정도가 나오며 이 때문에 조합 문제들은 일반적으로 n이 30 이하의 수를 가진다고 한다.

### SubSet (부분 집합)

집합에 있는 원소들 중 일부를 선택해서 집합을 만드는 것   
집합의 원소가 n개일 때, 공집합을 포함한 부분 집합의 수는 2^n개 이다. (각 원소가 포함되는 경우와 포함되지 않는 경우가 있으므로)

n이 30개 정도가 되면 10억정도의 수가 되므로 30개에 대해 부분집합을 해결하는 것은 피하자;

## Greedy (탐욕법)

현재 가장 최적해라고 생각되는 방법을 진행하고 다음 작업을 할 때는 이전의 작업을 신경쓰지 않고 진행하여 최종 해답에 도달하는 방식, 대표적으로 거스름돈을 걸러주는 문제가 있다.

당장 보기에는 최적으로 보이지만 그 선택을 진행해 나가면서 만든 해답은 정답이 아닐 수도 있기 때문에 탐욕법은 빠르게 검증하는 것이 어렵고 단순하고 제한적인 문제에만 적용이 된다.   
또한 정렬된 입력값을 주거나 그렇지 않다면 탐욕법의 기준이 되는 값으로 정렬을 하고 진행하는 것이 일반적이다.

어렵게 만들면 탐욕법으로 해결하는 문제인지 알지도 못할 수 있을 정도로 어려울수록 문제 파악과 검증이 의외로 힘든 알고리즘이다. 하지만 이렇게 어려운 문제는 코테에서는 나오지 않는다고 말할 수 있을 정도로 출제되지는 않는다.

## Divide & Conquer
 
문제를 작은 문제들로 나누어 해결하는 알고리즘 기법이다.   
세 가지 과정으로 나누는데 다음과 같다.

divide(분할) : 문제를 비슷하지만 더 작은 문제들로 나눈다.
conquer(정복) : 작은 문제들을 해결한다.
combine(결합) : 작은 문제들의 답을 활용하여(혹은 모아서) 더 큰 문제를 해결한다.

분할정복 알고리즘은 단순히 문제를 나눠서 해결하자는 개념에 가까운 알고리즘이여서 해당 알고리즘을 직접 활용하여 문제를 해결하기 보다는 다른 알고리즘 기법에 적용되어 문제를 해결하는 모습을 보인다. 대표적인 분할정복을 활용하는 알고리즘의 예는 [퀵 정렬](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Algorithm#quick-sort-%ED%80%B5-%EC%A0%95%EB%A0%AC), [합병 정렬](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Algorithm#merge-sort%ED%95%A9%EB%B3%91-%EC%A0%95%EB%A0%AC), 고속 푸리에 변환 등이 있다.

## Sort (정렬)

n개의 서로 다른 수를 오름차순 혹은 내림차순으로 만드는 알고리즘이다. 정말 많은 종류의 정렬 방법이 있으므로 각각의 방법과 장단점을 기억하자.

정렬 알고리즘은 크게 시간복잡도가 O(n^2)인 것과 O(nlogn)인 것으로 나눌 수 있는데 실질적으로 전자의 알고리즘은 사용하지 않는다.

정렬 알고리즘은 따로 알고리즘 문제가 있지는 않아 필자는 하나의 정렬 문제에 다양한 알고리즘을 적용시켜 잘 돌아가는지 확인하고 넘어갔다.

### Bubble Sort (거품 정렬)

순서대로 자신과 인접한 숫자와 비교를 하고 자리를 바꿔 나가면서 정렬하는 방식, 한 번의 사이클마다 (오름차순이라면)가장 큰 숫자가 가장 마지막 자리에 있는 것을 확인할 수 있다.   
정렬을 해나갈 때마다 각 수가 자신의 자리를 항해 한 칸씩 나아가는 모습이 거품이 올라오는 것처럼 보여 거품정렬이라고 한다. 가장 간단하고도 비효율적인 정렬의 대명사로 꼽힌다.  

각 숫자들은 (n-1)번, (n-2)번, ... , 1번의 비교를 하게되므로 n(n-1)/2의 비교를 진행하게 된다.   
입력과 관계없이 O(n^2) 의 시간복잡도를 가진다.

> 위키에 있었던 거품 정렬 예시   
> <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" width=200>

#### 구현 방법 

1. 첫 번째와 두 번째 숫자를 비교하여 정렬하고 두 번째와 세 번째, ... , (n-1)번째와 n번째를 비교하여 정렬한다.
2. 위와 같은 방법을 다시 첫 번째 비교부터 (n-2) 번째 비교까지, ..., 첫 번째 비교를 하여 정렬한다. 

#### 코드

버블 정렬 코드는 아래와 같다.   

```
// bubbleSort with kotlin
// flag 변수는 속도를 조금 빠르게 하기 위해 필자 임의로 추가하였으며 없어도 무방하다.
// flag 변수로 인하여 최선인 경우 O(1)이 될 수도 있다.

fun bubbleSort(A: Array<Int>){
    var flag = 0
    for (i in 0 until A.size - 1) {
        flag = 0
        for (j in 0 until  A.size - (i+1)) {
            if (A[j] > A[j + 1]) {
                flag = 1
                val temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
            }
        }
        if (flag == 0) break
    }
}
```

### Selection Sort (선택 정렬)

정렬되지 않은 숫자들 중 가장 작은 수를 탐색하고 선택하여 자리를 바꾸는 정렬하는 방식   
숫자를 한 칸씩 이동시키는 버블 정렬과는 다르게 한 번에 한 숫자를 올바른 위치로 바로 옮겨주는 특징이 있다.

 거품 정렬과 같은 이유로 O(n^2) 의 시간복잡도를 가진다.   
 하지만 숫자를 올바른 위치로 한 번에 옮겨주기 때문에 항상 거품 정렬보다는 빠르다.

> 위키에 있었던 선택 정렬 예시   
> <img src="https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif" height=300>

#### 구현 방법 

1. 숫자들 중 가장 작은 수를 탐색한다.
2. 1에서 찾은 가장 작은 수를 가장 첫 번째 위치의 숫자와 자리를 바꾼다.
3. 정렬이 되지 않은 숫자들을 대상으로 1~2과정을 통해 가장 작은 수를 찾아내고 자리를 교환해나간다.

#### 코드

```
// selectionSort with kotlin

fun selectionSort(A: Array<Int>){
    var indexMin: Int
    var temp: Int

    for (i in 0 until A.size - 1) {
        indexMin = i
        for (j in i + 1 until A.size) 
            if (A[j] < A[indexMin]) indexMin = j
        temp = A[indexMin]
        A[indexMin] = A[i]
        A[i] = temp
    }
}
```

### Insert Sort (삽입 정렬)

이미 정렬된 숫자들과 정렬되지 않은 숫자들로 나누고 정렬되지 않은 숫자들 중 하나를 골라 정렬된 숫자들 중 올바른 위치에 숫자를 삽입하는 정렬 방식

이미 정렬이 되어있는 숫자를 정렬하는 경우를 최선, 역순으로 정렬되어있는 수를 정렬하는 경우가 최악으로 최선의 경우 O(n), 최악의 경우 O(n^2) 의 시간복잡도를 가진다.   
거품 정렬보다는 항상 빠르고, 평균적으로 선택 정렬보다 빠르지만 특정한 상황(내림차순을 오름차순으로 정렬하는 경우 등)에서는 더 느리다.

> 위키에 있었던 삽입 정렬 예시   
> <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Insertion_sort_001.PNG" height=500>

#### 구현 방법 

1. 가장 첫 숫자를 정렬된 숫자로, 두 번째부터 마지막까지 정렬되지 않은 숫자들로 간주한다.
2. 정렬되지 않은 숫자들 중 가장 왼쪽 하나를 골라서 정렬된 숫자들과 차례로 비교하면서 정렬을 해나간다.
3. 2번의 작업을 정렬되지 않은 숫자들이 없어질 때까지 반복한다.

#### 코드

```
// insertSort with kotlin

fun insertSort(A: Array<Int>){
        for (index in 1 until A.size) {
            val temp: Int = A[index]
            var aux = index - 1
            while (aux >= 0 && A[aux] > temp) {
                A[aux + 1] = A[aux]
                aux--
            }
            A[aux + 1] = temp
        }
    }
```

### Merge Sort(합병 정렬)

[분할 정복 알고리즘](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/DataStructure#Divide-&-Conquer)을 활용한 정렬 방법으로 정렬할 리스트가 1개가 될 때 까지 부분 리스트로 분할하였다가 합병을 진행하면서 정렬을 하는 방식이다.   
나뉘는 부분리스트의 개수에 따라서 n-way 합병 정렬이라고도 하며 기본적으로는 2-way 합병 정렬을 사용한다.

일관적으로 O(nlog n)의 시간복잡도를 가진다.

> 위키에 있었던 합병 정렬 예시   
> <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif" width=300>

#### 구현 방법 

1. 정렬되지 않은 숫자들을 1개가 될 때까지 나눈다. (숫자가 1개인 리스트는 정렬된 것과 같으므로)
2. 다른 리스트와 숫자를 하나씩 비교하여 합병을 진행하면서 정렬한다.
3. 리스트가 하나만 남을 때 까지 2를 반복한다. 

#### 코드

```
// mergeSort with kotlin

// A: 정렬하고 싶은 리스트, tempA: A리스트의 복사본, low/high: 정렬하고 싶은 범위(low와 high 포함)
// A 리스트 자체를 정렬시킨다.

fun mergeSort(A: Array<Int>, tempA: Array<Int>, low: Int, high: Int){
    if (low >= high) return

    val mid = (low + high) / 2
    mergeSort(A, tempA, low, mid)
    mergeSort(A, tempA, mid+1, high)

    var leftIdx = low
    var rightIdx = mid+1
    var tempIdx = low
    while (tempIdx <= high){
        when {
            leftIdx > mid -> {
                tempA[tempIdx] = A[rightIdx]
                rightIdx += 1
            }
            rightIdx > high -> {
                tempA[tempIdx] = A[leftIdx]
                leftIdx += 1
            }
            A[leftIdx] < A[rightIdx] -> {
                tempA[tempIdx] = A[leftIdx]
                leftIdx += 1
            }
            else -> {
                tempA[tempIdx] = A[rightIdx]
                rightIdx += 1
            }
        }

        tempIdx += 1
    }

    for (i in low..high) A[i] = tempA[i]
}
```

위의 2-way 탑다운(top-down)방법 이외에도 많은 구현 방법이 있다.   


#### 백준 문제 풀이

[1838번 버블 정렬](https://www.acmicpc.net/problem/1838)     
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/1838.kt   
백준 풀이 공유 링크 : http://boj.kr/924fd08cd40c43cda9125313816e5157

이름은 버블 정렬이라고 적혀있지만 합병 정렬과 버블 정렬의 작동 원리를 확실히 알고 있어야 해결할 수 있는 문제이다.   
문제 해결을 위한 코드 생성보다 코드 생성을 위한 해결 방법을 고안하는 쪽이 훨씬 더 어려운 문제이다.   
필자는 문제 해결에 좀 많이 해매었지만 성취감도 있었고 기초를 확실히 다지는 문제같아 개인적으로는 좋은 문제라고 생각한다!👍

### Quick Sort (퀵 정렬)

[분할 정복 알고리즘](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/DataStructure#Divide-&-Conquer)을 활용하는 정렬 알고리즘이다. 사용자가 지정한 임의의 pivot을 기준으로 큰 값과 작은 값들을 분할하여 정렬을 진행하는 방식이다.   
정렬을 진행할 때 마다 1개의 숫자가 자신의 자리를 찾는다는 특징이 있다.

사용자가 지정한 pivot이 리스트들의 최소값 혹은 최대값인 경우가 최악의 경우이며 중앙값인 경우가 최선의 경우가 된다. 최선의 경우 O(n), 최악의 경우 O(n^2) 의 시간복잡도를 가진다.   

#### 구현 방법 

1. pivot이 되는 숫자를 하나 지정한다.
2. pivot을 기준으로 작거나 같은 수를 왼쪽 파티션, 큰 수를 오른쪽 파티션으로 보낸다.
3. 모든 수가 정렬될 때 까지 1~2를 반복한다.

#### 코드

```
// quickSort with kotlin

// A: 정렬하고 싶은 리스트, start/end: 정렬하고 싶은 범위(start와 end 포함)
// A 리스트 자체를 정렬시킨다.

fun quickSort(A: Array<Int>, start: Int, end: Int){
    val pivot = A[start]
    var left = start+1
    var right = end

    while (true){
        while (left <= right && A[left] <= pivot) left += 1
        while (left <= right && pivot <= A[right]) right -= 1

        if (left > right) break
        val temp = A[left]
        A[left] = A[right]
        A[right] = temp
    }

    A[start] = A[right]
    A[right] = pivot

    if (right - start > 2) quickSort(A, start, right-1)
    if (end - right > 2) quickSort(A, right+1, end)
}
```

#### 활용

정렬에도 쓰이지만 특정 원소를 기준으로 큰 값과 작은 값을 나눈다는 특징을 활용하여 n개의 데이터 중에서 k번째 원소를 찾는데 해당 알고리즘이 좋은 방안이 되기도 한다.

### Heap Sort (힙 정렬)

최소 힙(min heap) 혹은 최대 힙(max heap)을 활용한 정렬 알고리즘   
[자료구조의 힙](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/DataStructure#heap)을 숙지하고만 있다면 바로 적용할 수 있는 알고리즘이다.

힙의 특징을 그대로 이어받아 비어있는 힙에 원소를 삽입하고 하나씩 원소를 빼면서 생기는 heapify를 진행하는 시간복잡도 O(nlogn)을 가진다.   

로그를 계산하는 계산법에 의해서 O(nlogn)이 나온다고 하는데 이해를 못해서 필자는 단순히 n개의 데이터를 삽입/삭제하는데 O(logn)의 수행시간이 걸리는 최대/최소 힙을 활용하므로 O(nlogn) 시간복잡도라고 단순하게 생각하였다.

#### 구현 방법 

힙만 구현할 수 있다면 별도로 필요한 알고리즘은 없다.

#### 코드

```
// heapSort with kotlin


```

### Topological Sort (위상 정렬)



#### 구현 방법 

1. 

#### 코드

```
// topologicalSort with kotlin


```

## Sieve of Eratosthenes



## Two Pointer



## Sliding Window



## Binary Search

**정렬이 되어있는** 데이터들의 중앙에 있는 키 값을 기준으로 다음 검색의 위치를 결정하고 탐색을 진행하는 방법이다.

과정은 다음과 같다.

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 중앙 원소의 값과 찾고자 하는 목표 값이 일치하면 탐색을 마친다.
4. 목표 값이 중앙 원소의 값보다 작으면 왼쪽 데이터들을, 크다면 오른쪽 데이터들에 대해 탐색을 진행한다.
5. 원하는 값을 찾을 때 까지 위의 과정을 반복한다.

## Dynamic Programming


## Graph Search

그래프는 기본적으로 노드와 간선에 대한 순서나 규칙이 없다.   
때문에 그래프를 탐색할 때에는 모든 노드를 살펴야 하는 경우가 매우 많은데 그 방법은 아래의 두 알고리즘(DFS, BFS)을 기반으로 한다.

### DFS(Depth-First Search)
  
깊이 우선 탐색으로 불리며 stack을 사용하여 구현한다.   
시간 복잡도는 모든 노드와 간선을 조사하므로 O(V+E)이다.   
공간 복잡도는 각 노드에 방문 여부를 채크할 변수 크기 즉, O(V)이다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Depth-First-Search.gif/330px-Depth-First-Search.gif" width="200">
위키백과에 있던 깊이 우선 탐색 애니메이션 예시
  
### BFS(Breadth-First Search)

너비우선탐색이라고 불리며 깊이우선탐색과 마찬가지의 이유로 시간 복잡도는 O(V+E), 공간 복잡도는 O(V)이다.

시작 노드와 목표로 하는 노드를 정하고 시작 노드부터 너비 우선 탐색을 진행하였을 때   
**너비 우선 탐색을 적용하여 찾은 두 노드의 경로는 항상 최단거리이다.**

<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif" width="200">

</br>

## Minimum Spanning Tree, MST (최소 신장 트리)

그래프가 가진 간선의 일부 혹은 전체를 이용하여 그 그래프의 모든 노드를 잇는 트리(**비순환** 유향 그래프)를 <code>신장 트리(Spanning Tree)</code>라고 한다.\
가중치 그래프에서 **만들 수 있는 신장 트리 중 사용한 간선의 가중치 합이 가장 적은 것**를 최소 신장 트리라고 한다.\
간선의 가중치가 이 최소 신장 트리를 만드는 알고리즘은 대표적으로 2개가 있는데 아래와 같다.

### 1. Prim Algorithm (프림 알고리즘)

그래프에서 만들 수 있는 작은 트리를 점차 확장시켜 결국에는 최소 신장 트리를 만드는 방법

#### 동작 방식

1. 시작 노드를 선택한다. (시작 노드는 그래프 내 어떤 노드라도 상관없다.)
2. 가지고 있는 노드와 연결된 간선 중 (이미 사용한 간선을 제외하고 사이클이 되지 않는) 가장 가중치가 작은 값을 가지는 간선을 골라 잇는다.
3. 모든 노드와 이어질 때까지 2번을 반복한다.
4. 반복이 끝났을 때 그려진 트리가 최소 신장 트리이다.

#### 특징

1. 인접행렬로 구현시 시간 복잡도 O(V^2)를 가지며 힙을 사용하면 O(E log V)의 시간 복잡도를 가진다.

#### 예시 사진

<img src="../image/1.1%20Graph11.PNG" width="45%" height="60%">
<img src="../image/1.1%20Graph12.PNG" width="60%" height="60%">

### 2. Kruskal Algorithm (크루스칼 알고리즘)

탐욕법(Greedy) 알고리즘을 기본으로 하면서 사이클이 만들어 지지 않도록 조건을 두어 간선을 선택해 나가는 방법   
원래 탐욕법은 당장에는 최적이지만, 전체적인 관점에서 최적이라는 보장이 없기 때문에 반드시 검증해야 하지만   
다행히 Kruskal 알고리즘은 최적의 해답을 주는 것으로 증명되어 있다고 한다.

해당 알고리즘을 사용할 때 반드시 사이클 여부를 확인하는 Disjoint-set(Union-Find) 알고리즘이 부가적으로 필요하다.   
간단히 설명하자면 각 노드에 id를 부여하여 같은 트리에 속하는지 아닌지 파악하고   
간선이 생겨 두 트리가 연결될 때 빠르게 id를 통합시키는 알고리즘이다.

#### 동작 방식

1. 그래프의 각 노드에 번호(id)를 부여한다. 이는 각 노드의 그룹에 대한 정보이다.
2. 그래프의 모든 간선들을 가중치의 오름차순으로 정렬한다.
3. 정렬된 간선을 차례로 보면서 해당 간선을 추가 했을 때 양 노드의 그룹 정보를 Disjoint-set 알고리즘으로 확인하여 사이클 여부를 확인한다.
4. 두 노드가 같지 않은 그룹(사이클 생성이 안되면)이면 Disjoint-set의 병합과정을 거쳐 두 그룹을 합친다.
5. 같은 그룹이라면 다음 간선을 선택한다.
6. 간선의 개수가 '노드의 개수 - 1'이 될 때까지 2~5를 반복한다.

#### 특징

1. 시간복잡도는 O(E log V) 혹은 O(E log E)이다. (위키백과에 증명이 되어있지만 너무 어려워서 외우기만..)

#### 예시 사진

<img src="../image/1.1%20Graph13.PNG" width="70%" height="70%">

#### 참고

  + https://www.codeground.org/common/popCodegroundNote

</br>

## 그래프 최단 경로 문제

### 1. Dijkstra Algorithm (다익스트라 알고리즘)

**음의 가중치가 없는 그래프에서 사용해야한다**는 조건이 있다.   
한 노드에서 다른 모든 노드까지의 최단거리를 구하는 알고리즘이다.

#### 구현 방법

아래의 예시 사진을 참고하면서 보는 것을 추천한다.

0. 배열의 A번째 값을 d[A]라고 하고 A와 B사이의 간선을 P[i][j]라고 하겠다.
1. 최단거리를 저장할 배열을 만든다. 시작 노드의 배열 값은 0을, 그 외에는 매우 큰 값을 넣어 초기화한다.
2. 배열에서 이미 **탐색한 노드**를 제외하고 가장 작은 값을 가지는 노드를 가져온다.   
  가장 작은 값을 가지는 노드는 힙(을 활용해서 만든 우선순위 큐)이나 배열을 이용해서 구한다.
3. 가져온 노드를 A라고 하고 A와 인접한 노드를 B라고 할 때, d[B]와 d[A]+P[A][B]를 비교해서 더 작은 값을 d[B]에 넣는다.   
  A의 모든 이웃 노드 B에 대해 이 작업을 수행한다.
4. A의 상태를 **탐색한 노드**로 바꾼다.
5. 목표 노드가 "방문 완료" 상태가 되거나 더 이상 미방문 상태의 노드를 선택할 수 없을 때까지 2~4의 과정을 반복한다.

#### 특징

1. 가장 작은 값을 가진 노드를 가져올 때   
인접행렬로 구현시 시간 복잡도 O(V^2)를 가지고 (최대)힙(Heap)을 활용하면 O((V+E)logV)의 시간 복잡도를 가진다.

선택한 노드를 힙에 넣고 정렬하는데 O(logV), 노드마다 한번씩은 힙에 들어가므로 O(V) => O(VlogV)의 시간에
각 노드마다 이웃한 노드의 최단 거리를 탐색하고 O(E), 그 정보를 갱신하기 위해 힙을 탐색하는데 O(logV)가 필요하므로 => O(ElogV)
즉, O((E+V)logV)가 필요하다.

2. 시작 노드에서 목표 노드까지의 최단거리를 구하는 과정에서 시작 노드와 그 외의 노드 간의 최단거리까지 구해버린다.

#### 예시 사진

<img src="../image/1.1%20Graph14.gif" width="40%" height="40%">

*마지막에 노드 4의 값(20)과 '5-4 간선+노드 5의 값'(26)을 비교해야 할 것 같은데 안하는 것으로 보아 목표노드가 5인것 같다.*

#### 활용 예시

1. 네비게이션 길찾기
2. 지하철 최단거리
3. 네트워크 경로찾기

</br>

### 2. Bellman-Ford Algorithm (벨만-포드 알고리즘)

**음의 가중치가 있는 그래프에서도 사용이 가능**하며 **음의 사이클을 감지할 수 있다.**   
기능은 위의 다익스트라 알고리즘과 같다.

#### 동작 방식

0. 배열의 A번째 값을 d[A]라고 하고 A와 B사이의 간선을 P[i][j]라고 하겠다.
1. 다익스트라와 같이 최단거리를 저장할 배열을 만든다. 시작 노드의 배열 값은 0을, 그 외에는 매우 큰 값을 넣어 초기화한다.
2. 간선이 노드A와 B를 잇는다고 할 때, d[B]와 d[A]+P[A][B]를 비교해서 더 작은 값을 d[B]에 넣는다.   
  모든 간선에 대하여 위의 작업을 해준다.
3. 2번의 작업을 V번 해준다.
4. 만약 V번째에도 갱신이 되는 노드가 있다면 음수 사이클이 있다는 의미이다. (음수 사이클이 없다면 N-1내에 모든 노드가 최단 경로를 가진다.)

##### 특징

1. 시간복잡도는 O(EV)이다. 모든 간선을 V번 살펴보기 때문이다.   
   밀집 그래프일수록 느려지며 최악의 경우 E=V(V-1)/2로, O(V^3)의 속도를 가진다.
3. 다익스트라 알고리즘보다 느리다.
4. 음수 가중치가 있는 그래프에서도 사용 가능하다.
5. 음수 사이클이 존재하는지 판별이 가능하다.

#### 예시 사진

order에 적힌 순서로 간선을 탐색한다.

<img src="../image/1.1%20Graph15.png" width="60%" height="60%">
<img src="../image/1.1%20Graph16.png" width="60%" height="60%">

</br>

### 3. Floyd-Warshall Algorithm (플로이드-워셜 알고리즘)

**음의 가중치가 있는 그래프**에서 **모든 노드에서 다른 모든 노드까지의 최단 경로**를 구하기 위해 고안되었다.   
이해가 완벽히 되지는 않지만 이해가 된 부분만 글로 남겨보자면   
그래프 상의 한 노드부터 다른 노드까지의 최단 경로를 부분적으로 계산해나가 결국에는 최단거리를 구하는 알고리즘이다.

#### 동작 방식

모든 정점쌍 (i,j)에 대하여 k라는 경유지를 거쳤을 때, 기존의 정점쌍의 거리보다 짧아진다면, 정점쌍의 최단거리를 갱신시켜준다.   
모든 최단거리는 음수 사이클이 없다면, 그 경로의 길이는 당연히 N이하가 되고 이를 이용해 동적계획법으로 해결 가능하다.   

#### 특징

1. 시간복잡도는 O(V^3)이다. 모든 정점쌍과 경유지 모두 V개 이기 때문
2. 음수 가중치가 있는 그래프에서 사용 가능하다.
3. 그래프 상의 두 노드 사이의 최단 거리를 모두 구한다.

#### 참고

+ https://data-make.tistory.com/394

</br>

### 경로 종류별 사용 알고리즘
  + 시작 노드 하나, 도착 노드 하나   
  Dijkstra 알고리즘, Bellman-Ford 알고리즘 
  + 시작 노드 하나, 도착 노드 전체   
  위와 동문
  + 시작 노드 전체, 도착 노드 하나   
  그래프의 에지 방향을 모두 반대로 바꾸면 시작 노드 하나, 도착 노드 전체 문제로 바뀐다. 즉, 위와 동문
  + 시작 노드 전체, 도착 노드 전체   
  Dijkstra 알고리즘, Bellman-Ford 알고리즘의 도착/시작 노드를 모든 노드에 적용한다. 혹은 Floyd-Warshall Algorithm 사용

</br>

