# Class: Event
_An academic event is part of the established instruments of science communication as a format for conveying the latest scientific publications. It is defined by the meeting of researchers at a specific time and place (virtual or physical) and with a specific thematic focus to present, hear and discuss these publications. In contrast to other forms of events, academic events should primarily serve the exchange of results and methods of scientific research and their didactic mediation.  Furthermore, a significant participation of scientific organizations in the realization of an academic event is constitutive for this type of event; for example, to distinguish it from events in which researchers mainly act as external experts or with a purely legitimising function._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [ID](id.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 1..1 | A property to provide the internal identifier of an academic event.  | 
| [Official Name](official_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 1..1 | A property to provide the the official name of an academic event.  | 
| [Organizer](organized_by.md) | [Subobject Organizer](Organizer.md) | 1..* | A property to provide the organizer of an academic event.  | 
| [Start Date](start_date.md) | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | 1..1 | The start date of an academic event or event series. Wheres the latter will in reality most likely be the start date of the first event of this series, unless there is some other source from which it is possible to derive the date of the inception of the series.  | 
| [End Date](end_date.md) | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | 1..1 | Similar to start_date but only for the end of an academic event or event series.  | 
| [Event Status](event_status.md) | [Event Status](EventStatus.md) | 1..1 | A property to provide the status of an event from a controlled list (e.g. as scheduled (default), postpooned, canceld etc).  | 
| [Acronym](has_acronym.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 _recommended_ | The official acronym of an academic event.  | 
| [Academic Field](academic_field.md) | [Subobject Academic Field](AcademicField.md) | 0..* _recommended_ | A property to describe the scientific subject(s) associated with an academic event, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [schema_value](schema_value.md) and [schema_name](schema_name.md) are mandatory.  | 
| [Landing Page](landing_page.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 _recommended_ | A property to provide the website to which the DOI an academic event is resolving to.  | 
| [Publication](has_publication.md) | [Subobject Publication](Publication.md) | 0..* _recommended_ | A property to provide the publication associated with  | 
| [Sponsor](sponsored_by.md) | [Subobject Sponsor](Sponsor.md) | 0..* _recommended_ | A property to provide the sponsors of an academic event.  | 
| [Official Website](website.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 _recommended_ | A property to provide the URL the official website of an academic event.  | 
| [DOI](has_doi.md) | [Digital Object Identifier](DigitalObjectId.md) | 0..* _recommended_ | A property to provide a digital object identifier (DOI) for an event. This is set automatically.  | 
| [Event Type](type.md) | [Event Type](EventType.md) | 0..1 _recommended_ | A property to provide the format of an academic event according to the possible values of the [Event Type](EventType.md) enum.  | 
| [Location](at_location.md) | [Subobject Location](Location.md) | 0..1 _recommended_ | The location of the academic event.  | 
| [In Series](in_series.md) | [Event Series](EventSeries.md) | 0..1 _recommended_ | The relation used to provide the series of which an Event is a part.  | 
| [Deadline](has_deadline.md) | [Subobject Deadline](Deadline.md) | 0..* _recommended_ | A property to provide a deadline of an academic event.  | 
| [Related To](related_to.md) | [Subobject Process Relation](ProcessRelation.md) | 0..* _recommended_ | A property to be used to link events to each other.  | 
| [Alternative Name](alternative_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | A property to provide alternative names of an academic event.  | 
| [Former Name](former_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..1 | The former official name of an academic event. Usually this will only be needed in case an academic event has undergone a name change.  | 
| [Translated Name](translated_name.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | A translation of the official name of an event to be used in different language contexts.  | 
| [Context Information](context_info.md) | [Subobject Context](Context.md) | 0..1 | A property to provide extra information for an academic event.  | 
| [Metric](has_metric.md) | [Subobject Metric](Metric.md) | 0..* | A property to provide one ore more metrics of an academic event.  | 
| [Topic](has_topic.md) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | 0..* | A property to provide the theme and topics of an event as free keywords, phrases or text.  | 
| [External ID](external_id.md) | [External ID](ExternalIdentifier.md) | 0..* | The property to provide external identifiers for an academic event, including their identifier scheme.  | 
| [Wikidata ID](wikidata_id.md) | [Wikidata ID](WikidataId.md) | 0..* | A property to link an academic event with its Wikidata identifier.  | 
| [DBLP ID](dpbl_id.md) | [DBLP ID](DblpId.md) | 0..* | A property to link an academic event with its DBLP identifier.  | 
| [GND ID](gnd_id.md) | [GND ID](GndId.md) | 0..* | A property to link an academic event with its GND identifier.  | 
| [WikiCFP Event ID](wikicfp_event_id.md) | [WikiCFP Event ID](WikiCfpEventId.md) | 0..* | A property to link an academic event with its WikiCFP identifier.  | 
| [TIBKAT ID](tibkat_id.md) | [TIBKAT ID](TibkatId.md) | 0..* | A property to link an academic event with its TIBKAT identifier.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event Series](EventSeries.md) | [Series Of](series_of.md) | range | Event |
| [ConfIDent Records](ConfIDentRecords.md) | [Events](events.md) | range | Event |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['aeon:0000001'] |
| native | ['confident:Event'] |
| close | ['sdo:Event'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Event
description: An academic event is part of the established instruments of science communication
  as a format for conveying the latest scientific publications. It is defined by the
  meeting of researchers at a specific time and place (virtual or physical) and with
  a specific thematic focus to present, hear and discuss these publications. In contrast
  to other forms of events, academic events should primarily serve the exchange of
  results and methods of scientific research and their didactic mediation.  Furthermore,
  a significant participation of scientific organizations in the realization of an
  academic event is constitutive for this type of event; for example, to distinguish
  it from events in which researchers mainly act as external experts or with a purely
  legitimising function.
title: Event
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
close_mappings:
- sdo:Event
slots:
- id
- official_name
- organized_by
- start_date
- end_date
- event_status
- has_acronym
- academic_field
- landing_page
- has_publication
- sponsored_by
- website
- has_doi
- type
- at_location
- in_series
- has_deadline
- related_to
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
- wikicfp_event_id
- tibkat_id
slot_usage:
  id:
    name: id
    description: A property to provide the internal identifier of an academic event.
    ifabsent: string(confident:EventID)
  official_name:
    name: official_name
    description: A property to provide the the official name of an academic event.
  organized_by:
    name: organized_by
    description: A property to provide the organizer of an academic event.
  has_acronym:
    name: has_acronym
    description: The official acronym of an academic event.
  landing_page:
    name: landing_page
    description: A property to provide the website to which the DOI an academic event
      is resolving to.
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) for an event.
      This is set automatically.
  academic_field:
    name: academic_field
    description: A property to describe the scientific subject(s) associated with
      an academic event, according to some controlled vocabulary or thesaurus. If
      this is used, its subproperties [schema_value](schema_value.md) and [schema_name](schema_name.md)
      are mandatory.
  website:
    name: website
    description: A property to provide the URL the official website of an academic
      event.
  sponsored_by:
    name: sponsored_by
    description: A property to provide the sponsors of an academic event.
  has_publication:
    name: has_publication
    description: A property to provide the publication associated with
    comments:
    - It will be most common that the publications of an academic event series are
      the set of publications associated with the individual events of the series.
  type:
    name: type
    description: A property to provide the format of an academic event according to
      the possible values of the [Event Type](EventType.md) enum.
    title: Event Type
    designates_type: true
    range: EventType
    recommended: true
  alternative_name:
    name: alternative_name
    description: A property to provide alternative names of an academic event.
  former_name:
    name: former_name
    description: The former official name of an academic event. Usually this will
      only be needed in case an academic event has undergone a name change.
  translated_name:
    name: translated_name
    description: A translation of the official name of an event to be used in different
      language contexts.
  has_topic:
    name: has_topic
    description: A property to provide the theme and topics of an event as free keywords,
      phrases or text.
  has_metric:
    name: has_metric
    description: A property to provide one ore more metrics of an academic event.
  context_info:
    name: context_info
    description: A property to provide extra information for an academic event.
  external_id:
    name: external_id
    description: The property to provide external identifiers for an academic event,
      including their identifier scheme.
  wikidata_id:
    name: wikidata_id
    description: A property to link an academic event with its Wikidata identifier.
  gnd_id:
    name: gnd_id
    description: A property to link an academic event with its GND identifier.
  dpbl_id:
    name: dpbl_id
    description: A property to link an academic event with its DBLP identifier.
  wikicfp_event_id:
    name: wikicfp_event_id
    description: A property to link an academic event with its WikiCFP identifier.
  tibkat_id:
    name: tibkat_id
    description: A property to link an academic event with its TIBKAT identifier.
class_uri: aeon:0000001

```
</details>

### Induced

<details>
```yaml
name: Event
description: An academic event is part of the established instruments of science communication
  as a format for conveying the latest scientific publications. It is defined by the
  meeting of researchers at a specific time and place (virtual or physical) and with
  a specific thematic focus to present, hear and discuss these publications. In contrast
  to other forms of events, academic events should primarily serve the exchange of
  results and methods of scientific research and their didactic mediation.  Furthermore,
  a significant participation of scientific organizations in the realization of an
  academic event is constitutive for this type of event; for example, to distinguish
  it from events in which researchers mainly act as external experts or with a purely
  legitimising function.
title: Event
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
close_mappings:
- sdo:Event
slot_usage:
  id:
    name: id
    description: A property to provide the internal identifier of an academic event.
    ifabsent: string(confident:EventID)
  official_name:
    name: official_name
    description: A property to provide the the official name of an academic event.
  organized_by:
    name: organized_by
    description: A property to provide the organizer of an academic event.
  has_acronym:
    name: has_acronym
    description: The official acronym of an academic event.
  landing_page:
    name: landing_page
    description: A property to provide the website to which the DOI an academic event
      is resolving to.
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) for an event.
      This is set automatically.
  academic_field:
    name: academic_field
    description: A property to describe the scientific subject(s) associated with
      an academic event, according to some controlled vocabulary or thesaurus. If
      this is used, its subproperties [schema_value](schema_value.md) and [schema_name](schema_name.md)
      are mandatory.
  website:
    name: website
    description: A property to provide the URL the official website of an academic
      event.
  sponsored_by:
    name: sponsored_by
    description: A property to provide the sponsors of an academic event.
  has_publication:
    name: has_publication
    description: A property to provide the publication associated with
    comments:
    - It will be most common that the publications of an academic event series are
      the set of publications associated with the individual events of the series.
  type:
    name: type
    description: A property to provide the format of an academic event according to
      the possible values of the [Event Type](EventType.md) enum.
    title: Event Type
    designates_type: true
    range: EventType
    recommended: true
  alternative_name:
    name: alternative_name
    description: A property to provide alternative names of an academic event.
  former_name:
    name: former_name
    description: The former official name of an academic event. Usually this will
      only be needed in case an academic event has undergone a name change.
  translated_name:
    name: translated_name
    description: A translation of the official name of an event to be used in different
      language contexts.
  has_topic:
    name: has_topic
    description: A property to provide the theme and topics of an event as free keywords,
      phrases or text.
  has_metric:
    name: has_metric
    description: A property to provide one ore more metrics of an academic event.
  context_info:
    name: context_info
    description: A property to provide extra information for an academic event.
  external_id:
    name: external_id
    description: The property to provide external identifiers for an academic event,
      including their identifier scheme.
  wikidata_id:
    name: wikidata_id
    description: A property to link an academic event with its Wikidata identifier.
  gnd_id:
    name: gnd_id
    description: A property to link an academic event with its GND identifier.
  dpbl_id:
    name: dpbl_id
    description: A property to link an academic event with its DBLP identifier.
  wikicfp_event_id:
    name: wikicfp_event_id
    description: A property to link an academic event with its WikiCFP identifier.
  tibkat_id:
    name: tibkat_id
    description: A property to link an academic event with its TIBKAT identifier.
attributes:
  id:
    name: id
    description: A property to provide the internal identifier of an academic event.
    title: ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    ifabsent: string(confident:EventID)
    identifier: true
    alias: id
    owner: Event
    range: uriorcurie
    required: true
  official_name:
    name: official_name
    description: A property to provide the the official name of an academic event.
    title: Official Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: name
    slot_uri: skos:perfLabel
    alias: official_name
    owner: Event
    range: string
    required: true
  organized_by:
    name: organized_by
    description: A property to provide the organizer of an academic event.
    title: Organizer
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: organized_by
    owner: Event
    range: Organizer
    required: true
    inlined: true
    inlined_as_list: true
  start_date:
    name: start_date
    description: The start date of an academic event or event series. Wheres the latter
      will in reality most likely be the start date of the first event of this series,
      unless there is some other source from which it is possible to derive the date
      of the inception of the series.
    title: Start Date
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: aeon:start_date
    alias: start_date
    owner: Event
    range: datetime
    required: true
  end_date:
    name: end_date
    description: Similar to start_date but only for the end of an academic event or
      event series.
    title: End Date
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: aeon:end_date
    alias: end_date
    owner: Event
    range: datetime
    required: true
  event_status:
    name: event_status
    description: A property to provide the status of an event from a controlled list
      (e.g. as scheduled (default), postpooned, canceld etc).
    title: Event Status
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: aeon:event_status
    ifabsent: string(as scheduled)
    alias: event_status
    owner: Event
    range: EventStatus
    required: true
  has_acronym:
    name: has_acronym
    description: The official acronym of an academic event.
    title: Acronym
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: name
    alias: has_acronym
    owner: Event
    range: string
    required: false
    recommended: true
  academic_field:
    name: academic_field
    description: A property to describe the scientific subject(s) associated with
      an academic event, according to some controlled vocabulary or thesaurus. If
      this is used, its subproperties [schema_value](schema_value.md) and [schema_name](schema_name.md)
      are mandatory.
    title: Academic Field
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: aeon:0000040
    multivalued: true
    alias: academic_field
    owner: Event
    range: AcademicField
    required: false
    recommended: true
    inlined: true
    inlined_as_list: true
  landing_page:
    name: landing_page
    description: A property to provide the website to which the DOI an academic event
      is resolving to.
    title: Landing Page
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: landing_page
    owner: Event
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
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_publication
    owner: Event
    range: Publication
    required: false
    recommended: true
    inlined: true
    inlined_as_list: true
  sponsored_by:
    name: sponsored_by
    description: A property to provide the sponsors of an academic event.
    title: Sponsor
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: sponsored_by
    owner: Event
    range: Sponsor
    required: false
    recommended: true
    inlined: true
    inlined_as_list: true
  website:
    name: website
    description: A property to provide the URL the official website of an academic
      event.
    title: Official Website
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: website
    owner: Event
    range: uri
    recommended: true
  has_doi:
    name: has_doi
    description: A property to provide a digital object identifier (DOI) for an event.
      This is set automatically.
    title: DOI
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: has_doi
    owner: Event
    range: DigitalObjectId
    recommended: true
    inlined: true
    inlined_as_list: true
  type:
    name: type
    description: A property to provide the format of an academic event according to
      the possible values of the [Event Type](EventType.md) enum.
    title: Event Type
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    abstract: true
    designates_type: true
    alias: type
    owner: Event
    range: EventType
    recommended: true
  at_location:
    name: at_location
    description: The location of the academic event.
    title: Location
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: at_location
    owner: Event
    range: Location
    required: false
    recommended: true
  in_series:
    name: in_series
    description: The relation used to provide the series of which an Event is a part.
    title: In Series
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: in_series
    owner: Event
    range: EventSeries
    required: false
    recommended: true
  has_deadline:
    name: has_deadline
    description: A property to provide a deadline of an academic event.
    title: Deadline
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_deadline
    owner: Event
    range: Deadline
    required: false
    recommended: true
    inlined: true
    inlined_as_list: true
  related_to:
    name: related_to
    description: A property to be used to link events to each other.
    title: Related To
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: related_to
    owner: Event
    range: ProcessRelation
    required: false
    recommended: true
  alternative_name:
    name: alternative_name
    description: A property to provide alternative names of an academic event.
    title: Alternative Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: name
    slot_uri: skos:altLabel
    multivalued: true
    alias: alternative_name
    owner: Event
    range: string
    required: false
    recommended: false
  former_name:
    name: former_name
    description: The former official name of an academic event. Usually this will
      only be needed in case an academic event has undergone a name change.
    title: Former Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: name
    alias: former_name
    owner: Event
    range: string
    required: false
    recommended: false
  translated_name:
    name: translated_name
    description: A translation of the official name of an event to be used in different
      language contexts.
    title: Translated Name
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: name
    multivalued: true
    alias: translated_name
    owner: Event
    range: string
    required: false
    recommended: false
  context_info:
    name: context_info
    description: A property to provide extra information for an academic event.
    title: Context Information
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    alias: context_info
    owner: Event
    range: Context
    required: false
    recommended: false
  has_metric:
    name: has_metric
    description: A property to provide one ore more metrics of an academic event.
    title: Metric
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_metric
    owner: Event
    range: Metric
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  has_topic:
    name: has_topic
    description: A property to provide the theme and topics of an event as free keywords,
      phrases or text.
    title: Topic
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    multivalued: true
    alias: has_topic
    owner: Event
    range: string
    required: false
    recommended: false
  external_id:
    name: external_id
    description: The property to provide external identifiers for an academic event,
      including their identifier scheme.
    title: External ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    slot_uri: iao:0000235
    multivalued: true
    alias: external_id
    owner: Event
    range: ExternalIdentifier
    inlined: true
    inlined_as_list: true
  wikidata_id:
    name: wikidata_id
    description: A property to link an academic event with its Wikidata identifier.
    title: Wikidata ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: wikidata_id
    owner: Event
    range: WikidataId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  dpbl_id:
    name: dpbl_id
    description: A property to link an academic event with its DBLP identifier.
    title: DBLP ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: dpbl_id
    owner: Event
    range: DblpId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  gnd_id:
    name: gnd_id
    description: A property to link an academic event with its GND identifier.
    title: GND ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: gnd_id
    owner: Event
    range: GndId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  wikicfp_event_id:
    name: wikicfp_event_id
    description: A property to link an academic event with its WikiCFP identifier.
    title: WikiCFP Event ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: wikicfp_event_id
    owner: Event
    range: WikiCfpEventId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
  tibkat_id:
    name: tibkat_id
    description: A property to link an academic event with its TIBKAT identifier.
    title: TIBKAT ID
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
    is_a: external_id
    slot_uri: iao:0000235
    multivalued: true
    alias: tibkat_id
    owner: Event
    range: TibkatId
    required: false
    recommended: false
    inlined: true
    inlined_as_list: true
class_uri: aeon:0000001

```
</details>