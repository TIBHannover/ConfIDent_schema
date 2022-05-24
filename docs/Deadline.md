# Class: Subobject Deadline
_A container for event deadlines._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Deadline Type](type.md) | [Deadline Type](DeadlineType.md) | 1..1 | A propery to provide the type of the deadline.  | 
| [Deadline Date](deadline_date.md) | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | 1..1 | The date of a deadline.  | 
| [Other Deadline Type](deadline_other.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to specify another type of deadline, if this type of deadline is not within the allowed values of [DeadlineType](DeadlineType.md).  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [Deadline](has_deadline.md) | range | Deadline |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Deadline'] |
| native | ['confident:Deadline'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Deadline
description: A container for event deadlines.
title: Subobject Deadline
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
slots:
- type
slot_usage:
  type:
    name: type
    description: A propery to provide the type of the deadline.
    title: Deadline Type
    range: DeadlineType
    required: true
attributes:
  deadline_date:
    name: deadline_date
    description: The date of a deadline.
    title: Deadline Date
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: datetime
    required: true
  deadline_other:
    name: deadline_other
    description: A property to specify another type of deadline, if this type of deadline
      is not within the allowed values of [DeadlineType](DeadlineType.md).
    title: Other Deadline Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: string

```
</details>

### Induced

<details>
```yaml
name: Deadline
description: A container for event deadlines.
title: Subobject Deadline
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
slot_usage:
  type:
    name: type
    description: A propery to provide the type of the deadline.
    title: Deadline Type
    range: DeadlineType
    required: true
attributes:
  deadline_date:
    name: deadline_date
    description: The date of a deadline.
    title: Deadline Date
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: deadline_date
    owner: Deadline
    range: datetime
    required: true
  deadline_other:
    name: deadline_other
    description: A property to specify another type of deadline, if this type of deadline
      is not within the allowed values of [DeadlineType](DeadlineType.md).
    title: Other Deadline Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: deadline_other
    owner: Deadline
    range: string
  type:
    name: type
    description: A propery to provide the type of the deadline.
    title: Deadline Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    abstract: true
    alias: type
    owner: Deadline
    range: DeadlineType
    required: true

```
</details>