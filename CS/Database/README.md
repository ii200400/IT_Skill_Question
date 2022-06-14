# 1-4. 데이터 베이스

+ RDBMS (관계형(Relational) 데이터베이스 시스템)
+ ER Diagram (Entity-Relation Diagram 미완)
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

## 데이터베이스

여러 응용시스템(사용자)들이 공유해서 사용할 수 있는 통합 저장된 운영 데이터의 집합   
조금 더 풀어쓰면 여러 사람들이 다같이 사용할 수 있도록 중복 데이터를 최소화하여 필수 데이터를 저장한 집합

+ 용어
	+ 데이터 : 현실에세 관찰이나 측정을 통해 수집된 사실(facts)이나 값(values)
	+ 정보 : 데이터를 해석 및 분석하여 사람에게 유용하게 만든 가공 데이터
	+ 개체(Entity), 스키마(Schema), 인스턴스(객체, instance) 정리요망
	+ 필드(Field), 컬럼(Column), 속성(Attribute) : 데이터의 종류
	+ 레코드(Record), 튜플(Tuple) : 데이터 집합
	+ 테이블(Table) : 레코드의 집합
	+ DBA(Database Administration) : 데이터베이스 관리자

한 개념을 설명하는 용어가 저리 많은 이유는 아마도.. 데이터베이스를 관련해서 나온 이론들이(file system, E-R Diagram, DBMS 등) 각자 매우 비슷한 개념을 다른 용어를 붙여서 불렀는데 그것이 사람들에 의해서 섞인 것 같다;   
(스택 오버플로우에 의하면)현재는 우리나라뿐만 아니라 세계적으로도 비슷하게 대충 알아듣고 있는 것 같다.

+ 기능
	+ 데이터 정의어(DDL)
		+ 데이터 베이스를 정의하는 언어
		+ 논리적 구조(데이터 모델)
	+ 데이터 조작어(DML)
		+ 데이터를 조작하는 언어
	+ 데이터 제어어(DCL)
		+ 데이터베이스를 제어할 수 있도록 하는 언어

+ 특성
	+ 실시간 접근성(Real-time Accessibilities)
		+ 데이터가 생성되면 즉시 데이터베이스를 관리하는 컴퓨터에 보내어 처리를 하는 방식을 의미한다.
		+ 질의에 대해 실시간으로 처리하고 응답한다.
	+ 지속적인 변화(Continuous Evolution)
		+ 새로운 데이터의 삽입(Insert),삭제(Delete),갱신(Update)을 통해 항상 최신의 데이터를 유지한다.
	+ 동시 공유(Concurrent Sharing)
		+ 다수의 사용자가 원하는 내용의 데이터에 동시에 접근 및 사용이 가능
	+ 내용에 대한 참조(Content Reference)
		+ 데이터 레코드의 주소나 위치로 데이터를 참조하지 않는다.
		+ 사용자가 요구하는 데이터의 내용으로 데이터를 찾는다.

+ 데이터베이스 장점
	+ 데이터 중복 최소화
		+ 물론 데이터 모델링 설계가 잘 이루어져야 한다.
	+ 데이터 공유
	+ 일관성, 무결성, 보안성 유지
		+ 일관성 : 사용자들이 동시에 어떤 데이터를 읽었을 때 어떤 상황에서라도 데이터는 같아야 한다.
		+ 무결성 : 데이터의 유일성을 보장
			+ 개체 무결성 : PrimaryKey, 개체는 유일해야 한다. 같은 주민등록번호를 가지는 사람이 있으면 안된다.
			+ 참조 무결성 : ForeignKey, 개체의 데이터 관계가 일관되어야 한다. 사원A는 퇴사했는데 사원A의 급여데이터가 남아있으면 안된다.
			+ 도메인 무결성 : 데이터 형식을 만족하는 값만 저장되어있어야 한다. 주민등록번호에 문자가 적혀있으면 안된다.
			+ 등등 다양한 무결성이 있다.
		+ 보안성 : 특정 데이터베이스 관리자만이 데이터 읽기 혹은 읽기와 쓰기의 권한이 있도록 하는 등의 방식
	+ 데이터의 표준화 가능
		+ 표준화 : 데이터 요소에 대한 명칭, 정의, 형식, 규칙 등을 수립하여 전사적으로 적용한다.
	+ 최신의 데이터 유지
