![image](https://github.com/user-attachments/assets/e77443d0-d316-4cd5-9eb6-1e49193df8cc)


# SPARTAMARKET
Welcome to Spartamarket! 

Spartamarket is a comprehensive e-commerce platform designed to handle user accounts, product management, user interactions, and search functionality.

## Features
- **Accounts Management:** User registration, login, and account management.
- **Product Management:** Write, delete, edit and read a product sales post, manage comments, show view counts, wishlist, and categories.
- **User Profiles:** Follow users, manage profiles, show my product list and wishlist.
- **Search Functionality:** Search capabilities to find products efficiently.


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



## Installation

```
git clone https://github.com/MINJOO0613/spartamarket.git
cd spartamarket
```


## Install Dependencies
```
pip install -r requirements.txt
```

## Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```


## Start the Servers
```
python manage.py runserver
```



## File Structure


```
📦SPARTAMARKET
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂accounts
 ┃ ┃ ┃ ┣ 📜change_password.html
 ┃ ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┃ ┣ 📜signup.html
 ┃ ┃ ┃ ┗ 📜update.html
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂products
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0002_product_category_product_price.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0002_product_hits.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0002_product_product_views.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0002_product_seen_cnt.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0003_alter_product_price.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0003_remove_product_hits_product_views.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0003_remove_product_seen_cnt_product_product_views.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0004_alter_product_price.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0004_product_last_view_time.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0005_remove_product_last_view_time_alter_product_views.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┣ 📜0002_product_hits.py
 ┃ ┃ ┣ 📜0003_remove_product_hits_product_views.py
 ┃ ┃ ┣ 📜0004_product_last_view_time.py
 ┃ ┃ ┣ 📜0005_remove_product_last_view_time_alter_product_views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂tamplatetags
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂products
 ┃ ┃ ┃ ┣ 📜create.html
 ┃ ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┃ ┣ 📜product_detail.html
 ┃ ┃ ┃ ┣ 📜product_list.html
 ┃ ┃ ┃ ┗ 📜update.html
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂search_app
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📜search.html
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂spartamarket
 ┃ ┣ 📂templates
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜settings.cpython-310.pyc
 ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┣ 📜wsgi.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┗ 📂css
 ┃ ┃ ┣ 📜001.jpg
 ┃ ┃ ┣ 📜002.jpg
 ┃ ┃ ┣ 📜003.jpg
 ┃ ┃ ┣ 📜004.jpg
 ┃ ┃ ┣ 📜005.jpg
 ┃ ┃ ┣ 📜006.jpg
 ┃ ┃ ┣ 📜BI_1.png
 ┃ ┃ ┣ 📜BI_2.png
 ┃ ┃ ┣ 📜BI_3.png
 ┃ ┃ ┣ 📜BI_4.png
 ┃ ┃ ┗ 📜style.css
 ┣ 📂templates
 ┃ ┗ 📜base.html
 ┣ 📂users
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂users
 ┃ ┃ ┃ ┣ 📜edit_profile.html
 ┃ ┃ ┃ ┗ 📜profile.html
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜signals.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┃ ┣ 📂Scripts
 ┃ ┃ ┣ 📜activate
 ┃ ┃ ┣ 📜activate.bat
 ┃ ┃ ┣ 📜Activate.ps1
 ┃ ┃ ┣ 📜deactivate.bat
 ┃ ┃ ┣ 📜django-admin.exe
 ┃ ┃ ┣ 📜ipython.exe
 ┃ ┃ ┣ 📜ipython3.exe
 ┃ ┃ ┣ 📜pip.exe
 ┃ ┃ ┣ 📜pip3.10.exe
 ┃ ┃ ┣ 📜pip3.exe
 ┃ ┃ ┣ 📜pygmentize.exe
 ┃ ┃ ┣ 📜python.exe
 ┃ ┃ ┣ 📜pythonw.exe
 ┃ ┃ ┣ 📜sqlformat.exe
 ┃ ┃ ┣ 📜tree-cli-script.py
 ┃ ┃ ┗ 📜tree-cli.exe
 ┃ ┣ 📂share
 ┃ ┃ ┗ 📂man
 ┃ ┃ ┃ ┗ 📂man1
 ┃ ┃ ┃ ┃ ┗ 📜ipython.1
 ┃ ┗ 📜pyvenv.cfg
 ┣ 📜.gitignore
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt

```
