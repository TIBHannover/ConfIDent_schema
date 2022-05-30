# Class: Wikidata ID
_The identifier of a thing (item) in Wikidata._







## Inheritance
* [External ID](ExternalIdentifier.md) [ SchemaBasedThing]
    * **Wikidata ID**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Wikidata ID](wikidata_id.md) | range | WikidataId |
| [Event](Event.md) | [Wikidata ID](wikidata_id.md) | range | WikidataId |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['wikidata:Q43649390'] |
| native | ['confident:WikidataId'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WikidataId
description: The identifier of a thing (item) in Wikidata.
title: Wikidata ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(Wikidata)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://www.wikidata.org/entity/)
class_uri: wikidata:Q43649390

```
</details>

### Induced

<details>
```yaml
name: WikidataId
description: The identifier of a thing (item) in Wikidata.
title: Wikidata ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(Wikidata)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://www.wikidata.org/entity/)
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: WikidataId
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(Wikidata)
    alias: schema_name
    owner: WikidataId
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: uri(https://www.wikidata.org/entity/)
    alias: schema_base_uri
    owner: WikidataId
    range: uriorcurie
class_uri: wikidata:Q43649390

```
</details>