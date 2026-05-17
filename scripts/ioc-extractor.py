import re

sample_text = """
Suspicious connection detected from IP 185.220.101.45
User received phishing email from fake-support@security-alert.com
Malicious URL identified: http://secure-login-check.com
"""

ips = re.findall(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}', sample_text)
emails = re.findall(r'[\w\.-]+@[\w\.-]+', sample_text)
urls = re.findall(r'https?://[^\s]+', sample_text)

print("IPs Found:")
for ip in ips:
    print(ip)

print("\nEmails Found:")
for email in emails:
    print(email)

print("\nURLs Found:")
for url in urls:
    print(url)
