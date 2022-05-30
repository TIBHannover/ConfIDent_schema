# Class: Subobject Keynote Speaker
_A 'keynote speaker' is a presenter that is an invited person - often a multiplier in his or her (research) field - responsible for delivering a keynote speech._







## Inheritance
* [Subobject Contributor](Contributor.md) [ NamedThing]
    * [Subobject Presenter](Presenter.md)
        * **Subobject Keynote Speaker**



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Type](type.md) | [Contributor Type](ContributorType.md) | 0..1 | An abstract property that is reused in certain classes to differentiate their instances according to the type enums defined as the range.  | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide an internal id of a schema entity in the ConfIDent plattform.  | 
| [Name](name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide a name of a schema entity.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | A property to provide an external id of a schema entity.  | 


## Usages












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:KeynoteSpeaker'] |
| native | ['confident:KeynoteSpeaker'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KeynoteSpeaker
description: A 'keynote speaker' is a presenter that is an invited person - often
  a multiplier in his or her (research) field - responsible for delivering a keynote
  speech.
title: Subobject Keynote Speaker
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: Presenter

```
</details>

### Induced

<details>
```yaml
name: KeynoteSpeaker
description: A 'keynote speaker' is a presenter that is an invited person - often
  a multiplier in his or her (research) field - responsible for delivering a keynote
  speech.
title: Subobject Keynote Speaker
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
is_a: Presenter
attributes:
  type:
    name: type
    description: An abstract property that is reused in certain classes to differentiate
      their instances according to the type enums defined as the range.
    title: Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    abstract: true
    slot_uri: rdf:type
    designates_type: true
    alias: type
    owner: KeynoteSpeaker
    range: ContributorType
  id:
    name: id
    description: A property to provide an internal id of a schema entity in the ConfIDent
      plattform.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    identifier: true
    alias: id
    owner: KeynoteSpeaker
    range: uriorcurie
    required: true
  name:
    name: name
    description: A property to provide a name of a schema entity.
    title: Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: sdo:name
    alias: name
    owner: KeynoteSpeaker
    range: string
  external_id:
    name: external_id
    description: A property to provide an external id of a schema entity.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: KeynoteSpeaker
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true

```
</details>