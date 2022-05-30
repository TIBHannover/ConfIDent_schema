# Class: DBLP ID
_The identifier of an academic event or series in dblp._







## Inheritance
* [External ID](ExternalIdentifier.md) [ SchemaBasedThing]
    * **DBLP ID**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [DBLP ID](dpbl_id.md) | range | DblpId |
| [Event](Event.md) | [DBLP ID](dpbl_id.md) | range | DblpId |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:DblpId'] |
| native | ['confident:DblpId'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DblpId
description: The identifier of an academic event or series in dblp.
title: DBLP ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(dblp)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://dblp.org/db/conf/)

```
</details>

### Induced

<details>
```yaml
name: DblpId
description: The identifier of an academic event or series in dblp.
title: DBLP ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(dblp)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(https://dblp.org/db/conf/)
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: DblpId
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(dblp)
    alias: schema_name
    owner: DblpId
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: uri(https://dblp.org/db/conf/)
    alias: schema_base_uri
    owner: DblpId
    range: uriorcurie

```
</details>