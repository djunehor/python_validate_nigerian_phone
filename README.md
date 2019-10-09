# Nigerian Phone Number Validator (Python)
[![HitCount](http://hits.dwyl.io/djunehor/validate_nigerian_phone.svg)](http://hits.dwyl.io/djunehor/validate_nigerian_phone) [![CircleCI](https://circleci.com/gh/djunehor/validate_nigerian_phone.svg?style=svg)](https://circleci.com/gh/djunehor/validate_nigerian_phone)

#### Issues and pull requests welcome.

A Python module to validate and format a Nigerian phone number as well as deduce the network provider or area code.

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Contribute](#contribute)
* [Run Tests](#tests)

## Installation
You will need [Python 3.x](https://www.python.org/download/) and [pip](http://pip.readthedocs.org/en/latest/installing.html).

Install using pip: `pip install validate_nigerian_phone`
Install via repo:
- Clone repo `git clone https://github.com/djunehor/validate_nigerian_phone`
- Place validate_nigerian_phone in your project root folder

## Usage

```python
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

```

## Features
### Currently implemented
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

### Tests
* Run `python tests.py`

## Contribute
Check out the issues on GitHub and/or make a pull request to contribute!
