# 데이터베이스를 하면서 생긴 문제점들

1. MariaDB 설치 후 DBever 에서 DB 생성 중 생긴 에러

[블로그](https://goddaehee.tistory.com/202?category=198526)를 따라서 설치를 진행하였다. 공식 홈페이지에서 권장하는 
버전인 10.6.8을 받아서 진행하였다. mysql과 포트가 겹쳐서 임시적으로 3316으로 설정하였고 문제는 없을 것이라고 생각했는데 본인이 mariaDB를 모르는 것이 문제였다 하하하하!

본인의 에러 메시지를 적어두지 않았으나 아래의 에시지와 이름만다르고 완전히 같은 문제가 생겼다.

Caused by: java.sql.SQLInvalidAuthorizationSpecException: (conn=8512) Access denied for user 'root'@'centos7' (using password: YES)  Current charset is UTF-8. If password has been set using other charset, consider using option 'passwordCharacterEncoding'

[다른 블로그](https://yonglimlee.tistory.com/entry/%ED%95%B4%EA%B2%B0-%EC%99%84%EB%A3%8C-centos7-mariadb-Access-denied-for-user)의 도움을 받아서 해결했는데 권한 문제였다!

그리고 데이터베이스 생성해서 진행하려다가 말았다. 왜냐하면.. 원래 mysql 쓰고있었는데 더 좋다는 평가가 많은 mariaDB 사용하겠다고 오늘 하루내에 끝내야하는 과제2개를 다 못 끝낼 수도 있겠다는 생각이 들어서이다..

시간이 생기면 mariaDB랑 DBever 더 자주 쓰고 싶다.
