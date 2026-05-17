# Ransomware Incident Report

## Incident Summary

A ransomware infection was detected on multiple corporate endpoints after users reported inaccessible encrypted files. Security monitoring identified suspicious encryption activity and abnormal SMB traffic within the internal network.

## Attack Details

- Attack Type: Ransomware
- Initial Vector: Malicious Email Attachment
- Affected Systems:
  - HR-WS01
  - FINANCE-WS03
  - FILESERVER-02

## Indicators of Compromise (IOCs)

- Encrypted files with unusual extensions
- Ransom note creation
- High SMB file transfer activity
- Suspicious PowerShell commands

## Investigation Steps

1. Isolated infected systems
2. Disabled SMB file sharing temporarily
3. Collected forensic artifacts
4. Identified lateral movement activity
5. Reviewed endpoint detection alerts

## Mitigation Actions

- Contained affected endpoints
- Restored files from backups
- Blocked malicious indicators
- Reset privileged credentials
- Improved endpoint protection policies

## Lessons Learned

- Offline backups are critical
- Lateral movement detection needs improvement
- Email filtering must be strengthened
