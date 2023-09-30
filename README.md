# <p align="center"> __url-shortener__
__This is a Django based link shortener.__ 

-------

## Installation

path: /home/username/url-shortener

### virtualenv
Download virtualenv from [here](https://pypi.org/project/virtualenv/) and install it.
```
virtualenv env
source env/bin/activate
```

### Requirements: 
```
pip install -r requirements.txt
```

### .env file

create a .env file in the root directory and add the following variables

```
SECRET_KEY=django-insecure-hsb2h+6kkdesg)r(qm-q9$vgdaopxy^)yn=qdb^vg8p%@k7))t
DEBUG=1
ALLOWED_HOSTS='127.0.0.1 localhost'
```

### runserver
```
cd urlshortener
python manage.py runserver
```
