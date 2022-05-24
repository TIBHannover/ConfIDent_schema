# Class: ConfIDent Records
_A container to be able to bundle academic event data and series in one data file (e.g. YAML or JSON)._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Events](events.md) | [Event](Event.md) | 0..* | A property to provide a list of academic events within this container.  | 
| [Series](series.md) | [Event Series](EventSeries.md) | 0..* | A property to provide a list of academic event series within this container.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ConfIDent Records](ConfIDentRecords.md) | [Events](events.md) | domain | ConfIDentRecords |
| [ConfIDent Records](ConfIDentRecords.md) | [Series](series.md) | domain | ConfIDentRecords |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:ConfIDentRecords'] |
| native | ['confident:ConfIDentRecords'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConfIDentRecords
description: A container to be able to bundle academic event data and series in one
  data file (e.g. YAML or JSON).
title: ConfIDent Records
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
attributes:
  events:
    name: events
    description: A property to provide a list of academic events within this container.
    title: Events
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    domain: ConfIDentRecords
    multivalued: true
    range: Event
    inlined: true
    inlined_as_list: true
  series:
    name: series
    description: A property to provide a list of academic event series within this
      container.
    title: Series
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    domain: ConfIDentRecords
    multivalued: true
    range: EventSeries
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: ConfIDentRecords
description: A container to be able to bundle academic event data and series in one
  data file (e.g. YAML or JSON).
title: ConfIDent Records
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
attributes:
  events:
    name: events
    description: A property to provide a list of academic events within this container.
    title: Events
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    domain: ConfIDentRecords
    multivalued: true
    alias: events
    owner: ConfIDentRecords
    range: Event
    inlined: true
    inlined_as_list: true
  series:
    name: series
    description: A property to provide a list of academic event series within this
      container.
    title: Series
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    domain: ConfIDentRecords
    multivalued: true
    alias: series
    owner: ConfIDentRecords
    range: EventSeries
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>