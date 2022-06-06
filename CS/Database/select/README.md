# select절 실습 내용

실습 내용을 그대로 옮겨 작성하면서 내용을 상기하려고 작성한 페이지이다. 읽는 것은 원활하지만, 작성은.. 자신없다. 하하하하!   
내용이 부족한 부분은 웹 공부할 때 항상 그렇듯이 w3schools 홈페이지(혹은 영문 위키)를 참고하였다.

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

+ 특정 문자열을 다른 문자열로 대체하는 함수
	+ 해당 특정 문자열이 여러 번 들어가 있다면 모두 대체한다.
```
select replace('helloabcabc!!!', 'abc', ' world ')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172044964-6e3c2732-67c6-47f3-801b-319ac6ce2a1f.png)

### instr

+ 특정 문자열의 시작 위치를 찾는 함수
	+ 문자열이 여러 개 들어가 있어도 첫번째 문자열의 시작 위치만 반환한다.
	+ mysql에서는 인덱스가 1부터 시작하는 것 잊지말자;
```
select instr('hello world world!!!', 'world')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172062406-ac6405d9-6502-4497-a37f-007300cbadf9.png)

### mid & substring

+ 특정 위치부터 특정 개수의 문자열을 반환하는 함수
```
select mid('hello world !!!', 7, 5), substring('hello world !!!', 7, 5)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172062430-6241b0e0-8a4a-4858-a622-b919bb128e65.png)

### reverse

+ 문자열을 역순으로 바꾸는 함수
```
select reverse('!!! dlrow olleh')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063104-060fd37c-adbf-4247-9fc2-fe3068af652c.png)

### lower & lcase

+ 문자열의 모든 문자를 소문자로 바꾸는 함수
```
select lower('hELlo World !!!'), lcase('hELlo WorLd !!!')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063202-c81b1936-dd93-4851-9b32-fbd059f03af2.png)

### upper & ucase

+ 문자열의 모든 문자를 대문자로 바꾸는 함수
```
select upper('hELlo World !!!'), ucase('hELlo World !!!')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063213-529df17f-798c-40e6-a649-b221f3b611a1.png)

### left & right

+ 왼쪽/오른쪽의 특정 문자 수만을 잘라내는 함수
```
select left('hello world !!!', 5), right('hello world !!!', 6)
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063299-12e76262-600d-439c-bda9-d47284fdd9c4.png)

### now

+ 현재 시간을 초 단위까지 보여주는 함수
	+ sysdate과 current_timestamp도 같은.. 기능을 하는 함수인가 보다. (그럼 왜 여러 개가 있을까?)
```
select now(), sysdate(), current_timestamp()
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063352-46767060-587b-4a56-95ef-1798dc420d94.png)

### curdate & curtime

+ 각각 현재 날짜와 시간만을 보여주는 함수
	+ 각각 current_date와 current_time로 대체가 가능하다.
```
select curdate(), current_date(), curtime(), current_time()
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063479-444dd4ca-90f0-48c8-a559-c6d20cdd51a2.png)

### date_add

+ 특정 시간으로부터 이후의 시간을 계산하여 반환하는 함수
	+ 참고로 음수도 입력 가능해서 5시간 전과 같은 시간 연산도 가능하다.
```
select now() 현재시간, date_add(now(), interval 5 second) 5초후, date_add(now(), interval 5 hour) 5시간후, date_add(now(), interval 5 day) 5일후
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063532-281bd1fe-6fa4-49ce-b577-b27f66f7a856.png)

### 날짜 함수들

+ 주어진 시간에서 다음과 같은 정보를 반환한다.
	+ year(date) : 연도
	+ month(date) : 월(숫자)
	+ monthname(date) : 월(영문)
	+ dayname(date) : 일(영문)
	+ dayofmonth(date) : 월
	+ dayofweek(date) : 일(숫자)
	+ weekday(date) : 해당 월의 몇 번째 주 인지
	+ dayofyear(date) : 해당 연도의 몇 번째 일 인지
	+ week(date) : 해당 연도의 몇 번째 주 인지
+ 참고로 날짜는 0부터 시작하며, 월요일을 0으로 일요일을 6으로 치환한다.
```
select now(), year(now()), month(now()), monthname(now()), dayname(now())
from dual;

select dayofmonth(now()), dayofweek(now()), weekday(now()), dayofyear(now()), week(now())
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172063677-e4586006-0cdc-411f-ac01-c4098ab70f4f.png)
![image](https://user-images.githubusercontent.com/19484971/172063697-e087f2d7-67a0-4edd-9a3e-829cf3ec6537.png)

### date_format

+ date format 형식으로 날짜 표현 방식을 설정하여 표시하는 함수
	+ date format 형식은 [이곳](https://www.w3schools.com/mysql/func_mysql_date_format.asp)에서 확인
```
select now(), date_format(now(), '%Y %M %e %p %l %i %S'), date_format(now(), '%y-%m-%d %H:%i:%s'),
	   date_format(now(), '%y.%m.%d %W'), date_format(now(), '%H시%i분%s초')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172064424-04dff326-8162-4fb9-bfc2-6df7f21e9452.png)
