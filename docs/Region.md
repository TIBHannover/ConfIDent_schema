# Class: Region
_The region in which an academic event takes place. For non USA events this might often be negligible._







## Inheritance
* **Region** [ NamedThing]



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Subobject Location](Location.md) | [Region](has_region.md) | range | Region |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Region'] |
| native | ['confident:Region'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Region
description: The region in which an academic event takes place. For non USA events
  this might often be negligible.
title: Region
examples:
- value: Texas
  description: the US state Texas as an example of a region
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing

```
</details>

### Induced

<details>
```yaml
name: Region
description: The region in which an academic event takes place. For non USA events
  this might often be negligible.
title: Region
examples:
- value: Texas
  description: the US state Texas as an example of a region
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
attributes:
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: Region
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: Region
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: IAO:0000235
    multivalued: true
    alias: external_id
    owner: Region
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>