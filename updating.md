
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

$ rm -rf .mypy_cache/
$ rm -rf ~/.venv-daily-word-test/

$ python3 -m venv ~/.venv-daily-word-test
$ source ~/.venv-daily-word-test/bin/activate
$ python3 -m pip freeze
	(should be nothing installed)

python3 -m pip install fastapi
python3 -m pip install pytest
python3 -m pip install mock
python3 -m pip install mypy
python3 -m pip install uvicorn
python3 -m pip install httpx

words is now 9981 entries...

./test_wordlist.py:        assert wordlist.random_word(12365) == 'WINDY'
./gameserver.py:seed = 12365	# WINDY.

$ pytest --color=no -v --pdb
$ python3 -m pip freeze > requirements.txt


https://github.com/python/mypy/issues/7237
	With a system mypy installed, running mypy with the virtualenv
	activated before installing mypy in the virtualenv breaks the
	virtualenv so that mypy never works in it, even after installing
	it in the virtualenv.
https://github.com/python/mypy/issues/17214


$ mypy --check-untyped-defs *.py
    gamestate.py:16: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:17: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:18: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:47: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:48: error: "str" has no attribute "value"  [attr-defined]
    test_wordlist.py:5: error: Library stubs not installed for "mock"  [import-untyped]
    test_gamecontroller.py:6: error: Library stubs not installed for "mock"  [import-untyped]
    test_gamecontroller.py:6: note: Hint: "python3 -m pip install types-mock"
    test_gamecontroller.py:6: note: (or run "mypy --install-types" to install all missing stub packages)
    test_gamecontroller.py:6: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    Found 7 errors in 3 files (checked 7 source files)

$ mypy --install-types
    Installing missing stub packages:
    ~/.venv-daily-word-test/bin/python3 -m pip install types-Pygments types-colorama types-mock types-pexpect types-setuptools types-ujson
    Install? [yN] y

$ mypy --check-untyped-defs *.py
    gamestate.py:16: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:17: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:18: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:47: error: "str" has no attribute "value"  [attr-defined]
    gamestate.py:48: error: "str" has no attribute "value"  [attr-defined]
    Found 5 errors in 1 file (checked 7 source files)
