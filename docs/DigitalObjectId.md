# Class: Digital Object Identifier
_A centrally registered identifier symbol used to uniquely identify digital objects given by International DOI Foundation._







## Inheritance
* [External ID](ExternalIdentifier.md) [ SchemaBasedThing]
    * **Digital Object Identifier**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [DOI](has_doi.md) | range | DigitalObjectId |
| [Event](Event.md) | [DOI](has_doi.md) | range | DigitalObjectId |
| [Subobject Publication](Publication.md) | [DOI](has_doi.md) | range | DigitalObjectId |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['obi:0002110'] |
| native | ['confident:DigitalObjectId'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DigitalObjectId
description: A centrally registered identifier symbol used to uniquely identify digital
  objects given by International DOI Foundation.
title: Digital Object Identifier
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(DOI)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://doi.org/)
class_uri: obi:0002110

```
</details>

### Induced

<details>
```yaml
name: DigitalObjectId
description: A centrally registered identifier symbol used to uniquely identify digital
  objects given by International DOI Foundation.
title: Digital Object Identifier
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(DOI)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://doi.org/)
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: DigitalObjectId
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(DOI)
    alias: schema_name
    owner: DigitalObjectId
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: uri(https://doi.org/)
    alias: schema_base_uri
    owner: DigitalObjectId
    range: uriorcurie
class_uri: obi:0002110

```
</details>