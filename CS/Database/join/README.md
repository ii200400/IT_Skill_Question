# Join

원래는 DML의 select절에 같이 있어야 하나 내용과 종류가 많아 따로 작성한다.   

+ 서로 관련이 있는 둘 이상의 테이블에서 데이터가 필요한 경우에 사용한다.
+ 일반적으로 조인조건을 포함하는 WHERE절을 (테이블 수 - 1)개를 사용한다.
+ 조인조건은 일반적으로 각 테이블의 PK 혹은 FK를 사용한다.

+ 종류
	+ CROSS JOIN(CARTESIAN JOIN)
	+ INNER JOIN
		+ Equi JOIN
			+ NATURAL JOIN
		+ None - Equi JOIN
	+ OUTER JOIN
		+ LEFT OUTER JOIN
		+ RIGHT OUTER JOIN
		+ FULL OUTER JOIN (MySQL에는 없다.)
	+ SELF JOIN
	
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
	+ https://doh-an.tistory.com/30 (예시 이미지가 정말 좋다. 나보다 잘 정리한듯..)

</br>

## CROSS JOIN(CARTESIAN JOIN, 교차조인)

일반적으로 `CARTESIAN JOIN`보다는 `CARTESIAN PROJECT`라고 작성하는 것 같은데 필자는 수학의 곱집합과 영문명이 완전 똑같은 것에 햇갈려서 `CARTESIAN JOIN`라고 작성하였다. 조인 조건이 없거나 조건을 부적절하게 작성할 경우 일어나는 조인이다.

이름에서 유추할 수 있듯이 두 테이블의 행을 곱해서 (테이블A의 행 수)\*(테이블B의 행 수)의 행을 가지는 테이블이 만들어지는데, 거의 안쓰인다고 한다. ~~이거 쓰면 오히려 테이블 잘못 작성했다는 합리적 의심을 한다고 언급하셨다..~~

### 예시

아래의 두 테이블을 교차조인을 하면