![image](https://user-images.githubusercontent.com/19484971/172064430-ce477d41-49a3-4dde-b405-b55e9753f016.png)

### 조건 함수

+ 조건문의 특징을 가지는 함수들이다.
	+ if : 삼항연산자를 생각하자.
	+ nullif : 두 매개변수가 같다면 null, 그렇지 않다면 첫 번째 매개변수를 반환
	+ ifnull : 첫 번째 매개변수가 null이라면 두 번째 매개변수를, 그렇지 않다면 첫 번째 매개변수를 반환
```
select if(3 > 2, '크다', '작다'), if(3 > 5, '크다', '작다'), nullif(3, 3), nullif(3, 5), ifnull(null, 'b'), ifnull('a', 'b')
from dual;
```
![image](https://user-images.githubusercontent.com/19484971/172064496-db8f1629-1ced-4af3-9fb1-a5fc193f69a1.png)

### 집계 함수

+ 데이터의 수나 합, 평균 등을 구하는 함수들
	+ count : 데이터의 수
	+ sum : 데이터의 합
	+ avg : 데이터의 평균
	+ max : 데이터의 최대값
	+ min : 데이터의 최소값
+ 임의로 사원 테이블을 사용하였다.
```
select count(employee_id), sum(salary), avg(salary), max(salary), min(salary)
from employees;
```
![image](https://user-images.githubusercontent.com/19484971/172064785-55e6917b-71e0-4779-9610-f69077f14d83.png)

## Group By

+ 사원들의 부서 번호, 부서별 급여의 총합, 평균급여
	+ 부서가 지정되지 않은 사원데이터가 있어 not null 을 사용
	+ 부서별로 묶기 위해서 group by 사용
		+ group by를 사용한 상태로 집계함수를 사용하면 특정 집합의 평균이나 총합을 구할 수 있다.
	+ 시각적 편의성을 위해서 order by 사용
```
select department_id, sum(salary), avg(salary)
from employees
where department_id is not null
group by department_id
order by department_id;
```
![image](https://user-images.githubusercontent.com/19484971/172086169-1cbf355f-f769-4869-b448-82b69ba44a43.png)

+ 각 부서별 최고 급여와 최저 급여
```
select department_id, max(salary), min(salary)
from employees
group by department_id;
```
![image](https://user-images.githubusercontent.com/19484971/172086643-c8f2e1ff-bd75-4848-bf10-f19ba1d200b8.png)

+ 부서별 평균 급여가 7000이상인 부서 번호, 평균 급여
	+ group by에 대한 조건문을 넣으려면 having을 사용해야 한다.
	+ where 절에 집계함수를 넣으면 Invalid use of group function 이라는 에러가 생긴다.
```
-- 에러가 난다.
-- select department_id, avg(salary)
-- from employees
-- where avg(salary) > 7000
-- group by department_id;

select department_id, avg(salary)
from employees
group by department_id
having avg(salary) > 7000;
```
![image](https://user-images.githubusercontent.com/19484971/172087114-f5954f4c-5f9b-4ac5-8414-faf914325986.png)
![image](https://user-images.githubusercontent.com/19484971/172087129-880389ab-fe03-4685-b3d1-43e5fcf27b55.png)

+ 40, 50, 60번 부서에서 근무하는 사원들 중 job_id별 급여 합이 50000보다 큰 job_id별 평균 급여
	+ order by에는 집계함수가 사용 가능하다.
	+ 적절하게 where절을 사용해야 한다.
```
select job_id, avg(salary)
from employees
where department_id in (40, 50, 80)
group by job_id
having sum(salary) > 50000
order by avg(salary) desc;
```
![image](https://user-images.githubusercontent.com/19484971/172087410-c51c89e4-5267-4046-af5c-c4824402ea60.png)

+ 입사 년도별 인원수와 평균 급여
	+ 테이블의 컬럼이 아닌 값으로도 그룹으로 묶을 수 있다.
```
select year(hire_date) hd, count(*), avg(salary)
from employees
group by hd
order by hd desc;
```
![image](https://user-images.githubusercontent.com/19484971/172087622-29189350-590d-4fd5-90af-47286ed03193.png)

