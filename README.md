# daily-word-test

Take home coding test.

## Environment Set Up

```
% python3 -m venv ~/.venv-daily-word-test
% source ~/.venv-daily-word-test/bin/activate.csh 

(.venv-daily-word-test) % python
Python 3.9.13 (main, Sep 18 2022, 05:35:03) 
[Clang 13.0.0 (git@github.com:llvm/llvm-project.git llvmorg-13.0.0-0-gd7b669b3a on freebsd13
Type "help", "copyright", "credits" or "license" for more information.
>>>

% pip install -r requirements.txt
```

YMMV:
```
% sha256 /usr/share/dict/words
SHA256 (/usr/share/dict/words) = a80b7cac20dff2fd92e59bb58d2d581efa9b965756a8c8f03f754d3d98e92723
```

## Testing

```
% mypy --check-untyped-defs *.py
...
Found 6 errors in 2 files (checked 6 source files)

% pytest --color=no -v --pdb
...
============= 16 passed in 0.63s ===================

```


```
% uvicorn gameserver:app --reload
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


% curl -X POST http://127.0.0.1:8000/new_game
{"game_id":2}

% curl -X POST http://127.0.0.1:8000/guess \
	-H 'Content-Type: application/json' \
	-d '{"game_id": 2, "guess": "WINDY"}'
{"guess_result":"correct",
 "letter1":"correct",
 "letter2":"correct",
 "letter3":"correct",
 "letter4":"correct",
 "letter5":"correct",
 "incorrectly_guessed_letters":["notyet"]
}
```
