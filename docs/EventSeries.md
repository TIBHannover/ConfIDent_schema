# Class: Event Series
_An academic event series describes the set of academic events which take place on a regular basis and thus have an established common identity. This identity is constituted, for example, through institutional continuity in the hosting of a series (e.g. by a specialised society), thematic focuses and/or a common label under which a series is defined (particularly name and acronym). Nevertheless, it is possible that each of these criteria may change over time._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide the internal identifier of an academic event series.  | 
| [Official Name](official_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 1..1 | A property to provide the the official name of an academic event series.  | 
| [Organizer](organized_by.md) | [Subobject Organizer](Organizer.md) | 1..* | A property to provide the organizer of an academic event series.  | 
| [Acronym](has_acronym.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 _recommended_ | The official acronym of an academic event series.  | 
| [Academic Field](academic_field.md) | [Subobject Academic Field](AcademicField.md) | 0..* _recommended_ | A property to describe the scientific subject(s) associated with an academic event series, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [Schema Value](schema_value.md) and [Schema Name](schema_name.md) are mandatory.  | 
| [Landing Page](landing_page.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 _recommended_ | A property to provide the website to which the DOI an academic event series is resolving to.  | 
| [Publication](has_publication.md) | [Subobject Publication](Publication.md) | 0..* _recommended_ | A property to provide the publication associated with  | 
| [Sponsor](sponsored_by.md) | [Subobject Sponsor](Sponsor.md) | 0..* _recommended_ | A property to provide the sponsors of an academic event series.  | 
| [Official Website](website.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 _recommended_ | A property to provide the URL the official website of an academic event series.  | 
| [DOI](has_doi.md) | [Digital Object Identifier](DigitalObjectId.md) | 0..* _recommended_ | A property to provide a digital object identifier (DOI) for an event series. This is set automatically.  | 
| [Umbrella Of](umbrella_of.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 _recommended_ | A relation to be used to link a series that hosts several series to its subordinate parts.  | 
| [Has Umbrella](has_umbrella.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 _recommended_ | A relation to be used to link a series to its hosting superordinate series.  | 
| [Colocated With](colocated_with.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* _recommended_ | A relation to be used to link a series to one or more other series that share the same location but not the same schedule and that are open to all attendees.  | 
| [Joint Venture With](joint_venture_with.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* _recommended_ | A relation to be used to link a series to one or more other series that share the same location, have a joint schedule and that are open to all attendees.  | 
| [Series Of](series_of.md) | [Event](Event.md) | 0..1 _recommended_ | A property to link to the events that are part of an academic event series.  | 
| [Alternative Name](alternative_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | A property to provide alternative names of an academic event series.  | 
| [Former Name](former_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | The former official name of an academic event series. Usually this will only be needed in case an academic event series has undergone a name change.  | 
| [Translated Name](translated_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | A translation of the official name of an event series to be used in different language contexts.  | 
| [Context Information](context_info.md) | [Subobject Context](Context.md) | 0..1 | A property to provide extra information for an academic event series.  | 
| [Metric](has_metric.md) | [Subobject Metric](Metric.md) | 0..* | A property to provide one ore more metrics of an academic event series.  | 
| [Topic](has_topic.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | A property to provide the theme and topics of an event series as free keywords, phrases or text.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | The property to provide external identifiers for an academic event series, including their identifier scheme.  | 
| [Wikidata ID](wikidata_id.md) | [Wikidata ID](WikidataId.md) | 0..* | A property to link an academic event series with its Wikidata identifier.  | 
| [DBLP ID](dpbl_id.md) | [DBLP ID](DblpId.md) | 0..* | A property to link an academic event series with its DBLP identifier.  | 
| [GND ID](gnd_id.md) | [GND ID](GndId.md) | 0..* | A property to link an academic event series with its GND identifier.  | 
| [WikiCFP Series ID](wikicfp_series_id.md) | [WikiCFP Series ID](WikiCfpSeriesId.md) | 0..* | A property to link an academic event series with its WikiCFP identifier.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [In Series](in_series.md) | range | EventSeries |
| [ConfIDent Records](ConfIDentRecords.md) | [Series](series.md) | range | EventSeries |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['aeon:0000002'] |
| native | ['confident:EventSeries'] |
| close | ['sdo:EventSeries'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EventSeries
description: An academic event series describes the set of academic events which take
  place on a regular basis and thus have an established common identity. This identity
  is constituted, for example, through institutional continuity in the hosting of
  a series (e.g. by a specialised society), thematic focuses and/or a common label
  under which a series is defined (particularly name and acronym). Nevertheless, it
  is possible that each of these criteria may change over time.
title: Event Series
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
close_mappings:
- sdo:EventSeries
slots:
- id
- official_name
- organized_by
- has_acronym
- academic_field
- landing_page
- has_publication
- sponsored_by
- website
- has_doi
- umbrella_of
- has_umbrella
- colocated_with
- joint_venture_with
- series_of
- alternative_name
- former_name
- translated_name
- context_info
- has_metric
- has_topic
- external_id
- wikidata_id
- dpbl_id
- gnd_id
- wikicfp_series_id
slot_usage:
  id:
    name: id
    description: A property to provide the internal identifier of an academic event
      series.
    ifabsent: string(confident:SeriesID)
  official_name:
    name: official_name
    description: A property to provide the the official name of an academic event
      series.
  organized_by:
    name: organized_by
    description: A property to provide the organizer of an academic event series.
  has_acronym:
    name: has_acronym
    description: The official acronym of an academic event series.
  landing_page:
    name: landing_page
    description: A property to provide the website to which the DOI an academic event
      series is resolving to.
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) for an event
      series. This is set automatically.
  academic_field:
    name: academic_field
    description: A property to describe the scientific subject(s) associated with
      an academic event series, according to some controlled vocabulary or thesaurus.
      If this is used, its subproperties [Schema Value](schema_value.md) and [Schema
      Name](schema_name.md) are mandatory.
  website:
    name: website
    description: A property to provide the URL the official website of an academic
      event series.
  sponsored_by:
    name: sponsored_by
    description: A property to provide the sponsors of an academic event series.
  has_publication:
    name: has_publication
    description: A property to provide the publication associated with
    comments:
    - It will be most common that the publications of an academic event series are
      the set of publications associated with the individual events of the series.
  umbrella_of:
    name: umbrella_of
    description: A relation to be used to link a series that hosts several series
      to its subordinate parts.
    title: Umbrella Of
  has_umbrella:
    name: has_umbrella
    description: A relation to be used to link a series to its hosting superordinate
      series.
    title: Has Umbrella
  colocated_with:
    name: colocated_with
    description: A relation to be used to link a series to one or more other series
      that share the same location but not the same schedule and that are open to
      all attendees.
    title: Colocated With
  joint_venture_with:
    name: joint_venture_with
    description: A relation to be used to link a series to one or more other series
      that share the same location, have a joint schedule and that are open to all
      attendees.
    title: Joint Venture With
  alternative_name:
    name: alternative_name
    description: A property to provide alternative names of an academic event series.
  former_name:
    name: former_name
    description: The former official name of an academic event series. Usually this
      will only be needed in case an academic event series has undergone a name change.
  translated_name:
    name: translated_name
    description: A translation of the official name of an event series to be used
      in different language contexts.
  has_topic:
    name: has_topic
    description: A property to provide the theme and topics of an event series as
      free keywords, phrases or text.
    comments:
    - Most likely the values of this property will be the set of topics and free keywords
      aggregated from the academic events of the series.
  has_metric:
    name: has_metric
    description: A property to provide one ore more metrics of an academic event series.
  context_info:
    name: context_info
    description: A property to provide extra information for an academic event series.
  external_id:
    name: external_id
    description: The property to provide external identifiers for an academic event
      series, including their identifier scheme.
  wikidata_id:
    name: wikidata_id
    description: A property to link an academic event series with its Wikidata identifier.
  gnd_id:
    name: gnd_id
    description: A property to link an academic event series with its GND identifier.
  dpbl_id:
    name: dpbl_id
    description: A property to link an academic event series with its DBLP identifier.
  wikicfp_series_id:
    name: wikicfp_series_id
    description: A property to link an academic event series with its WikiCFP identifier.
class_uri: aeon:0000002

```
</details>

### Induced

<details>
```yaml
name: EventSeries
description: An academic event series describes the set of academic events which take
  place on a regular basis and thus have an established common identity. This identity
  is constituted, for example, through institutional continuity in the hosting of
  a series (e.g. by a specialised society), thematic focuses and/or a common label
  under which a series is defined (particularly name and acronym). Nevertheless, it
  is possible that each of these criteria may change over time.
title: Event Series
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
close_mappings:
- sdo:EventSeries
slot_usage:
  id:
    name: id
    description: A property to provide the internal identifier of an academic event
      series.
    ifabsent: string(confident:SeriesID)
  official_name:
    name: official_name
    description: A property to provide the the official name of an academic event
      series.
  organized_by:
    name: organized_by
    description: A property to provide the organizer of an academic event series.
  has_acronym:
    name: has_acronym
    description: The official acronym of an academic event series.
  landing_page:
    name: landing_page
    description: A property to provide the website to which the DOI an academic event
      series is resolving to.
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) for an event
      series. This is set automatically.
  academic_field:
    name: academic_field
    description: A property to describe the scientific subject(s) associated with
      an academic event series, according to some controlled vocabulary or thesaurus.
      If this is used, its subproperties [Schema Value](schema_value.md) and [Schema
      Name](schema_name.md) are mandatory.
  website:
    name: website
    description: A property to provide the URL the official website of an academic
      event series.
  sponsored_by:
    name: sponsored_by
    description: A property to provide the sponsors of an academic event series.
  has_publication:
    name: has_publication
    description: A property to provide the publication associated with
    comments:
    - It will be most common that the publications of an academic event series are
      the set of publications associated with the individual events of the series.
  umbrella_of:
    name: umbrella_of
    description: A relation to be used to link a series that hosts several series
      to its subordinate parts.
    title: Umbrella Of
  has_umbrella:
    name: has_umbrella
    description: A relation to be used to link a series to its hosting superordinate
      series.
    title: Has Umbrella
  colocated_with:
    name: colocated_with
    description: A relation to be used to link a series to one or more other series
      that share the same location but not the same schedule and that are open to
      all attendees.
    title: Colocated With
  joint_venture_with:
    name: joint_venture_with
    description: A relation to be used to link a series to one or more other series
      that share the same location, have a joint schedule and that are open to all
      attendees.
    title: Joint Venture With
  alternative_name:
    name: alternative_name
    description: A property to provide alternative names of an academic event series.
  former_name:
    name: former_name
    description: The former official name of an academic event series. Usually this
      will only be needed in case an academic event series has undergone a name change.
  translated_name:
    name: translated_name
    description: A translation of the official name of an event series to be used
      in different language contexts.
  has_topic:
    name: has_topic
    description: A property to provide the theme and topics of an event series as
      free keywords, phrases or text.
    comments:
    - Most likely the values of this property will be the set of topics and free keywords
      aggregated from the academic events of the series.
  has_metric:
    name: has_metric
    description: A property to provide one ore more metrics of an academic event series.
  context_info:
    name: context_info
    description: A property to provide extra information for an academic event series.
  external_id:
    name: external_id
    description: The property to provide external identifiers for an academic event
      series, including their identifier scheme.
  wikidata_id:
    name: wikidata_id
    description: A property to link an academic event series with its Wikidata identifier.
  gnd_id:
    name: gnd_id
    description: A property to link an academic event series with its GND identifier.
  dpbl_id:
    name: dpbl_id
    description: A property to link an academic event series with its DBLP identifier.
  wikicfp_series_id:
    name: wikicfp_series_id
    description: A property to link an academic event series with its WikiCFP identifier.
attributes:
  id:
    name: id
    description: A property to provide the internal identifier of an academic event
      series.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(confident:SeriesID)
    identifier: true
    alias: id
    owner: EventSeries
    range: uriorcurie
    required: true
  official_name:
    name: official_name
    description: A property to provide the the official name of an academic event
      series.
    title: Official Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: name
    slot_uri: skos:perfLabel
    alias: official_name
    owner: EventSeries
    range: string
    required: true
  organized_by:
    name: organized_by
    description: A property to provide the organizer of an academic event series.
    title: Organizer
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: organized_by
    owner: EventSeries
    range: Organizer
    required: true
    inlined_as_list: true
  has_acronym:
    name: has_acronym
    description: The official acronym of an academic event series.
    title: Acronym
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: name
    alias: has_acronym
    owner: EventSeries
    range: string
    required: false
    recommended: true
  academic_field:
    name: academic_field
    description: A property to describe the scientific subject(s) associated with
      an academic event series, according to some controlled vocabulary or thesaurus.
      If this is used, its subproperties [Schema Value](schema_value.md) and [Schema
      Name](schema_name.md) are mandatory.
    title: Academic Field
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: aeon:0000040
    multivalued: true
    alias: academic_field
    owner: EventSeries
    range: AcademicField
    required: false
    recommended: true
    inlined_as_list: true
  landing_page:
    name: landing_page
    description: A property to provide the website to which the DOI an academic event
      series is resolving to.
    title: Landing Page
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: landing_page
    owner: EventSeries
    range: uri
    required: false
    recommended: true
  has_publication:
    name: has_publication
    description: A property to provide the publication associated with
    title: Publication
    comments:
    - It will be most common that the publications of an academic event series are
      the set of publications associated with the individual events of the series.
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_publication
    owner: EventSeries
    range: Publication
    required: false
    recommended: true
    inlined_as_list: true
  sponsored_by:
    name: sponsored_by
    description: A property to provide the sponsors of an academic event series.
    title: Sponsor
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: sponsored_by
    owner: EventSeries
    range: Sponsor
    required: false
    recommended: true
    inlined_as_list: true
  website:
    name: website
    description: A property to provide the URL the official website of an academic
      event series.
    title: Official Website
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: website
    owner: EventSeries
    range: uri
    recommended: true
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) for an event
      series. This is set automatically.
    title: DOI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: IAO:0000235
    multivalued: true
    alias: has_doi
    owner: EventSeries
    range: DigitalObjectId
    recommended: true
    inlined_as_list: true
  umbrella_of:
    name: umbrella_of
    description: A relation to be used to link a series that hosts several series
      to its subordinate parts.
    title: Umbrella Of
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: umbrella_of
    owner: EventSeries
    range: string
    required: false
    recommended: true
  has_umbrella:
    name: has_umbrella
    description: A relation to be used to link a series to its hosting superordinate
      series.
    title: Has Umbrella
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: has_umbrella
    owner: EventSeries
    range: string
    required: false
    recommended: true
  colocated_with:
    name: colocated_with
    description: A relation to be used to link a series to one or more other series
      that share the same location but not the same schedule and that are open to
      all attendees.
    title: Colocated With
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: colocated_with
    owner: EventSeries
    range: string
    required: false
    recommended: true
    inlined_as_list: true
  joint_venture_with:
    name: joint_venture_with
    description: A relation to be used to link a series to one or more other series
      that share the same location, have a joint schedule and that are open to all
      attendees.
    title: Joint Venture With
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: joint_venture_with
    owner: EventSeries
    range: string
    required: false
    recommended: true
    inlined_as_list: true
  series_of:
    name: series_of
    description: A property to link to the events that are part of an academic event
      series.
    title: Series Of
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: series_of
    owner: EventSeries
    range: Event
    required: false
    recommended: true
  alternative_name:
    name: alternative_name
    description: A property to provide alternative names of an academic event series.
    title: Alternative Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: name
    slot_uri: skos:altLabel
    multivalued: true
    alias: alternative_name
    owner: EventSeries
    range: string
    required: false
    recommended: false
    inlined_as_list: true
  former_name:
    name: former_name
    description: The former official name of an academic event series. Usually this
      will only be needed in case an academic event series has undergone a name change.
    title: Former Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: name
    multivalued: true
    alias: former_name
    owner: EventSeries
    range: string
    required: false
    recommended: false
    inlined_as_list: true
  translated_name:
    name: translated_name
    description: A translation of the official name of an event series to be used
      in different language contexts.
    title: Translated Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: name
    multivalued: true
    alias: translated_name
    owner: EventSeries
    range: string
    required: false
    recommended: false
    inlined_as_list: true
  context_info:
    name: context_info
    description: A property to provide extra information for an academic event series.
    title: Context Information
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: context_info
    owner: EventSeries
    range: Context
    required: false
    recommended: false
  has_metric:
    name: has_metric
    description: A property to provide one ore more metrics of an academic event series.
    title: Metric
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_metric
    owner: EventSeries
    range: Metric
    required: false
    recommended: false
    inlined_as_list: true
  has_topic:
    name: has_topic
    description: A property to provide the theme and topics of an event series as
      free keywords, phrases or text.
    title: Topic
    comments:
    - Most likely the values of this property will be the set of topics and free keywords
      aggregated from the academic events of the series.
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_topic
    owner: EventSeries
    range: string
    required: false
    recommended: false
    inlined_as_list: true
  external_id:
    name: external_id
    description: The property to provide external identifiers for an academic event
      series, including their identifier scheme.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    slot_uri: IAO:0000235
    multivalued: true
    alias: external_id
    owner: EventSeries
    range: ExternalIdentifier
    inlined_as_list: true
  wikidata_id:
    name: wikidata_id
    description: A property to link an academic event series with its Wikidata identifier.
    title: Wikidata ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: IAO:0000235
    multivalued: true
    alias: wikidata_id
    owner: EventSeries
    range: WikidataId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  dpbl_id:
    name: dpbl_id
    description: A property to link an academic event series with its DBLP identifier.
    title: DBLP ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: IAO:0000235
    multivalued: true
    alias: dpbl_id
    owner: EventSeries
    range: DblpId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  gnd_id:
    name: gnd_id
    description: A property to link an academic event series with its GND identifier.
    title: GND ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: IAO:0000235
    multivalued: true
    alias: gnd_id
    owner: EventSeries
    range: GndId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  wikicfp_series_id:
    name: wikicfp_series_id
    description: A property to link an academic event series with its WikiCFP identifier.
    title: WikiCFP Series ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: IAO:0000235
    multivalued: true
    alias: wikicfp_series_id
    owner: EventSeries
    range: WikiCfpSeriesId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
class_uri: aeon:0000002

```
</details>