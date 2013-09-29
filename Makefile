CHECK=\033[32m✔\033[39m

help:
	@echo "\033]0;stuffed\007"
	@echo "\n\t\t\033[1m------ Stuff ------\033[0m \n\
	\033[94m\thttps://github.com/stevepeak/stuffed\033[0m\
	\n\n\
	\033[94m::dev\033[0m\n\
	\t\033[1mopen\033[0m =>\t\topens project in sublime\n\
	\t\033[1mcompare\033[0m =>\tcompare from last deploy\n\
	\033[94m::test \033[0m\n\
	\t\033[1mtest\033[0m =>\t\trun unittests\n\
	\n"

open:
	subl --project stuffed.sublime-project

test: 
	python -m stuffed.tests

tag:
	git tag -m "" -a v$(shell grep "version = " stuffed/__init__.py | cut -d"'" -f 2)
	git push origin v$(shell grep "version = " stuffed/__init__.py | cut -d"'" -f 2)

upload:
	python setup.py sdist upload
