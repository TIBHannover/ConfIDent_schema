# Class: Subobject Metric
_A container for statistical information about an event or event series._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Type](type.md) | [Metric Type](MetricType.md) | 0..1 | A property to provide the type of relation between academic events.  | 
| [Metric Integer Value](int_value.md) | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | 0..1 | A property to provide an integer value for a metric.  | 
| [Metric String Value](str_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a string value for a metric.  | 
| [Metric Rate Value](rate_value.md) | [xsd:float](http://www.w3.org/2001/XMLSchema#float) | 0..1 | A property to provide a rate value as float for a metric.  | 
| [Metric Truth Value](truth_value.md) | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) | 0..1 | A property to provide a truth value for a metric.  | 
| [Metric Year](metric_year.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the year for which the metric value is valid.  | 
| [Metric Description](description.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a description of a metric.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Metric](has_metric.md) | range | Metric |
| [Event](Event.md) | [Metric](has_metric.md) | range | Metric |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Metric'] |
| native | ['confident:Metric'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Metric
description: A container for statistical information about an event or event series.
title: Subobject Metric
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
slots:
- type
slot_usage:
  type:
    name: type
    description: A property to provide the type of relation between academic events.
    range: MetricType
attributes:
  int_value:
    name: int_value
    description: A property to provide an integer value for a metric.
    title: Metric Integer Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: integer
  str_value:
    name: str_value
    description: A property to provide a string value for a metric.
    title: Metric String Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: string
  rate_value:
    name: rate_value
    description: A property to provide a rate value as float for a metric.
    title: Metric Rate Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: float
  truth_value:
    name: truth_value
    description: A property to provide a truth value for a metric.
    title: Metric Truth Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: boolean
  metric_year:
    name: metric_year
    description: A property to provide the year for which the metric value is valid.
    title: Metric Year
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: string
    pattern: ^\d{4}$
  description:
    name: description
    description: A property to provide a description of a metric.
    title: Metric Description
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    range: string

```
</details>

### Induced

<details>
```yaml
name: Metric
description: A container for statistical information about an event or event series.
title: Subobject Metric
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
slot_usage:
  type:
    name: type
    description: A property to provide the type of relation between academic events.
    range: MetricType
attributes:
  int_value:
    name: int_value
    description: A property to provide an integer value for a metric.
    title: Metric Integer Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: int_value
    owner: Metric
    range: integer
  str_value:
    name: str_value
    description: A property to provide a string value for a metric.
    title: Metric String Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: str_value
    owner: Metric
    range: string
  rate_value:
    name: rate_value
    description: A property to provide a rate value as float for a metric.
    title: Metric Rate Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: rate_value
    owner: Metric
    range: float
  truth_value:
    name: truth_value
    description: A property to provide a truth value for a metric.
    title: Metric Truth Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: truth_value
    owner: Metric
    range: boolean
  metric_year:
    name: metric_year
    description: A property to provide the year for which the metric value is valid.
    title: Metric Year
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: metric_year
    owner: Metric
    range: string
    pattern: ^\d{4}$
  description:
    name: description
    description: A property to provide a description of a metric.
    title: Metric Description
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: description
    owner: Metric
    range: string
  type:
    name: type
    description: A property to provide the type of relation between academic events.
    title: Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    abstract: true
    alias: type
    owner: Metric
    range: MetricType

```
</details>