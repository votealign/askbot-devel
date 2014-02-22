PROJECT := VoteAlign
PACKAGE := askbot
SOURCES := setup.py askbot_requirements_dev.txt

ENV := env
DEPENDS := $(ENV)/.depends
INSTALLED :=$(ENV)/.installed
CACHE := .cache

PLATFORM := $(shell python -c 'import sys; print(sys.platform)')

ifneq ($(findstring win32, $(PLATFORM)), )
	SYS_PYTHON := C:\\Python27\\python.exe
	SYS_VIRTUALENV := C:\\Python27\\Scripts\\virtualenv.exe
	BIN := $(ENV)/Scripts
	EXE := .exe
	OPEN := cmd /c start
	# https://bugs.launchpad.net/virtualenv/+bug/449537
	export TCL_LIBRARY=C:\\Python27\\tcl\\tcl8.5
else
	SYS_PYTHON := python2
	SYS_VIRTUALENV := virtualenv
	BIN := $(ENV)/bin
	ifneq ($(findstring cygwin, $(PLATFORM)), )
		OPEN := cygstart
	else
		OPEN := open
	endif
endif

MAN := man
SHARE := share

PYTHON := $(BIN)/python$(EXE)
PIP := $(BIN)/pip$(EXE)
RST2HTML := $(BIN)/rst2html.py
PDOC := $(BIN)/pdoc
PEP8 := $(BIN)/pep8$(EXE)
PEP257 := $(BIN)/pep257$(EXE)
PYLINT := $(BIN)/pylint$(EXE)
NOSE := $(BIN)/nosetests$(EXE)

DEPLOY := deploy
SETUP := $(BIN)/askbot-setup$(EXE)
DB := $(DEPLOY)/db.sqlite3
MANAGE := $(PYTHON) $(DEPLOY)/manage.py

# Installation ###############################################################

.PHONY: all
all: env

.PHONY: env
env: .virtualenv depends $(INSTALLED)
$(INSTALLED): $(SOURCES)
	$(PYTHON) setup.py develop
	rm -rf $(DEPLOY) ; mkdir $(DEPLOY)
	# for --db-engine: 1 is PostgreSQL, 2 is SQLite, 3 is MySQL
	echo $(DB) | $(SETUP) --dir-name=deploy --db-engine=2 --db-name=votealign --db-user=votealign --db-password=votealign
	touch $(INSTALLED)  # flag to indicate project is installed

.PHONY: .virtualenv
.virtualenv: $(PIP)
$(PIP):
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)

.PHONY: depends
depends: $(DEPENDS) $(SOURCES)
$(DEPENDS):
	$(PIP) install -r askbot_requirements_dev.txt --download-cache=$(CACHE)
	$(PIP) install pep8 pep257 --download-cache=$(CACHE)
	touch $(DEPENDS)  # flag to indicate dependencies are installed

# Static Analysis ############################################################

.PHONY: pep8
pep8: env depends
	$(PEP8) $(PACKAGE) --ignore=E501

.PHONY: pep257
pep257: env depends
	$(PEP257) $(PACKAGE) --ignore=E501

.PHONY: pylint
pylint: env depends
	$(PYLINT) $(PACKAGE) --reports no \
	                     --msg-template="{msg_id}:{line:3d},{column}:{msg}" \
	                     --max-line-length=79 \
	                     --disable=I0011,W0142,W0511,R0801

.PHONY: check
check: pep8 pep257 pylint

# Testing ####################################################################

.PHONY: test
test: env depends
	DJANGO_SETTINGS_MODULE=$(DEPLOY)/settings $(NOSE)

.PHONY: ci
ci: all syncdb migrate

# Cleanup ####################################################################

.PHONY: clean
clean: .clean-dist .clean-test .clean-doc .clean-build
	rm -rf $(DB)

.PHONY: clean-all
clean-all: clean .clean-env
	rm -rf $(DEPLOY)

.PHONY: clean-all-cache
clean-all-cache: clean-all .clean-cache

.PHONY: .clean-env
.clean-env:
	rm -rf $(ENV)

.PHONY: .clean-cache
.clean-cache:
	rm -rf $(CACHE)

.PHONY: .clean-build
.clean-build:
	find $(PACKAGE) -name '*.pyc' -delete
	find $(PACKAGE) -name '__pycache__' -delete
	rm -rf *.pyc
	rm -rf *.egg-info

.PHONY: .clean-doc
.clean-doc:
	rm -rf apidocs docs/README*.html

.PHONY: .clean-test
.clean-test:
	rm -rf .coverage

.PHONY: .clean-dist
.clean-dist:
	rm -rf dist build

# Server ####################################################################

$(DB):
	$(MAKE) syncdb migrate

.PHONY: syncdb
syncdb:
	$(MANAGE) syncdb --noinput

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: delete_db
delete_db:
	rm -f $(DB)

.PHONY: reset_db
reset_db: delete_db syncdb migrate

.PHONY: run
run: env $(DB) syncdb
	$(MANAGE) runserver

.PHONY: launch
launch: env $(DB) syncdb
	eval "sleep 10; $(OPEN) http://localhost:8000" &
	$(MANAGE) runserver
