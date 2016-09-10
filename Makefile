.PHONY: install clean test retest coverage docs publish

install:
	pip install -e .[test]

lint:
	flake8 --ignore=E501 unitils/ test/

clean:
	find . -name '*.pyc' -delete
	python setup.py clean
	$(MAKE) -C docs clean
	rm -fr build/ dist/ unitils.egg-info/ .coverage

test:
	python setup.py nosetests

docs:
	$(MAKE) test
	$(MAKE) -C docs html
	mv cover/index.html cover/cover.html
	mv cover/* docs/_build/html/.
	rmdir cover/
	mv stats.dat docs/_build/html/.

release:
	pip install twine wheel
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload -s dist/*

publish:
	$(MAKE) docs
	git checkout gh-pages
	git add .
	git commit -m "Update docs"
	git push
	git checkout master
