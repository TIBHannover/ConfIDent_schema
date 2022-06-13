# Class: TIBKAT ID
_The identifier of a publication in the TIB catalog that references an event or event series._







## Inheritance
* [External ID](ExternalIdentifier.md) [ SchemaBasedThing]
    * **TIBKAT ID**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [TIBKAT ID](tibkat_id.md) | range | TibkatId |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:TibkatId'] |
| native | ['confident:TibkatId'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TibkatId
description: The identifier of a publication in the TIB catalog that references an
  event or event series.
title: TIBKAT ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(TIBKAT)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://www.tib.eu/en/search/id/TIBKAT:)

```
</details>

### Induced

<details>
```yaml
name: TibkatId
description: The identifier of a publication in the TIB catalog that references an
  event or event series.
title: TIBKAT ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(TIBKAT)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://www.tib.eu/en/search/id/TIBKAT:)
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: TibkatId
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(TIBKAT)
    alias: schema_name
    owner: TibkatId
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: uri(https://www.tib.eu/en/search/id/TIBKAT:)
    alias: schema_base_uri
    owner: TibkatId
    range: uriorcurie

```
</details>