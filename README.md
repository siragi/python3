# Python3 Code Repo

## Learning Resources and Tutorials
### Basics
- sololearn! (App)

### Courses
- Deutscher python3-Kurs:
  [Python3 Tutorial](https://www.python-kurs.eu/python3_interaktiv.php)
- [Python 3 Kurs, in English](http://www.learnpython.org/)
- https://learnpythonthehardway.org/python3/

### Tutorials
- https://www.tutorialspoint.com/python
- https://data-flair.training/blogs/python-tutorials-home/
- https://stackabuse.com/tag/python/
- more tutorials on TiddlyWiki: [python.html](python.html)
- http://www.greenteapress.com/thinkpython/html/index.html

### References
- The Python Standard Library: https://docs.python.org/3/library/index.html
- Python Language Reference: https://docs.python.org/3/reference/index.html#reference-index
- Code Style: https://pep8.org/
- pylint codes: https://pylint.readthedocs.io/en/latest/technical_reference/features.html

### Books
All from Al Sweigart:
* https://automatetheboringstuff.com/
* https://inventwithpython.com/makinggames.pdf
* https://inventwithpython.com/pygame/
* https://inventwithpython.com/cracking/ (Encrypt Messages and Hack Ciphers)

### Exercice Repo
* Exercism

## Development Environment
Install a Opensource IDE:
- 'Atom' Editor with Plugins:
  - atom-python-run
    (eg F5 "python -i {file}"/F6: "python3 -i {file}"")
  - autocomplete-python
  - linter-pylama
  - language-python (core package)
or
- IDLE, simple.
- just the python interactive shell.

## Python Libraries
- cpython implementation:
  - In cpython, many modules are implemented in C, and not in Python. You can find those in [Modules/](https://github.com/python/cpython/tree/master/Modules), whereas the pure Python ones reside in [Lib/](https://github.com/python/cpython/tree/master/Lib). In some cases (for example the json module), the Python source code provides the module on its own and only uses the C module if it's available (to improve performance).
- PyPy implementation:
  - For the remaining modules, you can have a look at [PyPy's implementations](https://bitbucket.org/pypy/pypy/src/tip/lib_pypy).
- The Python Package Index (PyPI) is a repository of software for the Python programming language: https://pypi.org/
