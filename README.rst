
Nigerian Phone Number Validator (Python)
========================================


.. image:: http://hits.dwyl.io/djunehor/validate_nigerian_phone.svg
   :target: http://hits.dwyl.io/djunehor/validate_nigerian_phone
   :alt: HitCount
 
.. image:: https://circleci.com/gh/djunehor/validate_nigerian_phone.svg?style=svg
   :target: https://circleci.com/gh/djunehor/validate_nigerian_phone
   :alt: CircleCI


Issues and pull requests welcome.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Python module to validate and format a Nigerian phone number as well as deduce the network provider or area code.

Table of Contents
^^^^^^^^^^^^^^^^^


* `Installation <#installation>`_
* `Usage <#usage>`_
* `Features <#features>`_
* `Contribute <#contribute>`_
* `Run Tests <#tests>`_

Installation
------------

You will need `Python 3.x <https://www.python.org/download/>`_ and `pip <http://pip.readthedocs.org/en/latest/installing.html>`_.

Install using pip: ``pip install validate_nigerian_phone``
Install via repo:


* Clone repo ``git clone https://github.com/djunehor/validate_nigerian_phone``
* Place validate_nigerian_phone in your project root folder

Usage
-----

.. code-block:: python

   from validate_nigerian_phone import NigerianPhone

   phone = NigerianPhone('+2348135087966')

   # Check if is valid
   phone.is_valid() #True

   # Get formatted
   phone.formatted() #08135087966

   # Get Network
   phone.get_network() #mtn

   # Check if is mtn
   phone.is_mtn() # True


   # Get network from phone number prefix e.g
   phone.get_network_by_prefix('0703') # mtn

Features
--------

Currently implemented
^^^^^^^^^^^^^^^^^^^^^


* is_valid
* formatted
* get_network
* get_area_code
* is_mtn
* is_glo
* is_airtel
* is_9mobile
* is_smile
* is_smile
* is_multilinks
* is_visafone
* is_ntel
* is_starcomms
* is_zoom
* get_prefixes_by_network
* get_network_by_prefix
* get_area_code_by_name

Tests
^^^^^


* Run ``python tests.py``

Contribute
----------

Check out the issues on GitHub and/or make a pull request to contribute!
