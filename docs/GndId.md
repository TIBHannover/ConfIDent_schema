# Class: GND ID
_The identifier of a thing (item) in the German National authority file._







## Inheritance
* [External ID](ExternalIdentifier.md) [ SchemaBasedThing]
    * **GND ID**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [GND ID](gnd_id.md) | range | GndId |
| [Event](Event.md) | [GND ID](gnd_id.md) | range | GndId |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:GndId'] |
| native | ['confident:GndId'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GndId
description: The identifier of a thing (item) in the German National authority file.
title: GND ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(GND)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(http://d-nb.info/gnd/)

```
</details>

### Induced

<details>
```yaml
name: GndId
description: The identifier of a thing (item) in the German National authority file.
title: GND ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(GND)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(http://d-nb.info/gnd/)
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: GndId
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(GND)
    alias: schema_name
    owner: GndId
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: uri(http://d-nb.info/gnd/)
    alias: schema_base_uri
    owner: GndId
    range: uriorcurie

```
</details>