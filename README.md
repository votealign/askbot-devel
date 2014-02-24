VoteAlign
=========

[![Build Status](https://travis-ci.org/votealign/votealign.png?branch=master)](https://travis-ci.org/votealign/votealign)
[![Coverage Status](https://coveralls.io/repos/votealign/votealign/badge.png?branch=master)](https://coveralls.io/r/votealign/votealign?branch=master)

VoteAlign is forked from Askbot, an open-source Q&A system.



For Contributors
================

Requirements
------------

* Python 2.7: http://www.python.org/getit/releases/2.7.6/#download
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* GNU gettext:
    * Windows: ???
    * Mac: `brew install gettext` (http://brew.sh)
    * Linux: ???


Installation
------------

Create a virtualenv and local deployment:

    make env

Build the database and messages:

    make assets

Start the server:

    make serve

Start the server and launch the site in your browser:

    make launch


Updating Strings
----------------

As far as we can tell, all displayed English text is located in:

* [askbot/locale/en/LC_MESSAGES/*.po](askbot/locale/en/LC_MESSAGES/)
* [askbot/conf/words.py](askbot/conf/words.py)

The compiled translations (*.mo) are created from *.po files using `gettext`.
Default (English) phrases are located in words.py. Compile new messages before starting the server:

    make messages
