PROJECT := VoteAlign
PACKAGE := askbot
SOURCES := Makefile setup.py askbot_requirements.txt askbot_requirements_dev.txt

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

# Installation ###############################################################

.PHONY: all
all: env

.PHONY: env
env: .virtualenv $(INSTALLED)
$(INSTALLED): $(SOURCES)
	$(PIP) install -r askbot_requirements.txt --download-cache=$(CACHE)
	touch $(INSTALLED)  # flag to indicate project is installed

.PHONY: .virtualenv
.virtualenv: $(PIP)
$(PIP):
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)

.PHONY: depends
depends: .virtualenv $(DEPENDS) $(SOURCES)
$(DEPENDS): $(SOURCES)
	$(PIP) install -r askbot_requirements_dev.txt pep8 pep257 --download-cache=$(CACHE)
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
	DJANGO_SETTINGS_MODULE=$(PACKAGE).settings $(NOSE)

# Cleanup ####################################################################

.PHONY: clean
clean: .clean-dist .clean-test .clean-doc .clean-build

.PHONY: clean-all
clean-all: clean .clean-env

.PHONY: .clean-env
.clean-env:
	rm -rf $(ENV)

.PHONY: .clean-build
.clean-build:
	find $(PACKAGE) -name '*.pyc' -delete
	find $(PACKAGE) -name '__pycache__' -delete
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

MANAGE := $(PYTHON) manage.py
DB := thrive.db

$(DB):
	$(MAKE) syncdb load_data

.PHONY: syncdb
syncdb:
	cp thrive_refugee/local_settings.default thrive_refugee/local_settings.py
	$(MANAGE) syncdb --noinput

.PHONY: load_data
load_data:
	$(MANAGE) loaddata thrive_refugee/fixtures/auth.json
	$(MANAGE) loaddata esl_manager/fixtures/eslstudent.json
	$(MANAGE) loaddata esl_manager/fixtures/attended.json
	$(MANAGE) loaddata esl_manager/fixtures/assesment.json
	$(MANAGE) loaddata refugee_manager/fixtures/volunteer.json
	$(MANAGE) loaddata refugee_manager/fixtures/case.json
	$(MANAGE) loaddata refugee_manager/fixtures/individual.json
	$(MANAGE) loaddata refugee_manager/fixtures/casedetail.json
	$(MANAGE) loaddata refugee_manager/fixtures/activitynote.json
	$(MANAGE) loaddata refugee_manager/fixtures/assessment.json
	$(MANAGE) loaddata swingtime/fixtures/eventtype.json
	$(MANAGE) loaddata swingtime/fixtures/event.json
	$(MANAGE) loaddata employment_manager/fixtures/employmentclient.json
	$(MANAGE) loaddata employment_manager/fixtures/job.json
	$(MANAGE) loaddata employment_manager/fixtures/skill.json
	$(MANAGE) loaddata employment_manager/fixtures/assesment.json
	$(MANAGE) loaddata employment_manager/fixtures/language.json

.PHONY: dump_data
dump_data:
	$(MANAGE) dumpdata auth > thrive_refugee/fixtures/auth.json
	$(MANAGE) dumpdata esl_manager.ESLStudent > esl_manager/fixtures/eslstudent.json
	$(MANAGE) dumpdata esl_manager.Attended > esl_manager/fixtures/attended.json
	$(MANAGE) dumpdata esl_manager.Assesment > esl_manager/fixtures/assesment.json
	$(MANAGE) dumpdata refugee_manager.Volunteer > refugee_manager/fixtures/volunteer.json
	$(MANAGE) dumpdata refugee_manager.Case > refugee_manager/fixtures/case.json
	$(MANAGE) dumpdata refugee_manager.Individual > refugee_manager/fixtures/individual.json
	$(MANAGE) dumpdata refugee_manager.CaseDetail > refugee_manager/fixtures/casedetail.json
	$(MANAGE) dumpdata refugee_manager.ActivityNote > refugee_manager/fixtures/activitynote.json
	$(MANAGE) dumpdata refugee_manager.Assessment > refugee_manager/fixtures/assessment.json
	$(MANAGE) dumpdata swingtime.EventType > swingtime/fixtures/eventtype.json
	$(MANAGE) dumpdata swingtime.Event > swingtime/fixtures/event.json
	$(MANAGE) dumpdata employment_manager.EmploymentClient > employment_manager/fixtures/employmentclient.json
	$(MANAGE) dumpdata employment_manager.Job > employment_manager/fixtures/job.json
	$(MANAGE) dumpdata employment_manager.Skill > employment_manager/fixtures/skill.json
	$(MANAGE) dumpdata employment_manager.Assesment > employment_manager/fixtures/assesment.json
	$(MANAGE) dumpdata employment_manager.Language > employment_manager/fixtures/language.json

.PHONY: delete_db
delete_db:
	rm -f $(DB)
	rm -f thrive_refugee/local_settings.py

.PHONY: reset_db
reset_db: delete_db syncdb load_data

.PHONY: run
run: develop $(DB) syncdb
	$(MANAGE) runserver

.PHONY: launch
launch: develop $(DB) syncdb
	eval "sleep 1; $(OPEN) http://localhost:8000" &
	$(MANAGE) runserver
