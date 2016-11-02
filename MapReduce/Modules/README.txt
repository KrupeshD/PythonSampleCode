## Screenshot of pyenv and python module path.
## See how pyenv changes current python version with local and global commands
## And how it affects the python's module search path.  


Krupeshs-MacBook-Air:Modules kdesai$ python
Python 3.5.1 (default, Jun 13 2016, 16:08:16)
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/local/var/pyenv/versions/3.5.1/lib/python35.zip', '/usr/local/var/pyenv/versions/3.5.1/lib/python3.5', '/usr/local/var/pyenv/versions/3.5.1/lib/python3.5/plat-darwin', '/usr/local/var/pyenv/versions/3.5.1/lib/python3.5/lib-dynload', '/usr/local/var/pyenv/versions/3.5.1/lib/python3.5/site-packages']
>>> exit()
Krupeshs-MacBook-Air:Modules kdesai$ pyenv versions
  system
* 3.5.1 (set by /Users/kdesai/.python-version)
Krupeshs-MacBook-Air:Modules kdesai$ pyenv local
3.5.1
Krupeshs-MacBook-Air:Modules kdesai$ pyenv global
3.5.1
Krupeshs-MacBook-Air:Modules kdesai$ pyenv global system
Krupeshs-MacBook-Air:Modules kdesai$ python
Python 3.5.1 (default, Jun 13 2016, 16:08:16)
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
Krupeshs-MacBook-Air:Modules kdesai$ pyenv local system
Krupeshs-MacBook-Air:Modules kdesai$ python
Python 2.7.10 (default, Oct 23 2015, 19:19:21)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC', '/Library/Python/2.7/site-packages']
>>>