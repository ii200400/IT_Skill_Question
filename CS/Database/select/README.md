# select절 실습 내용

실습 내용을 그대로 옮겨 작성하면서 내용을 상기하려고 작성한 페이지이다. 읽는 것은 원활하지만, 작성은.. 자신없다. 하하하하!

## keywords

DISTINCT나 GROUP BY는 Statement, WHERE는 Clause(절), ORDER BY는 Keyword, IN이나 BETWEEN은 Operator 등으로 분류하는데 실습을 분류 기준으로 나누면 순서가 어질러져서 그냥 그대로 작성하였다!

keywords나 Operator도 w3schools에서 정리한 내용 기준이고 강의에서는 따로 분류하지 않고 배워서 필자는 정확히 분류를 하지도 않고 신경도 잘 안쓰고 있다. 하지만, 강의에서 function 은 따로 분류하여 진행하였으므로 따로 있다.

각 분류별 내용을 확인하고 싶다면 [w3schools](https://www.w3schools.com/sql/default.asp)참고

### 기본

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

### DISTINCT

+ 사원이 근무하는 부서의 부서번호 검색. (distinct로 중복제거)
	+ **회사에 존재하는 모든 부서번호가 아니라** 테이블에서 확인할 수 있는 사원들의 부서번호들이다.
```
select distinct department_id
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172041169-4175c0c2-dd39-4585-942f-d929d26c53fb.png)

### Aliases

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

### CASE

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

### WHERE

+ 부서번호가 50인 사원중 급여가 7000이상인 사원의 사번, 이름, 급여, 부서번호
```
select employee_id, first_name, salary, department_id
from employees
where department_id = 50 and salary >= 7000;
```
![image](https://user-images.githubusercontent.com/19484971/172041580-3f839d60-f137-489a-9b9c-b56fe7402b32.png)

### IN

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

### BETWEEN

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

### Null

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

### like & wild Characters

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

### Order By

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

## Group By

```
-- 부서 번호, 부서별 급여의 총합, 평균급여

-- select department_id, sum(salary), avg(salary)
-- from employees;

select department_id, sum(salary), avg(salary)
from employees
where department_id is not null
group by department_id
order by department_id;

-- 각 부서별 최고 급여와 최저 급여

select department_id, max(salary), min(salary)
from employees
group by department_id;

-- 부서별 평균 급여가 7000이상인 부서 번호, 평균 급여
-- select department_id, avg(salary)
-- from employees
-- where avg(salary) > 7000
-- group by department_id;

select department_id, avg(salary)
from employees
group by department_id
having avg(salary) > 7000;

-- 40, 50, 60번 부서에서 근무하는 사원들 중 job_id별 급여 합이 50000보다 큰 job_id별 평균 급여
-- 평균급여를 내림차순으로 정렬
select job_id, avg(salary)
from employees
where department_id in (40, 50, 80)
group by job_id
having sum(salary) > 50000
order by avg(salary) desc;

-- 입사 년도별 인원수와 평균 급여를 구하여라

select year(hire_date) hd, count(*), avg(salary)
from employees
group by hd
order by hd desc;
```

## Function

### abs

+ 숫자의 절대값을 반환하는 함수
```
select abs(-5), abs(0), abs(+5)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044033-e0ec8057-8417-452f-97e8-a8abff1fadfe.png)

### ceil

+ 소수점 첫째 자리에서 올림을 하는 함수
```
select ceil(12.2), ceiling(12.2), ceil(-12.2), ceiling(-12.2)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044060-5e39f3c0-1fec-4716-a1bb-a71e5b66ba23.png)

### floor

+ 소수점 첫째 자리에서 버림을 하는 함수
```
select floor(12.6), floor(-12.2)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044094-73a597cd-31a5-4e0d-bb92-95d91eeaf4bc.png)

### round

+ 소수점 첫째 자리에서 반올림을 하는 함수
	+ 원한다면 다른 자리수에서도 반올림 가능
```
select round(1526.159), round(1526.159, 0), round(1526.159, 1), round(1526.159, 2), round(1526.159, -1), round(1526.159, -3)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044122-6f96beaf-3301-454f-afec-ea4dffc0cc85.png)

### truncate

+ 숫자를 자르는 함수
	+ 양수와 음수를 활용하여 수소점 아래, 위 부분에서 숫자를 잘라 표현한 위치를 지정한다.
```
select truncate(1526.159, 0), truncate(1526.159, 1), 
	   truncate(1526.159, 2), truncate(1526.159, -1), truncate(1526.159, -3)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044258-7d583d57-bcfe-4d58-ac10-96a175cf5ff3.png)

### pow

+ 제곱을 하는 함수
	+ 첫째 파라미터를 두번째 파라미터 만큼 제곱한 수를 반환한다.
