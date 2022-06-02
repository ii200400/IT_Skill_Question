# 1-4. 데이터 베이스

+ ER Diagram (Entity-Relation Diagram 미완)
+ RDBMS (관계형(Relational) 데이터베이스 시스템)
+ SQL
	+ DDL
	+ DML
	+ DCL
	+ Join
+ 정규화
  + 필요성
  + 종류
  + 역정규화
+ Transaction
  + 정의
  + 종류
+ 교착상태

## 개요

데이터는 아직 가공되지 않은 사실이나 값이고 이러한 데이터를 토대로 유용한 정보를 얻을 수 있다. 가치있는 정보를 얻기 위해서 다양하고 정확도가 높은 데이터가 필요하며, 그것들을 잘 관리하고 원하는 데이터만을 뽑아 활용할 수 있어야 하기 때문에 데이터베이스가 필요한 것 이다.

데이터베이스는 특정 조직의 여러 사용자가 `공유`하여 사용할 수 있도록 통합해서 저장한 관리받는 데이터의 집합이고 이러한 데이터베이스의 데이터를 저장하고, 저장된 데이터를 관리하는 프로그램을 데이터베이스 관리시스템(DataBase Management System)이라고 한다.

일반적으로 데이터베이스는 파일 형태로 존재하며 MySQL, OracleDB 등의 DBMS이 해당 파일을 조작하는데 사용하는 프로그램이된다.

해당 글은 본인이 듣고 있는 강의와 데이터베이스 개론 3판(김연희 저자)를 참고하여 작성하였음을 밝힌다.   
또한, 강의에서 MySQL을 사용하였기 때문에 해당 프로그램을 기준으로 작성할 예정이다.

강의 진행을 위해 교수님이 오라클에서 기본적으로 제공하는 더미 데이터를 MySQL에 맞춰 만든 것을 제공받아 사용했는데 그 파일을 그대로 올리면 저작권에 문제가 될 것 같아 올리지 않았다; 개인적으로 부분적으로 올리는 쿼리문만해도 신경이 많이 쓰인다.   

