# CMPE 131 Email Client

This email client is designed for the class project of CMPE 131 at SJSU.

## Table of Contents
- [Contributors](#contributors)
- [Dependencies](#dependencies)
- [Usage](#usage)
### Documentation
- [Meeting Notes](meetings.md)
- [Requirements](requirements.md)
- [Ethical Implications](ethics.md)

## Contributors
- Ky Saini (@ky135b) (Team Lead)
- Natalie Leung (@n-k-leung)
- Rudy Suarez Serrano (@rudysuarez1)

## Dependencies
| Package           | Version|
|------------------:|:-------|
| blinker           | 1.6.2  |
| click             | 8.1.3  |
| Flask             | 2.3.2  |
| Flask-Login       | 0.6.2  |
| Flask-Mail        | 0.9.1  |
| Flask-SQLAlchemy  | 3.0.3  |
| Flask-WTF         | 1.1.1  |
| greenlet          | 2.0.2  |
| itsdangerous      | 2.1.2  |
| Jinja2            | 3.1.2  |
| MarkupSafe        | 2.1.2  |
| SQLAlchemy        | 2.0.12 |
| typing_extensions | 4.5.0  |
| Werkzeug          | 2.3.4  |
| WTForms           | 3.0.1  |


## Usage
### Linux/MacOS
This section assumes you have Python 3 (python3) and pip3 installed.
1. ``git clone https://github.com/ky135b/cmpe131-milestone-1.git``
2. ``cd cmpe131-milestone-1``
3. ``python3 -m venv env``
4. ``source env/bin/activate``
5. ``pip3 install -r dependencies.txt``
6. ``python3 run.py``
Once you finish, run ``deactivate``.
