<h1>Mapping Methodology</h1>

___
<h2>Background</h2>
<p>
The [Vocabulary for Event Recording and Incident Sharing](http://veriscommunity.net) (VERIS) is a set of metrics designed to provide a common language for describing security incidents in a structured and repeatable manner. The overall goal is to lay a foundation from which we can constructively and cooperatively learn from our experiences to better measure and manage risk.
</p>
VERIS employs a threat model with four axes, the “A4” model, to describe incidents. The four axes are:
<ul>
<li><strong>Actors:</strong> Whose actions affected the asset?
<li><strong>Actions:</strong> What actions affected the asset?
<li><strong>Assets:</strong> Which assets were affected?
<li><strong>Attributes</strong>: How was the asset affected?
</ul>
<p>
Each axis has a categorized set of values, called an enumeration, associated with it. Incidents are classified with one or more of those enumeration values for each axis.  Examples of incidents mapped to VERIS can be seen in the VERIS Community Database.
</p>

<p>
In this document, VERIS enumeration values follow the form [Axis].[Category].[Subcategory].[Value], e.g.<strong> Action.Malware.Hacking.C2</strong> corresponds to the C2 value in the Action axis, Malware category, Hacking subcategory.
</p>

<p>
MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. ATT&CK focuses on how external adversaries compromise and operate within computer information networks.
</p>

ATT&CK describes adversary behaviors using the following core components: 
<ul>
<li><strong>Tactics:</strong> short-term, tactical adversary goals
<li><strong>Techniques:</strong> means by which adversaries achieve tactical goals
<li><strong>Sub-techniques:</strong> describing more specific means by which adversaries achieve tactical goals at a lower level than techniques
</ul>

<p>
Adversary behaviors can be described by mapping them to the appropriate tactics, techniques, and sub-techniques in ATT&CK.
</p>

<strong>This mapping takes enumeration values in VERIS and maps them to ATT&CK</strong>. *The resulting mapping can be used to either take a VERIS enumeration value and come up with a list of ATT&CK techniques and sub-techniques, or to take an ATT&CK technique or sub-technique and come up with a list of VERIS enumeration values*.

<h2>Scope</h2>
<p>
Not all VERIS axes or enumeration values describe adversary behaviors that can be found in ATT&CK. This mapping is constrained to just the portions of VERIS that map to ATT&CK techniques and sub-techniques.
</p>

<p>
First, the scope is narrowed by examining only those axes that describe adversary behaviors:
</p>

<p>
Within those axes, the scope is further narrowed based on whether the adversary behaviors for a particular enumeration category align to ATT&CK. For example, ATT&CK does not cover unintentional errors or natural disasters and therefore the Error and Environmental enumeration categories in the Action axis are not mapped.
</p>

<p><strong>Axis Scope</strong></p>
<strong>Axis | Description | In Scope | Comments</strong>
-----|-------------|----------|---------
<strong>Actor</strong> | Whose actions affected the asset? | No | While ATT&CK does catalog threat groups, it does not describe them using a mappable taxonomy 
<strong>Action</strong> | What actions affected the asset? | Yes | 
<strong>Asset</strong> | Which assets were affected? | No | Does not describe adversary behavior 
<strong>Attributes</strong> | How was the asset affected? | Yes | 

<p>
Within those axes, the scope is further narrowed based on whether the adversary behaviors for a particular enumeration category align to ATT&CK. For example, ATT&CK does not cover unintentional errors or natural disasters and therefore the <strong>Error</strong> and <strong>Environmental</strong> enumeration categories in the <strong>Action</strong> axis are not mapped.
</p>

<p><strong>Action Axis Scope</strong></p>
<strong>Category | Description | In Scope | Comments</strong>
---------|-------------|----------|---------
<strong>Hacking</strong> | Automated activity | Yes |
<strong>Social</strong> | Hands-on-keyboard activity | Yes |
<strong>Misuse</strong> | Exploitation of human element | Yes |
<strong>Physical</strong> | Unapproved use of access | No | Describes actor-focused categorizations, not behaviors.
<strong>Error</strong> | Actions involving proximity | No | Describes physical attacks, which are out of scope for ATT&CK.
<strong>Environmental</strong> | Unintentional actions | No | Does not describe intentionally malicious behavior by an adversary, and therefore out of scope for ATT&CK.
<p><strong>Attribute Axis Scope</strong></p> 
<strong>Category | Description | In Scope | Comments</strong>
---------|-------------|----------|---------
<strong>Confidentiality/Possession</strong> | Data disclosure | No | Describes strategic goals and adversary intent, which is out of scope for ATT&CK.
<strong>Integrity/Authenticity</strong> | State of system changed | Partial | Describes both tactical and strategic goals. Tactical goals were in-scope and mapped to ATT&CK.
<strong>Availability/Utility</strong> | Availability of system(s) impacted | No | Describes strategic goals and adversary intent, which is out of scope for ATT&CK.
<h2>Mapping Philosophy and Process</h2>
<p>
Based on those scoping decisions, the mappings were created by analyzing each in-scope ATT&CK technique/sub-technique and each in-scope VERIS enumeration value.
</p>

<p>
VERIS and ATT&CK are at different levels of abstraction and cannot always perfectly describe the adversary behaviors that they are meant to represent. Some amount of analyst judgment is required, and as always when analyst judgment is involved, there can be differences of opinion. These design decisions document the judgment of the project team and why they made the decisions that they did. They explain why certain mappings are there and others are not.
</p>

<h2>Design Decisions</h2>
<ol>
<li>Mappings are many-to-many
<ol><li>VERIS enumeration values may describe multiple adversary behaviors. Values are mapped to all relevant techniques and sub-techniques.
<li>ATT&CK techniques and sub-techniques may describe a behavior that’s also described by multiple VERIS enumeration values. All relevant values are mapped to that technique. As an example, </ol>
<li>VERIS enumeration values are mapped to the most specific ATT&CK entity (tactic, technique, or sub-technique) that applies.
<ol><li>If the VERIS enumeration value describes a behavior that maps to a sub-technique, it is mapped to that sub-technique.
<li>If the VERIS enumeration value describes a behavior that maps to a technique, it is mapped to that technique and all sub-techniques.
<li>If the VERIS enumeration value describes a behavior that maps to a tactic, it is mapped to all techniques and sub-techniques in that tactic.</ol>
<li>ATT&CK techniques are considered in the context of their descriptions and adversary goals (tactics). In some cases, techniques that appear to describe the same technical behavior are not mapped because the adversary objective differs from that described by the VERIS enumeration value.
<li>Many of the same adversary behaviors are described by values in both <strong>Action.Hacking</strong> and <strong>Action.Malware</strong>. Activities in the VERIS <strong>Action.Hacking</strong> category are those performed by hands-on-keyboard attackers. Activities in the VERIS <strong>Action.Malware</strong> category are automated by software/malware. ATT&CK techniques and subtechniques will be mapped to one or both depending on if they describe behaviors that are always automated, always manual, or might be either.
<li>Any techniques and sub-techniques that do not have an associated VERIS category based on the above design decisions are mapped to<strong> Action.Hacking.Variety.Other</strong>, <strong>Action.Hacking.Vector.Other</strong>, <strong>Action.Malware.Variety.Other</strong>, or <strong>Action.Malware.Vector.Other</strong>.
<li>Any techniques that have unspecified components of adversary behavior were mapped to <strong>Action.Hacking.Variety.Unknown</strong> or <strong>Action.Malware.Variety.Unknown</strong>.
</ol>

<h2>Mapping Format</h2>
<p>
The resulting mapings are available as JSON or Excel
</p>
