init:
	pip install -r requirements.txt

install:
	python setup.py install

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload --skip-existing dist/*

reqs:
	python -m pipreqs.pipreqs --force

.PHONY: init install build upload reqs
