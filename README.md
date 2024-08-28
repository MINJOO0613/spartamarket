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
 ┃ ┣ 📂templatetags
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜custom_filters.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜custom_filters.py
 ┃ ┃ ┗ 📜__init__.py
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
 ┣ 📂media
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📜buildings-8217275_1280.jpg
 ┃ ┃ ┣ 📜dd96ab6b02082a11d80586ef037cdbde.gif
 ┃ ┃ ┣ 📜dd96ab6b02082a11d80586ef037cdbde_fgARZKW.gif
 ┃ ┃ ┣ 📜Garabato_Kid_garabatokid_on_X.jpeg
 ┃ ┃ ┣ 📜다운로드.gif
 ┃ ┃ ┣ 📜다운로드_1.gif
 ┃ ┃ ┣ 📜다운로드_1_91ce1be.gif
 ┃ ┃ ┣ 📜다운로드_1_qjBSGss.gif
 ┃ ┃ ┣ 📜다운로드_1_sCc3pjy.gif
 ┃ ┃ ┣ 📜다운로드_3.gif
 ┃ ┃ ┣ 📜다운로드_5.gif
 ┃ ┃ ┣ 📜다운로드_6kFEOOq.gif
 ┃ ┃ ┗ 📜다운로드_7.gif
 ┃ ┗ 📂profile_images
 ┃ ┃ ┣ 📜dd96ab6b02082a11d80586ef037cdbde.gif
 ┃ ┃ ┣ 📜KakaoTalk_20240806_230938568.gif
 ┃ ┃ ┗ 📜lantern-1419582_1280.jpg
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
 ┃ ┃ ┃ ┣ 📜0006_hashtag_product_hashtags.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜0006_hashtag_product_tag_hashtags.cpython-310.pyc
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
 ┣ 📂venv
 ┃ ┣ 📂Include
 ┃ ┣ 📂Lib
 ┃ ┃ ┗ 📂site-packages
 ┃ ┃ ┃ ┣ 📂asgiref
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compatibility.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜current_thread_executor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜local.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜server.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sync.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜compatibility.py
 ┃ ┃ ┃ ┃ ┣ 📜current_thread_executor.py
 ┃ ┃ ┃ ┃ ┣ 📜local.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜server.py
 ┃ ┃ ┃ ┃ ┣ 📜sync.py
 ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┣ 📜timeout.py
 ┃ ┃ ┃ ┃ ┣ 📜typing.py
 ┃ ┃ ┃ ┃ ┣ 📜wsgi.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂asgiref-3.8.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂asttokens
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜astroid_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asttokens.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜line_numbers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mark_tokens.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜astroid_compat.py
 ┃ ┃ ┃ ┃ ┣ 📜asttokens.py
 ┃ ┃ ┃ ┃ ┣ 📜line_numbers.py
 ┃ ┃ ┃ ┃ ┣ 📜mark_tokens.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂asttokens-2.4.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂certifi
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜cacert.pem
 ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂certifi-2024.7.4.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂click
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formatting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜globals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shell_completion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜termui.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜types.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_termui_impl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_textwrap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_winconsole.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┣ 📜formatting.py
 ┃ ┃ ┃ ┃ ┣ 📜globals.py
 ┃ ┃ ┃ ┃ ┣ 📜parser.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜shell_completion.py
 ┃ ┃ ┃ ┃ ┣ 📜termui.py
 ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┣ 📜types.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜_compat.py
 ┃ ┃ ┃ ┃ ┣ 📜_termui_impl.py
 ┃ ┃ ┃ ┃ ┣ 📜_textwrap.py
 ┃ ┃ ┃ ┃ ┣ 📜_winconsole.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂click-8.1.7.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.rst
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂cloudinary
 ┃ ┃ ┃ ┃ ┣ 📂api_client
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜call_account_api.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜call_api.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜execute_request.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tcp_keep_alive_manager.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜call_account_api.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜call_api.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜execute_request.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tcp_keep_alive_manager.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂cache
 ┃ ┃ ┃ ┃ ┃ ┣ 📂adapter
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache_adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key_value_cache_adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache_adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key_value_cache_adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂storage
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_system_key_value_storage.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key_value_storage.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_system_key_value_storage.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key_value_storage.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜responsive_breakpoints_cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜responsive_breakpoints_cache.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂poster
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜streaminghttp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜encode.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜streaminghttp.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂provisioning
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜account.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜account_config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜account.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜account_config.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂static
 ┃ ┃ ┃ ┃ ┃ ┗ 📂cloudinary
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜cloudinary_cors.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜canvas-to-blob.min.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.cloudinary.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.fileupload-image.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.fileupload-process.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.fileupload-validate.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.fileupload.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.iframe-transport.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.ui.widget.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜load-image.all.min.js
 ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cloudinary_direct_upload.html
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cloudinary_includes.html
 ┃ ┃ ┃ ┃ ┃ ┗ 📜cloudinary_js_config.html
 ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cloudinary.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cloudinary.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜api.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜auth_token.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜http_client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜search.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜search_folders.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜uploader.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜api.py
 ┃ ┃ ┃ ┃ ┣ 📜auth_token.py
 ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┃ ┃ ┣ 📜http_client.py
 ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┣ 📜search.py
 ┃ ┃ ┃ ┃ ┣ 📜search_folders.py
 ┃ ┃ ┃ ┃ ┣ 📜uploader.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂cloudinary-1.41.0.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂colorama
 ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜isatty_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32_test.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi_test.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise_test.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜isatty_test.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm_test.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜ansi.py
 ┃ ┃ ┃ ┃ ┣ 📜ansitowin32.py
 ┃ ┃ ┃ ┃ ┣ 📜initialise.py
 ┃ ┃ ┃ ┃ ┣ 📜win32.py
 ┃ ┃ ┃ ┃ ┣ 📜winterm.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂colorama-0.4.6.dist-info
 ┃ ┃ ┃ ┃ ┣ 📂licenses
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂decorator-5.1.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜pbr.json
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂django
 ┃ ┃ ┃ ┃ ┣ 📂apps
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂conf
 ┃ ┃ ┃ ┃ ┃ ┣ 📂app_template
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de_CH
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_CA
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_IE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_NI
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_PR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr_BE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr_CA
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr_CH
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ig
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂project_template
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂project_name
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asgi.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜settings.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜manage.py-tpl
 ┃ ┃ ┃ ┃ ┃ ┣ 📂urls
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜global_settings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜global_settings.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┣ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂am
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜djangojs.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜djangojs.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_logentry_remove_auto_add.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0003_logentry_add_action_flag_choices.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_logentry_remove_auto_add.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0003_logentry_add_action_flag_choices.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂static
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vendor
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂select2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE-SELECT2.md
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select2.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜select2.min.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocomplete.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜changelists.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dark_mode.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dashboard.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜login.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_sidebar.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜responsive.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜responsive_rtl.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rtl.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unusable_password_field.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜widgets.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂img
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜move_vertex_off.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜move_vertex_on.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜calendar-icons.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-addlink.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-alert.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-calendar.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-changelink.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-clock.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-deletelink.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-hidelink.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-no.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-unknown-alt.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-unknown.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-viewlink.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜icon-yes.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inline-delete.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜README.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selector-icons.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sorting-icons.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tooltag-add.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜tooltag-arrowright.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜DateTimeShortcuts.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜RelatedObjectLookups.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vendor
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂jquery
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.min.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂select2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂i18n
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜af.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜az.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bg.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bn.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bs.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ca.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cs.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜da.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜de.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dsb.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜el.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜en.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜es.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜et.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜eu.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fa.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fi.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fr.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gl.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜he.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hi.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hr.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hsb.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hu.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hy.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜id.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜is.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜it.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ja.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ka.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜km.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ko.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lt.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lv.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mk.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ms.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nb.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ne.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nl.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pl.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ps.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pt-BR.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pt.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ro.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ru.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sk.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sl.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sq.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sr-Cyrl.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sr.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sv.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜th.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tk.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tr.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uk.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vi.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zh-CN.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜zh-TW.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE.md
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select2.full.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜select2.full.min.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂xregexp
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xregexp.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜xregexp.min.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocomplete.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜calendar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cancel.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜change_form.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inlines.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.init.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_sidebar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜popup_response.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepopulate.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepopulate_init.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SelectBox.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SelectFilter2.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜theme.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unusable_password_field.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜urlify.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂auth
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂user
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜add_form.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜change_password.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂edit_inline
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stacked.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜tabular.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂includes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fieldset.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜object_delete_summary.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearable_file_input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜date.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜foreign_key_raw_id.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜many_to_many_raw_id.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜radio.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_widget_wrapper.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜split_datetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜time.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜url.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜404.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜500.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app_index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app_list.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_site.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜change_form.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜change_form_object_tools.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜change_list.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜change_list_object_tools.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜change_list_results.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color_theme_toggle.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜date_hierarchy.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜delete_confirmation.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜delete_selected_confirmation.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜invalid_setup.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_sidebar.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜object_history.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pagination.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜popup_response.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepopulated_fields_js.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search_form.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜submit_line.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂registration
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logged_out.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_change_done.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_change_form.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_reset_complete.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_reset_confirm.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_reset_done.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_reset_email.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜password_reset_form.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_list.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_modify.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_list.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_modify.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocomplete.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocomplete.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sites.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sites.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂admindocs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂admin_doc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bookmarklets.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜missing_docutils.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model_detail.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model_index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜template_detail.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜template_filter_index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜template_tag_index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜view_detail.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜view_index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂auth
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂handlers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modwsgi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modwsgi.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜changepassword.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜createsuperuser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜changepassword.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜createsuperuser.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_permission_name_max_length.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0003_alter_user_email_max_length.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0004_alter_user_username_opts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0005_alter_user_last_login_null.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0006_require_contenttypes_0002.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0007_alter_validators_add_error_messages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0008_alter_user_username_max_length.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0009_alter_user_last_name_max_length.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0010_alter_group_name_max_length.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0011_update_proxy_permissions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0012_alter_user_first_name_max_length.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_permission_name_max_length.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0003_alter_user_email_max_length.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0004_alter_user_username_opts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0005_alter_user_last_login_null.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0006_require_contenttypes_0002.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0007_alter_validators_add_error_messages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0008_alter_user_username_max_length.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0009_alter_user_last_name_max_length.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0010_alter_group_name_max_length.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0011_update_proxy_permissions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0012_alter_user_first_name_max_length.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂auth
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜read_only_password_hash.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂registration
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜password_reset_subject.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜backends.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_user.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_validation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜backends.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_user.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common-passwords.txt.gz
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_validation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂contenttypes
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜remove_stale_contenttypes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜remove_stale_contenttypes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_remove_content_type_name.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_remove_content_type_name.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prefetch.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prefetch.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂flatpages
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flatpages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flatpages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sitemaps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sitemaps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂gis
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂base
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mysql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂oracle
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂postgis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pgraster.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pgraster.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂spatialite
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conversion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conversion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂forms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gdal
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂prototypes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ds.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜raster.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ds.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜raster.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂raster
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜band.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜source.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜band.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜source.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datasource.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜driver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜envelope.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feature.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜field.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geometries.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geomtype.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜libgdal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datasource.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜driver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜envelope.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feature.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜field.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geometries.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geomtype.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜libgdal.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂geos
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂prototypes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜misc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜predicates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepared.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜threadsafe.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜topology.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜misc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜predicates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepared.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜threadsafe.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜topology.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜factory.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geometry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜libgeos.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜linestring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mutable_list.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜point.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜polygon.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepared.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜factory.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geometry.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜libgeos.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜linestring.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mutable_list.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜point.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜polygon.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepared.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinspect.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂serializers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geojson.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geojson.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sitemaps
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kml.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kml.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂static
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂gis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ol3.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂img
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜draw_line_off.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜draw_line_on.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜draw_point_off.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜draw_point_on.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜draw_polygon_off.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜draw_polygon_on.svg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜OLMapWidget.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂gis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.kml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜placemarks.kml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜openlayers-osm.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜openlayers.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layermapping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinfo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layermapping.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinfo.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinspect.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feeds.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geoip2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geometry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜measure.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ptr.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feeds.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geoip2.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geometry.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜measure.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ptr.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂humanize
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜humanize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜humanize.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂messages
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂storage
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fallback.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜session.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fallback.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜session.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂postgres
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂aggregates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜general.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜statistics.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜general.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜statistics.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fields
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜array.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜citext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ranges.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜array.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜citext.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ranges.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂forms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜array.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ranges.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜array.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ranges.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂jinja2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂postgres
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜split_array.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂postgres
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜split_array.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constraints.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expressions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constraints.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expressions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂redirects
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_redirect_new_path_help_text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_redirect_new_path_help_text.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂sessions
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cached_db.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜db.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signed_cookies.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cached_db.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜db.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signed_cookies.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearsessions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearsessions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_session.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_session.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂sitemaps
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sitemap.xml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜sitemap_index.xml
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂sites
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂af
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂az
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂br
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ckb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_AU
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂en_GB
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_AR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_CO
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_MX
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂es_VE
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂et
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂eu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ga
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gd
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂he
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hsb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂io
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂is
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ka
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kab
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂km
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂my
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ne
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pa
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sq
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sw
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂te
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂th
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂udm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uk
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ur
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂uz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_domain_unique.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_domain_unique.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜management.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜managers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requests.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜management.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜managers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requests.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂staticfiles
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collectstatic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜findstatic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collectstatic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜findstatic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜finders.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handlers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜storage.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜finders.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handlers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜storage.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂syndication
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂core
 ┃ ┃ ┃ ┃ ┃ ┣ 📂cache
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜db.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜memcached.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜redis.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜db.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜memcached.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜redis.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂checks
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂compatibility
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django_4_0.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django_4_0.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂security
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜async_checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜caches.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜database.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜files.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜messages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model_checks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜translation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜async_checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜caches.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜database.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜files.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜messages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model_checks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜translation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂files
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂storage
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜memory.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handler.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜memory.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜images.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜move.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜temp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uploadedfile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uploadhandler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜images.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜move.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜temp.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uploadedfile.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uploadhandler.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂handlers
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asgi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exception.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asgi.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exception.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂mail
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smtp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smtp.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compilemessages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜createcachetable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dbshell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜diffsettings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumpdata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flush.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loaddata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makemessages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makemigrations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜migrate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizemigration.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sendtestemail.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜showmigrations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlflush.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlmigrate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlsequencereset.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜squashmigrations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜startapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜startproject.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testserver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compilemessages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜createcachetable.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dbshell.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜diffsettings.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumpdata.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flush.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loaddata.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makemessages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makemigrations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜migrate.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizemigration.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sendtestemail.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shell.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜showmigrations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlflush.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlmigrate.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlsequencereset.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜squashmigrations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜startapp.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜startproject.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testserver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sql.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂serializers
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyyaml.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xml_serializer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonl.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyyaml.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xml_serializer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂servers
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basehttp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basehttp.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asgi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜paginator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asgi.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜paginator.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜signing.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂base
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dummy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mysql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂oracle
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜oracledb_any.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜oracledb_any.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂postgresql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜psycopg_any.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜psycopg_any.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sqlite3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_functions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_functions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ddl_references.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ddl_references.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂operations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜special.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜special.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autodetector.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜executor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graph.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜migration.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜questioner.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recorder.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜state.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜writer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autodetector.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜executor.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜migration.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜questioner.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recorder.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜state.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜writer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fields
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜files.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generated.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_descriptors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_lookups.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reverse_related.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜files.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generated.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_descriptors.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_lookups.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reverse_related.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂functions
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜comparison.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜math.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜window.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜comparison.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜math.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜window.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subqueries.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜where.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subqueries.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜where.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constraints.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deletion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expressions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manager.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constraints.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deletion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expressions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manager.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query_utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜transaction.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜transaction.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂dispatch
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dispatcher.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dispatcher.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜license.txt
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂forms
 ┃ ┃ ┃ ┃ ┃ ┣ 📂jinja2
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂django
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂forms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂errors
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dict
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂list
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂formsets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜div.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜p.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜attrs.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checkbox.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checkbox_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checkbox_select.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearable_file_input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜date.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hidden.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜input_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multiple_hidden.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multiple_input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multiwidget.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜number.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜radio.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜radio_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select_date.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜splitdatetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜splithiddendatetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textarea.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜time.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜url.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜attrs.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜div.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜field.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜label.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜p.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂django
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂forms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂errors
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dict
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂list
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂formsets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜div.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜p.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜attrs.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checkbox.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checkbox_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checkbox_select.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearable_file_input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜date.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hidden.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜input_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multiple_hidden.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multiple_input.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multiwidget.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜number.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜radio.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜radio_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select_date.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select_option.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜splitdatetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜splithiddendatetime.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textarea.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜time.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜url.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜attrs.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜div.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜field.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜label.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜p.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ul.html
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜boundfield.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formsets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜renderers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜boundfield.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formsets.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜renderers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂http
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multipartparser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜multipartparser.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜request.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂middleware
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clickjacking.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locale.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜security.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜clickjacking.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜http.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜locale.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜security.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂template
 ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jinja2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jinja2.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂loaders
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app_directories.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cached.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app_directories.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cached.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaultfilters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaulttags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜engine.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜library.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader_tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smartif.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜context.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaultfilters.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaulttags.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜engine.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜library.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜loader_tags.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜smartif.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜l10n.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tz.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜l10n.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜static.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tz.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runner.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selenium.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testcases.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜html.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜runner.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜selenium.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜testcases.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂urls
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜converters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolvers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜conf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜converters.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolvers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┣ 📂translation
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reloader.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜template.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trans_null.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trans_real.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reloader.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜template.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trans_null.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trans_real.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜archive.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asyncio.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜choices.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜crypto.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dateformat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dateparse.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deconstruct.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜duration.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feedgenerator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functional.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipv6.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜itercompat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jslex.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lorem_ipsum.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜module_loading.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜numberformat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regex_helper.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜safestring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜termcolors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timesince.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timezone.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlutils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_os.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜archive.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asyncio.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜choices.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜crypto.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dateformat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dateparse.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dates.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜deconstruct.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜duration.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜feedgenerator.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜functional.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜hashable.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜html.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜http.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ipv6.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜itercompat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jslex.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lorem_ipsum.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜module_loading.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜numberformat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜regex_helper.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜safestring.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜termcolors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜timesince.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜timezone.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlutils.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_os.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┃ ┃ ┣ 📂decorators
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clickjacking.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vary.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clickjacking.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vary.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂generic
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜detail.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜edit.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜detail.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜edit.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf_403.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default_urlconf.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜directory_index.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n_catalog.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜technical_404.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜technical_500.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜technical_500.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜static.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜shortcuts.py
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂Django-5.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜AUTHORS
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.python
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂django_extensions
 ┃ ┃ ┃ ┃ ┣ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂auth
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂conf
 ┃ ┃ ┃ ┃ ┃ ┣ 📂app_template
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┣ 📂command_template
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sample.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┣ 📂jobs_template
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂jobs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂daily
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hourly
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂monthly
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂weekly
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂yearly
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sample.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┗ 📂template_tags_template
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sample.py.tmpl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py.tmpl
 ┃ ┃ ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┃ ┃ ┣ 📂fields
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂jobs
 ┃ ┃ ┃ ┃ ┃ ┣ 📂daily
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache_cleanup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜daily_cleanup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache_cleanup.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜daily_cleanup.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂hourly
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂minutely
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂monthly
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂weekly
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂yearly
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┣ 📂ar
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂el
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂en
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂fr
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂hu
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂id
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂it
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂ja
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pl
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pt
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_BR
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┣ 📂ro
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┃ ┗ 📂ru
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
 ┃ ┃ ┃ ┃ ┣ 📂logging
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_generator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean_pyc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clear_cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compile_pyc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜create_command.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜create_jobs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜create_template_tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜delete_squashed_migrations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜describe_form.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜drop_test_database.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumpscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜export_emails.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜find_template.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generate_password.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generate_secret_key.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graph_models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list_model_info.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list_signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mail_debug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜managestate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜merge_model_instances.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜notes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pipchecker.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜print_settings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜print_user_for_session.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜raise_test_exception.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reset_db.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reset_schema.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runjob.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runjobs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runprofileserver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver_plus.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set_default_site.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set_fake_emails.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set_fake_passwords.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shell_plus.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜show_template_tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜show_urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlcreate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqldiff.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqldsn.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syncdata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sync_s3.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unreferenced_files.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜update_permissions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validate_templates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_generator.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean_pyc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clear_cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compile_pyc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜create_command.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜create_jobs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜create_template_tags.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜delete_squashed_migrations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜describe_form.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜drop_test_database.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumpscript.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜export_emails.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜find_template.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generate_password.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generate_secret_key.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graph_models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list_model_info.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list_signals.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mail_debug.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜managestate.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜merge_model_instances.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜notes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pipchecker.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜print_settings.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜print_user_for_session.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜raise_test_exception.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reset_db.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reset_schema.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runjob.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runjobs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runprofileserver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runscript.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver_plus.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set_default_site.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set_fake_emails.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set_fake_passwords.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shell_plus.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜show_template_tags.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜show_urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlcreate.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqldiff.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sqldsn.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syncdata.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sync_s3.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unreferenced_files.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜update_permissions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validate_templates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug_cursor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_notifications.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jobs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modelviz.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mysql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜notebook_extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shells.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜technical_response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜color.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debug_cursor.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜email_notifications.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jobs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜modelviz.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mysql.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜notebook_extension.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shells.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜technical_response.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂mongodb
 ┃ ┃ ┃ ┃ ┃ ┣ 📂fields
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂static
 ┃ ┃ ┃ ┃ ┃ ┗ 📂django_extensions
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜jquery.autocomplete.css
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂img
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜indicator.gif
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.ajaxQueue.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jquery.autocomplete.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜jquery.bgiframe.js
 ┃ ┃ ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┗ 📂django_extensions
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂graph_models
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂django2018
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜digraph.dot
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜label.dot
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜relation.dot
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂original
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜digraph.dot
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜label.dot
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜relation.dot
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜foreignkey_searchinput.html
 ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debugger_tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜highlighting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indent_text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syntax_color.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widont.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debugger_tags.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜highlighting.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜indent_text.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜syntax_color.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜widont.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dia2django.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜internal_ips.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dia2django.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜internal_ips.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜collision_resolvers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜import_subclasses.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜settings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┃ ┃ ┣ 📜collision_resolvers.py
 ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┣ 📜import_subclasses.py
 ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┣ 📜settings.py
 ┃ ┃ ┃ ┃ ┣ 📜validators.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂django_extensions-3.2.3.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂exceptiongroup
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_catch.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_formatting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_suppress.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜_catch.py
 ┃ ┃ ┃ ┃ ┣ 📜_exceptions.py
 ┃ ┃ ┃ ┃ ┣ 📜_formatting.py
 ┃ ┃ ┃ ┃ ┣ 📜_suppress.py
 ┃ ┃ ┃ ┃ ┣ 📜_version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂exceptiongroup-1.2.2.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂executing
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜executing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_position_node_finder.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜executing.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┣ 📜_exceptions.py
 ┃ ┃ ┃ ┃ ┣ 📜_position_node_finder.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂executing-2.0.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂IPython
 ┃ ┃ ┃ ┃ ┣ 📂core
 ┃ ┃ ┃ ┃ ┃ ┣ 📂magics
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ast_mod.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜code.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜display.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜execution.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜history.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜namespace.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜osm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packaging.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pylab.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜script.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ast_mod.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜code.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜display.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜execution.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜history.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜namespace.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜osm.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packaging.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pylab.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜script.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂profile
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜README_STARTUP
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂daft_extension
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜daft_extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜daft_extension.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bad_all.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nonascii.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nonascii2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜print_argv.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜refbug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simpleerr.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tclass.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_alias.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_application.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_async_helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_autocall.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_compilerop.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_completer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_completerlib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_debugger.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_display.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_displayhook.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_events.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_exceptiongroup_tb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_formatters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_guarded_eval.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_handlers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_history.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_hooks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_imports.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputsplitter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputtransformer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputtransformer2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputtransformer2_line.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_interactiveshell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_iplib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_logger.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_magic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_magic_arguments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_magic_terminal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_oinspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_page.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_paths.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_prefilter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_profile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_prompts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pylabtools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_run.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_shellapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_splitinput.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_ultratb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜2x2.jpg
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜2x2.png
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bad_all.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nonascii.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nonascii2.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜print_argv.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜refbug.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simpleerr.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tclass.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_alias.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_application.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_async_helpers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_autocall.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_compilerop.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_completer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_completerlib.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_debugger.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_display.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_displayhook.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_events.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_exceptiongroup_tb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_extension.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_formatters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_guarded_eval.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_handlers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_history.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_hooks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_imports.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputsplitter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputtransformer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputtransformer2.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_inputtransformer2_line.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_interactiveshell.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_iplib.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_logger.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_magic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_magic_arguments.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_magic_terminal.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_oinspect.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_page.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_paths.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_prefilter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_profile.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_prompts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pylabtools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_run.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_shellapp.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_splitinput.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_ultratb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜alias.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜application.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜async_helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocall.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜builtin_trap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compilerop.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completerlib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜crashhandler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debugger.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜display.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜displayhook.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜displaypub.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜display_functions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜display_trap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜events.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜excolors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extensions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getipython.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜guarded_eval.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜history.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜historyapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hooks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inputsplitter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inputtransformer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inputtransformer2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜interactiveshell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latex_symbols.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logger.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macro.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜magic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜magic_arguments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜oinspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜page.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜payload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜payloadpage.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prefilter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜profileapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜profiledir.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prompts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pylabtools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜release.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shellapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜splitinput.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ultratb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜usage.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜alias.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜application.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜async_helpers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜autocall.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜builtin_trap.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compilerop.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜completer.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜completerlib.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜crashhandler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debugger.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜display.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜displayhook.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜displaypub.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜display_functions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜display_trap.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜error.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜events.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜excolors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜extensions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formatters.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜getipython.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜guarded_eval.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜history.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜historyapp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜hooks.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inputsplitter.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inputtransformer.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inputtransformer2.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜interactiveshell.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜latex_symbols.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜logger.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜macro.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜magic.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜magic_arguments.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜oinspect.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜page.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜payload.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜payloadpage.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prefilter.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜profileapp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜profiledir.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prompts.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pylabtools.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜release.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shellapp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜splitinput.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ultratb.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜usage.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂extensions
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_autoreload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_storemagic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_autoreload.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_storemagic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜storemagic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜storemagic.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂external
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_qt_loaders.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_qt_loaders.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜qt_for_kernel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜qt_loaders.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜qt_for_kernel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜qt_loaders.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_backgroundjobs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_clipboard.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_deepreload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_display.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_editorhooks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_imports.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_latextools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_lexers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pretty.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pygments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_backgroundjobs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_clipboard.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_deepreload.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_display.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_editorhooks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_imports.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_latextools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_lexers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pretty.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pygments.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜backgroundjobs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clipboard.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deepreload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜demo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜display.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜editorhooks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜guisupport.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latextools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pretty.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜backgroundjobs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜clipboard.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜deepreload.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜demo.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜display.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜editorhooks.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜guisupport.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜latextools.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lexers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pretty.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂sphinxext
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜custom_doctests.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipython_console_highlighting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipython_directive.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜custom_doctests.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ipython_console_highlighting.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ipython_directive.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂terminal
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pt_inputhooks
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asyncio.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜glut.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gtk.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gtk3.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gtk4.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜osx.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyglet.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜qt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tk.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wx.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asyncio.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜glut.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gtk.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gtk3.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gtk4.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜osx.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyglet.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜qt.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tk.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wx.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂shortcuts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_match.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_suggest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_match.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_suggest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_debug_magic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_embed.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_help.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_interactivshell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pt_inputhooks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_shortcuts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_debug_magic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_embed.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_help.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_interactivshell.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pt_inputhooks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_shortcuts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debugger.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜embed.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜interactiveshell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜magics.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prompts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ptutils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜console.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debugger.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜embed.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜interactiveshell.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ipapp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜magics.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prompts.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ptutils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂testing
 ┃ ┃ ┃ ┃ ┃ ┣ 📂plugin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dtexample.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipdoctest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pytest_ipdoctest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜setup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simplevars.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_ipdoctest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_refs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dtexample.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipdoctest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pytest_ipdoctest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜README.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜setup.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simplevars.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_combo.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_example.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_exampleip.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_ipdoctest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_refs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_ipunittest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_tools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_decorators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_ipunittest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_tools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜globalipapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipunittest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜skipdoctest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜globalipapp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ipunittest.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜skipdoctest.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tools.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_capture.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_deprecated.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_dir2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_imports.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_importstring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_io.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_module_paths.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_openpy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_path.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_process.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pycolorize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_shimmodule.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_sysinfo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_tempdir.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_tokenutil.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_wildcard.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_capture.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_decorators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_deprecated.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_dir2.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_imports.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_importstring.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_io.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_module_paths.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_openpy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_path.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_process.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pycolorize.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_shimmodule.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_sysinfo.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_tempdir.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_text.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_tokenutil.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_wildcard.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜capture.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜colorable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coloransi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜contexts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜daemonize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜data.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dir2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜docs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜eventful.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜frame.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generics.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜importstring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipstruct.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonutil.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜localinterfaces.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜module_paths.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜openpy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜path.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜process.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py3compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜PyColorize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sentinel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shimmodule.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signatures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜strdispatch.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sysinfo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syspathcontext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tempdir.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenutil.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜traitlets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tz.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ulinecache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wildcard.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_cli.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_emscripten.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_posix.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_win32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_win32_controller.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sysinfo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜capture.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜colorable.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜coloransi.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜contexts.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜daemonize.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜data.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dir2.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜docs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜eventful.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜frame.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜generics.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜importstring.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜io.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ipstruct.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonutil.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜localinterfaces.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜module_paths.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜openpy.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜path.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜process.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜py3compat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PyColorize.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sentinel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shimmodule.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜signatures.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜strdispatch.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sysinfo.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜syspathcontext.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tempdir.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜timing.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenutil.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜traitlets.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tz.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ulinecache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wildcard.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_cli.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_common.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_emscripten.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_posix.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_win32.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_process_win32_controller.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_sysinfo.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜conftest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜consoleapp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜display.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜paths.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜conftest.py
 ┃ ┃ ┃ ┃ ┣ 📜consoleapp.py
 ┃ ┃ ┃ ┃ ┣ 📜display.py
 ┃ ┃ ┃ ┃ ┣ 📜paths.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂ipython-8.26.0.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂jedi
 ┃ ┃ ┃ ┃ ┣ 📂api
 ┃ ┃ ┃ ┃ ┃ ┣ 📂refactoring
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extract.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extract.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜classes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion_cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜environment.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_name.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜interpreter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜keywords.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜project.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜replstartup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜strings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜classes.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜completion_cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜environment.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜file_name.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜interpreter.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜keywords.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜project.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜replstartup.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜strings.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂inference
 ┃ ┃ ┃ ┃ ┃ ┣ 📂compiled
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂subprocess
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜access.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getattr_static.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixed.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜value.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜access.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getattr_static.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixed.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜value.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂gradual
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜annotation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conversion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generics.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stub_value.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typeshed.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜type_var.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜annotation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conversion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generics.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stub_value.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typeshed.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜type_var.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂value
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dynamic_arrays.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜function.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜instance.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜iterable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜klass.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜module.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜namespace.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorator.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dynamic_arrays.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜function.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜instance.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜iterable.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜klass.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜module.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜namespace.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜analysis.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜arguments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_value.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜docstrings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜docstring_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dynamic_params.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜finder.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flow_analysis.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜imports.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lazy_value.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜names.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜param.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser_cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recursion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜references.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signature.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜star_args.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syntax_tree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sys_path.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜analysis.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arguments.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base_value.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜context.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜docstrings.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜docstring_utils.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dynamic_params.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜finder.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜flow_analysis.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜imports.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lazy_value.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜names.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜param.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parser_cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜recursion.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜references.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜signature.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜star_args.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜syntax_tree.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sys_path.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flask.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pytest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stdlib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜django.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜flask.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pytest.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stdlib.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂third_party
 ┃ ┃ ┃ ┃ ┃ ┣ 📂django-stubs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂django-stubs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂apps
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂conf
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂locale
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂urls
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜global_settings.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂admin
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_list.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_modify.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_static.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocomplete.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sites.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂admindocs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂auth
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂handlers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modwsgi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜changepassword.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜createsuperuser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜backends.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_user.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜password_validation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂contenttypes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜remove_stale_contenttypes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admin.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂flatpages
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flatpages.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sitemaps.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂gis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂humanize
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜humanize.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂messages
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂storage
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fallback.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜session.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂postgres
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂aggregates
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜general.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜statistics.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fields
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜array.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜citext.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ranges.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constraints.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂redirects
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sessions
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cached_db.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜db.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signed_cookies.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearsessions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_session.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sitemaps
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ping_google.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sites
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜management.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜managers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜middleware.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requests.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂staticfiles
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collectstatic.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜findstatic.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜staticfiles.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apps.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜checks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜finders.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handlers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜storage.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂syndication
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂core
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cache
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜db.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜memcached.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂checks
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂security
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜caches.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜database.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜messages.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model_checks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜registry.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜translation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂files
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜images.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜move.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜storage.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜temp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uploadedfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uploadhandler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂handlers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exception.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mail
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smtp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂management
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumpdata.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loaddata.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makemessages.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sql.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂serializers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂servers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basehttp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜paginator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂base
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dummy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mysql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂postgresql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sqlite3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ddl_references.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂operations
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜special.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autodetector.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜executor.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graph.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜migration.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜questioner.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recorder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜state.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜topological_sort.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜writer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fields
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜files.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_descriptors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_lookups.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reverse_related.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂functions
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜comparison.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜math.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜window.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subqueries.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜where.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constraints.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deletion.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expressions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manager.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜options.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query_utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜transaction.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dispatch
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dispatcher.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂forms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜boundfield.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formsets.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜renderers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜widgets.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂http
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multipartparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂middleware
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clickjacking.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locale.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜security.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂template
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜django.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jinja2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂loaders
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app_directories.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cached.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context_processors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaultfilters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaulttags.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜engine.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜library.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader_tags.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smartif.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂templatetags
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜l10n.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tz.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runner.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selenium.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testcases.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂urls
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜converters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolvers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂translation
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reloader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜template.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trans_null.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trans_real.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜archive.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autoreload.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜baseconv.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜crypto.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dateformat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dateparse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dates.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime_safe.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deconstruct.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜duration.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feedgenerator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functional.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashable.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipv6.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜itercompat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jslex.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lorem_ipsum.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜module_loading.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜numberformat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regex_helper.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜safestring.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜six.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜termcolors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timesince.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timezone.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜topological_sort.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlutils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_os.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂decorators
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clickjacking.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vary.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂generic
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dates.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜detail.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜edit.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜i18n.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜static.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shortcuts.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┃ ┗ 📂typeshed
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂stdlib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂distutils
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂command
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_dumb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_msi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_packager.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_wininst.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_clib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_ext.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_py.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_scripts.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_data.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_headers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_lib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_scripts.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜register.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜upload.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜archive_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bcppcompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cygwinccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dep_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dir_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emxccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fancy_getopt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filelist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜msvccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spawn.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sysconfig.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text_file.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unixccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂email
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mime
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜application.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜audio.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜image.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nonmultipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base64mime.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charset.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoders.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feedparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜header.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜iterators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜MIMEText.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜quoprimime.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_parseaddr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂encodings
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utf_8.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂multiprocessing
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dummy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pool.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜process.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜path.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ast.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜atexit.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜BaseHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜builtins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜CGIHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜commands.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compileall.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ConfigParser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cookie.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookielib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜copy_reg.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cPickle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cStringIO.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dircache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fcntl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fnmatch.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜future_builtins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getopt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getpass.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gettext.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜glob.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜heapq.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜htmlentitydefs.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜HTMLParser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜httplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜imp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜importlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜itertools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markupbase.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜md5.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mimetools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mutex.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ntpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nturl2path.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜os2emxpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pipes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜platform.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜popen2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posix.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posixpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Queue.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜random.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜re.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜repr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resource.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rfc822.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜robotparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runpy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sets.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sha.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shelve.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shlex.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SimpleHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smtplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SocketServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spwd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sre_constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sre_parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜string.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜StringIO.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringold.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜strop.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subprocess.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜symbol.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sys.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tempfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textwrap.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toaiff.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenize.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜types.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unittest.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urlparse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜user.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜UserDict.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜UserList.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜UserString.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜whichdb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlrpclib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_ast.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_functools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_hotshot.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_io.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_json.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_md5.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sha.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sha256.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sha512.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_socket.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sre.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_struct.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_symtable.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_threading_local.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_winreg.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__builtin__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂2and3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ctypes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wintypes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂curses
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ascii.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜panel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textpad.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ensurepip
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lib2to3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pgen2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜driver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜literals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pgen.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜token.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenize.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pygram.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pytree.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂logging
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handlers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂msilib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sequence.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pydoc_data
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜topics.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pyexpat
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sqlite3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dbapi2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂wsgiref
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handlers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜headers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple_server.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜types.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validate.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂xml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dom
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜domreg.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expatbuilder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜minicompat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜minidom.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜NodeFilter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pulldom.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlbuilder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂etree
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cElementTree.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ElementInclude.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ElementPath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ElementTree.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂parsers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂expat
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜model.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂sax
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜handler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜saxutils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlreader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂_typeshed
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xml.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aifc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜antigravity.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜argparse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜array.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asynchat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asyncore.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜audioop.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base64.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binascii.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binhex.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bisect.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bz2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜calendar.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cgi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cgitb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chunk.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜code.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codecs.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codeop.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜colorsys.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜contextlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜copy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cProfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜crypt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csv.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decimal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜difflib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dis.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜doctest.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy_threading.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errno.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filecmp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fileinput.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fractions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ftplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜genericpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜grp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hmac.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜imaplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜imghdr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜keyword.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜linecache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locale.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mailbox.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mailcap.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜marshal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜math.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mimetypes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mmap.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modulefinder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜msvcrt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜netrc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nis.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜numbers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜opcode.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optparse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pdb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pickle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pickletools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pkgutil.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜plistlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜poplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pprint.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜profile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pstats.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pty.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pwd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyclbr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pydoc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py_compile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜quopri.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜readline.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rlcompleter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sched.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜select.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shutil.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜site.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smtpd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sndhdr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socket.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sre_compile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringprep.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜struct.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sunau.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜symtable.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sysconfig.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syslog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tabnanny.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tarfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜telnetlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜termios.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜this.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜threading.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜time.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timeit.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜token.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trace.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜traceback.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tty.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜turtle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicodedata.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uu.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uuid.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜warnings.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wave.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜weakref.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜webbrowser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winsound.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xdrlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zipfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zipimport.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_bisect.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_codecs.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_csv.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_curses.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_dummy_threading.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_heapq.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_msi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_random.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_warnings.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_weakref.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_weakrefset.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__future__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂asyncio
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_futures.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_subprocess.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_tasks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coroutines.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜format_helpers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜futures.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proactor_events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜protocols.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queues.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runners.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selector_events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sslproto.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜staggered.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜streams.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subprocess.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tasks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜threads.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜transports.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trsock.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unix_events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜windows_events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜windows_utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂collections
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂concurrent
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂futures
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜process.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dbm
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gnu.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ndbm.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂distutils
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂command
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_dumb.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_msi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_packager.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_wininst.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_clib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_ext.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_py.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_scripts.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_data.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_headers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_lib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_scripts.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜register.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜upload.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜archive_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bcppcompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cygwinccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dep_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dir_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fancy_getopt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filelist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜msvccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spawn.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sysconfig.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text_file.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unixccompiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂email
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂mime
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜application.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜audio.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜image.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nonmultipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charset.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜contentmanager.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoders.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜feedparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜header.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜headerregistry.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜iterators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜policy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂encodings
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utf_8.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜entities.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂http
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookiejar.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookies.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂importlib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜machinery.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resources.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂json
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tool.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂multiprocessing
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dummy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜managers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pool.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜process.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queues.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sharedctypes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shared_memory.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spawn.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜synchronize.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂os
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜path.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tkinter
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜commondialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filedialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜font.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜messagebox.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ttk.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂unittest
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜async_case.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜case.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mock.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜result.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runner.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜suite.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂urllib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜robotparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂venv
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂xmlrpc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ast.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜atexit.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜builtins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compileall.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜copyreg.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enum.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜faulthandler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fcntl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fnmatch.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getopt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getpass.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gettext.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜glob.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gzip.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜heapq.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜imp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipaddress.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜itertools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lzma.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macurl2path.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nntplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ntpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nturl2path.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pathlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pipes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜platform.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posix.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posixpath.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queue.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜random.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜re.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reprlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resource.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runpy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜secrets.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selectors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shelve.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shlex.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smtplib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socketserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spwd.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sre_constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sre_parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜statistics.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜string.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subprocess.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜symbol.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sys.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tempfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textwrap.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenize.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tracemalloc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜types.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winreg.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xxlimited.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zipapp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_ast.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_bootlocale.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat_pickle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compression.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_decimal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_dummy_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_imp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_importlib_modulespec.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_json.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_markupbase.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_operator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_osx_support.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_posixsubprocess.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_pydecimal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sitebuiltins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_stat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_threading_local.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_tkinter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_tracemalloc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜_winapi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂3.7
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜contextvars.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dataclasses.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜_py_abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂3.9
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂zoneinfo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜graphlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂third_party
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂concurrent
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂futures
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜process.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂fb303
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜FacebookService.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kazoo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂recipe
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜watchers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂OpenSSL
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜crypto.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂routes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mapper.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂scribe
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scribe.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ttypes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂six
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂moves
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂urllib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜robotparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜BaseHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜CGIHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections_abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cPickle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_multipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_nonmultipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html_entities.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html_parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_cookiejar.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_cookies.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queue.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reprlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SimpleHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socketserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_error.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_robotparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlrpc_client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_dummy_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tornado
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜concurrent.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gen.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜httpclient.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜httpserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜httputil.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ioloop.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜netutil.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜process.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tcpserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜web.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enum.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ipaddress.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pathlib2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜pymssql.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂2and3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂atomicwrites
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂attr
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜converters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_version_info.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backports
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bleach
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜callbacks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜linkifier.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sanitizer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂boto
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ec2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂elb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layer1.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂s3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜acl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bucket.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bucketlistresultset.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bucketlogging.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deletemarker.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜keyfile.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lifecycle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multidelete.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜multipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prefix.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tagging.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜user.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜website.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth_handler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exception.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜plugin.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regioninfo.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cachetools
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜func.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lfu.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lru.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ttl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂characteristic
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂chardet
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langbulgarianmodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langcyrillicmodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langgreekmodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langhebrewmodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langhungarianmodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langthaimodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langturkishmodel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜universaldetector.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂click
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatting.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜globals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜termui.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜types.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_termui_impl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cryptography
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂hazmat
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backends
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜interfaces.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂bindings
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂openssl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binding.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂primitives
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂asymmetric
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dh.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dsa.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ec.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ed25519.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ed448.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜padding.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rsa.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜x25519.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜x448.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ciphers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aead.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜algorithms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂kdf
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜concatkdf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hkdf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kbkdf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pbkdf2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scrypt.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜x963kdf.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂serialization
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pkcs12.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂twofactor
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hotp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜totp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmac.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constant_time.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hmac.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜keywrap.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜padding.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜poly1305.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂x509
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extensions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜oid.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fernet.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂datetimerange
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dateutil
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tz.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_common.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜easter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜relativedelta.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rrule.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_common.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂deprecated
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜classic.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sphinx.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂emoji
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode_codes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂flask
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂json
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tag.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜blueprints.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cli.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ctx.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debughelpers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜globals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜signals.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templating.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜views.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wrappers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂geoip2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜database.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜records.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂google
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂protobuf
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂compiler
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜plugin_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂internal
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜containers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enum_type_wrapper.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension_dict.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message_listener.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python_message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜well_known_types.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wire_format.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂util
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜any_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜descriptor.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜descriptor_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜descriptor_pool.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜duration_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜empty_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜field_mask_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json_format.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message_factory.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reflection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜service.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜source_context_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜struct_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜symbol_database.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timestamp_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜type_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wrappers_pb2.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂jinja2
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bccache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜environment.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ext.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loaders.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜meta.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nodes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runtime.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sandbox.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜visitor.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_stringdefs.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂markdown
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂extensions
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abbr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜admonition.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜attr_list.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codehilite.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜def_list.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extra.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fenced_code.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜footnotes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜legacy_attrs.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜legacy_em.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜md_in_html.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜meta.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nl2br.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sane_lists.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smarty.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tables.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wikilinks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜blockparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜blockprocessors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inlinepatterns.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pep562.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜postprocessors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜preprocessors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜treeprocessors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__meta__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂markupsafe
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_native.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_speedups.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂maxminddb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂nmap
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nmap.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂paramiko
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜agent.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth_handler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ber.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜buffered_pipe.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜channel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compress.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dsskey.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ecdsakey.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ed25519key.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hostkeys.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_curve25519.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_ecdh_nist.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_gex.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_group1.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_group14.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_group16.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kex_gss.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜message.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packet.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pipe.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pkey.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜primes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py3compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rsakey.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp_attr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp_client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp_file.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp_handle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp_server.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sftp_si.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssh_exception.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssh_gss.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜transport.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win_pageant.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_winapi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pymysql
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂constants
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜CLIENT.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜COMMAND.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ER.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜FIELD_TYPE.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜FLAG.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SERVER_STATUS.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charset.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connections.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜converters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cursors.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜err.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜times.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pynamodb
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂connection
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜attributes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜indexes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜settings.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜throttle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜types.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pytz
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pyVmomi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vim
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜event.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fault.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜option.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜view.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂vmodl
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fault.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜query.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂redis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂requests
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂packages
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂urllib3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂packages
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂ssl_match_hostname
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_implementation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂util
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜url.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connectionpool.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filepost.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜poolmanager.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapters.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookies.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hooks.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status_codes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜structures.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂retry
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂simplejson
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoder.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scanner.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂slugify
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜slugify.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜special.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tzlocal
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂werkzeug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜atom.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fixers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜iterio.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsrouting.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜limiter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lint.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜profiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜securecookie.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testtools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wrappers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂debug
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜repr.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tbtools.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂middleware
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dispatcher.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_proxy.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lint.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜profiler.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy_fix.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shared_data.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜local.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posixemulation.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜routing.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜script.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜security.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serving.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testapp.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜useragents.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wrappers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wsgi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_internal.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_reloader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂yaml
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜composer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constructor.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cyaml.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dumper.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emitter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜events.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nodes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reader.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜representer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scanner.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serializer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜backports_abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜certifi.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜croniter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dateparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜first.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gflags.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜itsdangerous.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mock.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mypy_extensions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜polib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pycurl.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyre_extensions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜singledispatch.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tabulate.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜termcolor.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing_extensions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ujson.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂3
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂aiofiles
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂threadpool
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binary.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜os.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂docutils
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂parsers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂rst
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nodes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜roles.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜states.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜examples.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nodes.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂filelock
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂freezegun
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂jwt
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂algorithms
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pycrypto.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py_ecdsa.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜algorithms.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pkg_resources
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py31compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂pyrfc3339
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generator.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂six
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂moves
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂urllib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜robotparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜BaseHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜builtins.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜CGIHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections_abc.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cPickle.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_base.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_multipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_nonmultipart.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email_mime_text.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html_entities.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html_parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_client.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_cookiejar.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜http_cookies.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queue.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reprlib.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SimpleHTTPServer.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socketserver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter_commondialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter_constants.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter_dialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter_filedialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter_tkfiledialog.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tkinter_ttk.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_error.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_parse.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_request.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_response.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urllib_robotparser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_dummy_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_thread.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂typed_ast
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ast27.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ast3.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conversions.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂waitress
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adjustments.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜buffers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜channel.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy_headers.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜receiver.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rfc7230.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜runner.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜task.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trigger.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utilities.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wasyncore.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜contextvars.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dataclasses.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜frozendict.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜orjson.pyi
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜file_io.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parser_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜settings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_compatibility.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┃ ┃ ┣ 📜debug.py
 ┃ ┃ ┃ ┃ ┣ 📜file_io.py
 ┃ ┃ ┃ ┃ ┣ 📜parser_utils.py
 ┃ ┃ ┃ ┃ ┣ 📜settings.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜_compatibility.py
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂jedi-0.19.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜AUTHORS.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂matplotlib_inline
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜backend_inline.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜backend_inline.py
 ┃ ┃ ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂matplotlib_inline-0.1.7.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂parso
 ┃ ┃ ┃ ┃ ┣ 📂pgen2
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar_parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜generator.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar_parser.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂python
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜diff.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pep8.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prefix.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜token.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜diff.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar310.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar311.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar312.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar313.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar36.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar37.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar38.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar39.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pep8.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prefix.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜token.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tokenize.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜file_io.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜normalizer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_compatibility.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┣ 📜file_io.py
 ┃ ┃ ┃ ┃ ┣ 📜grammar.py
 ┃ ┃ ┃ ┃ ┣ 📜normalizer.py
 ┃ ┃ ┃ ┃ ┣ 📜parser.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜tree.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜_compatibility.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂parso-0.8.4.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜AUTHORS.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂PIL
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜BdfFontFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜BlpImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜BmpImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜BufrStubImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ContainerIO.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CurImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜DcxImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜DdsImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜EpsImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ExifTags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜FitsImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜FliImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜FontFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜FpxImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜FtexImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GbrImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GdImageFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GifImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GimpGradientFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GimpPaletteFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GribStubImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Hdf5StubImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜IcnsImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜IcoImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Image.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageChops.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageCms.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageColor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageDraw.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageDraw2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageEnhance.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageFilter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageFont.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageGrab.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageMath.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageMode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageMorph.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageOps.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImagePalette.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImagePath.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageQt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageSequence.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageShow.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageStat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageTk.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageTransform.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImageWin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ImtImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜IptcImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Jpeg2KImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜JpegImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜JpegPresets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜McIdasImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MicImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MpegImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MpoImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MspImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PaletteFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PalmImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PcdImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PcfFontFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PcxImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PdfImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PdfParser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PixarImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PngImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PpmImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PsdImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PSDraw.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PyAccess.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜QoiImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜report.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜SgiImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜SpiderImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜SunImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜TarIO.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜TgaImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜TiffImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜TiffTags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜WalImageFile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜WebPImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜WmfImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜XbmImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜XpmImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜XVThumbImagePlugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_binary.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_deprecate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_tkinter_finder.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_typing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜BdfFontFile.py
 ┃ ┃ ┃ ┃ ┣ 📜BlpImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜BmpImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜BufrStubImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜ContainerIO.py
 ┃ ┃ ┃ ┃ ┣ 📜CurImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜DcxImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜DdsImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜EpsImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜ExifTags.py
 ┃ ┃ ┃ ┃ ┣ 📜features.py
 ┃ ┃ ┃ ┃ ┣ 📜FitsImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜FliImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜FontFile.py
 ┃ ┃ ┃ ┃ ┣ 📜FpxImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜FtexImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜GbrImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜GdImageFile.py
 ┃ ┃ ┃ ┃ ┣ 📜GifImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜GimpGradientFile.py
 ┃ ┃ ┃ ┃ ┣ 📜GimpPaletteFile.py
 ┃ ┃ ┃ ┃ ┣ 📜GribStubImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜Hdf5StubImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜IcnsImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜IcoImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜Image.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageChops.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageCms.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageColor.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageDraw.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageDraw2.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageEnhance.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageFile.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageFilter.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageFont.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageGrab.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageMath.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageMode.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageMorph.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageOps.py
 ┃ ┃ ┃ ┃ ┣ 📜ImagePalette.py
 ┃ ┃ ┃ ┃ ┣ 📜ImagePath.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageQt.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageSequence.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageShow.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageStat.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageTk.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageTransform.py
 ┃ ┃ ┃ ┃ ┣ 📜ImageWin.py
 ┃ ┃ ┃ ┃ ┣ 📜ImImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜ImtImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜IptcImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜Jpeg2KImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜JpegImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜JpegPresets.py
 ┃ ┃ ┃ ┃ ┣ 📜McIdasImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜MicImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜MpegImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜MpoImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜MspImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PaletteFile.py
 ┃ ┃ ┃ ┃ ┣ 📜PalmImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PcdImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PcfFontFile.py
 ┃ ┃ ┃ ┃ ┣ 📜PcxImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PdfImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PdfParser.py
 ┃ ┃ ┃ ┃ ┣ 📜PixarImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PngImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PpmImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PsdImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜PSDraw.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜PyAccess.py
 ┃ ┃ ┃ ┃ ┣ 📜QoiImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜report.py
 ┃ ┃ ┃ ┃ ┣ 📜SgiImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜SpiderImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜SunImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜TarIO.py
 ┃ ┃ ┃ ┃ ┣ 📜TgaImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜TiffImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜TiffTags.py
 ┃ ┃ ┃ ┃ ┣ 📜WalImageFile.py
 ┃ ┃ ┃ ┃ ┣ 📜WebPImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜WmfImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜XbmImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜XpmImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜XVThumbImagePlugin.py
 ┃ ┃ ┃ ┃ ┣ 📜_binary.py
 ┃ ┃ ┃ ┃ ┣ 📜_deprecate.py
 ┃ ┃ ┃ ┃ ┣ 📜_imaging.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_imaging.pyi
 ┃ ┃ ┃ ┃ ┣ 📜_imagingcms.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_imagingcms.pyi
 ┃ ┃ ┃ ┃ ┣ 📜_imagingft.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_imagingft.pyi
 ┃ ┃ ┃ ┃ ┣ 📜_imagingmath.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_imagingmath.pyi
 ┃ ┃ ┃ ┃ ┣ 📜_imagingmorph.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_imagingmorph.pyi
 ┃ ┃ ┃ ┃ ┣ 📜_imagingtk.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_tkinter_finder.py
 ┃ ┃ ┃ ┃ ┣ 📜_typing.py
 ┃ ┃ ┃ ┃ ┣ 📜_util.py
 ┃ ┃ ┃ ┃ ┣ 📜_version.py
 ┃ ┃ ┃ ┃ ┣ 📜_webp.cp310-win_amd64.pyd
 ┃ ┃ ┃ ┃ ┣ 📜_webp.pyi
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂pillow-10.4.0.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┣ 📜WHEEL
 ┃ ┃ ┃ ┃ ┗ 📜zip-safe
 ┃ ┃ ┃ ┣ 📂pip
 ┃ ┃ ┃ ┃ ┣ 📂_internal
 ┃ ┃ ┃ ┃ ┃ ┣ 📂cli
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocompletion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_command.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmdoptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜command_context.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main_parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜progress_bars.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_command.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spinners.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status_codes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autocompletion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base_command.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmdoptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜command_context.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main_parser.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜progress_bars.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_command.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spinners.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status_codes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂commands
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configuration.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜download.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜freeze.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hash.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜help.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜show.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uninstall.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configuration.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜download.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜freeze.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hash.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜help.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspect.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜list.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜show.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uninstall.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂distributions
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜installed.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜installed.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂index
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collector.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜package_finder.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sources.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collector.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜package_finder.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sources.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂locations
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_distutils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sysconfig.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_distutils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sysconfig.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂metadata
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂importlib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_dists.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_envs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_dists.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_envs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pkg_resources.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_json.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pkg_resources.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_json.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜candidate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜direct_url.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜format_control.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜installation_report.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜link.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scheme.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search_scope.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selection_prefs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜target_python.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜candidate.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜direct_url.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜format_control.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜installation_report.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜link.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scheme.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search_scope.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜selection_prefs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜target_python.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂network
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜download.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lazy_wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜session.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlrpc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜download.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lazy_wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜session.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xmlrpc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂operations
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂build
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_tracker.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata_editable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata_legacy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_editable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_legacy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_tracker.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata_editable.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata_legacy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_editable.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_legacy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂install
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜editable_legacy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜legacy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜editable_legacy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜legacy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜freeze.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepare.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜freeze.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepare.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂req
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constructors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_file.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_install.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_set.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_uninstall.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constructors.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_file.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_install.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_set.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜req_uninstall.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂resolution
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂legacy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂resolvelib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜candidates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜factory.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜found_candidates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜provider.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reporter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolver.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜candidates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜factory.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜found_candidates.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜provider.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reporter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolver.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜appdirs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compatibility_tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜direct_url_helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜distutils_args.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜egg_link.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜entrypoints.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filetypes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜glibc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inject_securetransport.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜misc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packaging.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜setuptools_build.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subprocess.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜temp_dir.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unpacking.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜virtualenv.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜appdirs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compatibility_tags.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deprecation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜direct_url_helpers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜distutils_args.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜egg_link.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜encoding.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜entrypoints.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filetypes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜glibc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hashes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inject_securetransport.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜misc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packaging.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜setuptools_build.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subprocess.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜temp_dir.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unpacking.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜virtualenv.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_log.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂vcs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bazaar.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜git.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mercurial.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subversion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜versioncontrol.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bazaar.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜git.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mercurial.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜subversion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜versioncontrol.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_env.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configuration.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜main.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyproject.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜self_outdated_check.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_builder.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜build_env.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜configuration.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pyproject.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜self_outdated_check.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_builder.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂_vendor
 ┃ ┃ ┃ ┃ ┃ ┣ 📂cachecontrol
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂caches
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜redis_cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜redis_cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜controller.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filewrapper.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜heuristics.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serialize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wrapper.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_cmd.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜controller.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filewrapper.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜heuristics.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜serialize.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wrapper.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_cmd.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂certifi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cacert.pem
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂chardet
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂cli
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chardetect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chardetect.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂metadata
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜languages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜languages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜big5freq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜big5prober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chardistribution.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charsetgroupprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charsetprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codingstatemachine.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codingstatemachinedict.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cp949prober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜escprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜escsm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜eucjpprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euckrfreq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euckrprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euctwfreq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euctwprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gb2312freq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gb2312prober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hebrewprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jisfreq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜johabfreq.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜johabprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jpcntx.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langbulgarianmodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langgreekmodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langhebrewmodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langhungarianmodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langrussianmodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langthaimodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langturkishmodel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latin1prober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macromanprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mbcharsetprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mbcsgroupprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mbcssm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resultdict.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sbcharsetprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sbcsgroupprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sjisprober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜universaldetector.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utf1632prober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utf8prober.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜big5freq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜big5prober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chardistribution.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charsetgroupprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜charsetprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codingstatemachine.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codingstatemachinedict.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cp949prober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜escprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜escsm.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜eucjpprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euckrfreq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euckrprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euctwfreq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜euctwprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gb2312freq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gb2312prober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hebrewprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jisfreq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜johabfreq.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜johabprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jpcntx.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langbulgarianmodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langgreekmodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langhebrewmodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langhungarianmodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langrussianmodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langthaimodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜langturkishmodel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latin1prober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macromanprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mbcharsetprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mbcsgroupprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mbcssm.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resultdict.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sbcharsetprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sbcsgroupprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sjisprober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜universaldetector.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utf1632prober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utf8prober.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂colorama
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜isatty_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm_test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32_test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi_test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise_test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜isatty_test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm_test.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansitowin32.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜initialise.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜winterm.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂distlib
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜database.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manifest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resources.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scripts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜database.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜locators.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manifest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resources.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scripts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜t32.exe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜t64-arm.exe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜t64.exe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜w32.exe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜w64-arm.exe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜w64.exe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂distro
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜distro.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜distro.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂idna
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codec.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜idnadata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜intranges.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜package_data.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uts46data.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜codec.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜idnadata.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜intranges.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜package_data.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜uts46data.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂msgpack
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fallback.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ext.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fallback.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂packaging
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜specifiers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_manylinux.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_musllinux.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_structures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__about__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜specifiers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_manylinux.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_musllinux.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_structures.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__about__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pkg_resources
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py31compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py31compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂platformdirs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜android.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macos.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unix.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜windows.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜android.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macos.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unix.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜windows.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pygments
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂filters
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂formatters
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bbcode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜groff.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜img.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜irc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latex.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜other.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pangomarkup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rtf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜svg.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal256.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bbcode.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜groff.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜img.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜irc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latex.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜other.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pangomarkup.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rtf.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜svg.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal256.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂lexers
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂styles
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmdline.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modeline.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜plugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regexopt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scanner.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sphinxext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜style.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜token.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unistring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmdline.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modeline.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜plugin.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regexopt.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scanner.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sphinxext.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜style.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜token.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unistring.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pyparsing
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂diagram
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜results.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜results.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pyproject_hooks
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂_in_process
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_in_process.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_in_process.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_impl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_impl.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂requests
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜certs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookies.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜help.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hooks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packages.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status_codes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜structures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_internal_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__version__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜api.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auth.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜certs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cookies.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜help.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hooks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜packages.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sessions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status_codes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜structures.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_internal_utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__version__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂resolvelib
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂compat
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections_abc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collections_abc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜providers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reporters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolvers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜structs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜providers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reporters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolvers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜structs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂rich
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜align.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bar.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜box.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cells.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color_triplet.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜columns.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constrain.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜containers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜control.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default_styles.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜diagnose.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emoji.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesize.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_proxy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜highlighter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jupyter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜live.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜live_render.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜measure.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜padding.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pager.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜palette.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜panel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pretty.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜progress.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜progress_bar.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prompt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜protocol.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜region.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜repr.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rule.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scope.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜screen.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜segment.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spinner.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜style.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜styled.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syntax.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal_theme.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜theme.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜themes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜traceback.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_cell_widths.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_emoji_codes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_emoji_replace.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_export_format.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_inspect.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_log_render.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_loop.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_null_file.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_palettes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_pick.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_ratio.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_spinners.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_stack.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_timer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_win32_console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_windows.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_windows_renderer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_wrap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜align.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bar.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜box.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cells.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color_triplet.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜columns.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜constrain.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜containers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜control.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default_styles.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜diagnose.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emoji.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesize.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_proxy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜highlighter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jupyter.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layout.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜live.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜live_render.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markup.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜measure.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜padding.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pager.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜palette.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜panel.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pretty.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜progress.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜progress_bar.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prompt.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜protocol.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜region.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜repr.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rule.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scope.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜screen.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜segment.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spinner.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜status.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜style.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜styled.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜syntax.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜table.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal_theme.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜theme.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜themes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜traceback.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tree.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_cell_widths.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_emoji_codes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_emoji_replace.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_export_format.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_extension.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_inspect.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_log_render.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_loop.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_null_file.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_palettes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_pick.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_ratio.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_spinners.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_stack.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_timer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_win32_console.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_windows.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_windows_renderer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_wrap.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tenacity
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜after.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜before.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜before_sleep.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stop.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tornadoweb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wait.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_asyncio.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜after.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜before.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜before_sleep.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nap.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stop.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tornadoweb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wait.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_asyncio.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tomli
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_re.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_types.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_parser.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_re.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_types.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂urllib3
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂_securetransport
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bindings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜low_level.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bindings.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜low_level.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜appengine.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ntlmpool.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyopenssl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜securetransport.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_appengine_environ.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜appengine.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ntlmpool.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyopenssl.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜securetransport.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socks.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_appengine_environ.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂packages
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂backports
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makefile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makefile.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜six.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜six.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂util
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queue.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssltransport.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜url.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wait.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜queue.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssltransport.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜url.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wait.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connectionpool.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filepost.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜poolmanager.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connectionpool.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filepost.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜poolmanager.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂webencodings
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜labels.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mklabels.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜x_user_defined.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜labels.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mklabels.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜x_user_defined.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜six.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing_extensions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜six.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typing_extensions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vendor.txt
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__pip-runner__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📜__main__.py
 ┃ ┃ ┃ ┃ ┗ 📜__pip-runner__.py
 ┃ ┃ ┃ ┣ 📂pip-23.0.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂pkg_resources
 ┃ ┃ ┃ ┃ ┣ 📂extern
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂_vendor
 ┃ ┃ ┃ ┃ ┃ ┣ 📂importlib_resources
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜readers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_adapters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_legacy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜readers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_adapters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_common.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_legacy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂jaraco
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂text
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂more_itertools
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜more.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recipes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜more.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recipes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂packaging
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜specifiers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_manylinux.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_musllinux.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_structures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__about__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜specifiers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_manylinux.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_musllinux.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_structures.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__about__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pyparsing
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂diagram
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜results.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜results.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜appdirs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zipp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜appdirs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zipp.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂prompt_toolkit
 ┃ ┃ ┃ ┃ ┣ 📂application
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜application.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜current.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜run_in_terminal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜application.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜current.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜run_in_terminal.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂clipboard
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜in_memory.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyperclip.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜in_memory.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pyperclip.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂completion
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜deduplicate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fuzzy_completer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nested.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜word_completer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜deduplicate.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fuzzy_completer.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nested.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜word_completer.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┣ 📂completers
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜system.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜system.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂regular_languages
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regex_parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜regex_parser.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂ssh
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂telnet
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜protocol.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜protocol.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜server.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂eventloop
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜async_generator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inputhook.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜async_generator.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inputhook.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂filters
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜app.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cli.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜app.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cli.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂formatted_text
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pygments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜html.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pygments.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂input
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi_escape_sequences.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posix_pipe.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜posix_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typeahead.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vt100.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vt100_parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win32_pipe.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ansi_escape_sequences.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜posix_pipe.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜posix_utils.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typeahead.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vt100.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vt100_parser.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜win32_pipe.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂key_binding
 ┃ ┃ ┃ ┃ ┃ ┣ 📂bindings
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_suggest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cpr.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emacs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜focus.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mouse.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜named_commands.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜open_in_editor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜page_navigation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scroll.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_suggest.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basic.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜completion.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cpr.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emacs.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜focus.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mouse.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜named_commands.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜open_in_editor.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜page_navigation.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scroll.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜search.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vi.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜digraphs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emacs_state.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key_bindings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜key_processor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vi_state.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜digraphs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜emacs_state.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜key_bindings.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜key_processor.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vi_state.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂layout
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜containers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜controls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dimension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜layout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜margins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜menus.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mouse_handlers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜processors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜screen.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scrollable_pane.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜containers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜controls.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dimension.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜layout.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜margins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜menus.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mouse_handlers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜processors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜screen.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scrollable_pane.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂lexers
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pygments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pygments.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂output
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜color_depth.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜conemu.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜flush_stdout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜plain_text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vt100.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜windows10.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜color_depth.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜conemu.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜flush_stdout.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜plain_text.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vt100.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜win32.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜windows10.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂shortcuts
 ┃ ┃ ┃ ┃ ┃ ┣ 📂progress_bar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formatters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dialogs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prompt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dialogs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prompt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂styles
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜named_colors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pygments.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜style.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜style_transformation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜defaults.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜named_colors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pygments.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜style.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜style_transformation.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂widgets
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dialogs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜menus.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toolbars.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dialogs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜menus.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜toolbars.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜auto_suggest.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜buffer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cursor_shapes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜data_structures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜document.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜enums.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜history.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜keys.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mouse_events.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜patch_stdout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜renderer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜search.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜selection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜token.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜validation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜win32_types.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜auto_suggest.py
 ┃ ┃ ┃ ┃ ┣ 📜buffer.py
 ┃ ┃ ┃ ┃ ┣ 📜cache.py
 ┃ ┃ ┃ ┃ ┣ 📜cursor_shapes.py
 ┃ ┃ ┃ ┃ ┣ 📜data_structures.py
 ┃ ┃ ┃ ┃ ┣ 📜document.py
 ┃ ┃ ┃ ┃ ┣ 📜enums.py
 ┃ ┃ ┃ ┃ ┣ 📜history.py
 ┃ ┃ ┃ ┃ ┣ 📜keys.py
 ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┣ 📜mouse_events.py
 ┃ ┃ ┃ ┃ ┣ 📜patch_stdout.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜renderer.py
 ┃ ┃ ┃ ┃ ┣ 📜search.py
 ┃ ┃ ┃ ┃ ┣ 📜selection.py
 ┃ ┃ ┃ ┃ ┣ 📜token.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜validation.py
 ┃ ┃ ┃ ┃ ┣ 📜win32_types.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂prompt_toolkit-3.0.47.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜AUTHORS.rst
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂pure_eval
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜my_getattr_static.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┣ 📜my_getattr_static.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂pure_eval-0.2.3.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂pygments
 ┃ ┃ ┃ ┃ ┣ 📂filters
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂formatters
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bbcode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜groff.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜img.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜irc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜latex.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜other.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pangomarkup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rtf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜svg.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal256.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bbcode.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜groff.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜html.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜img.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜irc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜latex.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜other.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pangomarkup.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rtf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜svg.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜terminal256.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂lexers
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actionscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ada.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜agile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜algebra.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ambient.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜amdgpu.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ampl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apdlexer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜apl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜archetype.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜arrow.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜arturo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜asn1.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜automation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bare.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜basic.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdd.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜berry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bibtex.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜blueprint.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜boa.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bqn.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜business.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜capnproto.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜carbon.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cddl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chapel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜comal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compiled.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cplint.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜crystal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜csound.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜css.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜c_cpp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜c_like.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜d.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dalvik.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜data.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dax.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜devicetree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜diff.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dns.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dotnet.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dsls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dylan.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ecl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜eiffel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜elm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜elpi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜email.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜erlang.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜esoteric.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ezhil.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜factor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fantom.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜felix.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fift.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜floscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜forth.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fortran.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜foxpro.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜freefem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜func.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functional.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜futhark.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gcodelexer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gdscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜go.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar_notation.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graph.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graphics.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graphql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜graphviz.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gsql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜haskell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜haxe.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hdl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜hexdump.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜html.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜idl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜igor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inferno.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜installers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int_fiction.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜iolang.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜j.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜javascript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jmespath.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jslt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonnet.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsx.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜julia.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jvm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kuin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜kusto.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ldap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lean.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lilypond.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lisp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜macaulay2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜make.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markup.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜math.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜matlab.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜maxima.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜meson.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mime.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜minecraft.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mips.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ml.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modeling.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜modula2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mojo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜monte.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜mosel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ncl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nimrod.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nit.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nix.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜oberon.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜objective.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ooc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜openscad.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜other.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parasail.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parsers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pascal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pawn.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜perl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜phix.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜php.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pointless.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pony.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜praat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜procfile.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prolog.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜promql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ptx.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜python.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜q.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜qlik.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜qvt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜r.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rdf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rebol.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resource.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ride.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rita.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rnc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜roboconf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜robotframework.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ruby.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rust.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sas.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜savi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scdoc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜scripting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sgf.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shell.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sieve.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜slash.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smalltalk.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smithy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜smv.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜snobol.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜solidity.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜soong.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sophia.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜special.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spice.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜srcinfo.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stata.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜supercollider.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tact.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tcl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜teal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜teraterm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textedit.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜textfmts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜theorem.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜thingsdb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tlb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tls.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tnt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trafficscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typoscript.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typst.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ul4.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicon.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜urbi.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜usd.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜varnish.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜verification.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜verifpal.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vip.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vyper.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜web.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜webassembly.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜webidl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜webmisc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wgsl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜whiley.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wowtoc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wren.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜x10.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xorg.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜yang.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜yara.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zig.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_ada_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_asy_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_cl_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_cocoa_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_csound_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_css_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_julia_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_lasso_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_lilypond_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_luau_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_lua_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mql_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mysql_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_openedge_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_php_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_postgres_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_qlik_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_scheme_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_scilab_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_sourcemod_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_stan_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_stata_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_tsql_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_usd_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_vbscript_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_vim_builtins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜actionscript.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ada.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜agile.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜algebra.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ambient.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜amdgpu.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ampl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜apdlexer.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜apl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜archetype.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arrow.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arturo.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asm.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asn1.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜automation.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bare.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜basic.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bdd.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜berry.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bibtex.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜blueprint.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜boa.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bqn.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜business.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜capnproto.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜carbon.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cddl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜chapel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜clean.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜comal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compiled.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜configs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜console.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cplint.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜crystal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜csound.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜css.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜c_cpp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜c_like.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜d.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dalvik.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜data.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dax.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜devicetree.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜diff.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dns.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dotnet.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dsls.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dylan.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ecl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜eiffel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜elm.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜elpi.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜email.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜erlang.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜esoteric.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ezhil.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜factor.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fantom.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜felix.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fift.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜floscript.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜forth.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fortran.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜foxpro.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜freefem.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜func.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜functional.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜futhark.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gcodelexer.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gdscript.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜go.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grammar_notation.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜graphics.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜graphql.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜graphviz.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gsql.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜haskell.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜haxe.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜hdl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜hexdump.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜html.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜idl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜igor.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inferno.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜installers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜int_fiction.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜iolang.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜j.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜javascript.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jmespath.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jslt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonnet.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jsx.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜julia.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jvm.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜kuin.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜kusto.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ldap.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lean.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lilypond.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lisp.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜macaulay2.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜make.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜markup.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜math.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜matlab.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜maxima.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜meson.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mime.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜minecraft.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mips.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ml.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜modeling.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜modula2.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mojo.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜monte.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mosel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ncl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nimrod.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nit.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nix.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜oberon.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜objective.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ooc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜openscad.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜other.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parasail.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parsers.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pascal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pawn.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜perl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜phix.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜php.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pointless.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pony.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜praat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜procfile.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prolog.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜promql.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prql.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ptx.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜python.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜q.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜qlik.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜qvt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜r.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rdf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rebol.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resource.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ride.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rita.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rnc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜roboconf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜robotframework.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ruby.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rust.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sas.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜savi.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scdoc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scripting.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sgf.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shell.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sieve.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜slash.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜smalltalk.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜smithy.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜smv.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜snobol.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜solidity.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜soong.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sophia.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜special.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜spice.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sql.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜srcinfo.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stata.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜supercollider.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tact.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tcl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜teal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜templates.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜teraterm.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜textedit.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜textfmts.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜theorem.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜thingsdb.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tlb.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tls.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tnt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜trafficscript.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typoscript.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typst.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ul4.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜unicon.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜urbi.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜usd.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜varnish.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜verification.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜verifpal.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vip.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vyper.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜web.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜webassembly.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜webidl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜webmisc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wgsl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜whiley.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wowtoc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wren.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜x10.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜xorg.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜yang.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜yara.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zig.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_ada_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_asy_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_cl_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_cocoa_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_csound_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_css_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_julia_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_lasso_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_lilypond_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_luau_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_lua_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_mql_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_mysql_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_openedge_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_php_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_postgres_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_qlik_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_scheme_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_scilab_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_sourcemod_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_stan_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_stata_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_tsql_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_usd_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_vbscript_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_vim_builtins.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂styles
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abap.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜algol.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜algol_nu.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜arduino.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜autumn.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜borland.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bw.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coffee.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜colorful.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dracula.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emacs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜friendly.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜friendly_grayscale.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fruity.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gh_dark.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜gruvbox.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜igor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inkpot.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lightbulb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lilypond.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lovelace.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manni.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜material.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜monokai.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜murphy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜native.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nord.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜onedark.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜paraiso_dark.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜paraiso_light.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pastie.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜perldoc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rainbow_dash.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rrt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sas.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜solarized.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜staroffice.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stata_dark.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stata_light.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tango.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜trac.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vim.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜xcode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zenburn.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜abap.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜algol.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜algol_nu.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arduino.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜autumn.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜borland.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bw.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜coffee.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜colorful.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜default.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dracula.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜emacs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜friendly.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜friendly_grayscale.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fruity.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gh_dark.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gruvbox.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜igor.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inkpot.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lightbulb.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lilypond.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lovelace.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜manni.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜material.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜monokai.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜murphy.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜native.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nord.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜onedark.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜paraiso_dark.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜paraiso_light.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pastie.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜perldoc.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rainbow_dash.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rrt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sas.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜solarized.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜staroffice.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stata_dark.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stata_light.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tango.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜trac.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vim.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vs.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜xcode.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zenburn.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cmdline.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formatter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜modeline.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜plugin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜regexopt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scanner.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sphinxext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜style.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜token.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜unistring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜cmdline.py
 ┃ ┃ ┃ ┃ ┣ 📜console.py
 ┃ ┃ ┃ ┃ ┣ 📜filter.py
 ┃ ┃ ┃ ┃ ┣ 📜formatter.py
 ┃ ┃ ┃ ┃ ┣ 📜lexer.py
 ┃ ┃ ┃ ┃ ┣ 📜modeline.py
 ┃ ┃ ┃ ┃ ┣ 📜plugin.py
 ┃ ┃ ┃ ┃ ┣ 📜regexopt.py
 ┃ ┃ ┃ ┃ ┣ 📜scanner.py
 ┃ ┃ ┃ ┃ ┣ 📜sphinxext.py
 ┃ ┃ ┃ ┃ ┣ 📜style.py
 ┃ ┃ ┃ ┃ ┣ 📜token.py
 ┃ ┃ ┃ ┃ ┣ 📜unistring.py
 ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂pygments-2.18.0.dist-info
 ┃ ┃ ┃ ┃ ┣ 📂licenses
 ┃ ┃ ┃ ┃ ┃ ┣ 📜AUTHORS
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂setuptools
 ┃ ┃ ┃ ┃ ┣ 📂command
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜alias.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_egg.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_clib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_ext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_py.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜develop.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dist_info.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜easy_install.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜editable_wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜egg_info.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_lib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_scripts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py36compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜register.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rotate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜saveopts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜setopt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜upload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜upload_docs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜alias.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_egg.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜build.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜build_clib.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜build_ext.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜build_py.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜develop.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dist_info.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜easy_install.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜editable_wheel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜egg_info.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜install.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜install_lib.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜install_scripts.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜launcher manifest.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜py36compat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜register.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rotate.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜saveopts.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜setopt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜upload.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜upload_docs.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂config
 ┃ ┃ ┃ ┃ ┃ ┣ 📂_validate_pyproject
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error_reporting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extra_validations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fastjsonschema_exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fastjsonschema_validations.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜error_reporting.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extra_validations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fastjsonschema_exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fastjsonschema_validations.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜formats.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜expand.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyprojecttoml.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜setupcfg.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_apply_pyprojecttoml.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜expand.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pyprojecttoml.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜setupcfg.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_apply_pyprojecttoml.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂extern
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂_distutils
 ┃ ┃ ┃ ┃ ┃ ┣ 📂command
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_dumb.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_clib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_ext.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_py.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_scripts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_data.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_headers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_lib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_scripts.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py37compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜register.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜upload.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_framework_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_dumb.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_clib.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_ext.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_py.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build_scripts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜check.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clean.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_data.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_headers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_lib.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜install_scripts.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py37compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜register.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sdist.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜upload.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_framework_compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜archive_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bcppcompiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ccompiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cmd.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cygwinccompiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dep_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dir_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fancy_getopt.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filelist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜file_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜msvc9compiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜msvccompiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py38compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜py39compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spawn.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sysconfig.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text_file.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unixccompiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜versionpredicate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_functools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_macos_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_msvccompiler.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜archive_util.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bcppcompiler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ccompiler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cmd.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cygwinccompiler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜debug.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dep_util.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dir_util.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dist.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fancy_getopt.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filelist.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜file_util.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜msvc9compiler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜msvccompiler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜py38compat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜py39compat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜spawn.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sysconfig.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜text_file.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜unixccompiler.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜versionpredicate.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_functools.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_macos_compat.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_msvccompiler.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂_vendor
 ┃ ┃ ┃ ┃ ┃ ┣ 📂importlib_metadata
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_adapters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_functools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_meta.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_adapters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_functools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_meta.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_text.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂importlib_resources
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜readers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_adapters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_legacy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜abc.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜readers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜simple.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_adapters.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_common.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_legacy.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂jaraco
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂text
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜context.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functools.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂more_itertools
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜more.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recipes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜more.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recipes.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂packaging
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜specifiers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_manylinux.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_musllinux.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_structures.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__about__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜markers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜specifiers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_manylinux.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_musllinux.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_structures.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__about__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂pyparsing
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂diagram
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜results.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜helpers.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜results.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜testing.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂tomli
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_parser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_re.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_types.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_parser.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_re.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_types.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ordered_set.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typing_extensions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜zipp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ordered_set.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typing_extensions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zipp.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜archive_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜build_meta.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜depends.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dep_util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜discovery.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dist.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜extension.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜glob.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜installer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜launch.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜logging.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜monkey.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜msvc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜namespaces.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜package_index.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜py34compat.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sandbox.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode_utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜windows_support.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_deprecation_warning.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_entry_points.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_imp.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_importlib.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_path.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_reqs.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜archive_util.py
 ┃ ┃ ┃ ┃ ┣ 📜build_meta.py
 ┃ ┃ ┃ ┃ ┣ 📜cli-32.exe
 ┃ ┃ ┃ ┃ ┣ 📜cli-64.exe
 ┃ ┃ ┃ ┃ ┣ 📜cli-arm64.exe
 ┃ ┃ ┃ ┃ ┣ 📜cli.exe
 ┃ ┃ ┃ ┃ ┣ 📜depends.py
 ┃ ┃ ┃ ┃ ┣ 📜dep_util.py
 ┃ ┃ ┃ ┃ ┣ 📜discovery.py
 ┃ ┃ ┃ ┃ ┣ 📜dist.py
 ┃ ┃ ┃ ┃ ┣ 📜errors.py
 ┃ ┃ ┃ ┃ ┣ 📜extension.py
 ┃ ┃ ┃ ┃ ┣ 📜glob.py
 ┃ ┃ ┃ ┃ ┣ 📜gui-32.exe
 ┃ ┃ ┃ ┃ ┣ 📜gui-64.exe
 ┃ ┃ ┃ ┃ ┣ 📜gui-arm64.exe
 ┃ ┃ ┃ ┃ ┣ 📜gui.exe
 ┃ ┃ ┃ ┃ ┣ 📜installer.py
 ┃ ┃ ┃ ┃ ┣ 📜launch.py
 ┃ ┃ ┃ ┃ ┣ 📜logging.py
 ┃ ┃ ┃ ┃ ┣ 📜monkey.py
 ┃ ┃ ┃ ┃ ┣ 📜msvc.py
 ┃ ┃ ┃ ┃ ┣ 📜namespaces.py
 ┃ ┃ ┃ ┃ ┣ 📜package_index.py
 ┃ ┃ ┃ ┃ ┣ 📜py34compat.py
 ┃ ┃ ┃ ┃ ┣ 📜sandbox.py
 ┃ ┃ ┃ ┃ ┣ 📜script (dev).tmpl
 ┃ ┃ ┃ ┃ ┣ 📜script.tmpl
 ┃ ┃ ┃ ┃ ┣ 📜unicode_utils.py
 ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┣ 📜wheel.py
 ┃ ┃ ┃ ┃ ┣ 📜windows_support.py
 ┃ ┃ ┃ ┃ ┣ 📜_deprecation_warning.py
 ┃ ┃ ┃ ┃ ┣ 📜_entry_points.py
 ┃ ┃ ┃ ┃ ┣ 📜_imp.py
 ┃ ┃ ┃ ┃ ┣ 📜_importlib.py
 ┃ ┃ ┃ ┃ ┣ 📜_itertools.py
 ┃ ┃ ┃ ┃ ┣ 📜_path.py
 ┃ ┃ ┃ ┃ ┣ 📜_reqs.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂setuptools-65.5.0.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂six-1.16.0.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂sqlparse
 ┃ ┃ ┃ ┃ ┣ 📂engine
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜filter_stack.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜grouping.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜statement_splitter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filter_stack.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜grouping.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜statement_splitter.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂filters
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aligned_indent.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜others.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜output.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reindent.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜right_margin.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜aligned_indent.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜others.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜output.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜reindent.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜right_margin.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cli.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formatter.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜keywords.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sql.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tokens.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜cli.py
 ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┣ 📜formatter.py
 ┃ ┃ ┃ ┃ ┣ 📜keywords.py
 ┃ ┃ ┃ ┃ ┣ 📜lexer.py
 ┃ ┃ ┃ ┃ ┣ 📜sql.py
 ┃ ┃ ┃ ┃ ┣ 📜tokens.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜__main__.py
 ┃ ┃ ┃ ┣ 📂sqlparse-0.5.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📂licenses
 ┃ ┃ ┃ ┃ ┃ ┣ 📜AUTHORS
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂stack_data
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜formatting.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜serializing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┣ 📜formatting.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜serializing.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂stack_data-0.6.3.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂svgwrite
 ┃ ┃ ┃ ┃ ┣ 📂data
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜colors.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜full11.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pattern.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜svgparser.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜tiny12.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜typechecker.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜types.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜colors.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜full11.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pattern.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜svgparser.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tiny12.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜typechecker.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜types.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂extensions
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inkscape.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜shapes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜inkscape.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shapes.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜animate.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜container.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜drawing.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜elementfactory.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜etree.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filters.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜gradients.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜image.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜masking.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜params.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜path.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pattern.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜shapes.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜solidcolor.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜validator2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜animate.py
 ┃ ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┃ ┣ 📜container.py
 ┃ ┃ ┃ ┃ ┣ 📜drawing.py
 ┃ ┃ ┃ ┃ ┣ 📜elementfactory.py
 ┃ ┃ ┃ ┃ ┣ 📜etree.py
 ┃ ┃ ┃ ┃ ┣ 📜filters.py
 ┃ ┃ ┃ ┃ ┣ 📜gradients.py
 ┃ ┃ ┃ ┃ ┣ 📜image.py
 ┃ ┃ ┃ ┃ ┣ 📜masking.py
 ┃ ┃ ┃ ┃ ┣ 📜mixins.py
 ┃ ┃ ┃ ┃ ┣ 📜params.py
 ┃ ┃ ┃ ┃ ┣ 📜path.py
 ┃ ┃ ┃ ┃ ┣ 📜pattern.py
 ┃ ┃ ┃ ┃ ┣ 📜shapes.py
 ┃ ┃ ┃ ┃ ┣ 📜solidcolor.py
 ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┣ 📜validator2.py
 ┃ ┃ ┃ ┃ ┣ 📜version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂svgwrite-1.4.3.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE.TXT
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂traitlets
 ┃ ┃ ┃ ┃ ┣ 📂config
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜application.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜argcomplete_config.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜configurable.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜manager.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sphinxdoc.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜application.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜argcomplete_config.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜configurable.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜loader.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜manager.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sphinxdoc.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂tests
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test_traitlets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_traitlets.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bunch.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜descriptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜getargspec.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜importstring.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜nested_update.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜sentinel.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜warnings.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bunch.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜descriptions.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜getargspec.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜importstring.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nested_update.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sentinel.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜text.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜warnings.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜log.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜traitlets.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜log.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜traitlets.py
 ┃ ┃ ┃ ┃ ┣ 📜_version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂traitlets-5.14.3.dist-info
 ┃ ┃ ┃ ┃ ┣ 📂licenses
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂Tree
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cli.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜core.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜draw.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜cli.py
 ┃ ┃ ┃ ┃ ┣ 📜core.py
 ┃ ┃ ┃ ┃ ┣ 📜draw.py
 ┃ ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂Tree-0.2.4-py3.10.egg-info
 ┃ ┃ ┃ ┃ ┣ 📜dependency_links.txt
 ┃ ┃ ┃ ┃ ┣ 📜entry_points.txt
 ┃ ┃ ┃ ┃ ┣ 📜installed-files.txt
 ┃ ┃ ┃ ┃ ┣ 📜not-zip-safe
 ┃ ┃ ┃ ┃ ┣ 📜PKG-INFO
 ┃ ┃ ┃ ┃ ┣ 📜requires.txt
 ┃ ┃ ┃ ┃ ┣ 📜SOURCES.txt
 ┃ ┃ ┃ ┃ ┗ 📜top_level.txt
 ┃ ┃ ┃ ┣ 📂typing_extensions-4.12.2.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂tzdata
 ┃ ┃ ┃ ┃ ┣ 📂zoneinfo
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Africa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Abidjan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Accra
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Addis_Ababa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Algiers
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Asmara
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Asmera
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bamako
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bangui
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Banjul
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bissau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Blantyre
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Brazzaville
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bujumbura
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cairo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Casablanca
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ceuta
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Conakry
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dakar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dar_es_Salaam
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Djibouti
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Douala
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜El_Aaiun
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Freetown
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Gaborone
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Harare
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Johannesburg
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Juba
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kampala
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Khartoum
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kigali
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kinshasa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lagos
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Libreville
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lome
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Luanda
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lubumbashi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lusaka
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Malabo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Maputo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Maseru
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mbabane
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mogadishu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Monrovia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nairobi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ndjamena
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Niamey
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nouakchott
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ouagadougou
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Porto-Novo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sao_Tome
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Timbuktu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tripoli
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tunis
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Windhoek
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂America
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂Argentina
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Buenos_Aires
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Catamarca
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ComodRivadavia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cordoba
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jujuy
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜La_Rioja
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mendoza
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rio_Gallegos
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Salta
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜San_Juan
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜San_Luis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tucuman
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ushuaia
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂Indiana
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Indianapolis
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Knox
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Marengo
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Petersburg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tell_City
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vevay
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vincennes
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Winamac
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂Kentucky
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Louisville
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Monticello
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂North_Dakota
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Beulah
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Center
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜New_Salem
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Adak
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Anchorage
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Anguilla
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Antigua
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Araguaina
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Aruba
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Asuncion
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Atikokan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Atka
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bahia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bahia_Banderas
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Barbados
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Belem
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Belize
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Blanc-Sablon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Boa_Vista
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bogota
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Boise
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Buenos_Aires
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cambridge_Bay
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Campo_Grande
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cancun
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Caracas
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Catamarca
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cayenne
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cayman
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chicago
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chihuahua
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ciudad_Juarez
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Coral_Harbour
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cordoba
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Costa_Rica
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Creston
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cuiaba
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Curacao
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Danmarkshavn
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dawson
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dawson_Creek
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Denver
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Detroit
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dominica
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Edmonton
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Eirunepe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜El_Salvador
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ensenada
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Fortaleza
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Fort_Nelson
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Fort_Wayne
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Glace_Bay
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Godthab
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Goose_Bay
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Grand_Turk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Grenada
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guadeloupe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guatemala
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guayaquil
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guyana
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Halifax
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Havana
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Hermosillo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Indianapolis
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Inuvik
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Iqaluit
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jamaica
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jujuy
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Juneau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Knox_IN
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kralendijk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜La_Paz
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lima
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Los_Angeles
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Louisville
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lower_Princes
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Maceio
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Managua
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Manaus
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Marigot
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Martinique
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Matamoros
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mazatlan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mendoza
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Menominee
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Merida
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Metlakatla
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mexico_City
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Miquelon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Moncton
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Monterrey
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Montevideo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Montreal
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Montserrat
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nassau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜New_York
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nipigon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nome
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Noronha
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nuuk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ojinaga
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Panama
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pangnirtung
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Paramaribo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Phoenix
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Port-au-Prince
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Porto_Acre
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Porto_Velho
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Port_of_Spain
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Puerto_Rico
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Punta_Arenas
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rainy_River
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rankin_Inlet
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Recife
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Regina
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Resolute
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rio_Branco
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rosario
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Santarem
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Santa_Isabel
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Santiago
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Santo_Domingo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sao_Paulo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Scoresbysund
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Shiprock
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sitka
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Barthelemy
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Johns
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Kitts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Lucia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Thomas
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Vincent
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Swift_Current
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tegucigalpa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Thule
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Thunder_Bay
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tijuana
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Toronto
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tortola
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vancouver
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Virgin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Whitehorse
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Winnipeg
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yakutat
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yellowknife
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Antarctica
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Casey
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Davis
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜DumontDUrville
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Macquarie
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mawson
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜McMurdo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Palmer
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rothera
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜South_Pole
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Syowa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Troll
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vostok
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Arctic
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Longyearbyen
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Asia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Aden
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Almaty
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Amman
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Anadyr
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Aqtau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Aqtobe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ashgabat
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ashkhabad
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Atyrau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Baghdad
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bahrain
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Baku
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bangkok
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Barnaul
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Beirut
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bishkek
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Brunei
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Calcutta
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chita
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Choibalsan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chongqing
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chungking
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Colombo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dacca
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Damascus
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dhaka
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dili
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dubai
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dushanbe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Famagusta
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Gaza
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Harbin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Hebron
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Hong_Kong
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Hovd
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ho_Chi_Minh
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Irkutsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Istanbul
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jakarta
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jayapura
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jerusalem
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kabul
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kamchatka
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Karachi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kashgar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kathmandu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Katmandu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Khandyga
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kolkata
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Krasnoyarsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kuala_Lumpur
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kuching
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kuwait
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Macao
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Macau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Magadan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Makassar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Manila
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Muscat
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nicosia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Novokuznetsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Novosibirsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Omsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Oral
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Phnom_Penh
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pontianak
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pyongyang
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Qatar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Qostanay
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Qyzylorda
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rangoon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Riyadh
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Saigon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sakhalin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Samarkand
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Seoul
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Shanghai
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Singapore
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Srednekolymsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Taipei
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tashkent
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tbilisi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tehran
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tel_Aviv
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Thimbu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Thimphu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tokyo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tomsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ujung_Pandang
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ulaanbaatar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ulan_Bator
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Urumqi
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ust-Nera
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vientiane
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vladivostok
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yakutsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yangon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yekaterinburg
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yerevan
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Atlantic
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Azores
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bermuda
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Canary
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cape_Verde
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Faeroe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Faroe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jan_Mayen
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Madeira
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Reykjavik
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜South_Georgia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Stanley
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜St_Helena
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Australia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ACT
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Adelaide
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Brisbane
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Broken_Hill
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Canberra
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Currie
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Darwin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Eucla
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Hobart
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LHI
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lindeman
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lord_Howe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Melbourne
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜North
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜NSW
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Perth
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Queensland
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜South
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sydney
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tasmania
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Victoria
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜West
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yancowinna
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Brazil
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Acre
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜DeNoronha
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜East
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜West
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Canada
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Atlantic
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Central
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Eastern
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mountain
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Newfoundland
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pacific
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Saskatchewan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yukon
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Chile
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Continental
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜EasterIsland
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Etc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+0
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+1
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+10
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+11
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+12
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+2
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+3
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+4
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+5
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+6
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+7
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+8
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+9
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-0
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-1
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-10
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-11
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-12
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-13
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-14
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-2
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-3
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-4
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-5
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-6
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-7
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-8
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-9
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT0
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Greenwich
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜UCT
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Universal
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜UTC
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Zulu
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Europe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Amsterdam
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Andorra
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Astrakhan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Athens
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Belfast
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Belgrade
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Berlin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bratislava
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Brussels
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bucharest
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Budapest
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Busingen
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chisinau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Copenhagen
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Dublin
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Gibraltar
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guernsey
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Helsinki
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Isle_of_Man
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Istanbul
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Jersey
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kaliningrad
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kiev
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kirov
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kyiv
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Lisbon
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ljubljana
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜London
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Luxembourg
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Madrid
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Malta
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mariehamn
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Minsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Monaco
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Moscow
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nicosia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Oslo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Paris
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Podgorica
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Prague
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Riga
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rome
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Samara
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜San_Marino
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sarajevo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Saratov
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Simferopol
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Skopje
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Sofia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Stockholm
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tallinn
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tirane
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tiraspol
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ulyanovsk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Uzhgorod
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vaduz
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vatican
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vienna
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Vilnius
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Volgograd
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Warsaw
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Zagreb
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Zaporozhye
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Zurich
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Indian
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Antananarivo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chagos
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Christmas
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Cocos
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Comoro
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kerguelen
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mahe
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Maldives
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mauritius
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mayotte
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Reunion
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Mexico
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜BajaNorte
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜BajaSur
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜General
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂Pacific
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Apia
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Auckland
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Bougainville
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chatham
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Chuuk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Easter
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Efate
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Enderbury
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Fakaofo
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Fiji
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Funafuti
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Galapagos
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Gambier
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guadalcanal
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Guam
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Honolulu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Johnston
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kanton
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kiritimati
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kosrae
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Kwajalein
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Majuro
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Marquesas
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Midway
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Nauru
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Niue
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Norfolk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Noumea
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pago_Pago
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Palau
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pitcairn
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pohnpei
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Ponape
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Port_Moresby
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Rarotonga
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Saipan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Samoa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tahiti
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tarawa
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Tongatapu
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Truk
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Wake
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Wallis
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Yap
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂US
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Alaska
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Aleutian
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Arizona
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Central
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜East-Indiana
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Eastern
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Hawaii
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Indiana-Starke
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Michigan
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Mountain
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pacific
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Samoa
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CET
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CST6CDT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Cuba
 ┃ ┃ ┃ ┃ ┃ ┣ 📜EET
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Egypt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Eire
 ┃ ┃ ┃ ┃ ┃ ┣ 📜EST
 ┃ ┃ ┃ ┃ ┃ ┣ 📜EST5EDT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Factory
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GB
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GB-Eire
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT+0
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT-0
 ┃ ┃ ┃ ┃ ┃ ┣ 📜GMT0
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Greenwich
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Hongkong
 ┃ ┃ ┃ ┃ ┃ ┣ 📜HST
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Iceland
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Iran
 ┃ ┃ ┃ ┃ ┃ ┣ 📜iso3166.tab
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Israel
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Jamaica
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Japan
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Kwajalein
 ┃ ┃ ┃ ┃ ┃ ┣ 📜leapseconds
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Libya
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MET
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MST
 ┃ ┃ ┃ ┃ ┃ ┣ 📜MST7MDT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Navajo
 ┃ ┃ ┃ ┃ ┃ ┣ 📜NZ
 ┃ ┃ ┃ ┃ ┃ ┣ 📜NZ-CHAT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Poland
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Portugal
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PRC
 ┃ ┃ ┃ ┃ ┃ ┣ 📜PST8PDT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ROC
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ROK
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Singapore
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Turkey
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tzdata.zi
 ┃ ┃ ┃ ┃ ┃ ┣ 📜UCT
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Universal
 ┃ ┃ ┃ ┃ ┃ ┣ 📜UTC
 ┃ ┃ ┃ ┃ ┃ ┣ 📜W-SU
 ┃ ┃ ┃ ┃ ┃ ┣ 📜WET
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zone.tab
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zone1970.tab
 ┃ ┃ ┃ ┃ ┃ ┣ 📜zonenow.tab
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Zulu
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜zones
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂tzdata-2024.1.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE_APACHE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂urllib3
 ┃ ┃ ┃ ┃ ┣ 📂contrib
 ┃ ┃ ┃ ┃ ┃ ┣ 📂emscripten
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fetch.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜emscripten_fetch_worker.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fetch.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pyopenssl.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜socks.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pyopenssl.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜socks.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂util
 ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜request.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssltransport.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜url.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wait.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜request.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ssltransport.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜url.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wait.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜connectionpool.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜filepost.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜http2.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜poolmanager.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_base_connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_collections.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_request_methods.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜_version.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┃ ┃ ┣ 📜connectionpool.py
 ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
 ┃ ┃ ┃ ┃ ┣ 📜fields.py
 ┃ ┃ ┃ ┃ ┣ 📜filepost.py
 ┃ ┃ ┃ ┃ ┣ 📜http2.py
 ┃ ┃ ┃ ┃ ┣ 📜poolmanager.py
 ┃ ┃ ┃ ┃ ┣ 📜py.typed
 ┃ ┃ ┃ ┃ ┣ 📜response.py
 ┃ ┃ ┃ ┃ ┣ 📜_base_connection.py
 ┃ ┃ ┃ ┃ ┣ 📜_collections.py
 ┃ ┃ ┃ ┃ ┣ 📜_request_methods.py
 ┃ ┃ ┃ ┃ ┣ 📜_version.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂urllib3-2.2.2.dist-info
 ┃ ┃ ┃ ┃ ┣ 📂licenses
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LICENSE.txt
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┗ 📜WHEEL
 ┃ ┃ ┃ ┣ 📂wcwidth
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜table_vs16.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜table_wide.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜table_zero.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜unicode_versions.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wcwidth.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜table_vs16.py
 ┃ ┃ ┃ ┃ ┣ 📜table_wide.py
 ┃ ┃ ┃ ┃ ┣ 📜table_zero.py
 ┃ ┃ ┃ ┃ ┣ 📜unicode_versions.py
 ┃ ┃ ┃ ┃ ┣ 📜wcwidth.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂wcwidth-0.2.13.dist-info
 ┃ ┃ ┃ ┃ ┣ 📜INSTALLER
 ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┣ 📜METADATA
 ┃ ┃ ┃ ┃ ┣ 📜RECORD
 ┃ ┃ ┃ ┃ ┣ 📜REQUESTED
 ┃ ┃ ┃ ┃ ┣ 📜top_level.txt
 ┃ ┃ ┃ ┃ ┣ 📜WHEEL
 ┃ ┃ ┃ ┃ ┗ 📜zip-safe
 ┃ ┃ ┃ ┣ 📂_distutils_hack
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜override.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜override.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┣ 📜decorator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜six.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┗ 📜typing_extensions.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜decorator.py
 ┃ ┃ ┃ ┣ 📜distutils-precedence.pth
 ┃ ┃ ┃ ┣ 📜six.py
 ┃ ┃ ┃ ┗ 📜typing_extensions.py
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
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt

```

