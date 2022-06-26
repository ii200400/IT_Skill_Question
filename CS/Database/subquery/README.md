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

## Inline View



## Scalar Subquery




