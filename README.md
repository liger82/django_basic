# Django Tutorial

## Django project 만들기

1. 가상환경 만들기 (venv, conda, etc)
2. django 설치하기 (pip, conda)
3. 프로젝트 생성
    * $django-admin startproject project_name
4. 앱 생성(여러개의 앱을 만들 수 있다.)
    * $cd project_name
    * $./manage.py startapp app_name
5. database 생성하기
    * $./manage.py migrate
    * 아무런 세팅을 건드리지 않으면 sqlite3로 디비가 생성됨.
6. superuser 생성
    * $./manage.py createsuperuser
7. server 구동하기
    * $./manage.py runserver
    * $./manage.py runserver port_number
    
## Django framework는 협업하기 좋은 파이썬 웹 어플리케이션 프레임워크이다!

* model - view - controller 구조로 되어 있어서 프론트, 백엔드 개발자가 자기의 영역에서 개발을 할 수 있도록 만들어져 있습니다.
* 장고에서는 controller 대신에 template이라는 이름을 써서 mtv 구조라고 합니다.
* 이 프로젝트는 간단하게 write, list, view의 endpoint를 가지는 게시판 형태의 기초 내용을 담고 있습니다.


    
