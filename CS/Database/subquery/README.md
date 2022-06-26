다시 올리는 erd 이미지
![image](https://user-images.githubusercontent.com/19484971/172144116-61b67ae5-3427-4b12-8da2-6d827de0241b.png)

# Subquery

다른 쿼리 내부에 포함 되어있는 쿼리문을 의미한다.

+ 외부 쿼리(outer query) : 서브 쿼리를 포함하고 있는 쿼리, 메인 쿼리라고도 한다.
+ 내부 쿼리(inner query) : 서브 쿼리의 다른 이름
+ 서브 쿼리는 단일 행 또는 다중 행 비교 연산자와 함께 사용된다.
  + 비교 연산자 오른쪽에, 괄호로 감싸져 있어야 한다.
+ 다양한 절에서 사용할 수 있다.
  + select, from, where, having, order by 등.. 에서 사용이 가능하다.
+ 종류
  + 중첩 서브 쿼리(Nested Subquery) : Where 문에 작성하는 서브쿼리
    + 단일 행, 다중 행, 다중 컬럼이 있다.
  + 인라인 뷰(Inline View) : From 문에 작성하는 서브쿼리
  + 스칼라 서브쿼리(Scalar Subquery) : select 문에 작성하는 서브 쿼리

+ 예시

```
-- 사번이 100인 사원의 부서이름
-- join
select department_name
from employees e join departments d
on e.department_id = d.department_id
where e.employee_id = 100;

-- subquery
select department_name
from departments
where department_id = ( select department_id
						from employees
						where employee_id = 100);
```

![image](https://user-images.githubusercontent.com/19484971/175817774-f689b8b7-5135-4724-b442-85e85355f73a.png)

이렇게 조인을 서브쿼리로 바꿔 표현할 수 있다.   
기본적으로는 속도상 서브쿼리를 지양하고 조인을 지향한다.   
그런데 5.6버전부터 옵티마이저가 좋아지면서 꼭 조인을 사용하지 않아도 될 정도로 속도가 비슷해졌다고 한다.

+ 참고
  + https://jojoldu.tistory.com/520

## Nested Sebquery

Where 문에 작성하는 서브쿼리

### 단일행

서브쿼리의 결과가 단일행을 리턴하는 경우

#### 예시

```
-- 부서가 ‘seattle’에 있는 부서의 부서 번호, 부서 이름.
-- 단일행
select department_id, department_name
from departments
where location_id = (
	select location_id
	from locations
	where city = 'Seattle');
```
![image](https://user-images.githubusercontent.com/19484971/175820236-6ef033cb-b578-4e76-be1e-b280c4131b09.png)

```
-- ‘adam’과 같은 부서에 근무하는 사원의 사번, 이름, 부서번호.
select employee_id, first_name, department_id
from employees
where department_id = (
	select *
	from employees
	where first_name = 'Adam');
```
![image](https://user-images.githubusercontent.com/19484971/175820261-bb17d492-b7a8-4da4-a75e-f7e6499173cf.png)

```
-- 전체 사원의 평균 급여보다 많이 받는 사원의 사번, 이름, 급여.
-- 급여순 정렬
-- order by에 숫자를 넣으면 해당 번째의 컬럼의 내림차순으로 정렬이 된다.
select employee_id, first_name, salary
from employees
where salary > (select avg(salary) from employees)
order by 3 desc;
```
![image](https://user-images.githubusercontent.com/19484971/175821626-1f51efe5-1f9b-457c-8125-c6100867d6cb.png)

### 다중행

서브쿼리의 결과가 다중행을 리턴하는 경우

#### 예시

다중 행이 반환되므로 단일 행과는 다른 키워드를 사용해야 한다.   
대표적으로 `in`이 있다.

```
-- 근무 도시가 ‘seattle’(대소문자 구분X)인 사원의 사번, 이름.
-- 다중행 (in)
select employee_id, first_name
from employees
where department_id in (
	select department_id
	from departments
	where location_id = (
		select location_id
		from locations
		where upper(city) = upper('seattle')));
```
![image](https://user-images.githubusercontent.com/19484971/175823326-9d292c79-cea2-449a-81ad-f7fdc770286a.png)

```
-- 모든 사원 중 적어도(최소급여자보다) 30번 부서에서 근무하는 사원의 급여보다 많이 받는 사원의 사번, 이름, 급여, 부서번호
-- 다중행 (any)
select employee_id, first_name, salary, department_id
from employees
where salary > any (
	select salary
	from employees
	where department_id = 30);
	
-- 30번 부서의 가장 급여가 작은 사람보다 급여가 많은 사람이라고 해석할 수도 있으므로
select employee_id, first_name, salary, department_id
from employees
where salary > (
	select min(salary)
    from employees
    where department_id = 30);
```
![image](https://user-images.githubusercontent.com/19484971/175823406-f1c2e910-59e8-4b18-a862-6297c21db4ea.png)

```
-- 30번 부서에서 근무하는 모든(최대급여자보다) 사원들보다 급여를 많이 받는 사원의 사번, 이름, 급여, 부서번호.
-- 다중행 (all)
select employee_id, first_name, salary, department_id
from employees
where salary > all (
	select salary
    from employees
    where department_id = 30);

-- 30번 부서의 가장 급여가 많은 사람보다 급여가 많은 사람이라고 해석할 수도 있으므로
select employee_id, first_name, salary, department_id
from employees
where salary > (
	select max(salary)
	from employees
	where department_id = 30);
```
![image](https://user-images.githubusercontent.com/19484971/175823603-01a6dd55-9dc6-438e-a6c1-fb27a2c166e3.png)

### 다중열

서브쿼리의 결과가 다중열을 리턴하는 경우

#### 예시

```
-- 다중열
-- 커미션을 받는 사원중 매니저 사번이 148인 사원의 급여와 부서번호가 일치하는 사원의 사번, 이름
select salary, department_id
from employees
where (salary, department_id) in (
	select salary, department_id
 	from employees
	where commission_pct is not null
	and manager_id = 148);
```
![image](https://user-images.githubusercontent.com/19484971/175823718-3125fd3c-b296-4e00-adfb-ad65febb6786.png)


## Inline View

From 문에 작성하는 서브쿼리

+ View 처럼 결과가 동적으로 생성된 테이블로 사용이 가능하다.
	+ 임시적인 뷰이기 때문에 당연히 DB에는 저장되지 않는다.
	+ 동적으로 생성 되었으므로 컬럼을 참조할 수 있다.

### 예시

```
-- 인라인뷰(Inline View)
-- 모든 사원의 평균 급여보다 적게 받는 사원들과 같은 부서에서 근무하는 사원의 사번, 이름, 급여, 부서번호
select employee_id, first_name, salary, a.department_id
from employees e join (
	select distinct department_id
	from employees
	where salary < (select avg(salary) from employees)
) a
on e.department_id = a.department_id;

-- 아래와 같이 작성할 수도 있다.
select employee_id, first_name, salary, department_id
from employees
where department_id in (
	select department_id
	from employees
	where salary < (select avg(salary) from employees));
```
![image](https://user-images.githubusercontent.com/19484971/175825791-50184437-a966-4e10-9191-935a55601071.png)

상위 N개를 가져오는 쿼리문은 필수적이지만, 직접 구현하지는 않는다고 하셨다. 라이브러리를 사용한다는 의미로 받아들였다.
```
-- TopN 질의
-- 모든 사원의 사번, 이름, 급여를 출력.(단 아래의 조건 참조)
--   1. 사원 정보를 급여순으로 정렬.
--   2. 한 페이지당 5명이 출력.
--   3. 현재페이지가 3페이지라고 가정. (급여 순 11등 ~ 15등까지 출력)

-- @가 붙은 것은 변수이다.
-- 현재 페이지가 3페이지이므로...
set @pageno = 3;

-- 급여순으로 정렬한 테이블에 행 번호를 만든 테이블을 만들고 특정 행 번호만을 추출하면 원하는 테이블을 뽑을 수 있다.
select b.rn, b.employee_id, b.first_name, b.salary
from (
	select @rownum := @rownum + 1 as rn, a.*
	from (
			select employee_id, first_name, salary
			from employees
			order by salary desc
		) a, (select @rownum := 0) tmp
	) b
where b.rn > (@pageno * 5 - 5) and b.rn <= (@pageno * 5);

-- MySQL은 limit로 해결한다.
select first_name, salary
from employees
order by salary desc limit 10, 5;
```
![image](https://user-images.githubusercontent.com/19484971/175826094-cb64518f-df3e-4319-9d58-e4f1dec4c1d8.png)

## Scalar Subquery

select 절에 잇는 서브 쿼리, 한 개의 행만을 반환해야 한다.

### 예시

물론 조인으로도 만들 수 있다.   
교수님이 예시를 만들기 힘드셨나보다 하하..

```
-- 직급 아이디가 IT_PROG인 사원의 사번, 이름, 직급아이디, 부서이름
select employee_id, first_name, job_id,
	(select department_name
	from departments d
	where e.department_id = d.department_id) as department_name
from employees e
where job_id = 'IT_PROG';
```
![image](https://user-images.githubusercontent.com/19484971/175826767-3a9f09b0-6af3-436f-aeed-c2f7facb7ec2.png)

```
-- 60번 부서에 근무하는 사원의 사번, 이름, 급여, 부서번호, 60번부서의 평균급여
select e.employee_id, e.first_name, salary, department_id,
	(select avg(salary) from employees where department_id = 60) as avg60
from employees e
where department_id = 60;
```
![image](https://user-images.githubusercontent.com/19484971/175826983-22afb0a2-1de6-460b-9945-003a93f7d575.png)
