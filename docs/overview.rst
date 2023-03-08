Overview
========

To fully understand and document cybersecurity incidents requires two types of information: information about the organization, assets, and data targeted (the “who”, “what”, and “why”), as well as specifics on the tradecraft that the adversaries used to achieve their objectives (the “when” and “how”). Without the former, descriptions of incidents often lack important information that roughly translates into the “so what” — the true impact of the event. Without the latter, breach reports lack sufficient information to allow others to protect themselves from the threat. 

VERIS is a common representation and data model for describing the demographics, metadata, and some technical details about cybersecurity incidents. VERIS provides a standard, high-level representation that allows for the analysis of data across a variety of incidents. It is used, among other things, to generate the `Verizon Data Breach Investigation Report (DBIR) <https://www.verizon.com/business/resources/reports/dbir/>`_.

ATT&CK provides a common taxonomy for describing detailed adversary behavioral tactics and techniques. The ATT&CK knowledge base is a curated repository of adversary tactics, techniques, and procedures (TTPs) based on publicly available reporting and real-world observations.

While VERIS is comprehensive in describing most aspects of cybersecurity incidents, it is focused on the high-level description of an incident. Conversely, while ATT&CK describes adversary behavior in granular detail, it does not attempt to describe incidents or their overall impact.

To allow people to better connect the who, what, and why captured in VERIS with the when and how described in ATT&CK, the Center completed a project in 2021 to provide a mapping and translation layer between VERIS and ATT&CK for efficient usage of ATT&CK to describe the adversary behaviors observed in an incident coded in VERIS. This allows for a joint analysis of the information that ATT&CK describes well (the behaviors adversaries use to attack systems) alongside the incident demographics and metadata that VERIS describes well. 

The Center has now continued the work of the original project, developing an even more comprehensive translation between VERIS and ATT&CK. This work strengthens the connection between these frameworks to increase the community's ability to pivot between incidents coded in VERIS and adversary behaviors described in ATT&CK. 

