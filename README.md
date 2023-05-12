# Domain Expiration Date Checker

This is a Python script that checks the expiration date of a domain using the WHOIS protocol.

## Installation

 Install the whois library using pip:

> pip install python-whois


Clone this repository:

> git clone https://github.com/ramisaaa/expiration-domain.git


## Usage

Open a command prompt and navigate to the directory where you cloned the repository:


> cd domain-checker


Run the script and pass the domain name as an argument:


> python domain_checker.py example.com
> 
Replace example.com with the domain name you want to check.

The script will print the expiration date of the domain:


> Expiration date of example.com is 2023-09-15 04:00:00


If an error occurs (e.g. invalid domain name, WHOIS query blocked), the script will print an error message instead.

Notes
This script uses the whois library to query the domain registrar's database for the domain's registration details, including the expiration date. Note that some domain registrars may block WHOIS queries or may not provide the expiration date in the response.

