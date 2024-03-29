# todo

[![Python application](https://github.com/l-vamsi-krishna/todo/actions/workflows/python-app.yml/badge.svg)](https://github.com/l-vamsi-krishna/todo/actions/workflows/python-app.yml)![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)

A Simple Todo application, which persists/updates/deletes to database.  
It is updated to use sql alchemy to perform db operations, instead of sqlite connectors & cursors.  
It uses autopep8 to implement pep 8 coding standards.  

It can be used on CLI.  
Run below command inside venv, to interact within CLI.
```
python todo/cli/todo.py
```
![CLI](/assets/cli.jpg)

Flask GUI connects to the same database to perform db tasks.  
Run below command to start flask web server.
```
python -m todo.web.app
```
The above command, considers top level directory in sys.path, hence relative imports work.  

![Home Page](/assets/home.jpg)

# Contributions
I would be very happy for any contribution.

# Next Steps
1. Currently Flask GUI just retrieves the data, need to provide option to update/delete the data.
2. Use Bootstrap to beautify GUI.
