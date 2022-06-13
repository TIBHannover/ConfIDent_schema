# Class: Subobject Context
_A container to provide extra information, such as call of papers event description._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Context Description](text.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The free text used to provide more context information on an event or event series.  | 
| [Context License](license_str.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The license of the context information as text, which must be used when copying text from other sources.  | 
| [Context License URL](license_url.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The license of the context information as URL, which should be used when copying text from other sources and such a URL exists.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Context Information](context_info.md) | range | Context |
| [Event](Event.md) | [Context Information](context_info.md) | range | Context |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Context'] |
| native | ['confident:Context'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Context
description: A container to provide extra information, such as call of papers event
  description.
title: Subobject Context
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
attributes:
  text:
    name: text
    description: The free text used to provide more context information on an event
      or event series.
    title: Context Description
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: string
  license_str:
    name: license_str
    description: The license of the context information as text, which must be used
      when copying text from other sources.
    title: Context License
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: string
  license_url:
    name: license_url
    description: The license of the context information as URL, which should be used
      when copying text from other sources and such a URL exists.
    title: Context License URL
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: uriorcurie

```
</details>

### Induced

<details>
```yaml
name: Context
description: A container to provide extra information, such as call of papers event
  description.
title: Subobject Context
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
attributes:
  text:
    name: text
    description: The free text used to provide more context information on an event
      or event series.
    title: Context Description
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: text
    owner: Context
    range: string
  license_str:
    name: license_str
    description: The license of the context information as text, which must be used
      when copying text from other sources.
    title: Context License
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: license_str
    owner: Context
    range: string
  license_url:
    name: license_url
    description: The license of the context information as URL, which should be used
      when copying text from other sources and such a URL exists.
    title: Context License URL
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: license_url
    owner: Context
    range: uriorcurie

```
</details>