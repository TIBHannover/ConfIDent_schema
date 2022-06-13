# Class: Subobject Process Relation
_A container for relations between academic events._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Type](type.md) | [Event Relation Type](RelationType.md) | 0..1 | A property to provide the type of process relation.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [Related To](related_to.md) | range | ProcessRelation |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:ProcessRelation'] |
| native | ['confident:ProcessRelation'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessRelation
description: A container for relations between academic events.
title: Subobject Process Relation
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
slots:
- type
slot_usage:
  type:
    name: type
    description: A property to provide the type of process relation.
    range: RelationType

```
</details>

### Induced

<details>
```yaml
name: ProcessRelation
description: A container for relations between academic events.
title: Subobject Process Relation
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
slot_usage:
  type:
    name: type
    description: A property to provide the type of process relation.
    range: RelationType
attributes:
  type:
    name: type
    description: A property to provide the type of process relation.
    title: Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    abstract: true
    slot_uri: rdf:type
    alias: type
    owner: ProcessRelation
    range: RelationType

```
</details>