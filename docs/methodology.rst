.. vim: syntax=rst

Mapping Methodology
===================

The `Vocabulary for Event Recording and Incident Sharing
(VERIS) <http://veriscommunity.net/>`__ provides a common language for
describing security incidents in a structured and repeatable manner. The
overall goal is to lay a foundation from which we can constructively and
cooperatively learn from our experiences to better measure and manage
risk.

VERIS employs a threat model with four primary axes, the "A4" model, to
describe incidents. The four axes are:

-  **Actors:** Whose actions affected the asset?

-  **Actions:** What actions affected the asset?

-  **Assets:** Which assets were affected?

-  **Attributes:** How was the asset affected?

Each axis has a categorized set of values, called an enumeration,
associated with it. Incidents are classified with one or more of those
enumeration values for each axis. Examples of incidents mapped to VERIS
can be seen in the VERIS Community Database.

One other axis outside the 4A model is the **Value Chain**, which
represented pre-attack activities. These activities are essential to a
successful campaign and are very closely associated with an entire
category of behavior.

In this document, VERIS enumeration values follow the
form [Axis].[Category].[Subcategory].[Value]; for
example, *Action.Malware.Variety.C2* corresponds to the C2 value in
the Action axis, Malware category, Variety subcategory.

MITRE ATT&CK® is a globally-accessible knowledge base of adversary
tactics and techniques based on real-world observations. ATT&CK focuses
on how external adversaries compromise and operate within computer
information networks.

ATT&CK describes adversary behaviors using the following core
components:

-  **Tactics:** "why" - the adversary's objective or reason for
   performing an action

-  **Techniques:** "how" - the means by which adversaries achieve
   tactical goals

-  **Sub-techniques:** describing more specific means by which
   adversaries achieve tactical goals at a lower level than techniques

Adversary behaviors can be described by mapping them to the appropriate
tactics, techniques, and sub-techniques in ATT&CK.

This original Center ATT&CK Integration into VERIS mapping project took
enumeration values in VERIS and mapped them to ATT&CK Enterprise
Techniques. The resultant mappings could be used to either take a VERIS
enumeration value and come up with a list of ATT&CK techniques and
sub-techniques, or to take an ATT&CK technique or sub-technique and come
up with a list of VERIS enumeration values.

This VERIS II project continues the work of the original integration
project by updating and expanding the mapping and translation layer
between VERIS and ATT&CK to enhance the community's ability to pivot
from VERIS to ATT&CK Techniques related to a particular incident. In
addition, the creation of expanded mapping and usage documentation to
provide updated use cases and new scenario examples further demonstrate
how the integration or VERIS and ATT&CK translation can support
describing and communicating information about security incidents.**

The comprehensive mapping plan used for updating and expanding the
original translation between VERIS and ATT&CK includes:

-  Updates for the VERIS Community schema 1.3.7 from 1.3.5,

-  Updates for ATT&CK for Enterprise v12.1 from v9.0,

-  Revisiting unmapped VERIS Varieties,

-  Expansion of VERIS Attribute axis mappings,

-  Mapping VERIS Actors and ATT&CK Groups,

-  Mapping VERIS values to ATT&CK for Mobile, and

-  Mapping VERIS values to ATT&CK for ICS.

Scope
-----

Not all VERIS axes or enumeration values describe adversary behaviors
that can be found in ATT&CK. This mapping is constrained to just the
portions of VERIS that map to ATT&CK techniques and sub-techniques.

Axis Scope
~~~~~~~~~~

+-----------+-----------------------+-------+-------------------------------+
| Axis      | Description           | In    | Comments                      |
|           |                       | Scope |                               |
+===========+=======================+=======+===============================+
| Actor     | Whose actions         | Yes   | Aligns with ATT&CK groups of  |
|           | affected the asset?   |       | adversarial activity clusters |
|           |                       |       | tracked by common names in    |
|           |                       |       | the security community.       |
+-----------+-----------------------+-------+-------------------------------+
| Action    | What actions affected | Yes   | Describes adversary behaviors |
|           | the asset?            |       | performed by hands-on-keyboard|
|           |                       |       | attackers or automated by     |
|           |                       |       | software/malware.             |
+-----------+-----------------------+-------+-------------------------------+
| Asset     | Which assets were     | No    | Does not describe adversary   |
|           | affected?             |       | behavior.                     |
+-----------+-----------------------+-------+-------------------------------+
| Attributes| How was the asset     | Yes   | Describes strategical and     |
|           | affected?             |       | tactical impact.              |
+-----------+-----------------------+-------+-------------------------------+
| Value     | Capabilities and      | Yes   | Aligns with ATT&CK Tactic     |
| Chain     | investments an        |       | TA0042 Resource Development.  |
|           | attacker must acquire |       |                               |
|           | prior to the actions  |       |                               |
|           | on target.            |       |                               |
+-----------+-----------------------+-------+-------------------------------+

