오늘부터 파이썬을 시작해볼까 합니다.
솔로런으로 파이썬 기초를 배워보니, 재미있다.
파이썬을 공부하면서 언어가 발전하고 있다는 걸 느낄 수 있었다.
아무튼 장고걸스 튜토리얼로 웹 프로젝트를 하나 만들어볼 예정이다.

https://tutorial.djangogirls.org/ko/
여기 너무 설명이 잘 되어있어서 딱히 추가할 말이 없다.
그냥 개인 기록용으로 남겨두기 위해 글을 작성한다.
예외상황 같은 것은 장고걸스에서 확인하자. 
기본적인 것만 작성해두겠다.


1. 파이썬 설치
파이썬 홈피(https://www.python.org/)에서 다운받아서 설치하자. 

2. virtualenv 환경설정
파이썬은 가상환경을 제공한다. 프로젝트별로 폴더를 나누는 거랑 비슷한 개념으로 보인다.
$ mkdir djangogirls
$ cd djangogirls
$ python -m venv myvenv
myvenv라는 가상환경을 만든다. djangogirls 폴더에 myvenv라는 폴더가 만들어진다.
C:\Users\Name\djangogirls> myvenv\Scripts\activate
가상환경을 실행한다. 실행이 제대로 되면, 콘솔 프롬포트 앞에 (myvenv) 접두어가 붙는다.

3. 장고 설치
장고가 무엇인지는 https://tutorial.djangogirls.org/ko/django/ 여기서 참조.

(myvenv) ~$ pip install --upgrade pip
pip는 파이썬 패키지 소프트웨어를 설치하고 관리하는 패키지 관리 시스템이다.
node의 npm이랑 비슷해보인다.
(myvenv) ~$ pip install django~=1.11.0
장고를 설치한다!

4. 코드 에디터 설치
나는 Visual Studio Code를 쓴다.

5. Git 설치
git-scm.com 에서 다운받아 설치한다.
path 환경 설정에서 Use Git and optional Unix tools from the Windows Command Prompt을 선택한다.
나머지는 default로 해도 무방.

6. GitHub 계정 만들기

7. PythonAnywhere 계정 만들기