[w3schools](https://www.w3schools.com/mysql/default.asp)에서 쿼리문의 예시를 제공하고 있으니 필요하다면 참고하자.

미정리 내용들(언제 정리하니..)

용어 정리

+ 엔티티(Entity) : 현실에서 가치가 있는 사물이나 사람
+ 스키마(Schema) : 데이터베이스에 저장되는 데이터 구조와 제약조건을 정의한 것
+ 인스턴스(객체, instance) : 스키마의 정의를 기반으로 데이터베이스에 실제로 저장된 값

강의 중간에 index(색인, 목차)에 대한 설명도 조금 하셨다.   

+ 특정 데이터의 위치를 저장하여 검색 속도를 빠르게 하기 위해 사용한다.
+ 목차를 저장할 메모리 공간이 별도로 필요하다.
+ 데이터의 추가/삭제가 빈번히 일어나는 경우 목차의 수정에 걸리는 시간이 늘어나 오히려 비효율적일 수 있다.

## ER Diagram (Entity-Relation Diagram)

현실 세계의 물건이나 관계를 개체(entity)와 개체 사이의 관계로 표현하는 방법

실선과 점선 등의 테이블 사이의 관계를 표현할 때 사용하는 방식과 의미는 추후 정리

## RDBMS (관계형(Relational) 데이터베이스 시스템)

테이블기반(Table based)의 관계형 DBMS(Database Management system)을 의미한다.   
데이터들을 테이블 단위로 관리하며, 테이블끼리의 관계를 표시하여 데이터의 수정을 용이하도록 만든다.

예를 들어.. 아래와 같은 테이블을 사용하기보다는

| 사원 | 이름 | 부서 |
|---|---|---|
| 100 | 김 | 홍보부 |
| 101 | 이 | 촬영부 |
| 102 | 박 | 홍보부 |

아래와 같이 부서를 관리하는 테이블을 따로 관리하여 중복 데이터를 최소화시키고 데이터의 수정 및 삭제가 용이하도록 한다.   
예를 들어 홍보부 부서 명이 광고부로 바뀌는 상황이라면 두 번째 테이블의 홍보부 부서명만 바꾸면 된다. 만약 위의 테이블을 사용했다면, 부서가 홍보부인 사람을 모두 찾고 그 사람들의 부서를 모두 광고부로 고쳐야 할 것이다.  

| 사원 | 이름 | 부서 |
|---|---|---|
| 100 | 김 | 10 |
| 101 | 이 | 11 |
| 102 | 박 | 10 |

| 부서 | 부서명 |
|---|---|
| 10 | 홍보부 |
| 11 | 촬영부 |
| 12 | 의상부 |

위와같이 데이터들을 중복이 적게 테이블을 나누어 관리하는 과정을 정규화라고 한다.   
정규화 등의 이유로 분리된 테이블들의 관계를 살펴 테이블을 하나로 합치는 기능을 `join`이라고 한다.   
여러 데이터들을 관리하기 위해 테이블의 분리가 많이 일어나는 RDBMS에서 필수적인 기능이라고 생각한다.  

용어 정리

+ 필드(Field), 컬럼(Column), 속성(Attribute) : 데이터의 종류
+ 레코드(Record), 튜플(Tuple) : 데이터 집합
+ 테이블(Table) : 레코드의 집합

한 개념을 설명하는 용어가 저리 많은 이유는 아마도.. 데이터베이스를 관련해서 나온 이론들이(file system, E-R Diagram, DBMS 등) 각자 매우 비슷한 개념을 다른 용어를 붙여서 불렀는데 그것이 사람들에 의해서 섞인 것 같다;   
(스택 오버플로우에 의하면)현재는 우리나라뿐만 아니라 세계적으로도 비슷하게 대충 알아듣고 있는 것 같다.

## SQL (Structured Query Language)

+ Database에 있는 정보를 관리하는 프로그램인 DBMS를 조작할 수 있도록 지원하는 언어
  +  많은 종류가 있다
+ 기본적으로 언어의 대소문자는 구별하지 않는다. 
  + 데이터의 대소문자는 구별한다고 한다. 
  + Mysql은 인코딩에 따라 지원을 하지 않을 수도 있다.
+ 모든 DBMS에서 사용이 가능하다.
+ 크게 DCL, DDL, DML로 나눠진다.

### Data type

데이터베이스에서 사용하는 데이터 타입 중 기본적이고 자주 쓰이는 것만 간단하게 정리하겠다.

+ CHAR[M] : 고정 길이를 갖는 문자열, 최대 크기 2^8-1
+ VARCHAR[M] : 가변길이를 갖는 문자열, 최대크기 2^16-1
+ TEXT[] : 길이제한을 명시하지 않는 문자열, 최대 2^16-1
  + CHAR[20]과 VARCHAR[20]에 10자만 저장하면 
    CHAR의 경우는 20의 공간을 모두 사용하지만 
    VARCHAR의 경우 10자 만큼의 공간만 사용한다. 
    대신 varchar가 조금 더 느리다
+ INT[M] : 숫자형 데이터
  + 4byte의 크기를 가진다.
+ DATETIME : 날짜형 데이터를 표현하는 문자열
+ TIMESTAMP[M] : 날짜형 데이터를 표현하는 숫자 데이터
  + 둘 모두 YYYY-MM-DD HH:MM:SS의 형식을 가진다.
  + TIMESTAMP의 경우 추가적으로 ms이하까지도 표현이 가능하다. 
    YYYY-MM-DD HH:MM:SS.FFFFFF

참고로 데이터베이스에는 사진, 음악이나 영화도 저장할 수 있기는 하다.

### DDL (Data Definition Language)

+ 데이터 정의어
  + 데이터베이스 객체의 구조를 정의
  + 테이블/스키마/데이터베이스 생성, 컬럼 추가, 타입변경, 제약조건 지정/수정 등

+ 종류
  + create : 데이터베이스 객체를 생성
  + use: 데이터베이스 사용
  + drop : 데이터베이스 객체를 삭제
  + alter : 기존에 존재하는 데이터베이스 객체를 수정

+ 제약조건
	+ 컬럼에 저장될 데이터의 조건을 설정하는 것
	+ 제약조건에 위배되는 데이터는 저장이 불가하다.
	+ 테이블 생성 시에 조건을 지정하거나, ALTER로 설정이 가능하다.
	+ 종류
		+ NOT NULL : 컬럼에 NULL 값 저장 불가능
		+ UNIQUE : 컬럼에 중복된 값 저장 불가능, NULL 저장 가능
		+ PRIMARY KEY (기본키)   
		  NOT NULL + UNIQUE, NULL값 저장 불가능 및 중복 불가능
		+ FOREIGN KEY (참조키, 외래키)   
			특정 테이블의 PK 컬럼에 저장되어있는 값만 저장 가능, NULL 저장 가능
			references를 이용하여 어떤 컬럼의 어떤 데이터를 참조하는지 반드시 지정
		+ DEFAULT : NULL 값이 들어올 경우 기본으로 설정된 값으로 변경해서 저장
		+ CHECK : 값의 범위나 종류를 지정
		+ AUTO INCREMENT : 새 레코드가 추가될 때마다 필드 값을 자동으로 1 증가하여 저장

명확하지 않지만 강의에서 교수님이 스키마와 테이블을 데이터베이스라고 설명하신 것 같다.

#### create

데이터베이스를 생성한다.

```
-- 데이터베이스 생성 (인코딩 방식 utf-8, 이모지 입력 불가능) 
create database dbtest
default character set utf8mb3 collate utf8mb3_general_ci;

-- 데이터베이스 생성 (인코딩 방식 utf-8, 이모지 입력 가능) 
create database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;

-- ssafydb에 테이블 명이 ssafy_member인 테이블 생성
-- 회원 정보 table
create table ssafy_member(
	  idx			int			auto_increment,
    userid		varchar(16)	not null,
    username		varchar(20),
    userpwd		varchar(16),
    emailid		varchar(20),
    emaildomain	varchar(50),
    joindate		timestamp	default	current_timestamp,
    primary key (idx)
);
 ```
 
#### use

사용할 데이터베이스를 선택한다.

```
-- ssafydb를 선택한다.
use ssafydb;
```

#### alter

데이터베이스 변경한다.

```
-- 데이터베이스 변경
alter database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;
```

#### drop

데이터베이스나 스키마, 테이블을 삭제한다.

```
-- 데이터베이스 삭제
drop database dbtest;
```

### DML (Data Manipulation Language)

+ 데이터 조작어
  + 데이터를 추가, 삭제, 수정하거나 검색하는 명령어
  + 위의 기능을 짧게 CURD라고 통칭한다.
    + `INSERT(create)` `SELECT(retrieve)` `UPDATE` `DELETE`

+ 종류
  + insert(C) : 데이터베이스 객체에 데이터를 입력
  + select(R) : 데이터베이스 객체에 데이터를 조회
  + update(U) : 데이터베이스 객체에 데이터를 수정
  + delete(D) : 데이터베이스 객체에 데이터를 삭제

그룹함수를 사용하면 항상 한 줄로만 결과값이 나온다, 다른 일반 레코드 값을 사용해도 한 줄만 나온다.

#### insert

테이블에 레코드를 할 수 있다.

```
INSERT INTO table_name(col_name1, col_name2, ..., col_nameN)   
VALUES(col_val1, col_val2, ..., col_valN),
      (col_val1-2, col_val2-2, ..., col_valN-2)
```

컬럼은 생략이 가능한 경우도 있다.
1. NULL이 허용된 컬럼
2. DEFAULT가 설정된 컬럼
3. AUTO INCREMENT가 설정된 컬럼

```
-- 회원 정보 등록
-- 'kimssafy', '김싸피', '1234', 'kimssafy', 'ssafy.com', 등록시간 (id 생략)
insert into ssafy_member (userid, username, userpwd, emailid, emaildomain, joindate)
values('kimssafy', '김싸피', '1234', 'kimssafy', 'ssafy.com', now());

-- '김싸피', 'kimssafy', '1234' (id, emailid, emaildomain, joindate 생략)
insert into ssafy_member (username, userid, userpwd)
values('김싸피', 'kimssafy', '1234');

-- '이싸피', 'leessafy', '1234'
-- '박싸피', 'parkssafy', '9876'
insert into ssafy_member (username, userid, userpwd)
values('이싸피', 'leessafy', '1234'),
	('박싸피', 'parkssafy', '9876');
  
-- 모든 필드 값을 지정하는 경우 컬럼명 생략 가능
insert into ssafy_member
values(5, 'leessafy', '김싸피', '1234', 'leessafy', 'ssafy.com', now());
```

#### update

테이블에 레코드를 수정할 수 있다.

```
UPDATE table_name
SET col_name1 = col_val1[, col_name2 = col_val2, ..., col_nameN = col_valN]
WHERE conditions;
```

+ where절의 조건에 만족하는 레코드 값을 변경한다
  + 단! where절을 생략하면 모든 레코드의 값이 변경된다!!
  + mysql은 Edit - preferences - SQL Editor - Safe Updates 의 체크를 해제해야 레코드의 수정과 삭제가 가능하다.

```
-- userid가 kimssafy인 회원의 비번을 9876, 이메일 도메인을 ssafy.com으로 변경.
update ssafy_member
set userpwd = '9876', emaildomain = 'ssafy.co.kr'
where userid = 'kimssafy';

-- 모든 회원의 비번을 9876, 이메일 도메인을 ssafy.com으로 변경.
update ssafy_member
set userpwd = '9876', emaildomain = 'ssafy.co.kr';
```

#### Delete

테이블에 레코드를 삭제할 수 있다.

```
DELETE FROM table_name
WHERE conditions;
```

+ where절의 조건에 만족하는 레코드 값을 삭제한다.
  + 단! where절을 생략하면 모든 레코드의 값이 삭제된다!!
  + mysql은 Edit - preferences - SQL Editor - Safe Updates 의 체크를 해제해야 레코드의 수정과 삭제가 가능하다.

```
-- userid가 kimssafy 회원 탈퇴
delete from ssafy_member
where userid='kimssafy';

-- 모든 회원 탈퇴
delete from ssafy_member;
```

삭제나 수정같은 일을 할 때에는 TCL의 commit과 rollback을 잘 활용하여 안정적으로 수정과 삭제를 진행할 수 있다. 만약 사용한다면 Query - Auto-Commit Rtansaction 설정이 끄는 것을 잊지 말자;

#### select

테이블의 레코드를 선택할 수 있다.

```
SELECT *
FROM table_name;
```

+ select절에 다양한 옵션을 넣어줄 수 있다.
  + All : 선택된 모든 행을 반환, 기본값
  + DISTICT : 선택된 레코드 중 중복되는 레코드는 제거
  	+ 레코드의 표기되는 모든 값들이 중복되어야 제거가 된다.
  	+ 10, 20 과 10, 30 의 두 레코드가 있다면 10 이 겹친 것으로만 중복되었다고 판단하지 않는다.
  + column : FROM절에 나열된 테이블에서 원하는 열을 선택, * 은 모든 컬럼을 의미한다.
  + expression : 표현식
  + alias : 컬럼이나 테이블의 별칭
+ 특히 아주 다양한 절이 있다.
  + select와 from은 필수적인 절이다.
  + where, group by, having, order by 등의 구문을 활용하여 다양한 기능을 줄 수 있다.

select문 예시들이 너무 많도 생략하기에도 어려워서 [다른 곳](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database/select)에 정리를 하였다;

데이터베이스에서 논리연산시 Null이 포함되어 있다면 에러가나는 일반 언어와는 다르게 에러 대신 다른 값이 나올 수도 있다.

![image](https://user-images.githubusercontent.com/19484971/167288402-1680c4f9-b5cd-43be-b726-5d2ea2865df0.png)

Join도 설명을 해야하나 내용이 너무 많아 아래쪽에 따로 정리를 하였다.

### DCL (Data Control Language)

+ 데이터 제어어
  + DB, Table의 접근 권한이나 CRUD 권한을 정의
  + 특정 사용자에게 테이블의 검색 권한 부여/금지 등

+ 종류
  + grant : 데이터베이스 객체에 권한을 부여
  + revoke : 데이터베이스 객체 권한 취소

### TCL (Transaction Control Language)

+ 트랜잭션 제어어
  + 트랜젝션을 제어할 때 사용하는 명령어
    + Transaction : 데이터베이스 논리적 연산 단위

+ 종류
  + commit : 실행한 Query를 최종적으로 적용
  + rollback : 실행한 Query를 마지막 commit 전으로 취소시켜 데이터를 복구

DDL 이나 DCL의 모든 질의문은 무조건 commit이 진행된다.

### Join

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

</br>

#### CROSS JOIN(CARTESIAN JOIN, 교차조인)

일반적으로 `CARTESIAN JOIN`보다는 `CARTESIAN PROJECT`라고 작성하는 것 같은데 필자는 수학의 곱집합과 영문명이 완전 똑같은 것에 햇갈려서 `CARTESIAN JOIN`라고 작성하였다. 조인 조건이 없거나 조건을 부적절하게 작성할 경우 일어나는 조인이다.

이름에서 유추할 수 있듯이 두 테이블의 행을 곱해서 (테이블A의 행 수)\*(테이블B의 행 수)의 행을 가지는 테이블이 만들어지는데, 거의 안쓰인다고 한다. ~~이거 쓰면 오히려 테이블 잘못 작성했다는 합리적 의심을 한다고 언급하셨다..~~

##### 예시

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

#### INNER JOIN

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

##### 예시

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

#### OUTER JOIN

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

#### SELF JOIN

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

#### None - Equi JOIN

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

### 모델링

정규화 내용 조금만 정리, 이해가 조금;;

중복되는 데이터를 모아 다른 테이블로 분리 시키는 것을 제 1 정규화   
이미 기본키이거나 복합키에 속한 속성이 다른 속성을 포괄할 때 (예를 들어 회원id와 회원명이나 회원 등급 의 관계)해당 속성들 끼리 테이블을 새로 만드는 것은 제 2 정규화
일반키인 속성이 다른 속성을 포괄할 때 위와 같이 새로 테이블을 만드는 것은 제 3 정규화   