Within each of the axes that describe adversary behaviors, the scope is
further narrowed based on whether the adversary behaviors for a particular
enumeration category align to ATT&CK. For example, ATT&CK does not cover
unintentional errors or natural disasters and therefore the *Error* and
*Environmental* enumeration categories in the *Action* axis are not mapped.

Action Axis Scope
~~~~~~~~~~~~~~~~~

+------------------+----------------------+--------+------------------+
| Category         | Description          | In     | Comments         |
|                  |                      | Scope  |                  |
+==================+======================+========+==================+
| Malware          | Automated activity   | Yes    | Describes any    |
|                  |                      |        | malicious        |
|                  |                      |        | software,        |
|                  |                      |        | script, or code  |
|                  |                      |        | run on a device  |
|                  |                      |        | that alters      |
|                  |                      |        | state or         |
|                  |                      |        | function without |
|                  |                      |        | informed         |
|                  |                      |        | consent.         |
+------------------+----------------------+--------+------------------+
| Hacking          | Hands-on-keyboard    | Yes    | Describes all    |
|                  | activity             |        | attempts to      |
|                  |                      |        | intentionally    |
|                  |                      |        | access or harm   |
|                  |                      |        | information      |
|                  |                      |        | assets without   |
|                  |                      |        | (or exceeding)   |
|                  |                      |        | authorization.   |
+------------------+----------------------+--------+------------------+
| Social           | Exploitation of      | Yes    | Describes use of |
|                  | human element        |        | deception,       |
|                  |                      |        | manipulation,    |
|                  |                      |        | intimidation,    |
|                  |                      |        | etc., to exploit |
|                  |                      |        | users of         |
|                  |                      |        | information      |
|                  |                      |        | assets.          |
+------------------+----------------------+--------+------------------+
| Misuse           | Unapproved use of    | Yes    | Describes        |
|                  | access               |        | actor-focused    |
|                  |                      |        | categorizations, |
|                  |                      |        | not behaviors.   |
+------------------+----------------------+--------+------------------+
| Physical         | Actions involving    | No     | Describes        |
|                  | proximity            |        | physical         |
|                  |                      |        | attacks, which   |
|                  |                      |        | are out of scope |
|                  |                      |        | for ATT&CK.      |
+------------------+----------------------+--------+------------------+
| Error            | Unintentional        | No     | Does not         |
|                  | actions              |        | describe         |
|                  |                      |        | intentionally    |
|                  |                      |        | malicious        |
|                  |                      |        | behavior by an   |
|                  |                      |        | adversary, and   |
|                  |                      |        | therefore out of |
|                  |                      |        | scope for        |
|                  |                      |        | ATT&CK.          |
+------------------+----------------------+--------+------------------+
| Environmental    | Natural disaster     | No     | Describes        |
|                  | events               |        | physical         |
|                  |                      |        | accidents and    |
|                  |                      |        | not              |
|                  |                      |        | intentionally    |
|                  |                      |        | malicious        |
|                  |                      |        | actions.         |
+------------------+----------------------+--------+------------------+

Attribute Axis Scope
~~~~~~~~~~~~~~~~~~~~

+------------------------------+----------------+--------+------------+
| Category                     | Description    | In     | Comments   |
|                              |                | Scope  |            |
+==============================+================+========+============+
| Confidentiality/Possession   | Data           | Partial| Describes  |
|                              | disclosure     |        | both       |
|                              |                |        | tactical   |
|                              |                |        | and        |
|                              |                |        | strategic  |
|                              |                |        | goals.     |
|                              |                |        | Tactical   |
|                              |                |        | goals are  |
|                              |                |        | in-scope   |
|                              |                |        | and mapped |
|                              |                |        | to ATT&CK. |
+------------------------------+----------------+--------+------------+
| Integrity/Authenticity       | State of       | Partial| Describes  |
|                              | system changed |        | both       |
|                              |                |        | tactical   |
|                              |                |        | and        |
|                              |                |        | strategic  |
|                              |                |        | goals.     |
|                              |                |        | Tactical   |
|                              |                |        | goals are  |
|                              |                |        | in-scope   |
|                              |                |        | and mapped |
|                              |                |        | to ATT&CK. |
+------------------------------+----------------+--------+------------+
| Availability/Utility         | Availability   | Partial| Describes  |
|                              | of system(s)   |        | both       |
|                              | impacted       |        | tactical   |
|                              |                |        | and        |
|                              |                |        | strategic  |
|                              |                |        | goals.     |
|                              |                |        | Tactical   |
|                              |                |        | goals are  |
|                              |                |        | in-scope   |
|                              |                |        | and mapped |
|                              |                |        | to ATT&CK. |
+------------------------------+----------------+--------+------------+