+ 데이터베이스 단점
	+ 데이터베이스 전문가 필요
	+ 많은 비용 부담
		+ 대용량 메모리와 고속 CPU는 충분히 비싸다.
	+ 시스템의 복잡함
		+ 서로 다른 데이터들이 다양한 상호연관을 가진다면 제약 조건을 고려하여 설계하기 힘들고 고급 프로그래밍을 요구하게 된다.
	+ 데이터 백업과 복구가 어려움
		+ 
	+ 엑세스가 집중되면 과부하 발생

+ 참고
	+ https://www.youtube.com/watch?v=mehjXqNKvh8
	+ https://coding-factory.tistory.com/214
	+ https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4

## RDBMS (관계형(Relational) 데이터베이스 시스템)

테이블기반(Table based)의 관계형 DBMS(Database Management system)을 의미한다.   
데이터베이스를 다양한 응용프로그램들이 공유할 수 있도록 관리하는 일련의 소프트웨어 프로그램   
테이블 단위로 관리하며, 테이블끼리의 관계를 표시하여 데이터의 수정을 용이하도록 한다.

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

### Mysql

많은 DBMS 중 한 프로그램이다.   
필자가 듣는 강의에서 사용하는 DBMS는 MySQL이기 이것을 기준으로 작성할 예정이다.

일반적으로 데이터베이스 실습을 할 때에는 Mysql과 MariaDB 사용한다고 하는데 그 이유는 다음과 같다.
+ DB 시장에서 사용할 수 있는 최초의 오픈 DB 중 하나이다.
	+ 때문에 가장 널리 사용되는 DBMS가 되었다고 한다.
	+ 물론 상업적 이용시에는 상업용 라이선스를 구입해야 한다.
+ Mysql와 MariaDB의 호환성이 매우 높다.
	+ Mysql의 창시자인 몬티 와이드니어가 이후 프로젝트가 MariaDB이기 때문에 호환이 좋다고 한다.
	+ 간단히 사용하기에는 두 DB의 성능 차이가 크게 없는 편이다.
+ AWS의 Amazon Aurora와 교체 사용하기 용이하다.
+ Maria DB는 상용버전이 별도로 없는 것이, Mysql은 상대적으로 레퍼런스가 많다는 것이 장점

데이터베이스를 효율적으로 관리하기 위해서는 아래의 3가지를 고려해야 한다.

1. 파급효과
2. 간결함
3. 데이터 품질

그런데 아직 우리들은 데이터 품질까지 고려하지 않아도 된다고 한다.

## ER Diagram (Entity-Relation Diagram)

현실 세계의 물건이나 관계를 개체(entity)와 개체 사이의 관계로 표현하는 방법   
일반적으로 관계형 데이터 모델을 표현하기 위해서 사용된다.

실선과 점선 등의 테이블 사이의 관계를 표현할 때 사용하는 방식과 의미는 추후 정리

