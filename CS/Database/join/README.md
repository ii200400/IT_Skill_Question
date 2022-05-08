# Join 실습 내용

```
-- 사번이 100인 사원의 사번, 이름, 급여, 부서이름 (alias 사용)
select employee_id 사번, first_name 이름, salary 급여, department_name 부서이름
from employees e,  departments d
where e.department_id = d.department_id and employee_id = 100;


```
