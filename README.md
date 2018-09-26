# Sooltime_Share
API Server Souce code

## 술타임쉐어

불금, 친구들과 재밌는 술자리를 즐길 수 있는 서비스를 만들어보자!

## 주요 기능

> **술 레시피 게시판**

	젊은 세대를 강타한 술 레시피!
	메로나주, 고진감래주, 등등
	사람마다 특별한 레시피를 공유하자!

> **술 게임 게시판**

	그냥 마시면 재미없잖아?
	매일매일 새로 생기는 
	술게임 마스터해 인싸 되자~!

> **소소한 팁 게시판**

	잘못된 경로로 배운 술들!
	상사가 주는 술을 피하는 방법!
	술에 관한 소소한 팁을 공유하자!

## 개발환경

> **System**

	macOS Mojave 10.14
	MacBook Pro (13-inch, 2016, Two Thunderbolt 3 ports)
	2 GHz Intel Core i5
	8GB 1867 MHz LPDDR3
	Macintosh HD
	Intel Iris Graphics 540 1536 MB

> **Editor**

	Sublime Text 3.1.1 Build 3176

> **Server**

	python django 2.1 local server
	Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-1061-aws x86_64)
	Amazon AWS EC2 t2.micro

> **Software**

	Python 3.6.1
	django 2.1
	certifi 2018.8.24
	chardet 3.0.4
	coreapi 2.3.3
	coreschema 0.0.4
	defusedxml 0.5.0
	Django 2.1
	django-allauth 0.37.1
	django-rest-auth 0.9.3
	django-rest-swagger 2.2.0
	djangorestframework 3.8.2
	idna 2.7
	itypes 1.1.0
	Jinja2 2.10
	MarkupSafe 1.0
	oauthlib 2.1.0
	openapi-codec 1.3.2
	python3-openid 3.1.0
	pytz 2018.5
	requests 2.19.1
	requests-oauthlib 1.0.0
	simplejson 3.16.0
	six 1.11.0
	uritemplate 3.0.0
	urllib3 1.23

<hr/>

## 1. API 사용법

### 1.1 rest swagger api : MAIN
> **본 API 서버에는 rest-api 뿐 아니라 rest swagger api가 적용되어 있어 한 눈에 api 목록을 확인할 수 있다.**

* **http://서버주소/api/doc/**

위 url을 통해 메인 화면을 확인할 수 있다.
목록을 펼쳐보면 http 요청과 응답에 대한 간단한 요약과 api주소를 알 수 있다.

### 1.2 rest api : board
> **3가지 게시판의 글 정보를 json으로 불러올 수 있는 api이다.**

* **http://서버주소/api/board/recipes/**

<pre><code>#json response example
[
    {
        "id": 1,
        "TITLE": "recipestest",
        "LIKE": 1,
        "CONTEXT": "test",
        "UPLOADER": "test",
        "PHOTO": "test"
    }
]
</code></pre>

'술 레시피' 게시판 글 정보를 불러온다.

* **http://서버주소/api/board/soolgames/**

<pre><code>#json response example
[
    {
        "id": 1,
        "TITLE": "testTitle",
        "LIKE": 0,
        "CONTEXT": "test",
        "UPLOADER": "test",
        "PHOTO": "tset"
    },
    {
        "id": 2,
        "TITLE": "ㅌㅔ스트2",
        "LIKE": 2,
        "CONTEXT": "내용",
        "UPLOADER": "업로더",
        "PHOTO": "사진 링크"
    }
]
</code></pre>

'술 게임' 게시판 글 정보를 불러온다.

* **http://서버주소/api/board/tips/**

<pre><code>#json response example
[
    {
        "id": 1,
        "TITLE": "tiptest",
        "LIKE": 1,
        "CONTEXT": "test",
        "UPLOADER": "test",
        "PHOTO": "test"
    }
]
</code></pre>

'소소한 팁' 게시판 글 정보를 불러온다.

### 1.3 rest api : rest-auth
> **인증 정보를 관리하는 api이다.**

* **http://서버주소/api/rest-auth/login/**

<pre><code>#login request example
{
    "email": "test@test.com",
    "password": "test1234"
}
</code></pre>

<pre><code>#login success response example
{
    "key": "****************************************"
}
</code></pre>

<pre><code>#login failure response example1
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
</code></pre>

<pre><code>#login failure response example2
{
    "non_field_errors": [
        "Must include \"email\" and \"password\"."
    ]
}
</code></pre>

로그인 정보를 확인하고, REST 토큰을 발급&반환한다.
POST로 로그인 정보(email, password)를 담아 요청해야 한다.

* http://서버주소/api/rest-auth/logout/

<pre><code>#logout success response example
{
    "detail": "Successfully logged out."
}
</code></pre>

<pre><code>#logout failure response example
{
    "detail": "Method \"GET\" not allowed."
}
</code></pre>

로그아웃 메소드를 실행하고, REST 토큰을 해제한다.
POST 방식으로 요청해야 한다.

* http://서버주소/api/rest-auth/registration/

회원가입 메소드를 실행한다.

### 1.4 rest api : users
> **회원 정보를 불러올 수 있는 api이다.**

	http://서버주소/api/users/
사용자의 이메일과 닉네임을 json 객체로 반환한다.