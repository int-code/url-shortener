# <p align="center"> __url-shortener__
__This is a Django based link shortener.__ 

-------
## What is a URL Shortener ?

A URL shortener is a web-based service that condenses long and unwieldy URLs into shorter, more manageable links. It assigns a unique identifier to the original URL, reducing its length while redirecting users to the intended destination.  

## What is an URL? 

A URL (Uniform Resource Locator) is a web address that specifies the location of a resource on the internet, such as a webpage, file, or service. It consists of a protocol (e.g., "http" or "https"), a domain name (e.g., "example.com"), and a specific path or identifier to access the resource (e.g., "/page"). URLs allow browsers and applications to retrieve and display web content accurately.

## Why use this URL Shortener ?

This tool is valuable for sharing links in constrained spaces, such as social media posts or character-limited messages, where brevity is essential.

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
