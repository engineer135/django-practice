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

# 장고 프로젝트 시작
# 아래에서 이루어지는 모든 작업은 가상환경 안에서 해야하는 것을 꼭 기억하자. 
1. 장고 프로젝트 생성
(myvenv) C:\Users\Name\djangogirls> django-admin.py startproject mysite .
장고 프로젝트 기본 골격을 만드는 명령어. mysite 폴더 및 manage.py가 생기고, 
기타 등등 프로젝트에 필요한 파일 및 폴더를 자동으로 생성해준다.

2. 설정 변경
mysite/settings.py 파일을 열어
TIME_ZONE = 'Asia/Seoul' 
타임존 변경

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
정적파일 경로 추가

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
PythonAnywhere로 배포할 예정이므로, 호스트 이름을 맞춰주기 위해 변경
ALLOWED_HOSTS가 비어있으면 default는 ['localhost', '127.0.0.1', '[::1]'] 이다.

3. 데이터베이스 설정
sqlite3를 사용한다. 이미 settings.py 파일에 설치가 되어있다!
python manage.py migrate
데이터베이스를 생성한다.

4. 서버 시작
(myvenv) ~/djangogirls$ python manage.py runserver
http://127.0.0.1:8000/ 들어가서 It worked! 화면이 뜨면 셋팅 완료.

# Git 연결 (https://git-scm.com/book/ko/v2 참조)
# 장고 프로젝트를 만들었으니 Git으로 형상관리를 해보자.

1. init
$ git init
해당 폴더에서 git init 명령어 실행시
Initialized empty Git repository in D:/djangogirls/.git/
이런 문구가 뜨면서, .git 폴더가 생성된다.
이 상태에서는 아직 프로젝트의 어떤 파일도 관리하지 않는다. 
저장소에 파일을 추가하고 커밋한 후부터 관리가 시작된다.

2. add & commit
$ git add *
현재 디렉토리의 모든파일을 add한다.
용량이 50메가쯤 돼서 시간이 좀 걸린다.
$ git commit -m "initial project version"
첫 커밋을 진행!! 했는데 아무 반응이 없어서 다운된줄 알았다.
조금 기다리니 메세지들이 뜨면서 커밋완료!

3. status(https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%88%98%EC%A0%95%ED%95%98%EA%B3%A0-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)
여기서 잠깐 전에 이고잉님에게 배운 
Working copy ----add----> Index(Staging area) ----commit----> Repository(저장소. git이 저장해 놓은 log? 라고 봐도 될듯. 히스토리가 여기 쌓인다.)
이 개념을 기억하고 가자.

$ git status 
git은 파일을 Untracked와 Tracked 상태로 구분한다.
Untracked 파일은 아직 커밋하지 않은 파일이다. (Index(Staging Area)에도, Repository(저장소)에도 없는 파일)
Tracked 파일은 Index(Staging Area)에 들어가있는 파일이다.
Tracked 파일은 세가지로 나눠지는데
Unmodified Index(Staging area)에 들어간 후, (Working copy가) 변한 게 없는 상태
Modified Index(Staging area)에 들어간 후, (Working copy가) 변한 게 있음!
Staged modified 상태의 파일을 staged로 변경(add)하고, staged 상태의 파일을 커밋함.
그리고 다시 unmodified 상태로 돌아옴. 이런 라이프사이클을 반복한다.


README.md 파일을 생성한후 git status를 입력해보자.
D:\djangogirls>git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md

nothing added to commit but untracked files present (use "git add" to track)

D:\djangogirls>git add README.md

D:\djangogirls>git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   README.md


D:\djangogirls>git commit -m README.md
[master 39faa95] README.md
 1 file changed, 101 insertions(+)
 create mode 100644 README.md

D:\djangogirls>git status
On branch master
nothing to commit, working tree clean

그 밖에 자세한 내용(status 심플하게 보기, ignore 파일 만들기 등등)은 
위에 있는 참조 url을 확인하자.
재미있는 케이스가 많다.

4. gitHub에 올리기
일단 remote 레파지토리를 셋팅해야 한다.
$ git remote add origin https://github.com/engineer135/django-practice.git
실행하면 아무것도 안뜬다. (에러가 안났으니 된건가;;)

그리고 remote 레파지토리에 push한다.
$ git push -u origin master
반응이 없는데 조금 기다리면, GitHub 로그인창이 뜬다.
그런데 아래와 같은 에러가 났다.

To https://github.com/engineer135/django-practice.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/engineer135/django-practi
ce.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

GitHub 저장소를 만들때, README.md 파일을 만들었고, 이게 충돌이 난 것 같다.
pull 명령어로 원격 저장소 내용을 가져와서 합치고 다시 업로드해야한다.
















