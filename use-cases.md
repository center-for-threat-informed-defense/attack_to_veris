## VERIS Integration into ATT&CK Use Cases

This document describes the following use cases for the VERIS to MITRE ATT&CK integration mapping.
1. Provide more granular information about adversary activities during confirmed security events. (IR, CISO)
2. Allow a corpus of security events described in VERIS/ATT&CK to be analyzed to ensure that appropriate policies/controls/governance are in place to adequately address historical threats (CISO)
3. Provide guidance to staff to ensure alerting is sufficiently tuned and provides necessary context to quickly respond to a repeat of similar activity (SOC)

### Narrative ###
1. Provide more granular information about adversary activities during confirmed security events. (IR, CISO)

VERIS integrated with ATT&CK provides an optimal joint framework to comprehensively describe security events at a flexible level. At a very low level, the ATT&CK mappings allow incident response professionals to provide the necessary level of detail for adversary activities, thus creating a fingerprint of the event. This fingerprint can assist in analyzing the attacker’s tools, techniques, and procedures (TTP), which can assist with possible early-stage attribution. At the tactical level, such attribution can assist responders in potentially looking for additional TTP artifacts that a given adversary group may use. 

Strategically, a report in the joint VERIS/ATT&CK format naturally leads to a critical examination of each ATT&CK technique or sub-technique, to include the associated mitigations. This review can provide an action list of control/process changes for the organization at the security leadership level in the immediate aftermath of a breach.

2. Allow a corpus of security events described in VERIS/ATT&CK to be analyzed to ensure that appropriate policies/controls are in place to adequately address historical threats (CISO)

While individual reports can assist in the prevention of attack reoccurrence based on similar TTPs, collections of such reports, both internally generated and publicly available, can guide strategic direction. Such reports represent the state-of-the-art in currently effective attack TTPs. As such, they provide a necessary minimal bar for an organization’s security program to reach to be effective in the current threat landscape. Gaps in controls/process/governance can then be addressed through an action plan.

3. Provide guidance to staff to ensure alerting is sufficiently tuned and includes necessary context to quickly respond to a repeat of similar activity (SOC).

Every TTP available in an event description provides an actionable data point for SOC analysts. Conversely, any missed indicator can lead to the organization being victimized by a similar attack. A report based on ATT&CK Integrated VERIS can provide immediate opportunities to test, refine and add detections. 
Most ATT&CK techniques and sub-techniques narrative pages provides a detection section suggesting where to look for indicators. This often includes links to available tooling to assist in detection. For example, for technique T1137.005 Office Application Startup: Outlook Rules, the detection section notes that Microsoft has released a PowerShell script to gather mail forwarding rules. This provides another data point for potential adversary activity, potentially pre-breach. If these tools represent new detection functionality, they may serve to address a blind spot in an organization’s visibility into attacks. If the tool duplicates functionality, it may still serve to test that the existing detection technology is accurate and suggest possible tuning opportunities.

