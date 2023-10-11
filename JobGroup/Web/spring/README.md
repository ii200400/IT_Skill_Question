# Spring

`목차`

* [개요](#개요)
* [Container](#container)
* [Spring Framework 구조](#spring-framework-구조)
* [Spring Framework Module](#spring-framework-module)
	+ [IoC(Inversion of Control, 제어의 반전)](#iocinversion-of-control-제어의-반전)
	+ [DI(Dependency Injection, 의존성 주입)](#didependency-injection-의존성-주입)
* [AOP(Aspect Oriented Programming, 관점지향 프로그래밍)](#aopaspect-oriented-programming-관점지향-프로그래밍)
* [Spring MVC 모델](#spring-mvc-모델)
	+ [Controller](#controller)
	+ [View](#view)
	+ [Model](#model)
* [Spring Boot](#spring-boot)
	+ [mybatis](#mybatis)
	+ [Lombok](#lombok)
	+ [Spring Security 와 OAuth 2.0 와 JWT](#spring-security-와-oauth-20-와-jwt)

## 환경설정

필자의 환경설정

- Spring Tool Suite 3
  - Version: 3.9.14.RELEASE
  - Platform: Eclipse 2020-03 (4.15.0)
- tomcat
  - apache-tomcat-9.0.60
- mysql

  - 8.0.28

- 참고
  - [스프링 공식홈페이지](https://spring.io/projects/spring-framework)
  - [스프링 도큐먼트 공식홈페이지](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html)
  - [spring library download](https://mvnrepository.com/artifact/org.springframework)
  - 그.. 강의

## 개요

- 웹 사이트가 점점 커지면서 엔터프라이즈급(기업이나 회사 규모)의 서비스가 수요증대
  - 로깅, 분산처리, 보안 등의 기능을 쉽게 관리하고
  - 세션 빈에서 transaction 관리 용이한 서비스 수요 증대
- 자바 개발자들 사이에서는 엔터프라이즈급 서비스를 제공하는 EJB(Enterprise Java Bean)가 각광
  - 기존의 POJO(Plain Old Java Object)와는 다르게 EJB에 정의된 인터페이스에 따라 코드를 작성해야 한다.
  - 배우기 어렵고 설정이 많다.
  - EJB는 (RMI를 기반으로하는) 무거운 서버이자 Container이다.
  - 컨테이너에 배포를 해야 테스트가 가능하여 개발속도가 저하되었다.
- 점차 EJB를 사용하지 않고 엔터프라이즈급 애플리케이션을 작성할 수 있는 방법론이 거론
  - AOP나 DI 같은 새로운 프로그래밍 방법론 대두
  - POJO로도 엔터프라이즈급 프로그래밍 모델 작성 가능
- POJO와 경량 프레임워크를 사용하기 시작

POJO(Plain Old Java Object)는 아래와 같은 자바객체를 의미한다.

- 특정 프레임워크나 기술에 의존적이지 않은 자바 객체
- 위의 특성으로 기술에 종속적이지 않은 객체이기 때문에 생산성과 이식성 향상
- component interface를 상속받지 않는, 특정 framework에 종속되지 않는 객체 (Plain)
- EJB 이전의 자바 클래스 (Old)

경량 프레임워크란

- EJB가 제공하는 서비스를 지원해 줄 수 있는 프레임워크 등장
- Hibernate, JDO, iBatis, Spring 등

위의 POJO와 경량 프레임워크를 사용하여 웹 애플리케이션을 만들 경우 아래의 장점이 있다.

- EJB 서버와 같은 무거운 컨테이너가 필요하지 않음
- 오픈소스 프레임워크라 사용이 무료
- 엔터프라이즈급 애플리케이션 개발에 필요한 많은 라이브러리 지원
- 프레임워크가 스프링 프레임워크인 경우 모든 플랫폼에서 사용이 가능

많은 경량 프레임워크가 있어도 스프링을 사용하는 이유(특징)은 아래와 같다.

- 엔터프라이즈급 애플리케이션을 만들기 위한 모든 기능을 종합적으로 제공
  - configuration model 이나 애플리케이션 수준의 인프라 제공
  - 즉, 개발자가 복잡하고 실수하기 쉬운 Low Level 기능에 신경쓰지 않고 Business Logic 개발에 집중할 수 있도록 도움
- JEE이 제공하는 다수의 기능을 지원하고 있기 때문에 JEE 대체 프레임워크로 자리매김하고있다.
  - JEE(Java Enterprise Edition)는 자바를 이용한 서버측 개발을 위한 플랫폼 (위키백과)
- DI(Dependency Injection)이나 AOP(Aspect Oriented Programming) 등의 기능 지원

## Container

- 스프링은 자바 객체를 담고 있는 컨테이너
  - 언제든지 스프링 컨테이너로부터 필요한 자바 객체를 불러와 사용 가능
- 스프링 컨테이너는 객체의 생성, 사용, 소멸에 해당하는 라이프사이클을 관리

  - 라이프사이클을 기본으로 애플리케이션 사용에 유용한 기능을 제공

- 기능

  - 라이프사이클 관리
  - Dependency 객체 제공
  - Thread 관리
  - 기타 애플리케이션 실행에 필요한 환경

- 필요성
  - 비즈니스 로직 외 부가적인 기능들이 독립적으로 관리되도록 하기 위함
  - 서비스 look up 이나 Configuration에 대한 일관성을 갖기 위함
    - look up은 언급상 서비스 탐색을 의미하는 것 같다.
  - 서비스 객체를 사용하기 위해 개발자가 직접 Factory 또는 Singleton 패턴을 직접 구현하지 않아도 됨

## Spring Framework 구조

- Spring Framework 구조는 Spring의 삼각형으로 설명할 수 있다.
  - Spring의 삼각형은 Spring에서 엔터프라이즈 애플리케이션 개발 시 복잡함을 해결하는 Spring의 핵심 개념을 의미
  - 3개의 꼭지점과 중앙까지 포함하여 4가지 개념이 있다.

1. POJO(Plain Old Java Object)

- 특정 환경이나 기술에 종속적이지 않은 객체지향 원리에 충실한 자바 객체
- 테스트에 용이하며 프레임워크에 구속받지 않고 자유롭게 객체지향 설계를 자유롭게 적용 가능
- 특정 인터페이스를 구현하거나 클래스를 상속하지 않는 일반 자바 객체
- 일반적인 자바 객체를 호칭하는 개념

2. PSA(Portable Service Abstraction)

- 환경과 세부 기술의 변경과 관계없이 일관된 방식으로 기술을 활용할 수 있게 해주는 설계 원칙
- 트랜젝션 추상화, OXM 추상화 등의 기술의 추상화를 통해 Low Level의 기술 부분과 해당 기술을 사용하는 인터페이스로 분리
- 데이터베이스에 관계없이 동일하게 적용할 수 있는 트랜젝션 처리방식이 PSA의 한 예

3. IoC/DI (Inversion of Control / Dependency Injection, 제어의 반전 / 의존성 주입)

- 유연하게 확장 가능한 객체를 만들고 객체의 생성과 객체 간의 의존관계는 외부(컨테이너)에서 동적으로 설정
- IoC
  - Servlet과 EJB가 나타나면서 객체의 생성 및 의존관계 제어권이 대부분이 Servlet 혹은 EJB Container에게 쥐어짐
    - 그 전에는 개발자가 관리
  - 스프링에서도 객체의 생성과 생명주기를 관리하는 Spring Container 혹은 IoC Container 가 존재한다.
  - IOC 구현 방법 중 하나가 DI이다.
- DI
  - 객체가 의존하고 있는(has) 객체를 직접 생성하거나 검색하지 않아도 된다.
  - xml 설정 파일에서 Java bean으로 개발자가 클래스를 지정하거나 자바의 어노테이션을 활용하여 객체의 의존 관계를 설정하면 컨테이너가 의존관계를 설정한다.

4. AOP(Aspect Oriented Programming, 관점지향 프로그래밍)

- 문제를 바라보는 관점을 기준으로 프로그래밍하는 기법
- 문제를 해결하는 핵심 사항과 전체에 적용되는 공통관심 사항을 기준으로 나눠 공통 모듈을 여러 코드에 쉽게 적용할 수 있도록 한다.
- 관심사의 분리를 통해서 소프트웨어의 모듈성 향상하려는 의도
- 예를 들어 로그인 여부를 확인하는 모듈(공통모듈)을 생성하여 특정 라우터에 접근하기 전에 적용시키는 것

- 스프링 추가 개념
  - 일관된 트랜젝션 처리 방법
    - JDBC, JTA 등의 트랜젝션 관련 정보를 설정파일을 통해 입력하면 트랜젝션 구현에 상관 없이 동일한 코드를 여러 환경에서 사용 가능
  - 다양한 API 지원
    - JDBC, iBatis, Mybatis, Hibernate, JPA 등 DB 처리를 위해 널리 사용되는 라이브러리와 연동을 지원
    - DB뿐만 아니라 JMS, 메일, 스케쥴링 등의 애플리케이션 개발에 필요한 다양한 API를 지원

## Spring Framework Module

스프링을 구성하는 모듈은 대표적으로 7개로 나눠볼 수 있는데 아래와 같다. (업데이트할 때마다 구성모듈이 조금씩 바뀌는 듯 하다.)

| 모듈명         | 서술                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Spring Core    | Spring Framework의 핵심기능 제공, Core 컨테이너의 주요 컴포넌트는 Bean Factory로 스프링을 컨테이너로 만든다.                    |
| Spring Context | 스프링을 프레임워크로 만드는 모듈, 국제화된 메시지(?)나 생명주기 이벤트, 유효성 검증 등을 지원하여 빈 팩토리의 개념을 확장한다. |
| Spring AOP     | 스프링 프레임워크와 AOP 기능을 통합시키는 모듈                                                                                  |
| Spring DAO     | 다른 데이터베이스 벤더들의 예외 핸들링과 오류메시지를 관리하는 예외계층을 제공                                                  |
| Spring ORM     | 스프링이 여러 ORM 프레임워크에 플러그인되어 Object relational 툴(JDO, iBatis)들을 제공한다.                                     |
| Spring Web     | 웹 기반 애플리케이션 context를 제공한다.                                                                                        |
| Spring Web MVC | 스프링 자체적으로 MVC 프레임워크 제공을 하며 쉽게 MVC 기반의 웹 어플리케이션 개발이 가능하도록 한다.                            |

몇 개는 무슨 말인지를 모르겠다;

### IoC(Inversion of Control, 제어의 반전)

위에서는 스프링이 중점이 아니라서 조금 번잡하게 썼지만 이 부분부터는 스프링을 기준으로 서술할 예정  
안 그러면 필자가 이해를 못한다;

- IoC

  - 런타임시에 객체간의 연결관계를 동적으로 결정
  - 객체 간의 관계가 느슨하게 연결된다.(loose coupling)
    - 객체간 결합도가 높으면 유지보수 할 때 해당 클래스와 결합된 다른 클래스도 수정의 가능성이 높다.
  - Dependency Lookup 방식과 Dependency Injection 방식이 있다.
    - 전자는 컨테이너가 lookup context를 통해 필요한 Resource나 객체를 얻는 방식
    - 후자는 컨테이너가 직접 의존구조를 객체에 설정할 수 있도록 지정하는 방식, 객체는 컨테이너의 존재 여부를 알 필요가 없다.

- IoC Container
  - 오브젝트의 생성과 관계 설정, 사용, 제거 등의 작업을 애플리케이션 코드 대신 독립된 컨테이너가 담당
  - 컨테이너가 개발자 대신 객체 제어권을 가져 IoC라고 명명
    - 위의 이유로 스프링 컨테이너를 IoC 컨테이너라고도 한다.
  - 스프링에서 Ioc를 담당하는 컨테이너는 BeanFactory, ApplicationContext가 있다.

어.. 뭔가.. interface인 빈팩토리랑 그것을 상속받는 다양한 객체들이 있는데.. 그것까지는 뭔지 모르겠다! ^오^  
아무튼 applicationContext이 BeanFactory을 상속받고 있다는 정도만 알겠다.

예시

1. 팩토리 활용

- 각 서비스를 생성하여 반환하는 팩토리 사용
- 인터페이스만 알고 있다면 어떤 구현체가 어떻게 생성되는지 알 필요가 없다.
- 해당 패턴이 적용된 것이 Container이며 Container를 통해 제공하고자 하는 것이 IoC 모듈

```
public class HelloMain {

	public static void main(String[] args) {
		HelloMessage helloMessage = HelloMessageFactory.getHelloMessage("kor");
//		HelloMessage helloMessage = HelloMessageFactory.getHelloMessage("eng");

		String greeting = helloMessage.hello("임영선");
//		String greeting = helloMessage.hello("Im");

    System.out.println(greeting);
	}
}
```

```
public class HelloMessageFactory {

	public static HelloMessage getHelloMessage(String lang) {
		if("kor".equals(lang)) {
			return new HelloMessageKor();
		} else if("eng".equals(lang)) {
			return new HelloMessageEng();
		} else {
			return null;
		}
	}

}
```

2. IoC 활용

- 위의 팩토리 패턴의 장점을 더하여 어떤 것에도 의존하지 않는 형태가 됨
- 런타임 시점에 클래스 간의 관계가 형성이 된다.
- 각 Service의 생명주기를 관리하는 Assembler를 활용한다.
  - Spring Container가 조립기(Assembler) 역할

```
public class HelloMain {

	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("./application.xml");
//		HelloMessage helloMessage = (HelloMessage) context.getBean("kor");
		HelloMessage helloMessage = context.getBean("kor", HelloMessageKor.class);
//		HelloMessage helloMessage = context.getBean("eng", HelloMessageEng.class);

		String greeting = helloMessage.hello("임영선");
//		String greeting = helloMessage.hello("Im");

		System.out.println(greeting);

		System.out.println("----------------------------------------");

    // 싱글톤으로 만들어져 객체가 같음을 알 수 있다.
		HelloMessage kor1 = context.getBean("kor", HelloMessageKor.class);
		HelloMessage kor2 = context.getBean("kor", HelloMessageKor.class);
		System.out.println(kor1 + " ::::: " + kor2);
	}

}
```

application.xml 파일

```
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

<!-- scope="prototype" 속성을 넣어주면 싱글톤 객체가 아니도록 만들 수도 있다.
	init-method를 사용하면 자동으로 초기화에 사용할 함수를 선택할 수 있다.
  아래는 Spring DI의 설정정보(메타정보)
  -->

 	<bean id="kor" class="com.hello.di4.HelloMessageKor"></bean>
	<bean id="eng" class="com.hello.di4.HelloMessageEng"></bean>

  <!--
		위의 방식 대신 어노테이션이 있는 객체를 탐색하여 빈에 추가하고 싶다면 아래의 컴포넌트 스캔을 사용한다.
    <context:component-scan base-package="com.hello.di4"></context:component-scan>
	-->

</beans>
```

### DI(Dependency Injection, 의존성 주입)

- Spring DI Container
  - 이것이 관리하는 객체를 빈(Bean)이라 한다.
  - 빈들의 생명주기(Life-Cycle)를 관리하는 의미로 빈 팩토리(BeanFactory)라고 부른다.
  - 이 빈 팩토리에 여러 컨테이너 기능을 추가하여 applicationContext라고 한다.
    - 일반적으로는 BeanFactory보다는 applicationContext를 활용
    - 빈을 등록, 생성, 조회, 반환을 관리하는 등의 기본기능은 BeanFactory와 같다.
    - 보통 BeanFactory라고 하면 빈의 관리를 중점으로, applicationContext을 언급하면 스프링이 제공하는 애플리케이션 지원기능을 포함하여 언급하는 것이다.

DI를 설정하는데 메타정보의 표현 방식에 따라 크게 3가지 방법이 있다.

1. XML 문서를 통한 빈 설정 메타정보 기술
2. XML 문서와 자바 클래스에 Annotation을 통한 메타정보 표현
3. 자바 파일과 Annotation을 통한 메타정보 표현

본인의 코드를 올리고 싶지만.. 금기어가 너무 많아서 생략하겠다.  
어차피 나만보는 글이니까! 하핳!

또한 xml을 통한 설정 방법은 넘어간다.. 솔직히 어노테이션 안 사용하는 쪽이 이상하다고 생각한다.  
정말로 빈 등록 하나하나 하다가 에러나거나 꼬이는 것 생각하면 절대 어노테이션 사용해야 한다.

- 빈 생성범위

  - 기본적으로 싱글톤으로 만들어져 컨테이너가 제공하는 모든 빈의 인스턴스는 동일하다.
  - 만약 새로운 인스턴스를 반환하게 만들고 싶다면 scope에 prototype이나 request 등 다른 설정을 넣어주면 된다.
    - 어노테이션이라면 해당 객체 파일에 @scope()를 통해, xml 설정파일이라면 빈에 scope 속성을 넣어주면 된다.

- 빈 설정 Annotation
  - 빈을 자동등록할 수 있도록 하는 어노테이션은 다양하다.
    - 계층별로 개발자가 빈의 특성이나 종류를 구분하기 위해
    - AOP를 활용할 때 특정 어노테이션이 달린 클래스만 설정이 가능
    - 특정 계층의 빈에 부가 기능 부여

| 어노테이션  | 적용 대상                                                                              |
| ----------- | -------------------------------------------------------------------------------------- |
| @Repository | DAO 또는 Repository 클래스에 사용한다. AOP 적용 대상에 자주 선정된다.                  |
| @Service    | Service 클래스에 사용                                                                  |
| @Controller | MVC Controller에 사용, 스프링 웹 서블릿에 의해 웹 요청을 처리하는 컨트롤러 빈으로 선정 |
| @Component  | 위의 그 어느곳에도 분류되지 않는 일반적인 경우                                         |

- 빈 의존 관계 설정 Annotation
  - 멤버변수에 직접 정의하는 경우 setter method를 만들지 않아도 된다.
  - Spring Explorer나 Bean Graph에서 의존관계나 빈 등록 상태를 확인할 수 있다.
  - 만일 동일 타입의 빈이 여러 개인데 @autowired를 사용하는 경우 @Qulifier("name")을 사용하면 된다.

| 어노테이션 | 적용 대상                                                                                                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| @Aurowired | 스프링 프레임워크에서 지원하는 의존성 정의 용도의 어노테이션<br>스프링에 종속적이나 정밀한 의존성 주입에 유용하다.<br>타입에 맞춰서 빈을 연결한다.                                                    |
| @Resource  | 특정 빈이 JNDI 리소스에 대한 injection을 필요로 하는 경우에 사용<br>타입에 맞춰서 빈을 연결한다.                                                                                                      |
| @Inject    | 3.0버전부터 지원하는 어노테이션으로 특정 프레임워크에 종속하지 않은 애플리케이션을 구성하기 위해서 사용한다.<br>javax.inject-x.x.x.jar파일이 추가되어야 사용가능하다.<br>이름에 맞춰서 빈을 연결한다. |

- 멤버변수, setter, constructor, 일반 method에 사용가능하지만 @Resourse만 일반 메소드에 사용하지 못한다.
- 필자의 경우 일반적으로 @autowired 어노테이션을 사용하였다.

어노테이션을 활용하여 만든 xml 설정파일과 빈에 등록되는 클래스 파일 일부는 아래와 같다.

`ApplicationConfig.xml`

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:c="http://www.springframework.org/schema/c"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

<!-- context:component-scan base-package 내의 적절한 어노테이션이 붙은 클래스를 빈으로 등록한다.  -->
	<context:component-scan base-package="com.ssafy.model"></context:component-scan>

</beans>
```

`GuestBookMain.java`

```
public class GuestBookMain {

	public static void main(String[] args) throws IOException {

		ApplicationContext context = new ClassPathXmlApplicationContext("com/ssafy/configuration/applicationContext.xml");
		GuestBookService guestBookService = context.getBean(GuestBookServiceImpl.class);

		guestBookService.method();

		...

	}
}
```

`GuestBookServiceImpl.java`

```
@Service()
public class GuestBookServiceImpl implements GuestBookService {

	@Autowired
	private GuestBookDao guestBookDao;

	...business logic...
}
```

다른 파일(guestBookDao이나 guestBookDao)은 생략한다.

@Autowired 를 활용해서 의존 관계를 설정하는 방법은 아래와 같이 3가지가 있다.

```
// 필드 인젝션
// @Autowired
// MyDao dao;

// setter 인젝션
// @Autowired
// public void setDao(MyDao dao) {
//     this.dao = dao;
// }

// 생성자 인젝션
// @Autowired
// public MyServiceImpl(MyDao dao) {
//	   this.dao = dao;
// }
```

필자는 기본적으로 필드 인젝션을 활용하였다.

## AOP(Aspect Oriented Programming, 관점지향 프로그래밍)

어우.. 이해는 가는데.. 정리를 어떻게 해야할지.. 어음..

## Spring MVC 모델

### Controller

- 클라이언트의 요청을 처리
- @Controller와 @RequestMapping을 활용하여 컨트롤러와 함수 단위의 매핑 가능
  - @Controller는 클래스에만, @RequestMapping은 클래스와 함수에 적용 가능
  - 같은 URL요청이라도 HTTP method에 따라 서로 다른 메소드를 매핑
  - URL과 HTTP method에 따라 적절한 함수를 찾지 못하면 404에러
- Controller 함수는 다양한 파라미터를 object로 받을 수 있다.
- DefaultAnnotationHandlerMapping과 AnnotationHandlerAdapter를 사용
  - Spring 3.0부터는 기본 설정이 되어 별도의 추가없이 사용 가능

컨트롤러의 모든 파라매터를 작성하기는 어려워서 자주 사용하는 것만 정리하면 아래와 같다.
| parameter Type | 설명 |
| --- | --- |
| @RequestParam annotation 적용 파라미터 | |
| @RequestBody annotation 적용 파라미터 | HTTP 요청의 body 내용에 접근할 때 사용 |
| Map, Model, ModelMap | view에 전달할 model data를 설정할 때 사용 |
| DTO | |
컨트롤러의 return type 종류는 아래와 같다.
| Return Type | 설명 |
| --- | --- |
| ModelAndView | |

### View

- 클라이언트에 보낼 응답 페이지
- 컨트롤러로부터 받은 논리적 View 데이터를 통해 JSP 파일 매핑
  - ViewResolver가 논리적 View에 접두사(prefix)와 접미사(suffix)를 붙여 컨트롤러에게 알려준다.
  - 예를 들어 논리 view가 list, 접두어가 /WEB-INF/views/board/, 접미사가 .jsp라면  
    뷰 리졸버는 /WEB-INF/views/board/list.jsp를 반환한다.
- 컨트롤러는 ModelAndView 혹은 String 리턴 타입을 통해서 논리 view 데이터를 뷰에게 보낸다.
  - 컨트롤러가 Map이나 void를 반환하게 되는 경우 자동으로 해당 함수의 @RequestMapping의 문자열이 논리 view가 된다.
- 논리 view 앞에 `redirect:`를 붙여주면 forward 되지 않고 redirect가 된다.

### Model

- View에 전달하는 데이터
- Map, Model, ModelMap을 통해 생성이 가능

## Spring Boot

Spring의 경우 Application을 개발하려면 사전에 많은 작업(라이브러리 추가, dependency 설정 등)이 필요하다.  
이러한 번거로운 작업을 빠르고 쉽게 처리하기 위해 생겼다.

mybatis와 다르게 REST api를 구현하기 위해 만드는지 뷰나 설정파일 등을 담는 src 파일이 텅텅 비어있다.

서버에서는 단순히 요청에 대한 응답만을 보낼 뿐, 로그인과 같은 상태를 저장하는 일은 전혀 하지 않기 때문에 로그인과 같은 기능은 없고 대신해서 요청의 헤더부분에 쿠키나 키, 토큰을 포함해 전송하여 사용자를 구별한다.

장점

- project에 따라 자주 사용되는 라이브러리들이 미리 조합되어있어 선택만 하면된다.
- 복잡한 설정을 자동으로 처리
- 내장 서버를 포함해 톰캣 등의 WAS를 추가로 설치하지 않아도 개발 가능
- WAS에 배포하지 않고 실행할 수 있는 JAR파일로 웹 애플리케이션 개발 가능

[Spring Boot](https://spring.io/projects/spring-boot)

### mybatis

정리 필요

### Lombok

프로젝트에서 사용할 예정
두 자바 빈이 @autowired로 서로 가리킨다면 문제가 되고 단위 테스트도 어려워서(?) 롬복을 사용한다고 함

### Spring Security 와 OAuth 2.0 와 JWT

꼭 access와 refresh 토큰에 대한 내용이 선행되어야 한다.

그런데.. 언제하지;

https://velog.io/@tmdgh0221/Spring-Security-%EC%99%80-OAuth-2.0-%EC%99%80-JWT-%EC%9D%98-%EC%BD%9C%EB%9D%BC%EB%B3%B4

https://developers.naver.com/docs/login/devguide/devguide.md#%EB%84%A4%EC%9D%B4%EB%B2%84%20%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C

https://developers.naver.com/docs/login/windows/windows.md
