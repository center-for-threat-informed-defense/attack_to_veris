Overview
========

To fully understand and document cybersecurity incidents requires two types of information: information about the organization, assets, and data targeted (the “who”, “what”, and “why”), as well as specifics on the tradecraft that the adversaries used to achieve their objectives (the “when” and “how”). Without the former, descriptions of incidents often lack important information that roughly translates into the “so what” — the true impact of the event. Without the latter, breach reports lack sufficient information to allow others to protect themselves from the threat. 

To allow people to better connect the who, what, and why captured in VERIS with the when and how described in ATT&CK, the Center completed an R&D project in 2021 to provide a mapping and translation layer between VERIS and ATT&CK for efficient usage of ATT&CK to describe the adversary behaviors observed in an incident coded in VERIS. This allows for a joint analysis of the information that ATT&CK describes well (the behaviors adversaries use to attack systems) alongside the incident demographics and metadata that VERIS describes well. 

The Center has now continued the work of the original project, developing an even more comprehensive translation between VERIS and ATT&CK. This work strengthens the connection between these frameworks to increase the community's ability to pivot between incidents coded in VERIS and adversary behaviors described in ATT&CK.

Background
----------

VERIS is a common representation and data model for describing the demographics, metadata, and some technical details about cybersecurity incidents. VERIS provides a standard, high-level representation that allows for the analysis of data across a variety of incidents. It is used, among other things, to generate the `Verizon Data Breach Investigation Report (DBIR) <https://www.verizon.com/business/resources/reports/dbir/>`_.

ATT&CK provides a common taxonomy for describing detailed adversary behavioral tactics and techniques. The ATT&CK knowledge base is a curated repository of adversary tactics, techniques, and procedures (TTPs) based on publicly available reporting and real-world observations.

While VERIS is comprehensive in describing most aspects of cybersecurity incidents, it is focused on the high-level description of an incident. Conversely, while ATT&CK describes adversary behavior in granular detail, it does not attempt to describe incidents or their overall impact. . The Center’s VERIS ATT&CK translation empowers defenders to efficiently tie adversary TTPs to their real-world impact by connecting ATT&CK-based threat intel to VERIS-based incident reports.

Expanding the Translation
-------------------------
 
The mapping between VERIS and ATT&CK has been updated and expanded, strengthening the connection of the "business language" of VERIS with the "technical language" of ATT&CK. This project update builds upon the foundation of incidents coded in VERIS being enhanced with granular ATT&CK data, and vice versa. The update and expansion of the mapping repository ￼  s: 
- Updates for the VERIS Community schema 1.3.7 from 1.3.5, 
- Updates for ATT&CK for Enterprise v12.1 from v9.0, 
- Revisiting unmapped VERIS Vectors and Varieties, 
- Expansion of VERIS Attribute axis mappings, 
- Mapping VERIS Actors and ATT&CK Group TTPs, 
- Mapping VERIS values to ATT&CK for Mobile, and 
- Mapping VERIS values to ATT&CK for ICS.

The example below shows the bidirectional mapping of the VERIS Action.Hacking.Vector.Desktop sharing software to a more granular set of ATT&CK techniques. This granular description of an adversary's behavior allows users to better understand how to detect and mitigate the threat.

.. image:: docs/_static/veris-to-attack.png
   :width: 600    
   
In addition, expanded mapping and usage documentation further demonstrates how the translation can be used to describe and communicate information about security incidents. Updated use cases and new scenario examples are provided to illustrate ways for defenders to efficiently tie adversary TTPs and their real-world impact by connecting ATT&CK-based threat intel with VERIS-based incident reports, and vice versa. Defenders performing essential capabilities can use the VERIS/ATT&CK mapping to support a variety of `use cases <docs\use_cases.rst>`_.

STIX Representation and Mapping Tools
-------------------------------------

To make the mapping between VERIS and ATT&CK easily accessible to the cyber threat intel capabilities and teams that use STIX, we created a STIX 2 representation of the mappings. By representing VERIS Actions and Attributes as STIX Attack Patterns we were able to create STIX Relationships to represent the association between VERIS and ATT&CK.

.. image:: docs/_static/veris_in_stix.png
   :width: 600

A set of `Python tools <https://github.com/center-for-threat-informed-defense/attack_to_veris/blob/main/docs/tooling.md>`_ is provided to support data manipulation, including the creation of new mappings and the customization of existing mappings. A command line interface (CLI) tool is available for validation of mapping file syntax, ensuring conformity to the data format specification and accurate references of ATT&CK (sub-)techniques. The CLI tool also supports the production of the ATT&CK Navigator layers and Markdown Summary visualizations from mapping files. 

Users can easily refine and extend the mappings for their needs and locally rebuild the full set of supporting artifacts using the scripts in this repository. If you are simply ingesting the data from this repository, you likely will not need to install or run any of the provided scripts.

Get Involved
------------

The resulting mapping between VERIS and ATT&CK will allow cyber defenders to create an even fuller and more detailed picture of cyber incidents, including the threat actor, technical behavior, assets targeted, and impact. These improvements can be used to develop better predictions and insights into how we might be attacked in the future by better understanding how and why we were attacked in the past.

We encourage you to review the mappings, use them, and tell us what you think. This project also provides the methodology and tools needed to build collections tailored to any need. You can build proprietary collections to use within your organization, or you can share your collections to benefit the community.

We welcome your feedback and contributions to continue to advance ATT&CK Integration with VERIS. Please see the guidance for contributors if are you interested in `contributing <https://github.com/center-for-threat-informed-defense/attack_to_veris/blob/main/CONTRIBUTING.md>`_. You are also welcome to submit issues for any technical questions/concerns or contact `ctid@mitre-engenuity.org <mailto:ctid@mitre-engenuity.org>`_ directly for more general inquiries.