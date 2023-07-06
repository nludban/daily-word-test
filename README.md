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
% pytest --color=no -v --pdb
...

```

