# STIX Format
This document describes the formatting of the veris framework and mappings in STIX 2.0 JSON. You can find the STIX data in the `/frameworks/` folder:
- [VERIS STIX data](/frameworks/stix)

## STIX
Structured Threat Information eXpression (STIX&trade;) is a language and serialization format used to exchange cyber threat intelligence (CTI). STIX enables organizations to share CTI with one another in a consistent and machine-readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively. To find out more about STIX, please see [the STIX 2.0 website](https://oasis-open.github.io/cti-documentation/stix/intro). 

<img src="/docs/veris_in_stix.png" width="900px">

## Format
The veris objects and mapping data in this repository follows the STIX 2.0 format as follows:
- Both veris objects and mappings are represented in STIX 2.0 JSON.
- VERIS objects are represented as a STIX [Attack Pattern](http://docs.oasis-open.org/cti/stix/v2.0/cs01/part2-stix-objects/stix-v2.0-cs01-part2-stix-objects.html#_Toc496714301) object.
- **No** custom STIX properties or objects are used for the veris framework objects representation.
- Mappings from individual veris objects to ATT&CK techniques and sub-techniques are represented as a STIX [Relationship](https://docs.oasis-open.org/cti/stix/v2.0/csprd01/part2-stix-objects/stix-v2.0-csprd01-part2-stix-objects.html#_Toc476230970) object of type `related-to`, where the `source_ref` is the `id` of the veris object and the `target_ref` is the `id` of the technique or sub-technique.

## See also
- [Tooling](/docs/tooling.md) for more information about how the STIX data was created.
- [Visualization](/docs/visualization.md) for more information about how to visualize the mappings.
