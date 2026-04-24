# Subdomain Enumerator

A simple Python tool that probes HTTP connections to discover live subdomains using a wordlist.

## Requirements

```bash
pip install requests
```

## Usage

```bash
python subdomain_enum.py
```

```
Enter the domain to enumerate: example.com
Enter the wordlist path: /path/to/wordlist.txt
```

## Output

```
Connected to: http://admin.example.com
Connected to: http://mail.example.com
```

## Legal Notice

Only use against targets you have explicit permission to test.
