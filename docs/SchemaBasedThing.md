# Class: Subobject Schema Based Thing
_A mixin used in classes that contain schema based values, such as the classifications used to denote the academic field of an event or the external identifiers used to denote a thing._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly



<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:SchemaBasedThing'] |
| native | ['confident:SchemaBasedThing'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SchemaBasedThing
description: A mixin used in classes that contain schema based values, such as the
  classifications used to denote the academic field of an event or the external identifiers
  used to denote a thing.
title: Subobject Schema Based Thing
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixin: true
slots:
- schema_value
- schema_name
- schema_base_uri

```
</details>

### Induced

<details>
```yaml
name: SchemaBasedThing
description: A mixin used in classes that contain schema based values, such as the
  classifications used to denote the academic field of an event or the external identifiers
  used to denote a thing.
title: Subobject Schema Based Thing
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixin: true
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_value
    owner: SchemaBasedThing
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_name
    owner: SchemaBasedThing
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_base_uri
    owner: SchemaBasedThing
    range: uriorcurie

```
</details>