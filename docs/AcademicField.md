# Class: Subobject Academic Field
_An academic field is the scientific subject of an event or event series according to some controlled vocabulary or thesaurus and as such requires the scheme URI._







## Inheritance
* **Subobject Academic Field** [SchemaBasedThing]



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 1..1 | The classification label of a certain classification schema.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Academic Field](academic_field.md) | range | AcademicField |
| [Event](Event.md) | [Academic Field](academic_field.md) | range | AcademicField |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:AcademicField'] |
| native | ['confident:AcademicField'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AcademicField
description: An academic field is the scientific subject of an event or event series
  according to some controlled vocabulary or thesaurus and as such requires the scheme
  URI.
title: Subobject Academic Field
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixins:
- SchemaBasedThing
slot_usage:
  schema_value:
    name: schema_value
    description: The classification label of a certain classification schema.
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: AcademicField
description: An academic field is the scientific subject of an event or event series
  according to some controlled vocabulary or thesaurus and as such requires the scheme
  URI.
title: Subobject Academic Field
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixins:
- SchemaBasedThing
slot_usage:
  schema_value:
    name: schema_value
    description: The classification label of a certain classification schema.
    range: string
    required: true
attributes:
  schema_value:
    name: schema_value
    description: The classification label of a certain classification schema.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: AcademicField
    range: string
    required: true
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_name
    owner: AcademicField
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_base_uri
    owner: AcademicField
    range: uriorcurie

```
</details>