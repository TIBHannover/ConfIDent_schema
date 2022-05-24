# Class: External ID
_An identifer of an entity declared in another schema._







## Inheritance
* **External ID** [SchemaBasedThing]
    * [Digital Object Identifier](DigitalObjectId.md)
    * [Wikidata ID](WikidataId.md)
    * [GND ID](GndId.md)
    * [TIBKAT ID](TibkatId.md)
    * [DBLP ID](DblpId.md)
    * [WikiCFP Event ID](WikiCfpEventId.md)
    * [WikiCFP Series ID](WikiCfpSeriesId.md)



## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [Schema Value](schema_value.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the literal value of a schema based entity.  | 
| [Schema Name](schema_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | A property to provide the name of a schema.  | 
| [External formatter URI](schema_base_uri.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The base URI of the schema that provides the context for the schema based value.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Event](Event.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [City](City.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Country](Country.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Region](Region.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Venue](Venue.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Contributor](Contributor.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Sponsor](Sponsor.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Attendee](Attendee.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Moderator](Moderator.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Reviewer](Reviewer.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Organizer](Organizer.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Contact Person](ContactPerson.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Committee Member](CommitteeMember.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Committee Chair](CommitteeChair.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Presenter](Presenter.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Keynote Speaker](KeynoteSpeaker.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Publication](Publication.md) | [External ID](external_id.md) | range | ExternalIdentifier |
| [Subobject Named Thing](NamedThing.md) | [External ID](external_id.md) | range | ExternalIdentifier |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:ExternalIdentifier'] |
| native | ['confident:ExternalIdentifier'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExternalIdentifier
description: An identifer of an entity declared in another schema.
title: External ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixins:
- SchemaBasedThing
slot_usage:
  schema_value:
    name: schema_value
    slot_uri: obi:0002815

```
</details>

### Induced

<details>
```yaml
name: ExternalIdentifier
description: An identifer of an entity declared in another schema.
title: External ID
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
mixins:
- SchemaBasedThing
slot_usage:
  schema_value:
    name: schema_value
    slot_uri: obi:0002815
attributes:
  schema_value:
    name: schema_value
    description: A property to provide the literal value of a schema based entity.
    title: Schema Value
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: obi:0002815
    alias: schema_value
    owner: ExternalIdentifier
    range: string
  schema_name:
    name: schema_name
    description: A property to provide the name of a schema.
    title: Schema Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_name
    owner: ExternalIdentifier
    range: string
  schema_base_uri:
    name: schema_base_uri
    description: The base URI of the schema that provides the context for the schema
      based value.
    title: External formatter URI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: schema_base_uri
    owner: ExternalIdentifier
    range: uriorcurie

```
</details>