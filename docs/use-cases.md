## Use Cases

This document describes the following use cases for the VERIS to MITRE ATT&CK integration mapping.
1. Provide more granular information about adversary activities during confirmed security events. (IR, CISO)
2. Allow a corpus of security events described in VERIS/ATT&CK to be analyzed to ensure appropriate policies/controls/governance are in place to adequately address historical threats (CISO)
3. Provide guidance to staff to ensure alerting is sufficiently tuned and provides necessary context to quickly respond to a repeat of similar activity (SOC)

### Use Cases - as a user of the VERIS/ATT&CK mapping ###

1. I want a better understanding of an active or recent security incident (IR, CISO).

The VERIS/ATT&CK mapping provides an optimal joint framework to comprehensively describe security events at a flexible level. At a very low level, the ATT&CK mappings allow incident response professionals to provide the necessary level of detail for adversary activities, thus creating a fingerprint of the event. This fingerprint can provide an analysis of the attacker’s tools, techniques, and procedures (TTP), which can assist in activating responsive functionality in existing tools. At the tactical level, such attribution can assist responders in looking for additional TTP artifacts that may coexist with current observations. 

Strategically, a report in the joint VERIS/ATT&CK format naturally leads to a critical examination of each ATT&CK technique or sub-technique, to include the associated mitigations. This review can provide an action list of control/process changes for the organization at the security leadership level in the immediate aftermath of a breach.

2. I want to know that our current security posture addresses realworld threats that my organization is likely to encounter (CISO).

While individual reports can assist in the prevention of attack reoccurrence based on similar TTPs, collections of such reports, both internally generated and publicly available, can guide strategic direction. Such reports represent the state-of-the-art in currently effective attack methodologies. As such, they provide a necessary minimal bar for an organization’s security program to reach to be effective in the current threat landscape. Gaps in controls/process/governance can then be addressed through an action plan.

3. I want to be confident that we have sufficient visibility into threats launched against my organization with adequate time to analyze and respond (SOC).

Every TTP available in an event description provides an actionable data point for SOC analysts. Conversely, any missed indicator can lead to the organization being victimized by a similar attack. A report based on the VERIS/ATT&CK mapping can provide immediate opportunities to test, refine and add detections. 
Most ATT&CK technique and sub-technique narrative pages provide a detection section suggesting where to look for indicators. This often includes links to available tooling to assist in detection. For example, for technique T1137.005 Office Application Startup: Outlook Rules, the detection section notes that Microsoft has released a PowerShell script to gather mail forwarding rules. This provides another data point for potential adversary activity, potentially pre-breach. If these tools represent new detection functionality, they may serve to address a blind spot in an organization’s visibility into attacks. If the tool duplicates functionality, it may serve to test that the existing detection technology is accurate and suggest possible tuning opportunities.

