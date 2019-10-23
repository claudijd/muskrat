# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2014 Mozilla Corporation
#
PACKAGE := mustrat

.PHONY:list ## List all make targets
list:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile

.PHONY: dependencies ## install all dependencies
dependencies:
	pip3 install -e .
	pip3 install -r requirements.txt

.PHONY: tests ## run all unit tests
tests:
	pytest tests/unit-tests/
pep8:
	@find ./* `git submodule --quiet foreach 'echo -n "-path ./$$path -prune -o "'` -type f -name '*.py' -exec pep8 --show-source --max-line-length=100 {} \;

pylint:
	@find ./* `git submodule --quiet foreach 'echo -n "-path ./$$path -prune -o "'` -type f -name '*.py' -exec pylint -r no --disable=locally-disabled --rcfile=/dev/null {} \;

clean:
	rm -f muskrat/*.pyc tests/unit-tests/*.pyc