![image](https://user-images.githubusercontent.com/19484971/171558050-f26a3eef-5f21-4f27-a080-2c8d0ea6087b.png)

```
SELECT *
FROM employee CROSS JOIN department;

-- 교차조인을 암묵적으로 아래와 같이 사용할 수도 있다.

SELECT *
FROM employee, department;
```

아래와 같은 결과가 나온다.

![image](https://user-images.githubusercontent.com/19484971/171558093-be98d4f8-d809-454c-b4a7-3481a59630f7.png)

출처 : [위키백과](https://ko.wikipedia.org/wiki/Join_(SQL))

## INNER JOIN

+ 가장 일반적으로 사용되는 JOIN의 종류 
	+ 위의 예시도 INNER JOIN이다.
	+ 단순히 JOIN이라고 해도 INNER JOIN으로 판단한다.
+ 동등 조인(Equi-join)이라고도 하며, N개의 테이블 조인 시 N-1개의 조인 조건을 사용한다.
	+ 조인 조건은 두 테이블이 공통으로 가지는 컬럼을 사용한다.
	+ using절을 이용하면 조금 더 편하게 조인 조건을 만들 수 있다.
	+ natural join을 사용하면 두 테이블이 가지는 동일한 컬럼명들을 기준으로 자동으로 조인을 해준다.
		+ 하지만 원치않는 조인 조건이 포함되버릴 수도 있기 때문에 주의해주어야 한다.
+ on은 join이 실행되기 전에, where는 join이 실행된 후 실행된다.
	+ 때문에 join조건은 on절에, 일반조건은 where절에 작성하여 구분한다.

### 예시

```
-- 사번이 100인 사원의 사번, 이름, 급여, 부서이름
-- inner join
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름
from employees e inner join departments d
on e.department_id = d.department_id 
where employee_id = 100;

-- 사번이 100인 사원의 사번, 이름, 급여, 부서이름, 근무하는 도시 이름
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름, city
from employees e, departments d, locations l
where e.department_id = d.department_id 
and d.location_id = l.location_id
and	employee_id = 100;

-- 위와 같은 내용
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름, city
from employees e inner join departments d inner join locations l
on e.department_id = d.department_id 
and d.location_id = l.location_id
where employee_id = 100;

-- 가독성을 생각하여 아래와 같이 쓰는 방법도 있다, 속도와 의미는 동일하다.
select e.employee_id 사번, e.first_name 이름, e.salary 급여, department_name 부서이름, city
from employees e inner join departments d 
on e.department_id = d.department_id 
inner join locations l
on d.location_id = l.location_id
where employee_id = 100;

-- using 절
-- 조인 조건를 편리하게 작성할 수 한다. 
-- employees의 department_id나 departments의 department_id나 같은 컬럼명이기 때문에 둘 중 아무거나 사용해도 상관없으니 만들어진 듯 하다.
-- using e.departent_id 와 같이 쓰면 오히려 에러가 난다.
select e.employee_id 사번, e.first_name 이름, e.salary 급여, d.department_id, d.department_name 부서이름
from employees e inner join departments d
using (department_id) 
where employee_id = 100;
```

## OUTER JOIN

어느 한쪽 테이블에는 해당 데이터가 존재하는데 다른 쪽 테이블에는 존재하지 않을 경우 해당 데이터가 검색되지 않는 문제를 해결하기 위해 사용한다.

+ 종류
	+ LEFT OUTER JOIN
	+ RIGHT OUTER JOIN
	+ FULL OUTER JOIN

```
-- 회사에 근무하는 모든 사원의 사번, 이름, 부서이름
-- 106명 >> 문제 발생.. 1명이 없다;
select e.employee_id, e.first_name, ifnull(d.department_name, '승진발령')
from employees e join departments d
on e.department_id = d.department_id;

-- left outer join 사용
-- 조건에 만족은 하지 않지만 왼쪽(사원) 테이블의 데이터는 출력하도록 한다.
-- 부서가 없는(부서번호가 null) 사원 검색
-- 107명
select employee_id 사번, first_name 이름, ifnull(department_name, '승진 발령') 부서이름
from employees e left outer join departments d
on e.department_id = d.department_id;

-- 사원이 없는 부서의 정보는 출력이 안된다.
select department_id, department_name, employee_id, first_name
from employees e join departments d
using (department_id);

-- right outer join 사용
-- 조건에 만족은 하지 않지만 오른쪽 테이블의 데이터도 출력하도록 한다.
select department_id, department_name, employee_id, first_name
from employees e right outer join departments d
using (department_id);

-- union 두 컬럼을 더한다.(합집합의 개념) 단, 두 컬럼의 컬럼은 순서대로 매칭되어야 한다. 
-- full outer join과 같은 효과, mysql에는 full outer join이 없어 union으로 구현;
-- union all을 하면 중복되는 (교집합)부분을 그대로 한번 더 출력한다.
select ifnull(d.department_name, '승진발령'), e.employee_id, e.first_name
from employees e left outer join departments d
on e.department_id = d.department_id
union
select department_name, employee_id, first_name
from employees e right outer join departments d
using (department_id);

```

## SELF JOIN

같은 테이블끼리 하는 join

```
-- self join 사용
-- 매니저는 사원이기도 하므로 employees이 스스로를 join할 필요가 있다.
-- 사장님의 경우 매니저가 없으므로 left outer join을 활용하여 출력할 수 있도록 한다.
-- 모든 사원의 사번, 이름, 매니저사번, 매니저이름(!)
select e.employee_id, e.first_name, e.manager_id, ifnull(m.first_name, '사장님이당')
from employees e left outer join employees m
on e.manager_id = m.employee_id;
```

## None - Equi JOIN

테이블의 PK, FK가 아닌 일반 컬럼을 조인 조건으로 지정하는 join
+ 같지 않다가 아니라 단순히 equi이 아닌 비교문들 >, <= 같은 것들을 의미한다.

```
-- None-Equi join
-- 급여등급을 구하기 위해서는 salgrades의 losal과 hisal의 등급별 범위 내에 있어야 하므로 join 조건이 범위형식을 취하게 된다.
-- 모든 사원의 사번, 이름, 급여, 급여등급(!)
select e.employee_id, e.first_name, e.salary, s.grade
from employees e join salgrades s
on e.salary between s.losal and s.hisal;
```
