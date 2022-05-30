# Class: Subobject Event Format
_An academic event format specification is a plan specification that classifies a planned gathering of people in an academic context according to some sociocultural format, which provides implicit and explicit details on how this gathering is to be carried out by its participants in terms of achieving certain objectives, fulfilling certain conditions and performing certain actions. It thus concretizes the expectations of the contributors of an academic event. While the explicit details are often provided as concrete parts (e.g. deadline or attendance fee specifications), the implicit details depend on the semantics encoded in the words used for the classification of academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications can overlap or vary to a certain degree._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Other Event Format](other_format.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 1..1 | A mandatory property to provide the format of an academic event as string, in order to further specify its type in case it could not be specified according to the possible values of [Event Type](EventType.md).  | 


## Usages












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['aeon:0000004'] |
| native | ['confident:EventFormatSpecification'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EventFormatSpecification
description: An academic event format specification is a plan specification that classifies
  a planned gathering of people in an academic context according to some sociocultural
  format, which provides implicit and explicit details on how this gathering is to
  be carried out by its participants in terms of achieving certain objectives, fulfilling
  certain conditions and performing certain actions. It thus concretizes the expectations
  of the contributors of an academic event. While the explicit details are often provided
  as concrete parts (e.g. deadline or attendance fee specifications), the implicit
  details depend on the semantics encoded in the words used for the classification
  of academic events (e.g. "conference" or "workshop"). Depending on the sociocultural
  background these classifications can overlap or vary to a certain degree.
title: Subobject Event Format
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
attributes:
  other_format:
    name: other_format
    description: A mandatory property to provide the format of an academic event as
      string, in order to further specify its type in case it could not be specified
      according to the possible values of [Event Type](EventType.md).
    title: Other Event Format
    examples:
    - value: ad-hoc meeting of university presidents
      description: An example to provide a format specification for special type of
        academic event that is not in the schema's [EventType](EventType) enum.
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: obi:0002815
    range: string
    required: true
class_uri: aeon:0000004

```
</details>

### Induced

<details>
```yaml
name: EventFormatSpecification
description: An academic event format specification is a plan specification that classifies
  a planned gathering of people in an academic context according to some sociocultural
  format, which provides implicit and explicit details on how this gathering is to
  be carried out by its participants in terms of achieving certain objectives, fulfilling
  certain conditions and performing certain actions. It thus concretizes the expectations
  of the contributors of an academic event. While the explicit details are often provided
  as concrete parts (e.g. deadline or attendance fee specifications), the implicit
  details depend on the semantics encoded in the words used for the classification
  of academic events (e.g. "conference" or "workshop"). Depending on the sociocultural
  background these classifications can overlap or vary to a certain degree.
title: Subobject Event Format
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
attributes:
  other_format:
    name: other_format
    description: A mandatory property to provide the format of an academic event as
      string, in order to further specify its type in case it could not be specified
      according to the possible values of [Event Type](EventType.md).
    title: Other Event Format
    examples:
    - value: ad-hoc meeting of university presidents
      description: An example to provide a format specification for special type of
        academic event that is not in the schema's [EventType](EventType) enum.
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: obi:0002815
    alias: other_format
    owner: EventFormatSpecification
    range: string
    required: true
class_uri: aeon:0000004

```
</details>