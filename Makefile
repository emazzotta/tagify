venv:
	python3 -m venv venv

install:
	venv/bin/pip3 install -r requirements.txt

freeze:
	venv/bin/pip3 freeze > requirements.txt

pypitest-register:
	python3 setup.py register -r pypitest

pypitest-upload:
	python3 setup.py sdist upload -r pypitest

pypi-register:
	pandoc --from=markdown --to=rst README.md -o README.rst
	python3 setup.py register -r pypi

pypi-upload:
	python3 setup.py sdist upload -r pypi
	rm -rf README.rst

