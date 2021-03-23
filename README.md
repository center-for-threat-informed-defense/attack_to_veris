# attack_to_veris
Vocabulary for Event Recording and Incident Sharing (VERIS), is used by Verizon and others as a common representation and data model for describing the demographics, metadata, and some technical details about cybersecurity incidents. As a standard representation, it allows for the analysis of data across a variety of incidents and is used, among other things, to generate the Verizon Data Breach Investigation Report (DBIR).

While VERIS is very comprehensive in describing most aspects of cybersecurity incidents, it is focused on a high-level description of an incident as a whole, and as such does not provide the level of fidelity that ATT&CK provides in describing the adversary behaviors that were used to carry out the attack at the system level.

We propose developing a managed mapping and translation layer between VERIS and ATT&CK that allows for the usage of ATT&CK to describe the adversary behaviors that were observed in an incident coded in VERIS. This will allow for a joint analysis of the information that ATT&CK describes well (the behaviors adversaries use to attack systems) alongside the incident demographics and metadata that VERIS describes well.

The result of this effort would be a single, holistic framework describing all aspects of an incident, including threat actor, technical behavior, assets targeted and impact. While VERIS currently allows for the expression of all these aspects, ATT&CK provides a significant improvement in level of detail, consistency of detail, and comprehensiveness in describing technical behaviors. These improvements can be used to develop better predictions and insights about how we might be attacked in the future by understanding better how and why we were attacked in the past.

## Questions and Feedback
Please submit issues for any technical questions/concerns or contact ctid@mitre-engenuity.org directly for more general inquiries.

Also see the guidance for contributors if are you interested in contributing or simply reporting issues.

## Notice
Copyright 2021 MITRE Engenuity. Approved for public release. Document number XXXXX

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

This project makes use of ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)
