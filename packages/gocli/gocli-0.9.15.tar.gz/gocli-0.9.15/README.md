gocli - How to install as a dev
===============================

1. Within the gocli directory, make a virtual environment: `mkvirtualenv -a . {name of env}`
2. Install gocli (and dependencies): `pipsi install -e .`
3. Test to make sure that gocli works: `gocli --help`
4. A simple way to verify that the gocli version is a local version (and not from pip) is to modify one
of the docstrings (strings under function definition) in the commands.py file. Then run `gocli --help` again
and you should see your change in the help text for that command.
5. To install packages (to run make white and make test), run `pipenv install --dev`