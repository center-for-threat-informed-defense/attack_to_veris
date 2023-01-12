# Depricated Properties
# Added Properties
1. schema_name
# Property changes
## New field:
### .victim.properties.secondary.description
* ```Secondary victims indicates that the breach being coded is the first part of a supply chain breach.```
## New field:
### .victim.properties.secondary.description.properties.amount.definition
* ```The number of known secondary victims. Should always be a positive number if victim_id is filled in.  May not represent all victims if some are unknown.```
## Updated field:
### .victim.properties.secondary.revenue.properties.iso_currency_code.description
* Old: ```ISO_4217 currency code. <a href='https://en.wikipedia.org/wiki/ISO_4217' target='_blank'>More Info</a>```
* New: ```ISO4217 currency code. <a href='https://w.wiki/3Sfv' target='_blank'>More Info</a>```
## Updated field:
### .action.properties.hacking.properties.variety.items.enum
* Old: ```['Abuse of functionality', 'Brute force', 'Buffer overflow', 'Cache poisoning', 'Cryptanalysis', 'CSRF', 'DoS', 'Exploit misconfig', 'Exploit vuln', 'Footprinting', 'Forced browsing', 'Format string attack', 'Fuzz testing', 'HTTP request smuggling', 'HTTP request splitting', 'HTTP response smuggling', 'HTTP Response Splitting', 'Insecure deserialization', 'Integer overflows', 'LDAP injection', 'Mail command injection', 'MitM', 'Null byte injection', 'Offline cracking', 'OS commanding', 'Pass-the-hash', 'Path traversal', 'Reverse engineering', 'RFI', 'Routing detour', 'Session fixation', 'Session prediction', 'Session replay', 'Soap array abuse', 'Special element injection', 'SQLi', 'SSI injection', 'URL redirector abuse', 'Use of backdoor or C2', 'Use of stolen creds', 'User breakout', 'Virtual machine escape', 'XML attribute blowup', 'XML entity expansion', 'XML external entities', 'XML injection', 'XPath injection', 'XQuery injection', 'XSS', 'Other', 'Unknown']```
* New: ```['Abuse of functionality', 'Backdoor', 'Brute force', 'Buffer overflow', 'Cache poisoning', 'Cryptanalysis', 'CSRF', 'Disable controls', 'DoS', 'Evade Defenses', 'Exploit misconfig', 'Exploit vuln', 'Forced browsing', 'Format string attack', 'Fuzz testing', 'HTTP request smuggling', 'HTTP request splitting', 'HTTP response smuggling', 'HTTP response splitting', 'Insecure deserialization', 'Integer overflows', 'LDAP injection', 'Mail command injection', 'MitM', 'Null byte injection', 'Offline cracking', 'OS commanding', 'Pass-the-hash', 'Path traversal', 'Profile host', 'Reverse engineering', 'RFI', 'Routing detour', 'Scan network', 'Session fixation', 'Session prediction', 'Session replay', 'Soap array abuse', 'Special element injection', 'SQLi', 'SSI injection', 'URL redirector abuse', 'Use of stolen creds', 'User breakout', 'Virtual machine escape', 'XML attribute blowup', 'XML entity expansion', 'XML external entities', 'XML injection', 'XPath injection', 'XQuery injection', 'XSS', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.properties.variety.vector.items.enum
* Old: ```['3rd party desktop', 'Backdoor or C2', 'Command shell', 'Desktop sharing', 'Desktop sharing software', 'Hypervisor', 'Inter-tenant', 'Other', 'Partner', 'Physical access', 'VPN', 'Web application', 'Unknown']```
* New: ```['3rd party desktop', 'Backdoor', 'Command shell', 'Desktop sharing', 'Desktop sharing software', 'Hypervisor', 'Inter-tenant', 'Other network service', 'Partner', 'Physical access', 'VPN', 'Web application', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.properties.variety.items.enum
* Old: ```['Adminware', 'Adware', 'Backdoor', 'Brute force', 'C2', 'Capture app data', 'Capture stored data', 'Click fraud', 'Click fraud and cryptocurrency mining', 'Client-side attack', 'Cryptocurrency mining', 'Destroy data', 'In-memory', 'Modify data', 'Disable controls', 'DoS', 'Downloader', 'Exploit misconfig', 'Exploit vuln', 'Export data', 'Packet sniffer', 'Password dumper', 'RAM scraper', 'Ransomware', 'RAT', 'Rootkit', 'Scan network', 'Spam', 'Spyware/Keylogger', 'SQL injection', 'Trojan', 'Worm', 'Other', 'Unknown']```
* New: ```['Adminware', 'Adware', 'Backdoor', 'Backdoor or C2', 'Brute force', 'C2', 'Capture app data', 'Capture stored data', 'Click fraud', 'Click fraud and cryptocurrency mining', 'Client-side attack', 'Cryptocurrency mining', 'Destroy data', 'In-memory', 'MitM', 'Modify data', 'Disable controls', 'DoS', 'Downloader', 'Exploit misconfig', 'Evade Defenses', 'Exploit vuln', 'Export data', 'Packet sniffer', 'Pass-the-hash', 'Password dumper', 'Profile host', 'RAM scraper', 'Ransomware', 'RAT', 'Rootkit', 'Scan network', 'Spam', 'Spyware/Keylogger', 'Trojan', 'Worm', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.properties.variety.vector.items.enum
* Old: ```['Direct install', 'Download by malware', 'Email', 'Email attachment', 'Email autoexecute', 'Email link', 'Email unknown', 'Email other', 'Instant messaging', 'Network propagation', 'Remote injection', 'Removable media', 'Software update', 'Web application', 'Web application - download', 'Web application - drive-by', 'Other', 'Unknown']```
* New: ```['C2', 'Direct install', 'Download by malware', 'Email', 'Email attachment', 'Email autoexecute', 'Email link', 'Email unknown', 'Email other', 'Instant messaging', 'Network propagation', 'Remote injection', 'Removable media', 'Software update', 'Web application', 'Web application - download', 'Web application - drive-by', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.properties.variety.items.enum
* Old: ```['Baiting', 'Bribery', 'Elicitation', 'Extortion', 'Forgery', 'Influence', 'Phishing', 'Pretexting', 'Propaganda', 'Scam', 'Spam', 'Other', 'Unknown']```
* New: ```['Baiting', 'Bribery', 'Elicitation', 'Evade Defenses', 'Extortion', 'Forgery', 'Influence', 'Phishing', 'Pretexting', 'Propaganda', 'Scam', 'Spam', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.properties.variety.vector.items.enum
* Old: ```['Documents', 'Email', 'IM', 'In-person', 'Phone', 'Removable media', 'SMS', 'Social media', 'Software', 'Website', 'Other', 'Unknown']```
* New: ```['Documents', 'Email', 'IM', 'In-person', 'Phone', 'Removable media', 'SMS', 'Social media', 'Software', 'Web application', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.misuse.properties.variety.items.enum
* Old: ```['Data mishandling', 'Email misuse', 'Illicit content', 'Knowledge abuse', 'Net misuse', 'Possession abuse', 'Privilege abuse', 'Snap picture', 'Unapproved hardware', 'Unapproved software', 'Unapproved workaround', 'Other', 'Unknown']```
* New: ```['Data mishandling', 'Email misuse', 'Evade Defenses', 'Illicit content', 'Knowledge abuse', 'Net misuse', 'Possession abuse', 'Privilege abuse', 'Snap picture', 'Unapproved hardware', 'Unapproved software', 'Unapproved workaround', 'Other', 'Unknown']```
## Updated field:
### .action.properties.hacking.malware.social.misuse.physical.properties.variety.items.enum
* Old: ```['Assault', 'Bypassed controls', 'Connection', 'Destruction', 'Disabled controls', 'Skimmer', 'Snooping', 'Surveillance', 'Tampering', 'Theft', 'Wiretapping', 'Other', 'Unknown']```
* New: ```['Assault', 'Bypassed controls', 'Connection', 'Destruction', 'Disabled controls', 'Evade Defenses', 'Skimmer', 'Snooping', 'Surveillance', 'Tampering', 'Theft', 'Wiretapping', 'Other', 'Unknown']```
## Updated field:
### .actor.properties.internal.description
* Old: ```The victim or a part thereof (such as an employee). <a href='http://veriscommunity.net/actors.html#section-internal' target='_blank'>More Info</a>```
* New: ```The victim or a part thereof (such as an employee). <a href='http://veriscommunity.net/actors.html#section-internal' target='_blank'>More Info</a>.  Unless it is an error or intentional breaking of rules (misuse), the actor MUST be acting maliciously.```
## Updated field:
### .actor.properties.internal.partner.description
* Old: ```An entity with an organizational relationship to the victim, but not the victim. <a href='http://veriscommunity.net/actors.html#section-partner' target='_blank'>More Info</a>```
* New: ```An entity with an organizational relationship to the victim, but not the victim (such as a customer or supplier). <a href='http://veriscommunity.net/actors.html#section-partner' target='_blank'>More Info</a>```
## Updated field:
### .discovery_method.properties.external.properties.variety.items.enum
* Old: ```['Actor disclosure', 'Audit', 'Customer', 'Emergency response team', 'Found documents', 'Fraud detection', 'Incident response', 'Law enforcement', 'Other', 'Security researcher', 'Suspicious traffic', 'Unknown', 'Unrelated 3rd party']```
* New: ```['Actor disclosure', 'Audit', 'Customer', 'Emergency response team', 'Found documents', 'Fraud detection', 'Incident response', 'Law enforcement', 'Security researcher', 'Suspicious traffic', 'Unrelated 3rd party', 'Other', 'Unknown']```
## Updated field:
### .discovery_method.properties.external.internal.properties.variety.items.enum
* Old: ```['Antivirus', 'Break in discovered', 'Data loss prevention', 'Financial audit', 'Fraud detection', 'Hids', 'Incident response', 'Infrastructure monitoring', 'It review', 'Log review', 'Nids', 'Other', 'Reported by employee', 'Security alarm', 'Unknown']```
* New: ```['Antivirus', 'Break in discovered', 'Data loss prevention', 'Financial audit', 'Fraud detection', 'Hids', 'Incident response', 'Infrastructure monitoring', 'It review', 'Log review', 'Nids', 'Offboarding', 'Reported by employee', 'Security alarm', 'Other', 'Unknown']```
## Updated field:
### .value_chain.description
* Old: ```Capabilities and investments an attacker must aquire prior to the actions on target.  May be internal to the actors organization (vertically integrated org), or external (purchased in a criminal market).```
* New: ```Capabilities and investments an attacker must acquire prior to the actions on target, (either by purchase or investment in creating).  May be internal to the actors organization (vertically integrated org), or external (purchased in a criminal market).```
## Updated field:
### .value_chain.description.properties.development.properties.variety.items.enum
* Old: ```['Bot', 'Exploit', 'Exploit Kits', 'Payload', 'Persona', 'Ransomware', 'Trojan', 'Website', 'NA', 'Other', 'Unknown']```
* New: ```['Bot', 'Email', 'Exploit', 'Exploit Kits', 'Payload', 'Persona', 'Physical', 'Ransomware', 'Trojan', 'Website', 'NA', 'Other', 'Unknown']```
## Updated field:
### .value_chain.description.properties.development.targeting.properties.variety.items.enum
* Old: ```['Default credentials', 'Email addresses', 'Lost or stolen credentials', 'Misconfigurations', 'Partner', 'Personal Information', 'Organizational Information', 'Vulnerabilities', 'Weaknesses', 'NA', 'Other', 'Unknown']```
* New: ```['Default credentials', 'Email addresses', 'Lost or stolen credentials', 'Misconfigurations', 'Partner', 'Personal Information', 'Physical', 'Organizational Information', 'Vulnerabilities', 'Weaknesses', 'NA', 'Other', 'Unknown']```
## Updated field:
### .value_chain.description.properties.development.targeting.distribution.properties.variety.items.enum
* Old: ```['Botnet', 'Compromised server', 'Direct', 'Email', 'Loader', 'Partner', 'Phone', 'Website', 'NA', 'Other', 'Unknown']```
* New: ```['Botnet', 'Compromised server', 'Direct', 'Email', 'Loader', 'Partner', 'Phone', 'Physical', 'Website', 'NA', 'Other', 'Unknown']```
## Updated field:
### .value_chain.description.properties.development.targeting.distribution.cash-out.properties.variety.items.enum
* Old: ```['Cryptocurrency', 'Direct', 'Fraud', 'Hijacked rewards', 'Provide service', 'Sell stolen goods', 'NA', 'Other', 'Unknown']```
* New: ```['Cryptocurrency', 'Direct', 'Fraud', 'Hijacked rewards', 'Provide service', 'Sell stolen goods', 'Purchase stolen goods', 'NA', 'Other', 'Unknown']```
## Updated field:
### .value_chain.description.properties.development.targeting.distribution.cash-out.money laundering.properties.variety.items.enum
* Old: ```['Bank', 'Company', 'Cryptocurrency tumbling', 'Employment', 'Gambling', 'Physical', 'Provide service', 'Re-shipping', 'Smurfing', 'NA', 'Other', 'Unknown']```
* New: ```['Bank', 'Company', 'Cryptocurrency tumbling', 'Employment', 'Gambling', 'Physical', 'Provide service', 'Re-shipping', 'Smurfing', 'Sell stolen goods', 'NA', 'Other', 'Unknown']```
## Updated field:
### .impact.properties.iso_currency_code.description
* Old: ```ISO_4217 currency code. <a href='https://en.wikipedia.org/wiki/ISO_4217' target='_blank'>More Info</a>```
* New: ```ISO4217 currency code. <a href='https://w.wiki/3Sfv' target='_blank'>More Info</a>```
## Updated field:
### .schema_version.default
* Old: ```1.3.5```
* New: ```1.3.6```
