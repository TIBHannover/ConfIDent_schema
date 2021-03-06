# Class: Subobject Sponsor
_A person or an organization whose role it is to sponsor an academic event or event series._







## Inheritance
* [Subobject Contributor](Contributor.md) [ NamedThing]
    * **Subobject Sponsor**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Type](type.md) | [Contributor Type](ContributorType.md) | 0..1 | An abstract property that is reused in certain classes to differentiate their instances according to the type enums defined as the range.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Sponsor](sponsored_by.md) | range | Sponsor |
| [Event](Event.md) | [Sponsor](sponsored_by.md) | range | Sponsor |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Sponsor'] |
| native | ['confident:Sponsor'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sponsor
description: A person or an organization whose role it is to sponsor an academic event
  or event series.
title: Subobject Sponsor
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: Contributor

```
</details>

### Induced

<details>
```yaml
name: Sponsor
description: A person or an organization whose role it is to sponsor an academic event
  or event series.
title: Subobject Sponsor
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: Contributor
attributes:
  type:
    name: type
    description: An abstract property that is reused in certain classes to differentiate
      their instances according to the type enums defined as the range.
    title: Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    abstract: true
    slot_uri: rdf:type
    designates_type: true
    alias: type
    owner: Sponsor
    range: ContributorType
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: Sponsor
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: Sponsor
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: IAO:0000235
    multivalued: true
    alias: external_id
    owner: Sponsor
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>