# Class: Venue
_The venue at which an academic event takes place._







## Inheritance
* **Venue** [ NamedThing]



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Street](street.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The street of the venue including the house number seperated by comma.  | 
| [ZIP Code](zip_code.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The zip code of the venue.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Subobject Location](Location.md) | [Venue](has_venue.md) | range | Venue |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Venue'] |
| native | ['confident:Venue'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Venue
description: The venue at which an academic event takes place.
title: Venue
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
attributes:
  street:
    name: street
    description: The street of the venue including the house number seperated by comma.
    title: Street
    examples:
    - value: Am Welfengarten, 1
      description: street, hous number
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: string
  zip_code:
    name: zip_code
    description: The zip code of the venue.
    title: ZIP Code
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: string

```
</details>

### Induced

<details>
```yaml
name: Venue
description: The venue at which an academic event takes place.
title: Venue
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
attributes:
  street:
    name: street
    description: The street of the venue including the house number seperated by comma.
    title: Street
    examples:
    - value: Am Welfengarten, 1
      description: street, hous number
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: street
    owner: Venue
    range: string
  zip_code:
    name: zip_code
    description: The zip code of the venue.
    title: ZIP Code
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: zip_code
    owner: Venue
    range: string
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: Venue
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: Venue
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: Venue
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>