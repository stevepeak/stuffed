CHECK=\033[32m✔\033[39m

help:
	@echo "\033]0;stuffed\007"
	@echo "\n\t\t\033[1m------ stuffed ------\033[0m \n\
	\033[94m\thttps://github.com/stevepeak/stuffed\033[0m\
	\n\n\
	\t\033[1mopen\033[0m =>\t\topens project in sublime\n\
	\t\033[1mcompare\033[0m =>\tcompare from last deploy\n\
	\t\033[1mtest\033[0m =>\t\trun unittests\n\
	\t\033[1mdeploy\033[0m =>\t\ttag and upload\n\
	\n"

open:
	subl --project stuffed.sublime-project

test: 
	python -m stuffed.tests

tag:
	git tag -m "" -a v$(shell grep "version = " stuffed/__init__.py | cut -d"'" -f 2)
	git push origin v$(shell grep "version = " stuffed/__init__.py | cut -d"'" -f 2)

deploy: tag upload

upload:
	python setup.py sdist upload
