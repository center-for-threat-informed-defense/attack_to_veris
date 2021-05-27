This document describes the methodology used to map VERIS to MITRE ATT&CK©.  It aims to provide the community a reusable method of using ATT&CK to extend VERIS reporting.

MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base represents adversary goals as tactics and the specific behaviors employed by adversaries to achieve those goals (how) as techniques and sub-techniques. The methodology described below, utilizes the information in the ATT&CK knowledge base and its underlying data model.

The following assumptions were used to guide the the assignment of ATT&CK techniques to VERIS actions.

Sub-techniques must contain all the VERIS mappings of it's parent techniques. However, they may contain others actions that are more specific to that specific sub-technique.

Activities in the action.hacking category are those performed by a hands-on-keyboard threat actor. Activities in the action.malware category are automated and thus performed by malware.

The VERIS action, Abuse of functionality, is defined as tools or commands native to the "system" that would normally be used for administrative functions but have been utilized by a threat actor. The only additional criteria was where the ATT&CK technique's explanatory text explicitly states it as an abuse of functionality.

The VERIS actions action.hacking.variety.other and action.malware.variety.other were used in three situations. 

First, if the techniques did not obviously map to any other action, these two (along with action.hacking.vector.other and action.malware.vector.other) were used as the default targets. 

The second instance was if the technique had unspecified components of hacking or malware, it may have been included with other actions to reflect that fact. 

The third instance was to keep techniques and sub-techniques rationalized given the assumption that all sub-techniques must contain all parent mappings. This necessitated giving the parent a generic mapping that wouldn't be invalid for any of it's sub-techniques.