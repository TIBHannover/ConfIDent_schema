# Class: Subobject Contributor
_A contributor is a person or organization that holds a contributor role which is being realized in an event or event series._







## Inheritance
* **Subobject Contributor** [ NamedThing]
    * [Subobject Sponsor](Sponsor.md)
    * [Subobject Attendee](Attendee.md)
    * [Subobject Moderator](Moderator.md)
    * [Subobject Reviewer](Reviewer.md)
    * [Subobject Organizer](Organizer.md)
    * [Subobject Presenter](Presenter.md)



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Type](type.md) | [Contributor Type](ContributorType.md) | 0..1 | A property to provide the information whether the contributor is an organization or person.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | The internal ConfIDent identifier for a contibutor  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Contributor'] |
| native | ['confident:Contributor'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Contributor
description: A contributor is a person or organization that holds a contributor role
  which is being realized in an event or event series.
title: Subobject Contributor
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
slots:
- type
slot_usage:
  type:
    name: type
    description: A property to provide the information whether the contributor is
      an organization or person.
    designates_type: true
    range: ContributorType
  id:
    name: id
    description: The internal ConfIDent identifier for a contibutor

```
</details>

### Induced

<details>
```yaml
name: Contributor
description: A contributor is a person or organization that holds a contributor role
  which is being realized in an event or event series.
title: Subobject Contributor
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
slot_usage:
  type:
    name: type
    description: A property to provide the information whether the contributor is
      an organization or person.
    designates_type: true
    range: ContributorType
  id:
    name: id
    description: The internal ConfIDent identifier for a contibutor
attributes:
  type:
    name: type
    description: A property to provide the information whether the contributor is
      an organization or person.
    title: Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    abstract: true
    slot_uri: rdf:type
    designates_type: true
    alias: type
    owner: Contributor
    range: ContributorType
  id:
    name: id
    description: The internal ConfIDent identifier for a contibutor
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: Contributor
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: Contributor
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: Contributor
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>