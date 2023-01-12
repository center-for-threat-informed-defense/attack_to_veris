# Depricated Properties
# Added Properties
# Property changes
## New field:
### .source_id.description
* ```Source of the data (eg vcdb, vzir, hr dept)```
## Updated field:
### .action.properties.hacking.properties.variety.items.enum
* Old: ```['Abuse of functionality', 'Backdoor', 'Brute force', 'Buffer overflow', 'Cache poisoning', 'Cryptanalysis', 'CSRF', 'Disable controls', 'DoS', 'Evade Defenses', 'Exploit misconfig', 'Exploit vuln', 'Forced browsing', 'Format string attack', 'Fuzz testing', 'HTTP request smuggling', 'HTTP request splitting', 'HTTP response smuggling', 'HTTP response splitting', 'Insecure deserialization', 'Integer overflows', 'LDAP injection', 'Mail command injection', 'MitM', 'Null byte injection', 'Offline cracking', 'OS commanding', 'Pass-the-hash', 'Path traversal', 'Profile host', 'Reverse engineering', 'RFI', 'Routing detour', 'Scan network', 'Session fixation', 'Session prediction', 'Session replay', 'Soap array abuse', 'Special element injection', 'SQLi', 'SSI injection', 'URL redirector abuse', 'Use of stolen creds', 'User breakout', 'Virtual machine escape', 'XML attribute blowup', 'XML entity expansion', 'XML external entities', 'XML injection', 'XPath injection', 'XQuery injection', 'XSS', 'Other', 'Unknown']```
* New: ```['Abuse of functionality', 'Backdoor', 'Brute force', 'Buffer overflow', 'Cache poisoning', 'Cryptanalysis', 'CSRF', 'Disable controls', 'DoS', 'Evade Defenses', 'Exploit misconfig', 'Exploit vuln', 'Forced browsing', 'Format string attack', 'Fuzz testing', 'Hijack', 'HTTP request smuggling', 'HTTP request splitting', 'HTTP response smuggling', 'HTTP response splitting', 'Insecure deserialization', 'Integer overflows', 'LDAP injection', 'Mail command injection', 'MitM', 'Null byte injection', 'Offline cracking', 'OS commanding', 'Pass-the-hash', 'Path traversal', 'Profile host', 'Reverse engineering', 'RFI', 'Routing detour', 'Scan network', 'Session fixation', 'Session prediction', 'Session replay', 'Soap array abuse', 'Special element injection', 'SQLi', 'SSI injection', 'URL redirector abuse', 'Use of stolen creds', 'User breakout', 'Virtual machine escape', 'XML attribute blowup', 'XML entity expansion', 'XML external entities', 'XML injection', 'XPath injection', 'XQuery injection', 'XSS', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.properties.variety.result.items.enum
* Old: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Other', 'Unknown', 'NA']```
* New: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Persist', 'Other', 'Unknown', 'NA']```
## Updated field:
### .action.properties.hacking.malware.properties.vector.items.enum
* Old: ```['C2', 'Direct install', 'Download by malware', 'Email', 'Email attachment', 'Email autoexecute', 'Email link', 'Email unknown', 'Email other', 'Instant messaging', 'Network propagation', 'Remote injection', 'Removable media', 'Software update', 'Web application', 'Web application - download', 'Web application - drive-by', 'Other', 'Unknown']```
* New: ```['C2', 'Direct install', 'Download by malware', 'Email', 'Email attachment', 'Email autoexecute', 'Email link', 'Email unknown', 'Email other', 'Instant messaging', 'Network propagation', 'Partner', 'Remote injection', 'Removable media', 'Software update', 'Web application', 'Web application - download', 'Web application - drive-by', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.properties.vector.result.items.enum
* Old: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Other', 'Unknown', 'NA']```
* New: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Persist', 'Other', 'Unknown', 'NA']```
## Updated field:
### .action.properties.hacking.malware.social.properties.variety.items.enum
* Old: ```['Baiting', 'Bribery', 'Elicitation', 'Evade Defenses', 'Extortion', 'Forgery', 'Influence', 'Phishing', 'Pretexting', 'Propaganda', 'Scam', 'Spam', 'Other', 'Unknown']```
* New: ```['Baiting', 'Bribery', 'Elicitation', 'Evade Defenses', 'Extortion', 'Forgery', 'Influence', 'Phishing', 'Pretexting', 'Prompt bombing', 'Propaganda', 'Scam', 'Spam', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.properties.variety.vector.items.enum
* Old: ```['Documents', 'Email', 'IM', 'In-person', 'Phone', 'Removable media', 'SMS', 'Social media', 'Software', 'Web application', 'Other', 'Unknown']```
* New: ```['Documents', 'Email', 'IM', 'In-person', 'Partner', 'Phone', 'Removable media', 'SMS', 'Social media', 'Software', 'Web application', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.properties.variety.vector.result.items.enum
* Old: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Other', 'Unknown', 'NA']```
* New: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Persist', 'Other', 'Unknown', 'NA']```
## Updated field:
### .action.properties.hacking.malware.social.error.properties.variety.items.enum
* Old: ```['Capacity shortage', 'Classification error', 'Data entry error', 'Disposal error', 'Gaffe', 'Loss', 'Maintenance error', 'Malfunction', 'Misconfiguration', 'Misdelivery', 'Misinformation', 'Omission', 'Physical accidents', 'Programming error', 'Publishing error', 'Other', 'Unknown']```
* New: ```['Capacity shortage', 'Classification error', 'Data entry error', 'Disposal error', 'Gaffe', 'Loss', 'Maintenance error', 'Malfunction', 'Misconfiguration', 'Misdelivery', 'Misinformation', 'Physical accidents', 'Programming error', 'Publishing error', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.error.misuse.properties.result.items.enum
* Old: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Other', 'Unknown', 'NA']```
* New: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Persist', 'Other', 'Unknown', 'NA']```
## Updated field:
### .action.properties.hacking.malware.social.error.misuse.physical.properties.result.items.enum
* Old: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Other', 'Unknown', 'NA']```
* New: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Persist', 'Other', 'Unknown', 'NA']```
## Updated field:
### .action.properties.hacking.malware.social.error.misuse.physical.unknown.properties.result.items.enum
* Old: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Other', 'Unknown', 'NA']```
* New: ```['Infiltrate', 'Exfiltrate', 'Elevate', 'Lateral movement', 'Deploy payload', 'Persist', 'Other', 'Unknown', 'NA']```
## Updated field:
### .asset.properties.assets.items.properties.variety.enum
* Old: ```['M - Disk drive', 'M - Disk media', 'M - Documents', 'M - Flash drive', 'M - Payment card', 'M - Smart card', 'M - Tapes', 'M - Other', 'M - Unknown', 'M - Fax', 'N - Access reader', 'N - Broadband', 'N - Camera', 'N - Firewall', 'N - HSM', 'N - IDS', 'N - LAN', 'N - NAS', 'N - PBX', 'N - PLC', 'N - Private WAN', 'N - Public WAN', 'N - Router or switch', 'N - RTU', 'N - SAN', 'N - Telephone', 'N - VoIP adapter', 'N - WLAN', 'N - Other', 'N - Unknown', 'P - Auditor', 'P - Call center', 'P - Cashier', 'P - Customer', 'P - Developer', 'P - End-user', 'P - End-user or employee', 'P - Executive', 'P - Finance', 'P - Former employee', 'P - Guard', 'P - Helpdesk', 'P - Human resources', 'P - Maintenance', 'P - Manager', 'P - Other employee', 'P - Partner', 'P - System admin', 'P - Other', 'P - Unknown', 'S - Authentication', 'S - Backup', 'S - Configuration or patch management', 'S - Code repository', 'S - Database', 'S - DCS', 'S - DHCP', 'S - Directory', 'S - DNS', 'S - File', 'S - ICS', 'S - Log', 'S - Mail', 'S - Mainframe', 'S - Payment switch', 'S - POS controller', 'S - Print', 'S - Proxy', 'S - Remote access', 'S - VM host', 'S - Web application', 'S - Other', 'S - Unknown', 'T - ATM', 'T - Gas terminal', 'T - Kiosk', 'T - PED pad', 'T - Other', 'T - Unknown', 'U - Auth token', 'U - Desktop', 'U - Desktop or laptop', 'U - Laptop', 'U - Media', 'U - Mobile phone', 'U - Peripheral', 'U - POS terminal', 'U - Tablet', 'U - Telephone', 'U - VoIP phone', 'U - Other', 'U - Unknown', 'E - Telemetry', 'E - Telematics', 'E - Other', 'E - Unknown', 'Unknown', 'Other']```
* New: ```['M - Disk drive', 'M - Disk media', 'M - Documents', 'M - Flash drive', 'M - Payment card', 'M - Smart card', 'M - SIM card', 'M - Tapes', 'M - Other', 'M - Unknown', 'M - Fax', 'N - Access reader', 'N - Broadband', 'N - Camera', 'N - Firewall', 'N - HSM', 'N - IDS', 'N - LAN', 'N - NAS', 'N - PBX', 'N - PLC', 'N - Private WAN', 'N - Public WAN', 'N - Router or switch', 'N - RTU', 'N - SAN', 'N - Telephone', 'N - VoIP adapter', 'N - WLAN', 'N - Other', 'N - Unknown', 'P - Auditor', 'P - Call center', 'P - Cashier', 'P - Customer', 'P - Developer', 'P - End-user', 'P - End-user or employee', 'P - Executive', 'P - Finance', 'P - Former employee', 'P - Guard', 'P - Helpdesk', 'P - Human resources', 'P - Maintenance', 'P - Manager', 'P - Other employee', 'P - Partner', 'P - System admin', 'P - Other', 'P - Unknown', 'S - Authentication', 'S - Backup', 'S - Configuration or patch management', 'S - Code repository', 'S - Database', 'S - DCS', 'S - DHCP', 'S - Directory', 'S - DNS', 'S - File', 'S - ICS', 'S - Log', 'S - Mail', 'S - Mainframe', 'S - Payment switch', 'S - POS controller', 'S - Print', 'S - Proxy', 'S - Remote access', 'S - VM host', 'S - Web application', 'S - Other', 'S - Unknown', 'T - ATM', 'T - Gas terminal', 'T - Kiosk', 'T - PED pad', 'T - Other', 'T - Unknown', 'U - Auth token', 'U - Desktop', 'U - Desktop or laptop', 'U - Laptop', 'U - Media', 'U - Mobile phone', 'U - Peripheral', 'U - POS terminal', 'U - Tablet', 'U - Telephone', 'U - VoIP phone', 'U - Other', 'U - Unknown', 'E - Telemetry', 'E - Telematics', 'E - Other', 'E - Unknown', 'Unknown', 'Other']```
## Updated field:
### .attribute.properties.confidentiality.properties.data.items.properties.variety.enum
* Old: ```['Bank', 'Classified', 'Copyrighted', 'Credentials', 'Digital certificate', 'Internal', 'Medical', 'Payment', 'Personal', 'Secrets', 'Source code', 'System', 'Virtual currency', 'Other', 'Unknown']```
* New: ```['Bank', 'Classified', 'Copyrighted', 'Credentials', 'Digital certificate', 'Internal', 'Medical', 'Multi-factor credential', 'Payment', 'Personal', 'Sensitive Personal', 'Secrets', 'Source code', 'System', 'Virtual currency', 'Other', 'Unknown']```
## Updated field:
### .discovery_method.properties.internal.description
* Old: ```Discovered by an external partner.```
* New: ```Discovered by entity within the victim organization.```
## Updated field:
### .schema_version.description
* Old: ```Schema version in use. This should be 1.3.4 for this schema.```
* New: ```Schema version in use. This should be 1.3.7 for this schema.```
## Updated field:
### .schema_version.description.default
* Old: ```1.3.6```
* New: ```1.3.7```
