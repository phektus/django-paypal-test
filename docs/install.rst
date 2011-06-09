==================
Installation
==================

Pre-Requisites
===============

* `setuptools <http://pypi.python.org/pypi/setuptools>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_

To install all of these system dependencies on a Debian-based system, run::

	sudo apt-get install python-setuptools
	sudo easy_install virtualenvwrapper


Creating the Virtual Environment
================================

First setup the virtualenv wrapper by getting the path to the virtualenvwrapper shell script::
  
    $ which virtualenvwrapper.sh

You might want to write `marketplace` in a .venv file and update your .bashrc
or .zshrc with the script given in the wiki_. On some cases editing your ~/.bashrc file 
and appending this line will do::

    $ source /path/to/the/virtualenv/wrapper/script

Don't forget to restart your terminal if needed. Then, create a virtualenv named marketplace::

    $ mkvirtualenv hr_payment -p python2.6 --no-site-packages

Now marketplace will be added to the list of available environments, which you can see with::

    $ workon

To enable marketplace virtual environment, go the the marketplace/ directory and activate it using::

    $ workon hr_payment


Installing the Project
======================

Install the requirements and the project source::

	cd path/to/your/hr_payment/repository
    pip install -r requirements.pip
    pip install -e .


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp hr_payment/conf/local/example/* hr_payment/conf/local
    manage.py syncdb --migrate


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    pip install Sphinx
    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
