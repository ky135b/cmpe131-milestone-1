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
### Linux/MacOS
```
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_login
pip3 install flask_wtf
pip3 install flask_mail
```

## Usage
This section assumes you have Python 3 (python3) and pip3 installed.
1. ``git clone https://github.com/ky135b/cmpe131-milestone-1.git``
2. ``cd cmpe131-milestone-1``
3. ``python3 -m venv env``
4. ``source env/bin/activate``
5. ``pip3 install -r dependencies.txt``
6. ``python3 run.py``
Once you finish, run ``deactivate``.
