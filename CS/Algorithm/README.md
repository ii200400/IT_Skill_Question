# 1-2 알고리즘

+ Sort
  + Bubble Sort
  + Selection Sort
  + Insert Sort
  + Merge Sort
  + Quick Sort
  + Topological Sort
+ Sieve of Eratosthenes
+ Divide & Conquer
+ Binary Search
+ Graph Search
  + DFS(Depth-First Search)
  + BFS(Breadth-First Search)
+ Dynamic Programming
  + Knapsack

## Sort (정렬)

n개의 서로 다른 수를 오름차순 혹은 내림차순으로 만드는 알고리즘이다. 정말 많은 종류의 정렬 방법이 있으므로 각각의 방법과 장단점을 기억하자.

정렬 알고리즘은 크게 시간복잡도가 O(n^2)인 것과 O(nlogn)인 것으로 나눌 수 있는데 실질적으로 전자의 알고리즘은 사용하지 않는다.

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

### Merge Sort(병합 정렬)

[분할 정복 알고리즘](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/DataStructure#Divide-&-Conquer)을 활용한 정렬 방법   
나뉘는 부분리스트의 개수에 따라서 n-way 병합 정렬이라고도 하며 기본적으로는 2-way 병합 정렬을 사용한다.

일관적으로 O(nlog n)의 시간복잡도를 가진다.

> 위키에 있었던 병합 정렬 예시   
> <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif" width=300>

#### 구현 방법 

1. 정렬되지 않은 숫자들을 1개가 될 때까지 나눈다. (숫자가 1개인 리스트는 정렬된 것과 같으므로)
2. 다른 리스트들과 숫자를 하나씩 비교하여 병합을 진행한다.
3. 리스트가 하나만 남을 때 까지 2를 반복한다. 

#### 코드

```

```

### Quick Sort (퀵 정렬)

#### 구현 방법 

1. 

#### 코드

```

```

### Quick Sort (퀵 정렬)


#### 구현 방법 

1. 

#### 코드

```

```

### Topological Sort (위상 정렬)

#### 구현 방법 

1. 

#### 코드

```

```

## Divide & Conquer
 
문제를 작은 문제들로 나누어 해결하는 알고리즘 기법이다.   
세 가지 과정으로 나누는데 다음과 같다.

divide(분할) : 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
conquer(정복) : 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
combine(결합) : 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다. 이때 정렬 결과가 임시배열에 저장된다.


## Sieve of Eratosthenes






