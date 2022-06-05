# select절 실습 내용

+ 모든 사원의 모든 정보 검색.
```
select *
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041091-c4f0c4f0-560f-4631-9765-da36b0423b92.png)

+ 사원이 근무하는 부서의 부서번호 검색.
```
select department_id
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041127-fcfe00a0-ff1f-4a0a-873b-b5b7b670127a.png)

+ 사원이 근무하는 부서의 부서번호 검색. (distinct로 중복제거)
	+ **회사에 존재하는 모든 부서번호가 아니라** 테이블에서 확인할 수 있는 사원들의 부서번호들이다.
```
select distinct department_id
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041169-4175c0c2-dd39-4585-942f-d929d26c53fb.png)

+ 모든 사원의 사번, 이름, 급여, 급여 * 12 (연봉) 검색.
	+ as키워드로 alias를 사용할 수 있다. 키워드는 생략이 가능하며 띄어쓰기나 특수문자가 들어간 경우 "로 감싸주어야 한다.
	+ 사칙연산을 넣어 필드 값을 조정할 수 있다.
```
select employee_id 사번, first_name "이 름", salary as 급여, salary * 12
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041380-c5d299d3-7f51-4995-bf68-1431707e6cf4.png)


+ 모든 사원의 사번, 이름, 급여, 급여 * 12 (연봉), 커미션, 커미션포함 연봉 검색.
	+ ifnull은 null이면 두번째 파라미터를 반환하는 함수
```
select employee_id 사번, first_name "이 름", salary as 급여, salary * 12, commission_pct, salary * (1 + ifnull(commission_pct, 0)) * 12 "커미션포함연봉"
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041325-ed6ac4c6-3706-4f78-a7b8-afde9e2d6a41.png)

+ 모든 사원의 사번, 이름, 급여, 급여에 따른 등급표시 검색.
	+ 급여에 따른 등급
		+ 15000 이상 "고액연봉"
		+ 8000 이상 "평균연봉"
		+ 8000 미만 "저액연봉"      
```
select employee_id, first_name, salary,
	case when salary >= 15000 then '고액연봉'
		when salary >= 8000 then '평균연봉'
		else '저액연봉'
  end 등급
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041534-f5b7eb44-e933-4766-9319-1cee11bd0af8.png)

+ 부서번호가 50인 사원중 급여가 7000이상인 사원의 사번, 이름, 급여, 부서번호
```
select employee_id, first_name, salary, department_id
from employees
where department_id = 50 and salary >= 7000;
```
![image](https://user-images.githubusercontent.com/19484971/172041580-3f839d60-f137-489a-9b9c-b56fe7402b32.png)

+ 근무 부서번호가 50 혹은 60 혹은 70에 근무하는 사원의 사번, 이름, 부서번호
	+ in을 활용하면 좋다!
```
select employee_id, first_name, salary, department_id
from employees
where department_id = 50 or department_id = 60 or department_id = 70;

-- 위와 동일한 작업 수행
select employee_id, first_name, salary, department_id
from employees
where department_id in (50, 60, 70);
```
![image](https://user-images.githubusercontent.com/19484971/172041663-bee732bd-a527-49a2-bda2-c3916ee067fc.png)

+ 근무 부서번호가 50, 60, 70이 아닌 사원의 사번, 이름, 부서번호
	+ not in을 활용하면 좋다!
```
select employee_id, first_name, salary, department_id
from employees
where department_id != 50 and department_id != 60 and department_id != 70;

select employee_id, first_name, salary, department_id
from employees
where department_id not in (50, 60, 70);
```
![image](https://user-images.githubusercontent.com/19484971/172042269-07e56db3-5e9a-4aec-8f2b-11387ae65e91.png)

+ 급여가 6000이상 10000이하인 사원의 사번, 이름, 급여
```
select employee_id, first_name, salary, department_id
from employees
where salary >= 6000 and salary <= 10000;

select employee_id, first_name, salary, department_id
from employees
where salary between 6000 and 10000;
```
![image](https://user-images.githubusercontent.com/19484971/172042312-9e14eddb-2782-44af-961d-980cecea0563.png)

+ 근무 부서가 지정되지 않은(알 수 없는) 사원의 사번, 이름, 부서번호 검색.
	+ null은 is를 통해서 비교를 진행해야 한다.
```
select employee_id, first_name, salary, department_id
from employees
where department_id is null;
```
![image](https://user-images.githubusercontent.com/19484971/172042357-66520926-95c8-42bf-bc77-5921eb156639.png)

+ 근무 부서가 지정된 사원의 사번, 이름, 부서번호 검색.
```
select employee_id, first_name, salary, department_id
from employees
where department_id is null;
```
![image](https://user-images.githubusercontent.com/19484971/172042630-75f6bfc0-5572-46fb-a668-d7e8779257df.png)

+ 이름에 'x'가 들어간 사원의 사번, 이름
	+ %는 길이가 0 이상인 문자열을 대표한다.
```
select employee_id, first_name, salary, department_id
from employees
where first_name like '%x%';
```
![image](https://user-images.githubusercontent.com/19484971/172042644-416f501b-9bbb-4256-892e-c483ee0e24bc.png)

+ 이름의 끝에서 3번째 자리에 'x'가 들어간 사원의 사번, 이름
	+ \_는 문자 1개를 대표한다.
```
select employee_id, first_name, salary, department_id
from employees
where first_name like '%x__';
```
![image](https://user-images.githubusercontent.com/19484971/172042664-fb862d1b-bd71-44fe-a65a-cf2e6e95a799.png)

<br>

+ 더 많은 와일드 문자를 확인하려면 [링크](https://www.w3schools.com/sql/sql_wildcards.asp)를 확인하자.
	+ <img src="https://user-images.githubusercontent.com/19484971/172042781-89fd85f5-4069-437f-86e5-aca07755f35b.png"  width="400"/>

<br>

+ 모든 사원의 사번, 이름, 급여 / 단, 급여순 정렬(내림차순)
	+ asc 오름차순, desc 내림차순
```
select employee_id, first_name, salary, department_id
from employees
order by salary desc;
```
![image](https://user-images.githubusercontent.com/19484971/172042697-f9f660f4-8370-42d3-9237-64d21297f4d3.png)

+ 50, 60, 70에 근무하는 사원의 사번, 이름, 부서번호, 급여 / 단, 부서별 정렬(오름차순) 후 급여순(내림차순) 검색
```
select employee_id, first_name, salary, department_id
from employees
where department_id in (50, 60, 70)
order by department_id, salary desc;
```
![image](https://user-images.githubusercontent.com/19484971/172042707-608f1556-8bab-4602-b235-779869f10317.png)
