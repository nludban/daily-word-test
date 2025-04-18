
$ grep -hrw import . | sort -u
import dataclasses
import enum
import fastapi
import gamecontroller
import gamestate
import mock
import pydantic
import pytest
import random
import time
import typing
import wordlist

$ python3 -m pip install fastapi

$ mypy --check-untyped-defs *.py

$ python3 -m pip install pytest
$ python3 -m pip install mock
$ python3 -m pip install mypy
$ python3 -m pip install uvicorn

words is now 9981 entries...

./test_wordlist.py:        assert wordlist.random_word(12365) == 'WINDY'
./gameserver.py:seed = 12365	# WINDY.

$ pytest --color=no -v --pdb

$ python3 -m pip freeze
anyio==3.7.0			=> 4.9.0
click==8.1.3			=> 8.1.8
exceptiongroup==1.1.1
fastapi==0.99.0			=> 0.115.12
h11==0.14.0			=> same
httptools==0.5.0
idna==3.4			=> 3.10
iniconfig==2.0.0		=> 2.1.0
mock==5.0.2			=> 5.2.0
mypy==1.4.1			=> 1.15.0
mypy-extensions==1.0.0		=> same
packaging==23.1			=> 24.2
pluggy==1.2.0			=> 1.5.0
pydantic==1.10.10		=> 2.11.3
pytest==7.4.0			=> 8.3.5
python-dotenv==1.0.0
PyYAML==6.0
sniffio==1.3.0			=> 1.3.1
sqlite3==0.0.0
starlette==0.27.0		=> 0.46.2
tomli==2.0.1
types-mock==5.0.0.7		=> 5.2.020250306
typing_extensions==4.7.0	=> 4.13.2
uvicorn==0.22.0			=> 0.34.1
uvloop==0.17.0
watchfiles==0.19.0
websockets==11.0.3

