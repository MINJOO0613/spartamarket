![image](https://github.com/user-attachments/assets/e77443d0-d316-4cd5-9eb6-1e49193df8cc)


# SPARTAMARKET
Welcome to SPARTAMARKET! 

SPARTAMARKET is a comprehensive e-commerce platform designed to handle user accounts, product management, user interactions, and search functionality.

In our SPARTAMARKET project, we've named the shopping site QUIET. The image above is the site's main logo.

&nbsp;

## Features
- **Accounts Management:** User registration, login, and account management.
- **Product Management:** Write, delete, edit and read a product sales post, manage comments, show view counts, wishlist, and categories.
- **User Profiles:** Follow users, manage profiles, show my product list and wishlist.
- **Search Functionality:** Search capabilities to find products efficiently.

&nbsp;

## Requirements
- asgiref==3.8.1
- asttokens==2.4.1
- colorama==0.4.6
- decorator==5.1.1
- Django==4.2
- django-extensions==3.2.3
- exceptiongroup==1.2.2
- executing==2.0.1
- ipython==8.26.0
- jedi==0.19.1
- matplotlib-inline==0.1.7
- parso==0.8.4
- pillow==10.4.0
- prompt_toolkit==3.0.47
- pure_eval==0.2.3
- Pygments==2.18.0
- six==1.16.0
- sqlparse==0.5.1
- stack-data==0.6.3
- traitlets==5.14.3
- typing_extensions==4.12.2
- tzdata==2024.1
- wcwidth==0.2.13


&nbsp;

## Getting started
#### Installation

```python
git clone https://github.com/MINJOO0613/spartamarket.git
cd spartamarket
```


#### Install Dependencies
```python
pip install -r requirements.txt
```

#### Run Migrations

```python
python manage.py makemigrations
python manage.py migrate
```


#### Start the Servers
```python
python manage.py runserver
```

&nbsp;
&nbsp;

## Project structure
```
📦 SPARTAMARKET
├─ .gitignore
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ accounts
│  │     ├─ change_password.html
│  │     ├─ login.html
│  │     ├─ signup.html
│  │     └─ update.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ products
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ products
│  │     ├─ create.html
│  │     ├─ index.html
│  │     ├─ product_detail.html
│  │     ├─ product_list.html
│  │     └─ update.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirements.txt
├─ search_app
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ search.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ spartamarket
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ static
│  └─ css
│     ├─ 001.jpg
│     ├─ 002.jpg
│     ├─ 003.jpg
│     ├─ 004.jpg
│     ├─ 005.jpg
│     ├─ 006.jpg
│     ├─ BI_1.png
│     ├─ BI_2.png
│     ├─ BI_3.png
│     ├─ BI_4.png
│     └─ style.css
├─ templates
│  └─ base.html
└─ users
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ forms.py
   ├─ migrations
   │  ├─ 0001_initial.py
   │  └─ __init__.py
   ├─ models.py
   ├─ signals.py
   ├─ templates
   │  └─ users
   │     ├─ edit_profile.html
   │     └─ profile.html
   ├─ tests.py
   ├─ urls.py
   └─ views.py
```

&nbsp;

## ERD
![image](https://github.com/user-attachments/assets/88f860d0-6127-4384-8b94-22fe6922762f)

&nbsp;
&nbsp;
&nbsp;

## Role & Contribution
* Backend (Web)
  + 전체 아키텍처 구성 - 전 팀원
  + 사용자 계정 기능(회원가입, 로그인, 로그아웃, 탈퇴) 구현 - 김민주
  + 사용자 프로필 구현 - 김민주
  + 팔로우, 팔로잉 기능 구현 - 김민주
  + 상품 정렬 기능 구현 - 주성현
  + 카테고리 기능 구현 - 주성현
  + 좋아요(찜하기) 기능 구현 - 주성현
  + 검색기능 구현 - 강다영
  + 조회수 구현 - 강다영
  + 탈퇴, 취소 등 버튼 클릭 시 재확인 받도록 구현 - 강다영

* Frontend (Web)
  + 총괄 - 김민주

* etc
  + 전체 개발 일정 및 이슈 관리 - 전 팀원

&nbsp;

## Developer
- 강다영(HeureuseD)
- 김민주(MINJOO0613)
- 박건희(unseasol)
- 주성현(Joonim97)