**사용하고 있는 데이터의 erd 사진**
![image](https://user-images.githubusercontent.com/19484971/172144116-61b67ae5-3427-4b12-8da2-6d827de0241b.png)

[w3schools](https://www.w3schools.com/mysql/default.asp)에서 쿼리문의 예시를 제공하고 있으니 필요하다면 참고하자.

## SQL (Structured Query Language)

+ Database에 있는 정보를 관리하는 프로그램인 DBMS를 조작할 수 있도록 지원하는 언어
  +  많은 종류가 있다
+ 기본적으로 언어의 대소문자는 구별하지 않는다. 
  + 데이터의 대소문자는 구별한다고 한다. 
  + Mysql은 인코딩에 따라 지원을 하지 않을 수도 있다.
+ 모든 DBMS에서 사용이 가능하다.
+ 크게 DCL, DDL, DML로 나눠진다.

필자가 듣는 강의에서 MySQL을 사용하였기 때문에 해당 프로그램을 기준으로 작성함의 유의하자!   
또한, 모든 SQL을 다루는 것이 아니라 강의에서 다룬 것들을 중점으로 작성할 것이므로 다양한 SQL문을 확인학 싶다면 [w3schools](https://www.w3schools.com/sql/sql_alter.asp)를 참고하자!



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

참고로 데이터베이스에는 사진, 음악이나 영화도 저장할 수 있기는.. 하다. (너무 크기가 크기 때문에 보통은 저장하지 않는다.)

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

+ 기본 형식

```
-- 데이터베이스 생성
CREATE DATABASE 데이터베이스_이름;
```

+ 예시

```
-- 데이터베이스 생성
create database dbtest

-- 데이터베이스 생성 (인코딩 방식 utf-8, 이모지 입력 불가능) 
create database dbtest
default character set utf8mb3 collate utf8mb3_general_ci;

-- 데이터베이스 생성 (인코딩 방식 utf-8, 이모지 입력 가능) 
create database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;
```
 
+ 제약 조건 6가지
	+ Not Null(NN)
		+ 컬럼 레벨의 설정으로만 적용 가능
		+ null 허용하지 않음(반드시 값이 입력되어야 한다.)
	+ Unique(UK) 
		+ 입력되는 값이 고유해야 한다.
		+ **null값은 허용한다!**
	+ Primary Key(PK)
		+ 테이블당 하나만 설정 가능
		+ (테이블 레벨 설정을 통해) 여러 개의 컬럼을 조합해서 생성이 가능
		+ 데이터(행)를 구분하는 역할
		+ not null + unique
	+ check(CK)
		+ 입력되는 값의 조건 유효성 확인
	+ Foreign Key(FK)
		+ 다른 테이블의 컬럼의 값을 참조
		+ 또는 자기 테이블의 다른 컬럼을 참조
		+ 부모(참조되는쪽)와 자식(참조하는쪽) 테이블의 관계
	+ Default 
		+ 컬럼 정의시 별도로 지정하지 않으면 null을 지정한다.
		+ 형식> 컬럼 default 지정할값
		+ 컬럼의 값이 입력되지 않으면 디폴트로 설정된 값이 자동입력
 
+ 제약 조건 형식

```
-- 제약조건을 넣은 데이터베이스 생성
-- 1. 컬럼레벨 방식 (not null은 컬럼 레벨만 가능)
CREATE TABLE 테이블_이름(
	컬럼명 제약조건,
	컬럼명 제약조건,
	....
);

-- 2. 테이블레벨 방식 (primary key를 다중 컬럼으로 설정하는 경우 주로 사용)
CREATE TABLE 테이블_이름(
	컬럼명 ,
	컬럼명 ,
	....
	제약조건,
	제약조건
);
```

+ 예시

```
-- 컬럼 레벨 설정 
create table book (
	id int primary key,
	name varchar(20) not null,
	price int check(price > 0),
	isbn varchar(14) unique,
	pubDate timestamp default current_timestamp
);

-- 테이블 레벨 제약조건 설정방식
create table book (
	id int,
	name varchar(20) not null,
	price int,
	isbn varchar(14),
	pubDate timestamp default current_timestamp,
#	not null(name),	에러가 생긴다!
	primary key(id),
	check(price > 0),
	unique(isbn)
);

-- constraint 이름을 설정하는 경우
create table book (
	id int,
	name varchar(20) not null,
	price int,
	isbn varchar(14),
	pubDate timestamp default current_timestamp,
	#not null(name),	에러
	constraint book_id_pk primary key(id),
	constraint book_price_ck check(price > 0),
	constraint book_isbn_uk unique(isbn)
);
 ```
 
#### use

사용할 데이터베이스를 선택한다.

+ 기본 형식

```
use 데이터베이스_이름;
```

+ 예시

```
-- ssafydb를 선택한다.
use ssafydb;
```

#### alter

데이터베이스 혹은 테이블을 변경한다.   


+ 기본 형식

```
-- 데이터베이스의 문자 집합 변경
ALTER DATABASE 데이터베이스_이름 
CHARACTER SET=문자_집합_이름

-- 테이블에 컬럼을 추가할 때
ALTER TABLE 테이블_이름
ADD 컬럼_이름 데이터타입;

-- 테이블의 컬럼을 수정할 때
ALTER TABLE 테이블_이름
MODIFY 컬럼_이름 데이터타입;

-- 테이블의 컬럼을 삭제할 때
ALTER TABLE 테이블_이름
DROP 컬럼명;

-- 제약조건 추가하기
ALTER TABLE 테이블_이름
ADD CONSTRANINT 제약조건명 제약조건타입(컬럼명);

-- 제약조건 삭제하기
ALTER TABLE 테이블_이름
DROP 제약조건명;

-- 등등..

```

+ 예시

```
-- 데이터베이스 변경
alter database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;

-- email 컬럼 추가하기
alter table tb_alter 
add email varchar(20) default 'ssafy';

-- email 컬럼 삭제
alter table tb_alter
drop email;

-- 제약조건 추가하기
alter table book
add constraint book_isbn_uk unique(isbn);

-- 제약조건 삭제하기
alter table book
drop book_isbn_uk;

-- 부모(참조 컬럼)가 데이터를 삭제할때 자식들(외래키 컬럼)의 데이터도 동시에 제거하기 (cascade)
alter table comment 
add constraint comment_no_fk foreign key(no) references board(no) on delete cascade;
```

#### drop

데이터베이스나 스키마, 테이블을 삭제한다.   
단, Foregn key 제약조건이 있는 테이블은 제약조건이나 외래키 테이블을 먼저 삭제한 후에 삭제가 가능하다!

+ 기본 형식

```
-- 데이터베이스 삭제
DROP DATABASE 데이터베이스_이름;

-- 테이블 삭제
DROP TABLE 테이블_이름;
```

+ 예시

```
-- dbtest 데이터베이스 삭제
drop database dbtest;

-- book 테이블 삭제
drop table book;
```

#### View

쿼리문의 결과를 기반으로 생성된 **가상의 테이블**

+ 특징
	+ 특정 조건의 테이블을 쉽게 접근할 수 있도록 한다.
	+ 테이블이 하나 더 생성되는 것은 아니다.

+ 기본 형식 ([select문](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database#select)에 대한 내용은 링크 참조)

```
-- 뷰 생성
CREATE VIEW [OR REPLACE] view_name AS
SELECT col_name1, col_name2, ..., col_nameN
FROM table_name
WHERE condition;
```

+ 예시

```
-- employeedeptno50 뷰를 employees 테이블을 통해 생성
create or replace view employeedeptno50 as
select employee_id, first_name, job_id, salary, department_id
from employees
where department_id = 50;
 
-- 뷰를 사용할 때에는 다른 데이터 베이스와 비슷하게 작성하면 된다.
select *
from employeedeptno50;

-- 뷰 삭제
drop view employeedeptno50;
```

#### index

데이터베이스에서 빠르게 데이터를 검색하기 위해 사용하는 책의 목차와 같은 기능

- 테이블 데이터와 별개의 공간으로 관리된다.
- 기본 정렬된 데이터로 관리한다.
- 테이블의 조회 속도를 높이기 위해서 사용한다.
- primary key, unique, foreign key의 제약조건 들은 자동으로 인덱스를 생성한다.
- 자주 수정되는(insert, update, delete) 컬럼은 작업은 오버헤드를 불러 일으켜 오히려 비효율적일 수 있다.  
+ B+Tree 자료구조를 사용한다.
+ explain 을 사용하면 index를 사용하고 있는지 확인할 수 있다.
	+ ``` explain select * from table where condition="condition"```
	+ type 이 ALL이고 possible_keys와 key가 빈 칸이면 사용하지 않는 것
	+ type 이 ref이고 possible_keys와 key가 빈 칸이 아니면 사용하고 있는 것

간단히 수정이 많은 테이블에서는 인덱스가 없는 테이블이 있는 테이블보다 빠르다는 것만 보고 넘어가서 실재로 어떻게 사용되는지 감이 잘 오지 않는다. 개인적으로는 데이터베이스의 목차라고 생각하고 있다.

+ 기본 형식

```
-- 인덱스 생성
CREATE INDEX index_name
ON table_name (col_name1, col_name2, ..., col_nameN);

-- 테이블의 인덱스 조회
SHOW index_name 
FROM table_name;

-- 인덱스 삭제, 수정은 별도로 지원하지 않아 삭제 후 다시 생성해야 한다.
ALTER TABLE table_name DROP INDEX index_name;
```

+ 예시

```
-- 인덱스 idx_emp 생성
create index idx_emp 
on employees(employee_id);
  
-- 테이블 employees의 인덱스 조회
show index from employees;

-- 테이블 employees의 인덱스 idx_emp 삭제
alter table employees drop index idx_emp;
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

컬럼은 생략이 가능한 경우도 있다.
1. NULL이 허용된 컬럼
2. DEFAULT가 설정된 컬럼
3. AUTO INCREMENT가 설정된 컬럼


+ 기본 형식

```
-- 1. 특정 컬럼에 대한 값만 추가할 때
INSERT INTO table_name (col_name1, col_name2, ..., col_nameN)
VALUES (col_val1, col_val2, ..., col_valN)
			 (col_val1-2, col_val2-2, ..., col_valN-2);

-- 2. 모든 컬럼에 대한 값을 추가할 때
INSERT INTO table_name
VALUES (value1, value2, value3, ..., valueN)
			 (value1-2, value2-2, ..., valueN-2);
```

+ 예시

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

join은 내용이 너무 길어 [별도의 파일로 정리](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database/join)를 하였다.

#### update

테이블에 레코드를 수정할 수 있다.

+ where절의 조건에 만족하는 레코드 값을 변경한다
  + **where절을 생략하면 모든 레코드의 값이 변경된다!!**
  + mysql은 Edit - preferences - SQL Editor - Safe Updates 의 체크를 해제해야 레코드의 수정과 삭제가 가능하다.

+ 기본 형식

```
UPDATE table_name
SET col_name1 = col_val1[, col_name2 = col_val2, ..., col_nameN = col_valN]
WHERE conditions;
```

+ 예시

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

+ where절의 조건에 만족하는 레코드 값을 삭제한다.
  + 단! where절을 생략하면 모든 레코드의 값이 삭제된다!!
  + mysql은 Edit - preferences - SQL Editor - Safe Updates 의 체크를 해제해야 레코드의 수정과 삭제가 가능하다.


+ 기본 형식

```
DELETE FROM table_name
WHERE conditions;
```

+ 예시

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
-- 1. 특정 컬럼에 대한 데이터만 선택할 때
SELECT col_name1, col_name2, ..., col_nameN
FROM table_name;

-- 2. 모든 컬럼에 대한 데이터를 선택할 때
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
+ 논리연산시 Null이 포함되어 있다면 에러가나는 일반 언어와는 다르게 에러 대신 다른 값이 나올 수도 있다.
	+ <img src="https://user-images.githubusercontent.com/19484971/167288402-1680c4f9-b5cd-43be-b726-5d2ea2865df0.png"  width="300"/>

mysql document에서 select문을 다음의 사진과 같이 정리하고 있었다.

<img src="https://user-images.githubusercontent.com/19484971/171914787-eff7a45e-3c01-4ad5-bc55-de9f8fca8e40.png"  width="500"/>

으어어..!@,.@ 좀.. 많다..!   
select문 예시들이 너무 많아서 [다른 곳](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database/select)에 정리를 하였다;

Join도 설명을 해야하나 이것도 내용이 너무 많아 [또 다른 곳](https://github.com/ii200400/IT_Skill_Question/tree/master/CS/Database/join#join)에 따로 정리를 하였다.

### DCL (Data Control Language)

+ 데이터 제어어
  + DB, Table의 접근 권한이나 CRUD 권한을 정의
  + 특정 사용자에게 테이블의 검색 권한 부여/금지 등

+ 종류
  + grant : 데이터베이스 객체에 권한을 부여
  + revoke : 데이터베이스 객체 권한 취소

테스트용 사용자를 만들었을 때 이외에는 사용하지 않았다.   
유추하기를, DB 관리자가 자주 쓰는 것 같다.

### TCL (Transaction Control Language)

+ 트랜잭션 제어어
  + 트랜젝션을 제어할 때 사용하는 명령어
    + Transaction : 데이터베이스 논리적 연산 단위

+ 종류
	+ start transaction : COMMIT, ROLLBACK이 나올 때까지 실행되는 모든 Query를 추적
  + commit : 실행한 Query를 최종적으로 적용
  	+ DDL 이나 DCL의 모든 질의문은 무조건 commit이 진행된다.
  + rollback : 실행한 Query를 마지막 commit 으로 취소시켜 데이터를 복구
  + savepoint : Query 중간에 특정 포인트를 만든다.
  	+ rollback을 사용하여 해당 포인트로 되돌아갈 수 있다.
  	+ commit을 하면 해당 포인트는 사라진다.

```
-- 현재의 autocommit 속성을 확인한다.
select @@autocommit;

-- 만약 위의 조회 결과가 1(true) 이면 false 로 변경 후 처리한다.
set autocommit=false;

-- 임의의 테이블
create table tc_test
(
	val varchar(10)
);

start transaction;

insert into tc_test
values ('a');

-- 데이터가 'a'가 사라진다.
rollback;

insert into tc_test
values ('b');

-- 데이터가 'b'가 보존된다.
-- 이후 rollback을 진행해도 데이터는 사라지지 않는다.
commit;

insert into tc_test
values ('c');

-- 세이브 포인트 f1으로 명명하여 지정
savepoint f1;

insert into tc_test
values ('d');

-- 데이터 'b'와 'c'는 남아있지만, 'd'가 사라진다.
rollback to f1;
```

### 모델링

정규화 내용 조금만 정리, 이해가 조금;;

중복되는 데이터를 모아 다른 테이블로 분리 시키는 것을 제 1 정규화   
이미 기본키이거나 복합키에 속한 속성이 다른 속성을 포괄할 때 (예를 들어 회원id와 회원명이나 회원 등급 의 관계)해당 속성들 끼리 테이블을 새로 만드는 것은 제 2 정규화
일반키인 속성이 다른 속성을 포괄할 때 위와 같이 새로 테이블을 만드는 것은 제 3 정규화   


