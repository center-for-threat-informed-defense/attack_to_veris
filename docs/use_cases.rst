VERIS/ATT&CK Mappings Use Cases
===============================

Users
-----

The existing communities of VERIS and ATT&CK users include many roles and responsibilities associated with organizational risk management processes and procedures. These roles and responsibilities include:

  - **Incident Response (IR) Professional** - responsibilities include response, management, and coordination, and remediation activities for cyber incidents such as malware infections, data theft, ransomware encryption, denial of service, and control systems intrusions.
  - **Chief Information Security Officer (CISO)** - responsibilities include carrying out information security policies, procedures, and controls, and providing primary interface between senior managers and information system owners.
  - **Information System Security Officer (ISSO)** - responsibilities include ensuring the appropriate operational security posture is maintained for information systems or programs.
  - **Security Operations Center (SOC) Analyst** - responsibilities include monitoring an organization's networks and systems to detect threats and investigating potential security incidents.
  - **Security Engineer** - responsibilities include developing and implementing security controls and solutions to protect networks and systems from unauthorized access and attacks.

Usage
-----

The VERIS mappings to MITRE ATT&CK enable the following essential capabilities:

  1.	Expanded vocabulary for describing adversary behaviors in an incident. VERIS users can leverage ATT&CK's full range of TTPs when describing adversary activities during a security event. (IR, ISSO)
  2.	Enhanced analysis of historical incident information. Collecting and analyzing incident information with more granular descriptions of adversary behaviors using ATT&CK enables analysts and senior leaders to align policies/controls/governance to defend against adversary behaviors. (CISO, SOC)
  3.	Streamlined integration of incident reports into security operations. Using ATT&CK to describe adversary behaviors in an incident enables security operations teams that already use ATT&CK to easily leverage incident information to inform operations. (SOC)

Use Cases
---------

Users of the VERIS/ATT&CK mapping performing the essential capabilities as described above support a variety of use cases. Several of those use cases are described below.

  1. As an IR professional, I want to ensure I have a complete picture of an active security incident.
      * The VERIS/ATT&CK mapping provides an optimal joint framework to comprehensively describe security events at a flexible level. At a very low level, the ATT&CK mappings allow incident response professionals to understand the details of adversary activities, thus creating a fingerprint of the event. This fingerprint can provide an analysis of the attacker’s tools, techniques, and procedures (TTP), which can assist in real-time decision making and activating responsive functionality in existing tools. Additionally, such an analysis can assist responders in looking for additional TTP artifacts that may typically coexist with currently observed activity.
  2. As an CISO/ISSO, I want to understand how our current security posture addresses real-world threats that my organization is likely to encounter.
      * While individual reports can assist in the prevention of attack recurrence based on similar TTPs, collections of such reports, both internally generated and publicly available, can guide strategic direction. Such a corpus represents the state-of-the-art in effective attack methodologies. As such, they provide a necessary minimal bar for an organization's security program to reach to be effective in the current threat landscape. Gaps in process/governance can then be addressed.
  3. As a SOC analyst, I need to know that we have sufficient visibility into threats launched against my organization.
      * Every TTP available in an event description provides an actionable data point for SOC analysts. Conversely, any missed indicator can lead to the organization being victimized by a similar attack. A report based on the VERIS/ATT&CK mapping can provide immediate opportunities to test, refine and add detections. Most ATT&CK technique and sub-technique narrative pages provide a detection section suggesting where to look for indicators. This often includes links to available tooling to assist in detection. For example, for technique T1137.005 Office Application Startup: Outlook Rules, the detection section notes that Microsoft has released a PowerShell script to gather mail forwarding rules. This provides another data point for potential adversary activity, potentially pre-breach. If these tools represent new detection functionality, they may serve to address a blind spot in an organization's visibility into attacks. If the tool duplicates functionality, it may serve to test that the existing detection technology is accurate and suggest possible tuning opportunities.
  4. As a Security Engineer, I want to understand what mitigations are necessary to prevent classes of attacker activity.
      * Most ATT&CK techniques and sub-technique narrative pages provide a section on applicable mitigations. Careful examination and correlation may suggest control improvements that can mitigate classes of adversary activity rather than individual threats. This represents a significant improvement, both from the constant pressures faced by most information security budgets, and increasing complexity that leads to more gaps in control coverage.
