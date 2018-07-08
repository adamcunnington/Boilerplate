===========
Boilerplate
===========

This is a very light weight template for starting a python project. In the author's opinion, it contains the absolute bare minimum


-----------
Assumptions
-----------
1. The project is a python package. If it isn't, remove the pakages kwarg from setup.py and replace with py_modules=[<project>.py]. Depending on the complexity of the tests, the tests directory can probably be replaced with a single test_<project>.py file.
2. The project itself should be installed in editable mode when running 'pip install -r requirements.txt'. If not, remove the '-e .' line from requirements.txt
3. Sphinx is being used for documentation.


-----
Usage
-----
Duplicate the project contents into your project dir and make the following changes:

1. Edit the copyright notice in LICENSE.
2. Edit the following kwargs in setup.py; description, name, author, author_email.