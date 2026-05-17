# Brute Force Investigation

## Incident Summary

A brute force attack was identified against an internal VPN authentication portal. Multiple failed login attempts were detected from a suspicious external IP address targeting administrative accounts.

## Attack Details

- Attack Type: Brute Force
- Target: VPN Authentication Portal
- Source IP: 185.220.101.45
- Affected Accounts:
  - admin
  - support
  - helpdesk

## Indicators of Compromise (IOCs)

- High volume of failed logins
- Repeated authentication attempts
- Suspicious foreign IP address
- Account lockout events

## Investigation Steps

1. Reviewed VPN authentication logs
2. Identified repeated failed logins
3. Correlated source IP activity
4. Verified account lockout alerts
5. Blocked malicious IP address

## Mitigation Actions

- Blocked attacker IP
- Enabled MFA for VPN access
- Increased login monitoring
- Updated firewall rules
- Alerted IT security team

## Lessons Learned

- MFA significantly reduces brute force risk
- Login anomaly monitoring is critical
- VPN access requires continuous monitoring
