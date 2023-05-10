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
|:------------------|:-------|
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
#### Installing Python 3 (Skippable)
If you already have python3 (3.10.6+) and pip3 installed, you can skip this section. 

Run ``python3 --version`` to find which version of python is installed. If the command ``python3`` is not found, or the version is less then 3.10.6, visit [this site on Linux](https://wiki.python.org/moin/BeginnersGuide/Download#Linux) or [this site on MacOS](https://docs.python.org/3/using/mac.html) for help installing python3; pip3 is included with python3 since version 3.4, so it should be installed at the same time.

#### Instructions
This section guides you through cloning the repository, creating a virtual environment, installing all dependencies in the virtual environment, and running the project in debug mode. You must have Python 3 (python3, tested on 3.10.6) and pip3 installed.
1. ``git clone https://github.com/ky135b/cmpe131-milestone-1.git``
2. ``cd cmpe131-milestone-1``
3. ``python3 -m venv env``
4. ``source env/bin/activate``
5. ``pip3 install -r dependencies.txt``
6. ``python3 run.py``

To exit the virtual environment, run ``deactivate``. [Visit this page for more on virtual environments.](https://docs.python.org/3/library/venv.html#module-venv)
#### Clearing Database
To clear the database, run ``python3 tables.py``. This will drop all the tables and create them again by referencing ``app/models.py``.

### Windows
This project does not support Windows. To run the project on Windows, we reccommend [setting up WSL with Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install) and following the [Linux instructions](#linuxmacos).
