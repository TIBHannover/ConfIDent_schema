# Class: Subobject Organizer
_An organizer of an academic event or event series._







## Inheritance
* [Subobject Contributor](Contributor.md) [NamedThing]
    * **Subobject Organizer**
        * [Subobject Contact Person](ContactPerson.md)
        * [Subobject Committee Member](CommitteeMember.md)



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Contact](contact.md) | [Subobject Contact Person](ContactPerson.md) | 0..1 _recommended_ | The contact person of an academic event or event series.  | 
| [Type](type.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | An abstract property that is reused in certain classes to differentiate their instances according to the type enums defined as the range.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Organizer](organized_by.md) | range | Organizer |
| [Event](Event.md) | [Organizer](organized_by.md) | range | Organizer |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Organizer'] |
| native | ['confident:Organizer'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organizer
description: An organizer of an academic event or event series.
title: Subobject Organizer
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: Contributor
attributes:
  contact:
    name: contact
    description: The contact person of an academic event or event series.
    title: Contact
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: ContactPerson
    required: false
    recommended: true
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: Organizer
description: An organizer of an academic event or event series.
title: Subobject Organizer
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: Contributor
attributes:
  contact:
    name: contact
    description: The contact person of an academic event or event series.
    title: Contact
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: contact
    owner: Organizer
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
    owner: Organizer
    range: string
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: Organizer
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: Organizer
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: Organizer
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>