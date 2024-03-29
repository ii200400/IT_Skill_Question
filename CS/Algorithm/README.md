# 1-2 알고리즘

`목차`

* [개요](#개요)
* [빅-오 표기법](#빅-오-표기법)
* [Brute-Force Search (완전탐색)](#brute-force-search-완전탐색)
  + [Permutation (순열)](#permutation-순열)
  + [Combination (조합)](#combination-조합)
  + [SubSet (부분 집합)](#subset-부분-집합)
* [BitMask (비트마스크)](#bitmask-비트마스크)
  + [코드 (Next Permutation)](#코드-next-permutation)
* [Backtracking (백트래킹)](#backtracking-백트래킹)
* [Greedy (탐욕법)](#greedy-탐욕법)
* [Divide & Conquer](#divide--conquer)
* [Sort (정렬)](#sort-정렬)
  + [Bubble Sort (거품 정렬)](#bubble-sort-거품-정렬)
  + [Selection Sort (선택 정렬)](#selection-sort-선택-정렬)
  + [Insert Sort (삽입 정렬)](#insert-sort-삽입-정렬)
  + [Merge Sort(합병 정렬)](#merge-sort-합병-정렬)
  + [Quick Sort (퀵 정렬)](#quick-sort-퀵-정렬)
  + [Heap Sort (힙 정렬)](#heap-sort-힙-정렬)
  + [Topological Sort (위상 정렬)](#topological-sort-위상-정렬)
* [Sieve of Eratosthenes](#sieve-of-eratosthenes)
* [Two Pointer](#two-pointer)
* [Sliding Window](#sliding-window)
* [Binary Search](#binary-search)
* [Graph Search](#graph-search)
  + [DFS(Depth-First Search)](#dfsdepth-first-search)
  + [BFS(Breadth-First Search)](#bfsbreadth-first-search)
* [Minimum Spanning Tree, MST (최소 신장 트리)](#minimum-spanning-tree-mst-최소-신장-트리)
  + [1. Prim Algorithm (프림 알고리즘)](#1-prim-algorithm-프림-알고리즘)
  + [2. Kruskal Algorithm (크루스칼 알고리즘)](#2-kruskal-algorithm-크루스칼-알고리즘)
    - [Disjoint-set (서로소 집합)](#disjoint-set-서로소-집합)
    - [빠른 대표자 확인](#빠른-대표자-확인)
* [그래프 최단 경로 문제](#그래프-최단-경로-문제)
  + [1. Dijkstra Algorithm (다익스트라 알고리즘)](#1-dijkstra-algorithm-다익스트라-알고리즘)
  + [2. Bellman-Ford Algorithm (벨만-포드 알고리즘)](#2-bellman-ford-algorithm-벨만-포드-알고리즘)
  + [3. Floyd-Warshall Algorithm (플로이드-워셜 알고리즘)](#3-floyd-warshall-algorithm-플로이드-워셜-알고리즘)
  + [경로 종류별 사용 알고리즘](#경로-종류별-사용-알고리즘)
* [Dynamic Programming (다이나믹 프로그래밍)](#dynamic-programming-다이나믹-프로그래밍)
  + [최적 부분문제 구조 (Optimal substructure)](#최적-부분문제-구조-optimal-substructure)
  + [중복 부분문제 구조 (Overlapping subproblems)](#중복-부분문제-구조-overlapping-subproblems)
  + [memoization (메모이제이션)](#memoization-메모이제이션)
  + [knapsack (배낭)](#knapsack-배낭)
  + [LIS(Longest Increasing Subsequence, 최장 증가 수열)](#lislongest-increasing-subsequence-최장-증가-수열)
    - [이진탐색 활용](#이진탐색-활용)
  + [LCS(Longest Common Subsequence)](#lcslongest-common-subsequence)
  + [Edit Distance](#edit-distance)
  + [Matrix Chain Multiplication](#matrix-chain-multiplication)
* [Pattern Matching (문자열 패턴 매칭)](#pattern-matching-문자열-패턴-매칭)
  + [Rabin-karp (라빈-카프)](#rabin-karp-라빈-카프)
  + [Boyer Moore (보이어-무어)](#boyer-moore-보이어-무어)
  + [KMP](#kmp)

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

라고는 쓰여있지만.. 솔직히 잘 모르겠다. 
시간/공간 복잡도를 계산하고 알고리즘 중 어떤 것을 사용할지 고민도 하지만, 어떤 방법으로 문제가 해결될 것 같아 문제를 푼 다음 알고보니 00알고리즘인 것을 알아차리는 경우도 꽤 있기 때문이다. 즉, 신경은 쓰지만 스스로 잘하고 있는지 잘 모르겠다. ^ㅠ^

해당 글은 Codeground Note와 본인이 들은 멀티캠퍼스 강의를 참고하여 작성하였다.

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

완전탐색이라고 하면 대표적으로 순열, 조합, 부분집합을 구하는 알고리즘이 있는데 필자는 그것을 정리할 예정이다.

### 문제 풀이

[백준 2563번 색종이](https://www.acmicpc.net/problem/2563)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2563/Main.java     
백준 풀이 공유 링크 : http://boj.kr/af6571d60d8a440886a3b67d11d98bc7

[백준 2567번 색종이 - 2](https://www.acmicpc.net/problem/2567)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2567/Main.java     
백준 풀이 공유 링크 : http://boj.kr/1bf00512f7d64d869651ac3568de7f05

### Permutation (순열)

**서로 다른** 것들 중 몇 개를 **순서를 고려**하여 선택하는 것

서로다른 n개 중 r개를 선택하는 순열을 nPr이라고 표현한다. 식으로 표현하면 아래와 같다.   
nPr = n * (n - 1) * … * (n - r + 1) = n! / (n - r)!

여기에서 r이 n이라면 nPn = n! 로 표기하며 n-Factorial(팩토리얼)이라고 말한다.   
n과 r이 10개인 경우 순열의 개수는 360만, 11인 경우에는 3990만, 12인 경우에는 4억 7천만으로, 시간초과가 생길 수 있음을 고려해서 풀어야 한다.   

일반적으로 순열을 구하는 문제는 11 이하의 수를 나열하라고 주어지는데 그 이상의 수가 주어진다면 다른 알고리즘(DP의 TSP)으로 풀어야 하는 문제이다.

순열은 아래와 같이 재귀를 활용하여 해결하는 것이 일반적이며 r의 값이 매우 작다면(3이하) for문으로 해결하는 것도 방법이다.   
이미 선택한 값도 자주 방문하게 되기 때문에 방문체크를 할 배열이 꼭 필요한 것을 잊지 말자.

#### 코드

```
// Permutation with Java

// nPr로 표현되는 순열을 구현하기 위해 사용하는 코드
// r=2로 고정되어다면 단순히 이중 for문을 사용하는 것이 연산과 구현이 더 빠르다.
// 그렇지 않으면 재귀함수를 사용하는 것이 좋다.

public class Permutation {

    static int N, R;
    static int[] input, numbers;
    static boolean[] v;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();   // 전체 숫자 개수
        R = sc.nextInt();   // 고를 숫자의 개수
        input = new int[N]; // 입력 받은 N개의 숫자 배열
        numbers = new int[R];   // 선택한 R개의 숫자 배열 (순열)
        v = new boolean[N];     // 선택 여부

        //input data 입력 받기
        for(int i = 0; i < N; i++) {
            input[i] = sc.nextInt();
        }

        //순열 생성
        perm(0);
    }

    // 순열 만들기
    static void perm(int idx) { //idx 현재 자리
        // R개를 선택했다면 선택한 숫자 출력
        if(idx == R) {
            System.out.println(Arrays.toString(numbers));
            return;
        }

        // 모든 자리의 수를 선택해 보는데
        for(int i =0; i < N; i++) {

            // 이미 해당 수를 선택했다면 다음 수를 탐색한다.
            if(v[i]) {
                continue;
            }

            // 현재 자리의 숫자를 선택함
            numbers[idx] = input[i];
            v[i] = true;

            // 다음 수 뽑으러 가기
            perm(idx + 1);

            // 이번에는 선택하지 않고 진행해본다.
            v[i] = false; // 백트래킹에서 원상 복구
        }
    }
}
```

#### 문제 풀이

[백준 15654번 N과 M (5)](https://www.acmicpc.net/problem/15654)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java15654/Main.java   
백준 풀이 공유 링크 : http://boj.kr/f8f284fee352495cabc463ffa7aed3b0

[SWEA 1247. [S/W 문제해결 응용] 3일차 - 최적 경로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/ssafy/swea/java1247/Solution.java

[SWEA 6808. 규영이와 인영이의 카드게임](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/ssafy/swea/java6808/Solution.java

### Combination (조합)

**서로 다른** 것들 중 몇 개를 **순서를 고려하지 않고** 선택하는 것

서로 다른 n개 중 r개를 선택하는 조합을 nCr이라고 표현한다. 서로 다른 n개 중 사용하지 않을 n-r개를 선택하는 것으로도 볼 수 있기 때문에 nCr = nCn-r이라는 특징이 있다! 이러한 특징으로 알고리즘을 작성할 때는 r이나 n-r 중 더 적은 수를 선택하는 쪽으로 구현하는 것이 더 빠르다!

같은 이유로 n개 중 n/2개의 조합을 찾는 것이 가장 조합의 수가 많은데, n = 30 이고 r = 15일 때 1.5억 정도가 나오며 이 때문에 조합 문제들은 일반적으로 n이 30 이하의 수를 가진다고 한다.

순열과 마찬가지로 같이 재귀를 활용하여 해결하는 것이 일반적이며 r의 값이 매우 작다면(3이하) for문으로 해결하는 것도 좋다.   
하지만 순열과는 다르게, 이미 선택한 값에 방문하지 않기 때문에 방문체크를 할 배열을 사용하지 않는다.

#### 코드

```
// Combination with Java

public class Combination {

    static int N,R;
    static int[] input, numbers;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();   // 전체 숫자 개수
        R = sc.nextInt();   // 고를 숫자의 개수
        input = new int[N]; // 입력 받은 N개의 숫자 배열
        numbers = new int[R];   // 선택한 R개의 숫자 배열 (조합)

        //input data 입력 받기
        for(int i = 0; i<N; i++){
            input[i] = sc.nextInt();
        }
        
        // 조합 시작
        combination(0, 0);
    }

    // 조합 만들기
    static void combination(int cnt, int start){
        // R개를 선택했다면 선택한 숫자 출력
        if (cnt == R){
            System.out.println(Arrays.toString(numbers));
            return;
        }

        // 이전에 선택한 숫자를 기준으로 탐색 재개
        for (int i = start; i<N; i++){
            // i번째 숫자를 선택하고
            numbers[cnt] = input[i];
            // i+1번째부터 다음 숫자를 선택하는 것을 진행한다.
            combination(cnt+1, i+1);
        }
    }
}
```

#### 문제 풀이

[백준 15655번 N과 M (6)](https://www.acmicpc.net/problem/15655)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java15654/Main.java   
백준 풀이 공유 링크 : http://boj.kr/953d1a6be3a346389ecf0a9a186b0335

[백준 2798번 블랙잭](https://www.acmicpc.net/problem/2798)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2798/Main.java   
백준 풀이 공유 링크 : http://boj.kr/c35d1dc92c564dfbae9be314a1aefa5d

### SubSet (부분 집합)

집합에 있는 원소들 중 일부를 선택해서 집합을 만드는 것   
집합의 원소가 n개일 때, 공집합을 포함한 부분 집합의 수는 2^n개 이다. (각 원소가 포함되는 경우와 포함되지 않는 경우가 있으므로)   
n이 30개 정도가 되면 10억정도의 수가 되므로 30개에 대해 부분집합을 해결하는 것은 피하자;

순열, 조합과 같이 재귀로 아래와 같이 구현한다.

#### 코드

```
// SubSet with Java

public class SubSet {

    static int N;
    static int[] input;
    static boolean[] isSelected;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 초기화
        N = sc.nextInt();   // 집합의 원소 수
        input = new int[N];   // 부분 집합 배열
        isSelected = new boolean[N];    // 부분집합 선택 여부
        for (int i = 0; i<N; i++){
            input[i] = sc.nextInt();
        }

        // 부분 집합 시작
        generateSubset(0);
    }

    // 부분 집합 만들기
    static void generateSubset(int cnt){ // 집합의 인덱스
        // 부분 집합을 완성했다면
        if (cnt == N){
            // 부분집합 출력
            for (int i = 0; i<N; i++){
                System.out.print( isSelected[i]? input[i] + " " : "");
            }
            System.out.println();
            return;
        }

        // cnt 인덱스의 요소를 선택하고 다음 요소로 넘어가는 경우와
        isSelected[cnt] = true;
        generateSubset(cnt+1);

        // 선택하지 않고 다음 요소로 넘어가는 경우를 탐색
        isSelected[cnt] = false;
        generateSubset(cnt+1);
    }
}
```

#### 문제 풀이

[백준 1961번 도영이가 만든 맛있는 음식](https://www.acmicpc.net/problem/2961)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2961/Main.java   
백준 풀이 공유 링크 : http://boj.kr/6c2fa4c2698f45bf8291952721c04d8a

## BitMask (비트마스크)

비트 연산자를 알고리즘에 활용하는 기술이다.   

단순히 boolean 배열을 대체하는 정도라면 크게 도움이 되지 않지만 특정 연산에서는 큰 도움이 된다고 한다. 바이너리 카운팅 혹은 NextPermutation 등의 알고리즘 기법에 활용된다.

NP, NC(NextPermutation, NextCombination)는 순열 및 조합을 생성할 때 재귀적으로 구현하지 않고 각 인덱스 값을 비교하여 수를 선택하는 모든 경우 수를 찾는 알고리즘이다. 재귀로 구현하는 방식보다 빠르다는 특징이 있으나 상대적으로 이해하기 힘들다는 단점이 있다.

### 코드 (Next Permutation)

```
// NP with Java

public class NextPermutation {
    static int[] input;
    static int N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        input = new int[N];

        for (int i = 0; i<N; i++){
            input[i] = sc.nextInt();
        }

        // 0. 오름차순 정렬
        Arrays.sort(input);  //제일 작은 순열이 무조건 하나 만들어진다.

        long start = System.nanoTime();
        do {
            // 순열 하나씩 출력
           System.out.println(Arrays.toString(input));
        }while (np());
        long end = System.nanoTime();

        System.out.println(end-start);
    }

    private static boolean np(){

        // 1. 교환할 숫자의 위치 찾기 (역순 탐색)
        int i = N-1;
        while(i>0 && input[i-1] >= input[i])
            --i;

        //맨 앞에까지 왔거나, 마지막 순열까지 다 구한상태
        if(i == 0)
            return false;

        // 2. 다른 교환할 숫자의 위치 찾기 (역순 탐색)
        int j = N-1;
        while(input[i-1] >= input[j])
            --j;

        // 3. 교환하기
        swap(i-1, j);

        // 4. 첫번째로 선택한 위치(i)부터 맨 뒤까지 만들 수 있는 가장 작은 순열 생성(오름차순 정렬)
        int k = N-1;
        while (i<k) {
            swap(i++, k--);
        }

        return true;
    }

    static void swap(int i, int j){
        int temp = input[i];
        input[i] = input[j];
        input[j] = temp;
    }
}
```

### 문제 풀이

비트 연산자를 연습하는 아주 대표적인 문제라고 한다.

[백준 11723번 집합](https://www.acmicpc.net/problem/11723)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java11723/Main.java     
백준 풀이 공유 링크 : http://boj.kr/cdb1567dd484488fba707a6bd407343e

## Backtracking (백트래킹)

가능한 방식을 모두 살펴보면서 문제의 해를 살펴나가는데 해가 되지 않을 것이라고 판명되면 해당 방식에서 파생되는 방식은 모두 생략하고 다른 방식을 탐색해 나가는 기법이다.

본인은 완전탐색에서 파생되거나 완전탐색에 포함된 알고리즘 방식이라고 생각하고 있다. 그저 조건에 따라서 탐색하는 경우가 많이 생략되냐 아니냐의 차이정도밖에 보이지 않는다;   

완전탐색과는 다르게 백트래킹은 탐색을 생략하는 조건을 잘 넣지 않으면 시간초과가 날 수 있을 정도로 탐색을 생략할 수 있는 부분이 크다.

대표적으로 백준의 N-Queen문제 시리즈가 있다.

### 문제 풀이

[백준 9663번 N-Queen](https://www.acmicpc.net/problem/9663)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java9663/Main.java     
백준 풀이 공유 링크 : http://boj.kr/8c1c595d74c54c3e946b622a60251c6a

<br/>

## Greedy (탐욕법)

현재 가장 최적해라고 생각되는 방법을 진행하고 다음 작업을 할 때는 이전의 작업을 신경쓰지 않고 진행하여 최종 해답에 도달하는 방식, 대표적으로 거스름돈을 걸러주는 문제가 있다.

당장 보기에는 최적으로 보이지만 그 선택을 진행해 나가면서 만든 해답은 정답이 아닐 수도 있기 때문에 탐욕법은 빠르게 검증하는 것이 어렵고 단순하고 제한적인 문제에만 적용이 된다.   
또한 정렬된 입력값을 주거나 그렇지 않다면 탐욕법의 기준이 되는 값으로 정렬을 하고 진행하는 것이 일반적이다.

어렵게 만들면 탐욕법으로 해결하는 문제인지 알지도 못할 수 있을 정도로 어려울수록 문제 파악과 검증이 의외로 힘든 알고리즘이다. 하지만 이렇게 어려운 문제는 코테에서는 나오지 않는다고 말할 수 있을 정도로 출제되지는 않는다.

### 문제 풀이

[백준 1931번 회의실 배정](https://www.acmicpc.net/problem/1931)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java1931/Main.java     
백준 풀이 공유 링크 : http://boj.kr/9c5e70cc7094473c86c4f4915c96c32a

[정올 1828번 냉장고](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1101&sca=99&sfl=wr_hit&stx=1828)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/jungol/java1828/Main.java

[백준 3109번 빵집](https://www.acmicpc.net/problem/3109)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java3109/Main.java     
백준 풀이 공유 링크 : http://boj.kr/f6a5ee7e9edd40f7a871935e7f393143


## Divide & Conquer
 
문제를 작은 문제들로 나누어 해결하는 알고리즘 기법이다.   
세 가지 과정으로 나누는데 다음과 같다.

divide(분할) : 문제를 비슷하지만 더 작은 문제들로 나눈다.
conquer(정복) : 작은 문제들을 해결한다.
combine(결합) : 작은 문제들의 답을 활용하여(혹은 모아서) 더 큰 문제를 해결한다.

분할정복 알고리즘은 단순히 문제를 나눠서 해결하자는 개념에 가까운 알고리즘이여서 해당 알고리즘을 직접 활용하여 문제를 해결하기 보다는 다른 알고리즘 기법에 적용되어 문제를 해결하는 모습을 보인다. 대표적인 분할정복을 활용하는 알고리즘의 예는 [퀵 정렬](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Algorithm#quick-sort-%ED%80%B5-%EC%A0%95%EB%A0%AC), [합병 정렬](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Algorithm#merge-sort%ED%95%A9%EB%B3%91-%EC%A0%95%EB%A0%AC), 고속 푸리에 변환 등이 있다.

### 백준 문제 풀이

[1780번 종이의 개수](https://www.acmicpc.net/problem/1780)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java1780/Main.java   
백준 풀이 공유 링크 : http://boj.kr/f4d19fb0deec4bf6b6405baa6b0bd33e

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

<br/>

## Graph Search

그래프는 기본적으로 노드와 간선에 대한 순서나 규칙이 없다.   
때문에 그래프를 탐색할 때에는 모든 노드를 살펴야 하는 경우가 매우 많은데 그 방법은 아래의 두 알고리즘(DFS, BFS)을 기반으로 한다.

### DFS(Depth-First Search)

한 노드에서 시작하여 갈 수 있는 최대한의 경로까지 탐색해나가는 탐색방법, 깊이 우선 탐색으로 불리며 stack이나 재귀함수를 사용하여 구현한다.   

시간 복잡도는 모든 노드와 간선을 조사하므로 O(V+E)이다.   
공간 복잡도는 각 노드에 방문 여부를 채크할 변수 크기 즉, O(V)이다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Depth-First-Search.gif/330px-Depth-First-Search.gif" width="200">
위키백과에 있던 깊이 우선 탐색 애니메이션 예시

```
// 인접 행렬 DFS
static void dfs(int[][] adjMatrix, boolean[] visited, int current){
    visited[current] = true;
    System.out.print(current + " ");

    for (int i = 0; i<N; i++){
        if (!visited[i] && adjMatrix[current][i] != 0){
            dfs(adjMatrix, visited, i);
        }
    }
}
```

#### 문제 풀이

[백준 1987번 알파벳](https://www.acmicpc.net/problem/1987)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java1987/Main.java   
백준 풀이 공유 링크 (방법1) : http://boj.kr/8bb0dbda81524da2891ade56501530cd

[백준 10026번 적록색약](https://www.acmicpc.net/problem/10026)    
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java10026/Main.java   
백준 풀이 공유 링크 : http://boj.kr/3f0fbd26355e4a72ba2428ab283ee6f6

### BFS(Breadth-First Search)

한 노드에서 시작하여 현재 노드에서 접근할 수 있는 노드들을 우선으로 방문한 뒤에 방문했던 노드들에서 또 다시 접근할 수 있는 노드를 다시 차례로 방문하는 방식, 너비우선탐색이라고 불리며 큐로 구현한다.

깊이우선탐색과 마찬가지의 이유로 시간 복잡도는 O(V+E), 공간 복잡도는 O(V)이다.

시작 노드와 목표로 하는 노드를 정하고 시작 노드부터 너비 우선 탐색을 진행하였을 때   
**너비 우선 탐색을 적용하여 찾은 두 노드의 경로는 항상 최단거리이다.**

<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif" width="200">

```
// 인접행렬의 BFS
static void bfs(int[][] adjMatrix, int start){
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[N];

    // 시작 지점을 큐에 넣고 방문 처리를 하여 초기화를 하고
    queue.offer(start);
    visited[start] = true;

    // 너비우선탐색을 진행한다.
    while (!queue.isEmpty()){
        int current = queue.poll();
        System.out.print(current + " ");

        // 인접 행렬의 경우
        for (int i = 0; i<N; i++){
            // current 정점에서 인접하면서 방문하지 않은 정점을
            if (!visited[i] && adjMatrix[current][i] != 0){
                // 큐에 넣는다.
                queue.offer(i);
                visited[i] = true;
            }
        }
    }
}
```

#### 문제 풀이

[백준 2644번 촌수계산](https://www.acmicpc.net/problem/2644)    
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2644/Main.java   
백준 풀이 공유 링크 : http://boj.kr/70616841a85a425eb8cdbd2dabe812a3

[SWEA 1238. [S/W 문제해결 기본] 10일차 - Contact](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/ssafy/swea/java1238/Solution.java   

</br>

## Minimum Spanning Tree, MST (최소 신장 트리)

그래프가 가진 간선의 일부 혹은 전체를 이용하여 그 그래프의 모든 노드를 잇는 트리(**비순환** 유향 그래프)를 <code>신장 트리(Spanning Tree)</code>라고 한다.   
가중치 그래프에서 **만들 수 있는 신장 트리 중 사용한 간선의 가중치 합이 가장 적은 것**를 최소 신장 트리라고 한다.   

간선의 가중치가 이 최소 신장 트리를 만드는 알고리즘은 대표적으로 2개가 있는데 두 가지 모두 탐욕법(Greedy) 알고리즘을 기본으로 하면서 사이클이 만들어 지지 않도록 간선을 선택해 나가는 방법이다.   
원래 탐욕법은 당장에는 최적이지만, 전체적인 관점에서 최적이라는 보장이 없기 때문에 반드시 검증해야 하지만...   
다행히 Prim, Kruskal 알고리즘은 최적의 해답을 주는 것으로 증명되어 있다고 한다.

### 1. Prim Algorithm (프림 알고리즘)

그래프에서 만들 수 있는 작은 트리(정점 1개)에서 인접한 정점들을 잇는 간선 중 가장 적은 가중치를 가지는 간선을 추가시켜나가 점차 확장시켜 결국에는 최소 신장 트리를 만드는 방법

#### 동작 방식

1. 임의의 시작 노드를 선택하여 시작한다.
2. 가지고 있는 노드와 선택한 간선 중 (이미 사용한 간선을 제외하고 사이클이 되지 않는) 가장 가중치가 작은 값을 가지는 간선을 골라 잇는다.
3. 모든 노드와 이어질 때까지 2번을 반복한다.
4. 반복이 끝났을 때 그려진 트리가 최소 신장 트리이다.

#### 특징

1. 인접행렬로 구현시 시간 복잡도 O(V^2)를 가지며 힙을 사용하면 O(E log V)의 시간 복잡도를 가진다.
2. 가까운 간선들만을 비교하기 때문에 크루스칼 알고리즘과 비교하여 간선이 많은 그래프일수록 빠르다.

#### 예시 사진

추가예정

### 2. Kruskal Algorithm (크루스칼 알고리즘)

그래프 전체에서 사이클이 생기지 않는 가장 가중치가 작은 간선을 선택해 최소 신장 트리를 만드는 방법

알고리즘을 사용할 때 반드시 사이클 여부를 확인하는 Disjoint-set(Union-Find) 알고리즘이 부가적으로 필요하다.   
간단히 설명하자면 각 노드에 id를 부여하여 같은 트리에 속하는지 아닌지 파악하고   
간선이 생겨 두 트리가 연결될 때 빠르게 id를 통합시키는 알고리즘이다.

#### 동작 방식

1. 그래프의 모든 간선들을 가중치의 오름차순으로 정렬한다.
2. 정렬된 간선이 사이클이 생기지 않도록 차례로 추가한다.   
   이때, 사이클 여부는 Disjoint-set 알고리즘으로 확인한다.
3. 간선의 개수가 '노드의 개수 - 1'이 될 때까지 위를 반복한다.

#### 특징

1. 시간복잡도는 O(E log V) 혹은 O(E log E)이다. (위키백과에 증명이 되어있지만 너무 어려워서 외우기만..)
2. 전체 간선들을 가중치 기준으로 정렬을 하고 시작하기 때문에 프림 알고리즘과 비교하여 간선이 적을수록 빠르다.

#### 예시 사진

추가예정

#### Disjoint-set (서로소 집합)

서로 중복되어 포함된 원소가 없는 집합들을 의미한다, 집합에 속한 하나의 원소를 대표자(representative)로 취급하여 집합을 구분한다.

위의 크루스칼 알고리즘에서 사이클이 없는 트리를 만들거나 서로소 집합을 찾는데 사용되며 아래의 과정을 통해서 집합을 찾거나 합친다.

+ 집합의 대표자를 찾을 때   
  각 노드는 자신의 대표자를 찾을 수 있는 링크를 가지며 대표자는 스스로를 가리키는 링크를 가진다   
  일반적으로 링크는 스스로를 가리키도록 초기화 된다.
  
+ 집합을 합칠 때   
  두 집합 중 한 집합의 대표자의 링크를 다른 집합의 대표자를 가리키도록 만든다.

#### 빠른 대표자 확인

1. Rank   
   각 노드가 자신을 루트로 하는 서브 트리의 높이를 랭크로 저장하고 두 집합을 합칠 때, 랭크가 낮은 집합을 높은 집합에 붙여 대표자를 찾는 속도를 높이는 방법

2. Path compression   
   대표자를 찾는 과정에서 만나는 모든 노드들이 대표자 노드를 직접 가리키도록 포인터를 바꾸는 방법

두 방법 중 본인은 두 번째 방법을 선호한다.

#### 문제 풀이

일반적으로 최소 신장 트리 문제라면 다익스트라든 프림이든 문제가 되지 않는다.   
하지만 알고리즘 특징 상 간선이 많으면 프림, 간선이 적으면 크루스칼이 유리하다.

[백준 2644번 촌수계산](https://www.acmicpc.net/problem/2644)    
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2644/Main.java   
백준 풀이 공유 링크 : http://boj.kr/70616841a85a425eb8cdbd2dabe812a3

[SWEA 3124. 최소 스패닝 트리](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_mSnmKUckDFAWb)    
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/ssafy/swea/java3124/Solution.java   

+ 유니온 파인드 참고 문제

[SWEA 7465. 창용 마을 무리의 개수](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU)    
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/ssafy/swea/java7465/Solution.java   

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

![Dijkstra_Animation](https://user-images.githubusercontent.com/19484971/171373359-6b5368ab-ba50-4fde-ae34-136bc2832e1e.gif)   
출처 : [위키백과](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

#### 활용 예시

1. 네비게이션 길찾기
2. 지하철 최단거리
3. 네트워크 경로찾기

#### 문제 풀이

[백준 1753번 최단경로](https://www.acmicpc.net/problem/1753)    
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java1753/Main.java   
백준 풀이 공유 링크 : http://boj.kr/e4577836dc65419382588a5460bb76a4

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

#### 특징

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

## Dynamic Programming (다이나믹 프로그래밍)

이름만 들었을 때는 잘 와닿지 않지만, 그리디 알고리즘과 같이 `최적화 문제를 해결하는 알고리즘` 작은 혹은 부분적인 문제의 해들을 구하고 이것들을 활용하여 더 큰 크기의 문제를 해결해나가 최종적으로 원하는 문제의 결과를 구하는 알고리즘 설계 기법

그리디와 DP 둘 모두 작은 문제를 풀어 최종 문제의 결과를 구하는데 활용할 수 있다는 점이 같지만, 개인적으로 그리디 알고리즘은 위의 조건이 충족되는지 따지는 것(예외를 찾는 것)이 훨씬 더 어려워서 DP가 더 쉽게 느껴진다. DP의 경우 점화식이든 반복되는 구간이든 반복 하나만 찾으면 되니까..

지금보니까.. 분할정복과도 비슷해 보인다.. 교수님은 상향식/ 하향식이 다르다고 하셨지만, 그 정도로는 크게 달라보이지 않아서 잘 모르겠다.

### 최적 부분문제 구조 (Optimal substructure)

.. 위에서 작성한 '작은 문제를 풀어 최종 문제의 결과를 구하는데 활용할 수 있다는 점'을 고급 용어로 불렀을 때 위와 같이 말한다.

조금 더 정확하게 작성하면, 어떤 문제에 대한 해가 최적일 때, 그 해를 구성하는 작은 문제들의 해 역시 최적이여야 한다는 것


### 중복 부분문제 구조 (Overlapping subproblems)

.. 이번에는 위에서 언급한 'DP의 경우 점화식이든 반복되는 구간 하나만 찾으면 되니까'를 고급용어를 바꾸었을 때의 용어같다.

문제를 해결할 때 더 작은 부분문제를 활용하면서 문제의 크기에 상관없이 같은 구조를 가진다는 의미같다... 

아니., 용어 정의는 안하고 해당 구조로 인해 얻을 수 있는 장점만 써놓아서 이해가 어렵다, 용어 정리가 틀렸을 수도 있다;;
 
### memoization (메모이제이션)

연산을 진행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 만들어 전체적인 실행속도를 개선하는 기-술이다. 동적계획법에서 자주 쓰이고도 중점이 되는 기술이다. (그렇다고 DP에서만 사용하는 것은 아니므로 오해 주의) 

순수함수에 대한 결과들만이 메모이제이션을 활용하여 반복된 연산을 수행하지 않도록 만들수 있으며 그렇지 않은 값들은 때마다 결과가 달라지기 때문에 메모이제이션을 활용하지 못한다.   
순수함수가 아닌 함수의 대표적인 예는 두 수를 바꾸는 함수로, 배열과 바꾸고 싶은 두 수의 위치가 들어왔을 때 배열과 위치가 같아도 해당 위치에 저장된 수는 다를 수 있기 때문에 순수함수가 아니다.

그냥.. 메모리와 시간을 등가교환하는 방법으로만 알고 있었는데 해당 방식에 대한 용어가 있었는지는 몰랐다;; 메모이제이션을 직역하면 `메모리에 넣기` 라고 한다.

#### 문제 풀이

[백준 2579번 계단 오르기](https://www.acmicpc.net/problem/2579)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2579/Main.java   
백준 풀이 공유 링크 : http://boj.kr/e41a636640e046c68efbdf0144ecd63d

[백준 2133번 타일 채우기](https://www.acmicpc.net/problem/2579)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java2133/Main.java   
백준 풀이 공유 링크 : http://boj.kr/8581607c75ab46ccb5802a788a71ad32

[백준 9184번 신나는 함수 실행](https://www.acmicpc.net/problem/9184)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java9184/Main.java   
백준 풀이 공유 링크 : http://boj.kr/f0b7684d044d4e2ab8ac9ac807aaa63d

<br/>

### knapsack (배낭)

DP를 활용하여 해결하는 대표적인 문제 중 하나로, 무게 제한이 K인 배낭과 무게와 가치가 정해진 N개의 물건이 있을 때 가치의 총합이 가장 크도록 배낭을 싸는 **문제**를 의미한다.   

이때 지문에는 보통 각 물건은 하나씩만 존재하며 나누어 넣을 수 없다는 조건이 있어서 각 물건은 배낭에 넣거나, 넣지 않거나 둘 중 하나의 경우만을 가지는 특징이 있다. 이러한 조건으로 부분집합을 써도 되지만.. 일반적인 냅섹 문제는 부분집합으로 푸는 경우 시간초과가 나도록 만들기 때문에 물건의 종류가 너무 많으면 냅색 문제임을 고려하자!

냅색 문제 예를 들어보겠다.   
무게 제한이 7kg인 배낭과 4개의 물건 무게(W)와 가치(V)가 아래와 같이 있다고 할 때,   

| i |	V |	W |
| --|--|--|
| 1 |	13 | 6 |
| 2 |	8 |	4 |
| 3 |	6 |	3 |
| 4 |	12 | 5 |

가치의 총합이 가장 크도록 가방을 싸는 방법으로 (본인이) 가장 먼저 생각났던 것은 무게당 가치가 가장 높은 물건을 먼저 넣는 방법이었다. 물건별 무게당 가치를 계산하면 아래와 같다.

| i |	V |	W | V / W |
| --|--|--| -- |
| 4 |	12 | 5 | 2.40 |
| 1 |	13 | 6 | 2.17 |
| 2 |	8 |	4 | 2.00 |
| 3 |	6 |	3 | 2.00 |

가장 먼저 무게당 가치가 가장 높은 4번 물건을 가방에 넣으면 가방은 5kg가 되고 이때 가치의 합은 12가 되는데, 남은 무게 2kg에 대해 더 넣을 수 있는 물건이 없으므로 12가 최적값의 후보가 된다. 하지만 실재로는 2번 물건과 3번 물건을 넣어 7kg으로 가방을 채운 가치의 합 14가 최적해로 탑욕적인 방법으로는 최적해를 구할 수가 없다.

이 때 사용하는 것이 DP이다, 배열을 활용하여 각 무개별로 가장 가치가 많은 경우를 저장하고 그것을 활용하여 최적해를 계산하여 답을 도출해낸다. 한 물건을 특정 무게에서 가방에 넣는 것`D[i-1][j - W[i]] + V[i]`이 그대로가 더 좋을지 아닐지`D[i-1][j]`를 계산하여 저장하는 방식이다.   
식으로 표현하면 아래와 같다. (이해하기 힘들면 문제풀이도 참고해보자.)

    D[i][j] = Max(D[i-1][j], D[i-1][j - W[i]] + V[i])

메모이제이션을 활용할 때 이중배열을 사용한다는 특징이 있는데.. 나중에 보니 설명을 위해서 이중배열을 사용하는 것일 뿐 단일배열로도 가능하다.

#### 문제 풀이

[백준 1535번 안녕](https://www.acmicpc.net/problem/1535)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java1535/Main.java   
백준 풀이 공유 링크 : http://boj.kr/a74618fd9e0c423ba143a7f59df97b0a

### LIS(Longest Increasing Subsequence, 최장 증가 수열)

왼쪽에서 오른쪽으로 나열된 어떤 수열의 순서를 유지하면서 크기가 점진적으로 커지는 가장 긴 부분 수열을 구하는 문제를 의미한다. 단순히 최장 증가 수열의 **길이**를 요구하는 경우도 많다.

DP문제 특성상 완전탐색을 활용하면 O(2^N)으로 시간초과가 일어나기 때문에 DP로 해결하는 것이 좋다.   

DP로 푸는 방법도 크게 2가지로 나뉘는데,   
하나는 시간복잡도가 O(N^2)이지만 최장 증가 수열을 구할 때 좋다.
다른 하나는 이분탐색을 활용하여 시간복잡도가 O(NLogN)이지만 최장 증가 수열의 길이만 구할 수 있다.   
상황에 따라서 원하는 방식으로 사용하자!

먼저 시간복잡도가 O(N^2)이지만 최장 증가 수열을 구할 수 있는 방식부터 설명하겠다.   
먼저 수열A의 길이만큼의 배열D을 활용한다. 배열D는 최소 하나의 숫자가 있으므로 1로 초기화한다.    
수열은 A = {20, 1, 7, 4, 5, 6, 13, 3}라고 가정하고 D[i]를 'A[i]번째 원소를 마지막으로 갖는 최장 증가 수열의 길이'라고 정의하고 진행하겠다.

A[i]가 마지막 원소이면서, 증가 수열을 만들어야 하는 조건에서 D[i]를 구하기 위해서는   
D[i]의 값은 i보다 작은 j에 대해 A[j] < A[i]를 만족하는 D[j] 중 최댓값 + 1을 저장해야 한다.....   
솔직히 이해한 필자도 이해 잘 안가는 글이다;;; 아래에 예시를 한번 들어보겠다.

수열 A의 5번째 값(5)의 D[4]는 아래와 같은 방법으로 3이 저장된다.   
참고로 A = {20, 1, 7, 4, 5, 6, 13, 3} D = {1, 1, 2, 2, 1, 1, 1, 1} 값을 가지고 있다.   
(D는 1로 초기화 되는 것과 4미만의 인덱스는 이미 연산을 마친 상태이다.)

j:0 A[0]=20>5으로 안되고   
j:1 A[1]=1<5이면서 D[5]=1<D[1]+1=2 이므로D[5]에 2을 저장하고   
j:2 A[2]=7>5으로 안되고   
j:3 A[3]=4<5이면서 D[5]=2<D[4]+1=3 이므로 D[5]에 3을 저장하고   
j:4 현재 탐색하고 있는 수열이 D[4]이므로 j:4이상은 탐색하지 않는다.

결과적으로 모든 수들에게 위의 연산을 진행하면 아래와 같은 결과가 나온다.

| idx |	0 |	1 |	2 |	3 |	4 |	5 |	6 |	7 |
| -- |	-- |	- |	- |-- |-- |	- |	- |	- |
| A[i] | 20 |	1 |	7 |	4 |	5 |	6 |	13 | 3 |
| D[j] | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 2 |

위의 과정을 수열의 각 n개의 수들이 자신의 자리수-1 만큼의 비교를 수행하므로 시간복잡도가 O(N^2)가 되고 배열D의 값 중 가장 큰 값이 최장 증가 수열의 길이가 된다.   
만약 여기서 최장 증가 수열을 구하고자하면 증가 수열을 저장하는 리스트를 사용하거나 이전 수의 인덱스를 저장하는 배열을 사용하면 된다. 방법은 위와 크게 다를 것이 없고 D[i]에 값을 저장할 때 리스트나 배열을 관리해주면 된다. 

필자는 메모리를 적게 사용하는, 이전 수의 인덱스를 저장하여 수열의 첫번째 수를 역추적하는 방식(서로소 집합 알고리즘)의 코드를 사용한다. 아래의 백준 14002번 가장 긴 증가하는 부분 수열 4 문제풀이를 참고하자!

#### 이진탐색 활용

리스트과 이진탐색을 활용하면 조금 더 빠르게 최장 증가 수열의 길이를 구할 수 있다.
수열은 A = {20, 1, 7, 4, 5, 6, 13, 3}라고 가정하고 D[i]를 이번에는 '증가 수열에서 i번째 위치에 올 수 있는 가장 작은 수'라고 정의하고 진행하겠다. (수열의 앞 부분에 더 작은 값이 있어야 뒷 부분에 더 많은 값이 쌓이기(?) 쉬우므로)

D에 저장되어있는 값들 중 A[i]보다 크면서 가장 작은 값에 A[i]를 덮어 씌워 저장한다. 조건에 맞는 수를 찾을 때 이분탐색을 사용한다.    
만약 위의 조건을 만족하는 수가 없다면(D에 저장된 모든 값이 A[i]보다 작다면) D리스트 뒤에 A[i]를 추가한다.   

이렇게 만들어진 D리스트의 길이가 최장 증가 수열의 길이이다. 수열 N개에 저장할 위치를 이분탐색을 사용하여 찾아내므로 시간복잡도가 O(NlogN)인 것이다. 코드를 보고 싶다면 백준 11053번 가장 긴 증가하는 부분 수열 문제 풀이를 참고하자.

참고로! A[i]를 D에 덮어 씌워 저장하는 방식을 취하기 때문에 리스트D가 최장 증가 수열이 아닌 것에 주의하자!

#### 문제 풀이

[백준 11053번 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java11053/Main.java   
백준 풀이 공유 링크 : http://boj.kr/427e13b63f0b49b385c0431ff3be0301

[백준 14002번 가장 긴 증가하는 부분 수열 4](https://www.acmicpc.net/problem/14002)   
깃허브 풀이 링크 : https://github.com/ii200400/algorithm/blob/master/Baekjoon/kotlin/src/com/baekjoon/problem/java14002/Main.java   
백준 풀이 공유 링크 : http://boj.kr/d44edda18aa7445a93fd05bc3043ef10

### LCS(Longest Common Subsequence)


### Edit Distance


### Matrix Chain Multiplication



## Pattern Matching (문자열 패턴 매칭)

특정 문자열이 포함되어 있는지 찾아보는 알고리즘   
대표적으로 4가지가 있는데 그 중 완전탐색을 사용하는 패턴매칭은 생략하고 나머지 라빈-카프, 보이어-무어, KMP 알고리즘만 이론 정리하고 넘어가겠다. (코드는 봤는데 이해를 정확히 못해서;)

### Rabin-karp (라빈-카프)

문자를 하나씩 비교하는 것이 아니라 해시 함수를 활용하여 본문의 부분 문자열과 해시 값과 패턴 문자열의 해시 값을 비교하는 알고리즘

다음 부분 문자열의 해시 값을 찾을 때 원래의 해시값의 빠지는 문자에 해당하는 해시를 빼고 추가되는 문자의 해시를 더해주는 방식을 활용한다.   
예를 들어.. 원래 문자열 "1234567890"에서 "234"를 찾는다고 하면 처음에는 "123"의 해시와 "234"의 해시를 비교하고 다음에는 "123"에서 "1"의 해시값을 빼고 "4"의 해시값을 더한 해서와 "234"의 해시를 비교한다.   
한 칸 이동할 때 마다 부분 문자열에 대해서 해시 값을 구하는 것이 아니라 빠지고 추가되는 문자열에 대한 해시 값을 더하고 빼주기 때문에 더 빠르게 작동한다고 한다.

하지만 해시 함수 특징과 해시 값을 mod로 나누는 상황(해시 값을 일정 길이로 맞춰주기 위함)으로 인하여 다른 문자열이라도 같은 해시값(해시 충돌)을 가질 수 있다. 그래서 해시값이 맞다면 문자열을 직접 확인을 하는 작업을 한다고 한다.

#### 특징

전체 문자열의 길이를 N, 패턴 문자열의 길이를 M이라고 하였을 때

+ 해시 값이 일치해도 한 번 더 문자열을 직접 확인해주는 작업이 꼭 필요하다.
+ 위의 원인으로 시간 복잡도는 최선의 경우O(N), 최악의 경우 O(MN)의 시간복잡도를 가지는데 평균적으로는 선평시간에 가깝다.

[16일 알고리즘 실습 추가 요망]()

### Boyer Moore (보이어-무어)

전체 문자열과 패턴 문자열을 **반대로 탐색**하면서 불일치한 문자가 발견되면 **불일치한 문자**에 따라서 탐색을 적절하게 뛰어넘는 알고리즘

불일치하는 문자에 따라서 얼마나 뛰어넘을지에 관한 정보를 담는 변수(보통 배열)가 필요하며 패턴 문자열은 내부에 반복되는 문자열이 있어도 가능은 하나, KMP 알고리즘에 비해서 느리게 된다. 참고로 반대로 탐색하는 이유는 일반적으로 문자열이 앞보다는 뒤에서 틀리는 경우가 많아서 라고 한다.

스킵 배열을 만들고 문자열과 패턴 문자열을 비교해 나가는데 두 문자열이 일치하지 않았을 때, 가장오른쪽(처음)에 비교했던 문자에 따라서 비교 위치를 뛰어 넘는다. 패턴 문자열이 "water"라면 아래와 같다.

| w | a | t | e | r | 그 외 문자 |
|---|---|---|---|---|---|
| 4 | 3 | 2 | 1 | 5 | 5 |

```
    *             *
melorwater  => melorwater  => 스킵 배열의 r 문자에 대응하는 숫자는 5이므로.. 5칸 건너뛴다.   
water       => water       => 
         *             *             *             *             *   
melorwater  => melorwater  => melorwater  => melorwater  => melorwater  => 패턴 문자 찾음!   
     water  =>      water  =>      water  =>      water  =>      water  => 끝!   
```

좀 더 잘 설명하고 싶은데.. 그림 그릴 시간까지 투자하기 힘들어서;; 일단 글로 짧게 예시를 들었다.

#### 특징

전체 문자열의 길이를 N, 패턴 문자열의 길이를 M이라고 하였을 때

+ 시간 복잡도는 최선의 경우O(N/M), 최악의 경우 O(MN)의 시간복잡도를 가진다.
+ 패턴 문자열의 내부에 반복되는 문자열이 있다면, 상대적으로 KMP 알고리즘이 더 적절하다.   

KMP 알고리즘이 어떤 문자열에 대해서도 평균적으로 더 빠르다고 하지만 현실에서는 패턴 문자열의 내부에 반복되는 문자열이 있는 경우가 많이 없기 때문에 실질적으로는 KMP보다는 보이어-무어를 더 널리 사용하며 오히려 KMP보다 보이어-무어가 더 빠르다고 한다.

[16일 알고리즘 실습 추가 요망]()

### KMP

보이어-무어 알고리즘의 단점을 보완한 알고리즘으로 패턴 문자열 내부에서 반복되는 문자열에 관한 부분일치 테이블 배열을 만들어 **불일치한 문자 위치**에 따라서 탐색을 적절하게 뛰어넘는 알고리즘   
예를 들어 test = "aaaaaaaaaaab", pattern = "aaaab" 라면 KMP가 보이어-무어보다 더 빠르다.

보이어-무어 알고리즘은 스킵 배열을 이용해서 해당 배열의 값만큼 비교를 뛰어넘어가는데 비해 KMP 알고리즘의 부분 일치 테이블 배열은 인덱스를 배열의 값으로 넣어서 뛰어넘어간다. (꽤 햇갈리다.)

#### 특징

전체 문자열의 길이를 N, 패턴 문자열의 길이를 M이라고 하였을 때

+ 시간 복잡도는 O(M+N)으로 어떤 문자열에 대해서도 평균적으로 가장 빠른 알고리즘이다.

[16일 알고리즘 실습 추가 요망]()

<br/>
