# Class: Subobject Contact Person
_The contact person of an academic event or event series._







## Inheritance
* [Subobject Contributor](Contributor.md) [NamedThing]
    * [Subobject Organizer](Organizer.md)
        * **Subobject Contact Person**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Email](email.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The email address of the contact person.  | 
| [Telephone](telephone.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The telephone number of the contact person.  | 
| [Contact](contact.md) | [Subobject Contact Person](ContactPerson.md) | 0..1 _recommended_ | The contact person of an academic event or event series.  | 
| [Type](type.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | An abstract property that is reused in certain classes to differentiate their instances according to the type enums defined as the range.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Subobject Organizer](Organizer.md) | [Contact](contact.md) | range | ContactPerson |
| [Subobject Contact Person](ContactPerson.md) | [Contact](contact.md) | range | ContactPerson |
| [Subobject Committee Member](CommitteeMember.md) | [Contact](contact.md) | range | ContactPerson |
| [Subobject Committee Chair](CommitteeChair.md) | [Contact](contact.md) | range | ContactPerson |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:ContactPerson'] |
| native | ['confident:ContactPerson'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContactPerson
description: The contact person of an academic event or event series.
title: Subobject Contact Person
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: Organizer
attributes:
  email:
    name: email
    description: The email address of the contact person.
    title: Email
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:email
    range: string
    pattern: \b[-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
  telephone:
    name: telephone
    description: The telephone number of the contact person.
    title: Telephone
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:telephone
    range: string

```
</details>

### Induced

<details>
```yaml
name: ContactPerson
description: The contact person of an academic event or event series.
title: Subobject Contact Person
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: Organizer
attributes:
  email:
    name: email
    description: The email address of the contact person.
    title: Email
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:email
    alias: email
    owner: ContactPerson
    range: string
    pattern: \b[-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
  telephone:
    name: telephone
    description: The telephone number of the contact person.
    title: Telephone
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:telephone
    alias: telephone
    owner: ContactPerson
    range: string
  contact:
    name: contact
    description: The contact person of an academic event or event series.
    title: Contact
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: contact
    owner: ContactPerson
    range: ContactPerson
    required: false
    recommended: true
    inlined: true
  type:
    name: type
    description: An abstract property that is reused in certain classes to differentiate
      their instances according to the type enums defined as the range.
    title: Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    abstract: true
    alias: type
    owner: ContactPerson
    range: string
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: ContactPerson
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: ContactPerson
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: ContactPerson
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>