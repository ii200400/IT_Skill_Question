까먹어서 다시 올리는 erd 이미지
![image](https://user-images.githubusercontent.com/19484971/172144116-61b67ae5-3427-4b12-8da2-6d827de0241b.png)

# Join

원래는 DML의 select절에 같이 있어야 하나 내용과 종류가 많아 따로 작성한다.   

+ 서로 관련이 있는 둘 이상의 테이블에서 데이터가 필요한 경우에 사용한다.
	+ 컬럼을 조회할 때, 테이블들이 같은 컬럼명을 가진다면 컬럼 앞에 테이블 명을 적어주어야 한다.
+ 일반적으로 조인조건을 포함하는 WHERE절을 (테이블 수 - 1)개를 사용한다.
+ 조인조건은 일반적으로 각 테이블의 PK 혹은 FK를 사용한다.

+ 종류
	+ INNER JOIN
		+ Equi JOIN
			+ NATURAL JOIN
		+ None - Equi JOIN
	+ OUTER JOIN
		+ LEFT OUTER JOIN
		+ RIGHT OUTER JOIN
		+ FULL OUTER JOIN (MySQL에는 없다.)
	+ SELF JOIN
	+ CROSS JOIN(CARTESIAN JOIN)
	
+ 주의사항
	+ 어느 테이블을 먼저 읽을지를 결정하는 것이 중요하다
		+ 처리할 작업량이 크게 달라질 수도 있기 때문이다.
		+ 하지만 버전(5.5 이후)이 올라가면서 프로그램이 자동으로 최적화를 진행해준다고 한다.
		+ 위의 기능을 수행하는 DBMS 핵심엔진을 옵티마이저라고 한다.
	+ INNER JOIN : 어느 테이블을 먼저 읽어도 결과가 달라지지 않아 MYSQL 옵티마이저가 조인의 순서를 조절해서 다양한 방법으로 최적화를 수행할 수 있다.
	+ OUTER JOIN : 반드시 OUTER가 되는 테이블을 먼저 읽어야 하므로 옵티마이저가 조인 순서를 선택할 수 없다. 즉, 테이블 순서에 유의해야 한다. 

이곳저곳 살펴 보니 분류방법이 공식적으로 정해져 있지 않은지 분류하는 방법이 사람마다 다른 경우도 많았다. 위의 분류는 위키백과의 분류체계를 가져온 것이다.

간단하게 이해하기 좋은 이미지가 있어서 가져왔다.

![image](https://user-images.githubusercontent.com/19484971/171563387-d057bf46-e38d-4cbe-994c-ec1cba6e0043.png)

출처 : [wikiwebpedia](https://wikiwebpedia.com/join-in-microsoft-sql)

+ 참고 블로그
	+ https://doh-an.tistory.com/30 
		+ 예시 이미지가 정말 좋다. 강의나 내가 정리한 것보다 잘 정리한듯..

</br>

## INNER JOIN

+ 가장 일반적으로 사용되는 JOIN의 종류 
	+ 위의 예시도 INNER JOIN이다.
	+ 단순히 JOIN이라고 해도 INNER JOIN으로 판단한다.
+ 동등 조인(Equi-join)은 N개의 테이블 조인 시 N-1개의 조인 조건을 사용한다.
	+ 조인 조건은 두 테이블이 공통으로 가지는 컬럼을 사용한다.
	+ using절을 이용하면 조금 더 편하게 조인 조건을 만들 수 있다.
	+ natural join을 사용하면 두 테이블이 가지는 동일한 컬럼명들을 기준으로 자동으로 조인을 해준다.
		+ 하지만 원치않는 조인 조건이 포함되버릴 수도 있기 때문에 주의해주어야 한다.
+ on은 join이 실행되기 전에, where는 join이 실행된 후 실행된다.
	+ 때문에 join조건은 on절에, 일반조건은 where절에 작성하여 구분하자.
+ 종류
	+ Equi JOIN
		+ NATURAL JOIN
	+ None - Equi JOIN

### 형식

```
1)
SELECT 컬럼명
FROM 테이블_이름1, 테이블_이름2
WHERE 테이블_이름1.컬럼 = 테이블_이름2.컬럼;


2)
SELECT 컬럼명
FROM 테이블_이름1 [[INNER] JOIN] 테이블_이름2
ON 테이블_이름1.컬럼 = 테이블_이름2.컬럼;

3)
SELECT 컬럼명
FROM 테이블_이름1 [[INNER] JOIN] 테이블_이름2
USING (컬럼명, ...);
```

### 예시

+ 사번이 100인 사원의 사번, 이름, 급여, 부서이름
	+ 가독성을 위해서 on에 테이블을 join하는 조건, where에는 일반조건을 넣는 것이 좋다.
	+ inner join은 단순히 테이블을 `,`로 나열하기만해도 되고 join 이나 inner join을 적어도 된다.
```
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름
from employees e inner join departments d
on e.department_id = d.department_id 
where employee_id = 100;
```
![image](https://user-images.githubusercontent.com/19484971/172136229-f5a8bd87-7541-4682-ae51-1320c874da33.png)


+ 사번이 100인 사원의 사번, 이름, 급여, 부서이름, 근무하는 도시 이름
	+ 3개 이상의 테이블을 join 하는 것도 가능하다.
	+ join과 inner join, `,`를 섞어서 사용해도 inner join으로 된다.
	+ on 뒤에 또 다시 테이블을 join 해도 문제없다.
```
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름, city
from employees e, departments d join locations l
where e.department_id = d.department_id 
and d.location_id = l.location_id
and	employee_id = 100;

-- 위와 같은 내용
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름, city
from employees e inner join departments d inner join locations l
on e.department_id = d.department_id and d.location_id = l.location_id
where employee_id = 100;

-- 가독성을 생각하여 아래와 같이 쓰는 방법도 있다, 속도와 의미는 동일하다.
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름, city
from employees e inner join departments d 
on e.department_id = d.department_id 
inner join locations l
on d.location_id = l.location_id
where employee_id = 100;
```
![image](https://user-images.githubusercontent.com/19484971/172136843-d03ab035-5ee9-4b57-ab4f-af8b9df7f885.png)

### using

+ 조인 조건를 편리하게 작성할 수 한다. 
	+ 두 테이블에 같은 컬럼명이 있는 경우 사용 가능하다.
	+ using 테이블명.컬럼명 와 같이 쓰면 오히려 에러가 난다.
```
-- 첫번째 예시에 using을 사용한 것
select e.employee_id 사번, e.first_name 이름, e.salary 급여, d.department_id, d.department_name 부서이름
from employees e inner join departments d
using (department_id)  -- e.departent_id 와 같이 쓰면 오히려 에러가 난다.
where employee_id = 100;
```
![image](https://user-images.githubusercontent.com/19484971/172136229-f5a8bd87-7541-4682-ae51-1320c874da33.png)
결과는 예시의 첫번째와 같다.

### Equi JOIN

단순히 조인 조건에 `=`를 사용하는 경우를 의미한다.   
`is null`이라던가 `<=` 등을 사용하는 경우에는 None - Equi JOIN으로 구분된다.

위의 예시들 모두 Equi JOIN이므로 별도의 예시는 보여주지 않겠다.

### Natural JOIN

+ 이름이 같은 컬럼을 기준으로 join 해주는 조인 방식
	+ 컬럼명만 같으면 무조건 조인조건으로 들어가게 되므로 의도적으로 안 쓰는 경우도 많다고 한다.
+ 조인 조건이 항상 동등조인(=)이므로 Equi JOIN으로 분류된다.

#### 형식

```
SELECT 컬럼명
FROM 테이블_이름1 NATURAL JOIN 테이블_이름2;
```

#### 예시

+ Natural JOIN 특성상 컬럼명이 같으면 무조건 조인조건이 된다.
	+ 최상단 사진을 참고하면 employees와 departments에 같은 컬럼명인 것이 department_id와 manager_id 2개로 적합한 데이터가 없어서 출력되는 데이터가 없다.
	+ 위의 이유로 해당 natural join 은 사용시에 주의해야 한다.
```
-- 첫번째 예시에 natural join을 (무지성으로) 사용한 것
select employee_id 사번, first_name 이름, salary 급여, department_id, department_name 부서이름
from employees e natural join departments d
where employee_id = 100;
```
![image](https://user-images.githubusercontent.com/19484971/172152489-3540e5d8-0916-48f2-be69-2cfa3459bc19.png)

### None - Equi JOIN

+ 단순히 equi`=`이 아닌 비교문들 `Between`, `>`, `<=` 등의 연산자를 사용하여 조인조건을 만든 inner join을 의미한다.
	+ 보통 PK-FK 연관관계를 가지는 테이블은 보통 `=` 연산자를 사용하고 그렇지 않고 일반 컬럼을 조인조건으로 사용하면 `=`외의 연산자를 사용하는 것이 일반적이라고 한다.
	+ 즉, 일반 컬럼을 조인 조건으로 할 때 주로 사용되는 join 방식이다.

#### 예시

+ 일반 컬럼을 조인 조건이 되야한다.
	+ 직원 테이블과 급여등급 테이블을 통해서 각 직원이 받는 임금의 급여등급을 계산한다.
	+ 직원의 급여와 급여등급 테이블은 크게 연관성이 없어 단순히 일반컬럼이 조인조건으로 쓰이게 된다.
```
-- 모든 사원의 사번, 이름, 급여, 급여등급(!)
select e.employee_id, e.first_name, e.salary, s.grade
from employees e join salgrades s
on e.salary between s.losal and s.hisal;
```
![image](https://user-images.githubusercontent.com/19484971/172211767-cafa9814-1fcf-4d67-b5de-b3a5cf0088f7.png)

## OUTER JOIN

한쪽 테이블에는 특정 데이터(컬럼)가 존재하는데 다른 테이블에는 존재하지 않을 경우 해당 데이터가 검색되지 않는 문제를 해결하기 위해 사용한다.

+ 종류
	+ LEFT OUTER JOIN
	+ RIGHT OUTER JOIN
	+ FULL OUTER JOIN (MySQL에는 없다.)

### LEFT OUTER JOIN

왼편에 있는 테이블의 조건에 일치하지 않는 데이터까지 출력하는 join 방식

#### 형식

```
1)
SELECT 컬럼명
FROM 테이블_이름1 LEFT OUTER JOIN 테이블_이름2
ON 조건문;

2)
SELECT 컬럼명
FROM 테이블_이름1 LEFT OUTER JOIN 테이블_이름2
USING (컬럼명, ...);
```

#### 예시

+ 모든 사원의 부서를 출력하려는데 사원(왼쪽 테이블) 부서가 발령되지 않은 경우
	+ 부서가 없는(부서번호가 null) 사원 검색되도록 left outer join을 사용한다.
	+ null 대신 임의로 승진발령 문자열이 나오도록 설정하였다.
```
select e.employee_id, e.first_name, ifnull(d.department_name, '승진발령')
from employees e left outer join departments d
on e.department_id = d.department_id;
```
![image](https://user-images.githubusercontent.com/19484971/172169194-dda657ea-0ba4-41ea-a95f-d90f0e4a0c08.png)

### RIGHT OUTER JOIN

오른편에 있는 테이블의 조건에 일치하지 않는 데이터까지 출력하는 join 방식, 기본적으로 left outer join과 비슷하다.

#### 형식

```
1)
SELECT 컬럼명
FROM 테이블_이름1 RIGHT OUTER JOIN 테이블_이름2
ON 조건문;

2)
SELECT 컬럼명
FROM 테이블_이름1 RIGHT OUTER JOIN 테이블_이름2
USING (컬럼명, ...);
```

#### 예시

+ 모든 부서의 사원 정보를 보려는데 부서(오른쪽 테이블)에 사원이 없는 부서가 있는 경우
	+ 사원이 없는 부서(부서번호가 null)가 검색되도록 right outer join을 사용한다.
```
select department_id, department_name, employee_id, first_name
from employees e right outer join departments d
using (department_id);
```
![image](https://user-images.githubusercontent.com/19484971/172204740-64dc3038-0d46-49d2-bd1f-7bed73c00086.png)

### FULL OUTER JOIN

두 테이블의 테이블의 조건에 일치하지 않는 데이터까지 출력하는 join 방식   
mysql에서는 full outer join이 따로 없다. 때문에 left/right outer join을 활용해서 만들어야 한다.

#### 예시

+ mysql에는 full outer join이 없어 union으로 full outer join 구현
	+ union은 두 컬럼을 더한다.(합집합의 개념) 단, 두 컬럼의 컬럼은 순서대로 매칭되어야 한다. 
	+ union all을 하면 중복되는 (교집합)부분을 그대로 한번 더 출력한다.
	+ union하는 두 테이블의 컬럼은 같아야 한다.
```
-- 부서의 모든 사원의 부서명, 사원id, 이름을 출력한다.
-- 단, 부서가 없는 사원과 사원이 없는 부서도 출력해야 한다.
select ifnull(d.department_name, '승진발령'), e.employee_id, e.first_name
from employees e left outer join departments d
on e.department_id = d.department_id
union
select department_name, employee_id, first_name
from employees e right outer join departments d
using (department_id);
```
![image](https://user-images.githubusercontent.com/19484971/172208168-0d9c5af2-25b5-4187-b505-ca7949152364.png)
![image](https://user-images.githubusercontent.com/19484971/172208210-55d7a97c-f24f-464a-b68c-3c00ccbe8dfa.png)
두 테이블의 조건에 맞지 않는 데이터가 보이는 것을 확인할 수 있다.

## SELF JOIN

같은 테이블끼리 하는 join

#### 형식

+ 같은 테이블이 2번 쓰이는 것이 특징이다.
```
1)
SELECT 컬럼명
FROM 테이블_이름1 조인_방식 테이블_이름1
ON 조건문;

2)
SELECT 컬럼명
FROM 테이블_이름1 조인_방식 테이블_이름1
USING (컬럼명, ...);
```

#### 예시

+ 모든 사원의 사번, 이름, 매니저사번, 매니저이름을 출력하고자 한다.
	+ 매니저는 사원이기도 하므로 employees이 스스로를 join을 해야 한다.
	+ 사장님의 경우 매니저가 없으므로 left outer join을 활용하여 출력할 수 있도록 한다.
```
-- 모든 사원의 사번, 이름, 매니저사번, 매니저이름(!)
select e.employee_id, e.first_name, e.manager_id, ifnull(m.first_name, '사장님이당')
from employees e left outer join employees m
on e.manager_id = m.employee_id;
```
![image](https://user-images.githubusercontent.com/19484971/172211687-8fafa909-9ed8-44de-b2cc-cb94e625ef5f.png)


## CROSS JOIN(CARTESIAN JOIN, 교차조인)

일반적으로 `CARTESIAN JOIN`보다는 `CARTESIAN PROJECT`라고 작성하는 것 같은데 필자는 수학의 곱집합과 영문명이 완전 똑같은 것에 햇갈려서 `CARTESIAN JOIN`라고 작성하였다. 조인 조건이 없거나 조건을 부적절하게 작성할 경우 일어나는 조인이다.

이름에서 유추할 수 있듯이 두 테이블의 행을 곱해서 (테이블A의 행 수)\*(테이블B의 행 수)의 행을 가지는 테이블이 만들어지는데, 거의 안쓰인다고 한다. ~~이거 쓰면 오히려 테이블 잘못 작성했다는 합리적 의심을 한다고 언급하셨다..~~

### 형식

```
SELECT 컬럼명
FROM 테이블_이름1 CROSS JOIN 테이블_이름2;

-- 암묵적으로 아래와 같이 사용할 수도 있다.

SELECT 컬럼명
FROM 테이블_이름1, 테이블_이름2;
```

### 예시

아래의 두 테이블을 교차조인을 하면

![image](https://user-images.githubusercontent.com/19484971/171558050-f26a3eef-5f21-4f27-a080-2c8d0ea6087b.png)

아래와 같은 결과가 나온다.

![image](https://user-images.githubusercontent.com/19484971/171558093-be98d4f8-d809-454c-b4a7-3481a59630f7.png)

출처 : [위키백과](https://ko.wikipedia.org/wiki/Join_(SQL))

## quiz

```
-- 사번이 101인 사원의 근무 이력.
-- 근무 당시의 정보를 아래를 참고하여 출력.
-- 출력 컬럼명 : 사번, 이름, 부서이름, 직급이름, 시작일, 종료일
-- 날짜의 형식은 00.00.00
select employee_id, first_name, department_name , job_title, start_date, date_format(start_date, '%y.%m.%d') 시작일, date_format(end_date, '%y.%m.%d') 종료일
from employees e join job_history jh
using (employee_id)
join departments d
on jh.department_id = d.department_id
join jobs j
on j.job_id = jh.job_id
where employee_id = 101;

-- 위의 정보를 출력 하였다면 위의 정보에 현재의 정보를 출력.
-- 현재 근무이력의 시작일은 이전 근무이력의 종료일 + 1일로 설정.
-- 종료일은 null로 설정.
select employee_id, first_name, department_name, job_title, date_format(start_date, '%y.%m.%d') 시작일, date_format(end_date, '%y.%m.%d') 종료일
from employees e join job_history jh
using (employee_id)
join departments d
on jh.department_id = d.department_id
join jobs j
on j.job_id = jh.job_id
where employee_id = 101
union
select e.employee_id, e.first_name, d.department_name, job_title, 
	(select date_format(date_add(max(end_date), interval 1 day), '%y.%m.%d') from job_history where employee_id = 101) 시작일
    , null 종료일
from employees e join job_history jh
using (employee_id)
join departments d
on e.department_id = d.department_id
join jobs j
on j.job_id = e.job_id
where e.employee_id = 101
order by 시작일 desc; -- 이쁘게 시작일 내림차순 실시
```
