import requests
import sys

domain = input("Enter the domain to enumerate: ")
wordlist_path = input("Enter the wordlist path: ")

try:
    with open(wordlist_path, "r") as wordlist:
        sub_domains = wordlist.read().splitlines()
except FileNotFoundError:
    print(f"Error: File '{wordlist_path}' not found.")
    sys.exit(1)

for sub_domain in sub_domains:
    if not sub_domain.strip():
        continue
    url = f"http://{sub_domain.strip()}.{domain}"
    try:
        requests.get(url, timeout=3)
    except requests.ConnectionError:
        pass
    else:
        print(f"Connected to: {url}")
