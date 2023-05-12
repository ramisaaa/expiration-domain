import whois
import sys

if len(sys.argv) < 2:
    print("Usage: python expiration.py domain_name")
    sys.exit(1)

domain_name = sys.argv[1]

try:
    domain_info = whois.whois(domain_name)
    expiration_date = domain_info.expiration_date
    print("Expiration date of", domain_name, "is", expiration_date)
except Exception as e:
    print("Error:", e)
