# Class: Subobject Publication
_A published work, e.g. proceedings or conferenc paper, that is the output of an academic event or series._







## Inheritance
* **Subobject Publication** [NamedThing]



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [DOI](has_doi.md) | [Digital Object Identifier](DigitalObjectId.md) | 0..* _recommended_ | A property to provide a digital object identifier (DOI) according to https://doi.org/.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Publication](has_publication.md) | range | Publication |
| [Event](Event.md) | [Publication](has_publication.md) | range | Publication |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Publication'] |
| native | ['confident:Publication'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Publication
description: A published work, e.g. proceedings or conferenc paper, that is the output
  of an academic event or series.
title: Subobject Publication
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
slots:
- has_doi

```
</details>

### Induced

<details>
```yaml
name: Publication
description: A published work, e.g. proceedings or conferenc paper, that is the output
  of an academic event or series.
title: Subobject Publication
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixins:
- NamedThing
attributes:
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) according
      to https://doi.org/.
    title: DOI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    exact_mappings:
    - datacite:doi
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: has_doi
    owner: Publication
    range: DigitalObjectId
    recommended: true
    inlined: true
    inlined_as_list: true
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: Publication
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: Publication
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: Publication
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>