```
select pow(2, 3), power(3, 2)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044380-30c9dabe-5aa6-4fcf-aa73-bebd77877f4a.png)

### mod

+ 나누기 연산을 하는 함수
	+ 함수를 사용하지 않고 연산자를 이용하도 된다.
```
select mod(8, 3), 8 % 3
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044413-98ea6056-2d3c-4efe-8ac0-d7821746ceb8.png)

### greatest & least

+ 수들 중 가장 큰 / 작은 수를 반환하는 함수
```
select greatest(4, 3, 7, 5, 9), least(4, 3, 7, 5, 9)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044726-c7a5dbad-1b99-4a6f-8650-e53e84dfee04.png)

### ASCII

+ 문자의 아스키 값을 반환하는 함수
```
select ASCII('0'), ASCII('A'), ASCII('a')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044739-18887640-b38a-4e95-9d19-ee35b6881e52.png)

### concat

+ 문자들을 합치는 함수
	+ 임의로 회원번호가 100인 사원의 이름을 테이블에서 가져와 사용하였다.
```
select concat(employee_id, '번 사원의 이름 ', first_name,' ' , last_name)
from employees
where employee_id = 100;
```
![image](https://user-images.githubusercontent.com/19484971/172044801-8990703a-5356-4c4c-adf1-738206b58911.png)

### insert

+ 문자열에서 특정 위치의 문자열을 다른 문자열로 대체하는 함수
	+ mysql에서는 인덱스가 1부터 시작한다. 햇갈린다;
```
select insert('helloabc!!!', 6, 3, ' world ')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044825-61a89fc6-eaf8-4c9f-9f1a-bc82aa91f4e4.png)

### replace

+ 문자열에서 특정 문자열을 다른 문자열로 대체하는 함수
	+ 해당 특정 문자열이 여러 번 들어가 있다면 모두 대체한다.
```
select replace('helloabcabc!!!', 'abc', ' world ')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044964-6e3c2732-67c6-47f3-801b-319ac6ce2a1f.png)


```
-- 7
select instr('hello ssafy !!!', 'ssafy')
from dual;

-- ssafy
select mid('hello ssafy !!!', 7, 5), substring('hello ssafy !!!', 7, 5)
from dual;

-- hello ssafy !!!
select reverse('!!! yfass olleh')
from dual;

-- hello ssafy !!!  hello ssafy !!!
select lower('hELlo SsaFy !!!'), lcase('hELlo SsaFy !!!')
from dual;

-- HELLO SSAFY !!!  HELLO SSAFY !!!
select upper('hELlo SsaFy !!!'), ucase('hELlo SsaFy !!!')
from dual;

-- hello  fy !!!
select left('hello ssafy !!!', 5), right('hello ssafy !!!', 6)
from dual;

-- ------------------- 날짜 관련 함수 ----------------------
-- 2020-08-01 23:17:11  2020-08-01 23:17:11  2020-08-01 23:17:11
select now(), sysdate(), current_timestamp()
from dual;

-- 2020-08-01  2020-08-01  23:18:33  23:18:33
select curdate(), current_date(), curtime(), current_time()
from dual;

-- 2020-08-01 23:23:19	2020-08-01 23:23:24	2020-08-02 04:23:19	2020-08-06 23:23:19
select now() 현재시간, date_add(now(), interval 5 second) 5초후,
	   date_add(now(), interval 5 hour) 5시간후, date_add(now(), interval 5 day) 5일후
from dual;

-- 2020	8	August	Saturday	1	7	5	214	30
select year(now()), month(now()), monthname(now()), 
       dayname(now()), dayofmonth(now()), dayofweek(now()), 
	   weekday(now()), dayofyear(now()), week(now())
from dual;

-- 2020-08-02 00:21:50  2020 August 2 AM 12 21 50  20-08-02 00:21:50  20.08.02 Sunday  00시21분50초
select now(), date_format(now(), '%Y %M %e %p %l %i %S'), date_format(now(), '%y-%m-%d %H:%i:%s'),
	   date_format(now(), '%y.%m.%d %W'), date_format(now(), '%H시%i분%s초')
from dual;

-- ------------------- 논리 관련 함수 ----------------------
-- 크다  작다  3  b  a
select if(3 > 2, '크다', '작다'), if(3 > 5, '크다', '작다'), 
       nullif(3, 3), nullif(3, 5), 
	   ifnull(null, 'b'), ifnull('a', 'b')
from dual;

-- ------------------- 집계 함수 ----------------------
-- 사원의 총수, 급여의 합, 급여의 평균, 최고급여, 최저급여
select count(employee_id), sum(salary), avg(salary), max(salary), min(salary)
from employees;
```