Value Chain Axis Scope
~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------------------+------+------------------------+
| Category    | Description             | In   | Comments               |
|             |                         | Scope|                        |
+=============+=========================+======+========================+
| Development | Software that must be   | Yes  | Describes activities   |
|             | developed to accomplish |      | establishing           |
|             | the actions on target   |      | capabilities and       |
|             |                         |      | infrastructure.        |
+-------------+-------------------------+------+------------------------+
| Distribution| Services used to        | Yes  | Describes activities   |
|             | distribute actor        |      | for establishing       |
|             | content                 |      | delivery mechanisms.   |
+-------------+-------------------------+------+------------------------+
| Non-        | Services other than     | Yes  | Describes staging      |
| Distribution| those used for          |      | activities for         |
| Services    | distribution of actor   |      | engagement.            |
|             | content                 |      |                        |
+-------------+-------------------------+------+------------------------+
| Targeting   | Things that identify    | Yes  | Aligns with ATT&CK     |
|             | exploitable             |      | Tactic TA0042 Resource |
|             | opportunities           |      | Development.           |
+-------------+-------------------------+------+------------------------+
| Cash-Out    | Methods for converting  | No   | Describes activities   |
|             | something into currency |      | after involvement with |
|             |                         |      | victim.                |
+-------------+-------------------------+------+------------------------+
| Money       | Methods for concealing  | No   | Describes activities   |
| Laundering  | the origins of          |      | after involvement with |
|             | illegally obtained      |      | victim.                |
|             | money                   |      |                        |
+-------------+-------------------------+------+------------------------+

Mapping Philosophy and Process
------------------------------

Based on those scoping decisions, the mappings were created by analyzing
each in-scope ATT&CK technique/sub-technique and each in-scope VERIS
enumeration value.

VERIS and ATT&CK are at different levels of abstraction and cannot
always perfectly describe the adversary behaviors that they are meant to
represent. Some amount of analyst judgment is required, and as always
when analyst judgment is involved, there can be differences of opinion.
These design decisions document our judgement and rationale. They
explain why certain mappings are there and others are not.

Guiding Principles and Design Decisions
---------------------------------------

1. Mappings are many-to-many.

   -  VERIS enumeration values may describe multiple adversary
      behaviors. Values are mapped to all relevant techniques and
      sub-techniques.

   -  ATT&CK techniques and sub-techniques may describe a behavior that
      is also described by multiple VERIS enumeration values. Techniques
      are mapped to all relevant values.

2. VERIS enumeration values are mapped to the most specific ATT&CK
   entity (i.e., tactic, technique, or sub-technique) that applies.

   -  If the VERIS enumeration value describes a behavior that maps to a
      sub-technique, it is mapped to that sub-technique.

   -  If the VERIS enumeration value describes a behavior that maps to a
      technique, it is mapped to that technique and all sub-techniques.

   -  If the VERIS enumeration value describes a behavior that maps to a
      tactic, it is mapped to all techniques and sub-techniques in that
      tactic.

3. ATT&CK techniques are considered in the context of their descriptions
   and adversary goals (tactics). In some cases, techniques that appear
   to describe the same technical behavior are not mapped because the
   adversary objective differs from that described by the VERIS
   enumeration value.

4. Many of the same adversary behaviors are described by values in both
   *Action.Hacking* and *Action.Malware*. Activities in the VERIS
   *Action.Hacking* category are those performed by hands-on-keyboard
   attackers. Activities in the VERIS *Action.Malware* category are
   automated by software/malware. ATT&CK techniques and sub-techniques
   will be mapped to one or both depending on if they describe behaviors
   that are always automated, always manual, or might be either.

5. Any techniques and sub-techniques that do not have an associated
   VERIS category based on the above design decisions are mapped to
   *Action.Hacking.Variety.Other*, *Action.Hacking.Vector.Other*,
   *Action.Malware.Variety.Other*, or *Action.Malware.Vector.Other*.

6. Any techniques that have unspecified components of adversary behavior
   were mapped to *Action.Hacking.Variety.Unknown* or
   *Action.Malware.Variety.Unknown*.

Mapping Format
--------------

The resulting mappings are available as JSON or Excel.
