# Use Cases

The VERIS mappings to MITRE ATT&CK enable the following essential capabilities: 
1.	Expanded vocabulary for describing adversary behaviors in an incident. VERIS users can leverage ATT&CK’s full range of TTPs when describing adversary activities during a security event. (IR, CISO)
2.	Enhanced analysis of historical incident information. Collecting and analyzing incident information with more granular descriptions of adversary behaviors using ATT&CK enable analysts and senior leaders to align policies/controls/governance to defend against adversary behaviors. (CISO, CTI)
3.	Streamlined integration of incident reports into security operations. Using ATT&CK to describe adversary behaviors in an incident enables security operations teams that already use ATT&CK to easily leverage incident information to inform operations. (SOC)


## Use Cases - as a user of the VERIS/ATT&CK mapping ###
The essential capabilities describe above support a variety of use cases. Several of those use cases are described below.

### 1. As an Incident Response (IR) professional, I want to ensure I have a complete picture of an active security incident.

The VERIS/ATT&CK mapping provides an optimal joint framework to comprehensively describe security events at a flexible level. At a very low level, the ATT&CK mappings allow incident response professionals to understand the details of adversary activities, thus creating a fingerprint of the event. This fingerprint can provide an analysis of the attacker’s tools, techniques, and procedures (TTP), which can assist in real-time decision making and activating responsive functionality in existing tools. Additionally, such an analysis can assist responders in looking for additional TTP artifacts that may typically coexist with currently observed activity. 

### 2. As an ISSO, I want to understand how our current security posture addresses real-world threats that my organization is likely to encounter.

While individual reports can assist in the prevention of attack reoccurrence based on similar TTPs, collections of such reports, both internally generated and publicly available, can guide strategic direction. Such a corpus represents the state-of-the-art in effective attack methodologies. As such, they provide a necessary minimal bar for an organization’s security program to reach to be effective in the current threat landscape. Gaps in process/governance can then be addressed.

### 3. As a Security Operations Center (SOC) analyst, I need to know that we have sufficient visibility into threats launched against my organization.

Every TTP available in an event description provides an actionable data point for SOC analysts. Conversely, any missed indicator can lead to the organization being victimized by a similar attack. A report based on the VERIS/ATT&CK mapping can provide immediate opportunities to test, refine and add detections. 

Most ATT&CK technique and sub-technique narrative pages provide a detection section suggesting where to look for indicators. This often includes links to available tooling to assist in detection. For example, for technique T1137.005 Office Application Startup: Outlook Rules, the detection section notes that Microsoft has released a PowerShell script to gather mail forwarding rules. This provides another data point for potential adversary activity, potentially pre-breach. 

If these tools represent new detection functionality, they may serve to address a blind spot in an organization’s visibility into attacks. If the tool duplicates functionality, it may serve to test that the existing detection technology is accurate and suggest possible tuning opportunities.

### 4. As a Security Engineer, I want to understand what mitigations are necessary to prevent classes of attacker activity.

Most ATT&CK techniques and sub-technique narrative pages provide a section on applicable mitigations. Careful examination and correlation may suggest control improvements that can mitigate classes of adversary activity rather than individual threats. This represents a significant improvement, both from the constant pressures faced by most information security budgets, and increasing complexity that leads to more gaps in control coverage.

## Additional Use Cases
Do you have additional use cases that we haven't thought of? We'd love to hear about them! Please share your ideas by submitting an issue or contacting ctid@mitre-engenuity.org.
