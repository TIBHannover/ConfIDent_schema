# Class: WikiCFP Series ID
_The identifier of an academic event or series in WikiCFP._







## Inheritance
* [External ID](ExternalIdentifier.md) [SchemaBasedThing]
    * **WikiCFP Series ID**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [WikiCFP Series ID](wikicfp_series_id.md) | range | WikiCfpSeriesId |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:WikiCfpSeriesId'] |
| native | ['confident:WikiCfpSeriesId'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WikiCfpSeriesId
description: The identifier of an academic event or series in WikiCFP.
title: WikiCFP Series ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(WikiCFP)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(http://www.wikicfp.com/cfp/program?id=$1)

```
</details>

### Induced

<details>
```yaml
name: WikiCfpSeriesId
description: The identifier of an academic event or series in WikiCFP.
title: WikiCFP Series ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: ExternalIdentifier
slot_usage:
  schema_name:
    name: schema_name
    ifabsent: string(WikiCFP)
  schema_base_uri:
    name: schema_base_uri
    ifabsent: uri(http://www.wikicfp.com/cfp/program?id=$1)
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: WikiCfpSeriesId
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(WikiCFP)
    alias: schema_name
    owner: WikiCfpSeriesId
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: uri(http://www.wikicfp.com/cfp/program?id=$1)
    alias: schema_base_uri
    owner: WikiCfpSeriesId
    range: uriorcurie

```
</details>