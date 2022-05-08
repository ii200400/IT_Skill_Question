# select절 실습 내용 (미완료)

```
-- 모든 사원의 모든 정보 검색.
select *
from employees;

-- 사원이 근무하는 부서의 부서번호 검색.
select department_id
from employees;

-- 사원이 근무하는 부서의 부서번호 검색.(중복제거)
-- 회사에 존재하는 모든 부서번호가 아님에 주의
select distinct department_id
from employees;

-- 모든 사원의 사번, 이름, 급여, 급여 * 12 (연봉) 검색.
-- as키워드로 alias를 사용할 수 있다. 키워드는 생략이 가능하며 띄어쓰기나 특수문자가 들어간 경우 "로 감싸주어야 한다.
-- 사칙연산을 넣어 필드 값을 조정할 수 있다.
select employee_id 사번, first_name "이 름", salary as 급여, salary * 12
from employees;

-- 모든 사원의 사번, 이름, 급여, 급여 * 12 (연봉), 커미션, 커미션포함 연봉 검색.
-- ifnull은 null이면 두번째 파라미터를 반환하는 함수
select employee_id 사번, first_name "이 름", salary as 급여, salary * 12,
commission_pct, salary * (1 + ifnull(commission_pct, 0)) * 12 "커미션포함연봉"
from employees;

-- 모든 사원의 사번, 이름, 급여, 급여에 따른 등급표시 검색.
-- 급여에 따른 등급
--   15000 이상 “고액연봉“      
--   8000 이상 “평균연봉”      
--   8000 미만 “저액연봉＂

select employee_id, first_name, salary,
	case when salary >= 15000 then '고액연봉'
		when salary >= 8000 then '평균연봉'
		else '저액연봉'
  end 등급
from employees;


-- 근무 부서번호가 50 혹은 60 혹은 70에 근무하는 사원의 사번, 이름, 부서번호
select employee_id, first_name, salary, department_id
from employees
where department_id = 50 or department_id = 60 or department_id = 70;

select employee_id, first_name, salary, department_id
from employees
where department_id in (50, 60, 70);

-- 급여가 6000이상 10000이하인 사원의 사번, 이름, 급여
select employee_id, first_name, salary, department_id
from employees
where salary >= 6000 and salary <= 10000;

select employee_id, first_name, salary, department_id
from employees
where salary between 6000 and 10000;

-- 근무 부서가 지정되지 않은(알 수 없는) 사원의 사번, 이름, 부서번호 검색.
-- null은 is를 통해서 비교를 진행해야 한다.
select employee_id, first_name, salary, department_id
from employees
where department_id is null;

-- 이름에 'x'가 들어간 사원의 사번, 이름
-- %는 크기가 0 이상의 문자열을 대표한다.
select employee_id, first_name, salary, department_id
from employees
where first_name like '%x%';

-- 이름의 끝에서 3번째 자리에 'x'가 들어간 사원의 사번, 이름
-- _는 문자 1개를 대표한다.
select employee_id, first_name, salary, department_id
from employees
where first_name like '%x__';

-- 모든 사원의 사번, 이름, 급여
-- 단 급여순 정렬(내림차순)
-- asc 오름차순, desc 내림차순
select employee_id, first_name, salary, department_id
from employees
order by salary desc;

-- 50, 60, 70에 근무하는 사원의 사번, 이름, 부서번호, 급여
-- 단, 부서별 정렬(오름차순) 후 급여순(내림차순) 검색
select employee_id, first_name, salary, department_id
from employees
where department_id in (50, 60, 70)
order by department_id, salary desc;
```
