# Mapping Methodology

## Background
The [Vocabulary for Event Recording and Incident Sharing (VERIS)](http://veriscommunity.net) is a set of metrics designed to provide a common language for describing security incidents in a structured and repeatable manner. The overall goal is to lay a foundation from which we can constructively and cooperatively learn from our experiences to better measure and manage risk.

VERIS employs a threat model with four primary axes, the "A4" model, to describe incidents. The four axes are:
- **Actors:** Whose actions affected the asset?
- **Actions:** What actions affected the asset?
- **Assets:** Which assets were affected?
- **Attributes** How was the asset affected?

Each axis has a categorized set of values, called an enumeration, associated with it. Incidents are classified with one or more of those enumeration values for each axis.  Examples of incidents mapped to VERIS can be seen in the VERIS Community Database.

One other axis outside the 4A model that was scrutinized was the **Value Chain**, which represented pre-attack activities. These activities are essential to a successful campaign and are very closely associated with an entire category of behavior.

In this document, VERIS enumeration values follow the form `[Axis].[Category].[Subcategory].[Value]`, e.g. **Action.Malware.Variety.C2** corresponds to the C2 value in the Action axis, Malware category, Variety subcategory.

MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. ATT&CK focuses on how external adversaries compromise and operate within computer information networks.

ATT&CK describes adversary behaviors using the following core components: 
- **Tactics:** short-term, tactical adversary goals
- **Techniques:** means by which adversaries achieve tactical goals
- **Sub-techniques:** describing more specific means by which adversaries achieve tactical goals at a lower level than techniques

Adversary behaviors can be described by mapping them to the appropriate tactics, techniques, and sub-techniques in ATT&CK.

**This mapping takes enumeration values in VERIS and maps them to ATT&CK**. *The resulting mapping can be used to either take a VERIS enumeration value and come up with a list of ATT&CK techniques and sub-techniques, or to take an ATT&CK technique or sub-technique and come up with a list of VERIS enumeration values*.

## Scope
Not all VERIS axes or enumeration values describe adversary behaviors that can be found in ATT&CK. This mapping is constrained to just the portions of VERIS that map to ATT&CK techniques and sub-techniques.

First, the scope is narrowed by examining only those axes that describe adversary behaviors:

Within those axes, the scope is further narrowed based on whether the adversary behaviors for a particular enumeration category align to ATT&CK. For example, ATT&CK does not cover unintentional errors or natural disasters and therefore the Error and Environmental enumeration categories in the Action axis are not mapped.

**Axis Scope**

| Axis | Description | In Scope | Comments |
| --- | --- | --- | --- |
| **Actor** | Whose actions affected the asset? | No | While ATT&CK does catalog threat groups, it does not describe them using a mappable taxonomy. |
| **Action** | What actions affected the asset? | Yes | |
| **Asset** | Which assets were affected? | No | Does not describe adversary behavior. |
| **Attributes** | How was the asset affected? | Yes | |
| **Value Chain** | Capabilities and investments an attacker must aquire prior to the actions on target. | Yes | Aligns with TA0042 Resource Development |

Within those axes, the scope is further narrowed based on whether the adversary behaviors for a particular enumeration category align to ATT&CK. For example, ATT&CK does not cover unintentional errors or natural disasters and therefore the **Error** and **Environmental** enumeration categories in the **Action** axis are not mapped.

**Action Axis Scope**

| Category | Description | In Scope | Comments |
| --- | --- | --- | --- |
| **Malware** | Automated activity | Yes| |
| **Hacking** | Hands-on-keyboard activity | Yes | |
| **Social** | Exploitation of human element  | Yes | |
| **Misuse** | Unapproved use of access| Yes | Describes actor-focused categorizations, not behaviors |
| **Physical** | Actions involving proximity | No | Describes physical attacks, which are out of scope for ATT&CK |
| **Error** | Unintentional actions | No | Does not describe intentionally malicious behavior by an adversary, and therefore out of scope for ATT&CK |
| **Environmental** | Natural disaster events | No | Describes physical accidents and not intentionally malicious actions |

**Attribute Axis Scope**

| Category | Description | In Scope | Comments |
| --- | --- | --- | --- |
| **Confidentiality/Possession** | Data disclosure | No | Describes strategic goals and adversary intent, which is out of scope for ATT&CK. |
| **Integrity/Authenticity** | State of system changed | Partial | Describes both tactical and strategic goals. Tactical goals were in-scope and mapped to ATT&CK. |
| **Availability/Utility** | Availability of system(s) impacted | No | Describes strategic goals and adversary intent, which is out of scope for ATT&CK. |

**Value Chain Axis Scope**

| Category | Description | In Scope | Comments |
| --- | --- | --- | --- |
| **Development** | Software that must be developed to accomplish the actions on target | Yes | |
| **Distribution** | Services used to distribute actor content | Yes | |
| **Non-Distribution Services** | Services used other than those used for distribution of actor content | Yes | |
| **Targeting** | Things that identify exploitable opportunities | Yes | |
| **Cash-Out** | Methods for converting something into currency | No | Describes activities after involvement with victim |
| **Money Laundering** | Methods for concealing the origins of illegally obtained money | No | Describes activities after involvement with victim |

## Mapping Philosophy and Process
Based on those scoping decisions, the mappings were created by analyzing each in-scope ATT&CK technique/sub-technique and each in-scope VERIS enumeration value.

VERIS and ATT&CK are at different levels of abstraction and cannot always perfectly describe the adversary behaviors that they are meant to represent. Some amount of analyst judgment is required, and as always when analyst judgment is involved, there can be differences of opinion. These design decisions document the judgment of the project team and why they made the decisions that they did. They explain why certain mappings are there and others are not.

## Design Decisions

1. Mappings are many-to-many
    - VERIS enumeration values may describe multiple adversary behaviors. Values are mapped to all relevant techniques and sub-techniques.
    - ATT&CK techniques and sub-techniques may describe a behavior that’s also described by multiple VERIS enumeration values. All relevant values are mapped to that technique.
2. VERIS enumeration values are mapped to the most specific ATT&CK entity (tactic, technique, or sub-technique) that applies.
    - If the VERIS enumeration value describes a behavior that maps to a sub-technique, it is mapped to that sub-technique.
    - If the VERIS enumeration value describes a behavior that maps to a technique, it is mapped to that technique and all sub-techniques.
    - If the VERIS enumeration value describes a behavior that maps to a tactic, it is mapped to all techniques and sub-techniques in that tactic.
3. ATT&CK techniques are considered in the context of their descriptions and adversary goals (tactics). In some cases, techniques that appear to describe the same technical behavior are not mapped because the adversary objective differs from that described by the VERIS enumeration value.
4. Many of the same adversary behaviors are described by values in both **Action.Hacking** and **Action.Malware**. Activities in the VERIS **Action.Hacking** category are those performed by hands-on-keyboard attackers. Activities in the VERIS **Action.Malware** category are automated by software/malware. ATT&CK techniques and subtechniques will be mapped to one or both depending on if they describe behaviors that are always automated, always manual, or might be either.
5. Any techniques and sub-techniques that do not have an associated VERIS category based on the above design decisions are mapped to **Action.Hacking.Variety.Other**, **Action.Hacking.Vector.Other**, **Action.Malware.Variety.Other**, or **Action.Malware.Vector.Other**.
6. Any techniques that have unspecified components of adversary behavior were mapped to **Action.Hacking.Variety.Unknown** or **Action.Malware.Variety.Unknown**.

## Mapping Format

The resulting mappings are available as JSON or Excel
