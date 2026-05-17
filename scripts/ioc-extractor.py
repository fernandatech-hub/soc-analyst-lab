import re

sample_text = """
Suspicious IP: 185.220.101.45
Malicious domain: fake-login-security.com
"""

ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', sample_text)
domains = re.findall(r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', sample_text)

print("IPs Found:")
for ip in ips:
    print(ip)

print("\nDomains Found:")
for domain in domains:
    print(domain)
