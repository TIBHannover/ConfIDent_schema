# ConfIDent Metadata Schema

This is a schema for the ConfIDent project that describes the necessary metadata requirements of academic events and event series.

URI: [https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml)

Version: 0.4.3

## Classes

| Class | Description |
| --- | --- |
| [Subobject Academic Field](AcademicField.md) | An academic field is the scientific subject of an event or event series according to some controlled vocabulary or thesaurus and as such requires the scheme URI. |
| [Subobject Attendee](Attendee.md) | A person whose only role it is to attend an academic event. |
| [City](City.md) | The city in which an academic event takes place. |
| [Subobject Committee Chair](CommitteeChair.md) | The head of an academic event committee. |
| [Subobject Committee Member](CommitteeMember.md) | A members of an academic event committee. |
| [ConfIDent Records](ConfIDentRecords.md) | A container to be able to bundle academic event data and series in one data file (e.g. YAML or JSON). |
| [Subobject Contact Person](ContactPerson.md) | The contact person of an academic event or event series. |
| [Subobject Context](Context.md) | A container to provide extra information, such as call of papers event description. |
| [Subobject Contributor](Contributor.md) | A contributor is a person or organization that holds a contributor role which is being realized in an event or event series. |
| [Country](Country.md) | The country in which an academic event takes place. |
| [DBLP ID](DblpId.md) | The identifier of an academic event or series in dblp. |
| [Subobject Deadline](Deadline.md) | A container for event deadlines. |
| [Digital Object Identifier](DigitalObjectId.md) | A centrally registered identifier symbol used to uniquely identify digital objects given by International DOI Foundation. |
| [Event](Event.md) | An academic event is part of the established instruments of science communication as a format for conveying the latest scientific publications. It is defined by the meeting of researchers at a specific time and place (virtual or physical) and with a specific thematic focus to present, hear and discuss these publications. In contrast to other forms of events, academic events should primarily serve the exchange of results and methods of scientific research and their didactic mediation.  Furthermore, a significant participation of scientific organizations in the realization of an academic event is constitutive for this type of event; for example, to distinguish it from events in which researchers mainly act as external experts or with a purely legitimising function. |
| [Subobject Event Format](EventFormatSpecification.md) | An academic event format specification is a plan specification that classifies a planned gathering of people in an academic context according to some sociocultural format, which provides implicit and explicit details on how this gathering is to be carried out by its participants in terms of achieving certain objectives, fulfilling certain conditions and performing certain actions. It thus concretizes the expectations of the contributors of an academic event. While the explicit details are often provided as concrete parts (e.g. deadline or attendance fee specifications), the implicit details depend on the semantics encoded in the words used for the classification of academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications can overlap or vary to a certain degree. |
| [Event Series](EventSeries.md) | An academic event series describes the set of academic events which take place on a regular basis and thus have an established common identity. This identity is constituted, for example, through institutional continuity in the hosting of a series (e.g. by a specialised society), thematic focuses and/or a common label under which a series is defined (particularly name and acronym). Nevertheless, it is possible that each of these criteria may change over time. |
| [External ID](ExternalIdentifier.md) | An identifer of an entity declared in another schema. |
| [GND ID](GndId.md) | The identifier of a thing (item) in the German National authority file. |
| [Subobject Keynote Speaker](KeynoteSpeaker.md) | A 'keynote speaker' is a presenter that is an invited person - often a multiplier in his or her (research) field - responsible for delivering a keynote speech. |
| [Subobject Location](Location.md) | A container for the information about the location in which an academic event takes place. |
| [Subobject Metric](Metric.md) | A container for statistical information about an event or event series. |
| [Subobject Moderator](Moderator.md) | A person that has the role to moderate an academic event. |
| [Subobject Named Thing](NamedThing.md) | A mixin used to provide the attributes needed for the identification of a thing. |
| [Subobject Organizer](Organizer.md) | An organizer of an academic event or event series. |
| [Subobject Presenter](Presenter.md) | A person that presents its work at an academic event. |
| [Subobject Process Relation](ProcessRelation.md) | A container for relations between academic events. |
| [Subobject Publication](Publication.md) | A published work, e.g. proceedings or conferenc paper, that is the output of an academic event or series. |
| [Region](Region.md) | The region in which an academic event takes place. For non USA events this might often be negligible. |
| [Subobject Reviewer](Reviewer.md) | A person that has the role to review the submissions of an academic event. |
| [Subobject Schema Based Thing](SchemaBasedThing.md) | A mixin used in classes that contain schema based values, such as the classifications used to denote the academic field of an event or the external identifiers used to denote a thing. |
| [Subobject Sponsor](Sponsor.md) | A person or an organization whose role it is to sponsor an academic event or event series. |
| [TIBKAT ID](TibkatId.md) | The identifier of a publication in the TIB catalog that references an event or event series. |
| [Venue](Venue.md) | The venue at which an academic event takes place. |
| [WikiCFP Event ID](WikiCfpEventId.md) | The identifier of an academic event or series in WikiCFP. |
| [WikiCFP Series ID](WikiCfpSeriesId.md) | The identifier of an academic event or series in WikiCFP. |
| [Wikidata ID](WikidataId.md) | The identifier of a thing (item) in Wikidata. |


## Slots

| Slot | Description |
| --- | --- |
| [Academic Field](academic_field.md) | A property to describe the scientific subject(s) of an event or event series, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [Schema Value](schema_value.md) and [Schema Name](schema_name.md) are mandatory. |
| [Alternative Name](alternative_name.md) | A property to provide alternative names of an event or event series. |
| [Location](at_location.md) | The location of the academic event. |
| [Contact](contact.md) | The contact person of an academic event or event series. |
| [Context Information](context_info.md) | A property to provide extra information, such as call of papers summary,  event or event series description. |
| [Deadline Date](deadline_date.md) | The date of a deadline. |
| [Other Deadline Type](deadline_other.md) | A property to specify another type of deadline, if this type of deadline is not within the allowed values of [DeadlineType](DeadlineType.md). |
| [Metric Description](description.md) | A property to provide a description of a metric. |
| [DBLP ID](dpbl_id.md) | A property to link the an event or event series with its DBLP identifier. |
| [Email](email.md) | The email address of the contact person. |
| [End Date](end_date.md) | Similar to start_date but only for the end of an academic event or event series. |
| [Event Format](event_format.md) | A property to provide an event format specification, if none of the [Event Types](EventType.md) are applicable to specify the format of an academic event. |
| [Event Mode](event_mode.md) | The event mode describes whether the event is a physical, virtual or hybrid event. |
| [Event Status](event_status.md) | A property to provide the status of an event from a controlled list (e.g. as scheduled (default), postpooned, canceld etc). |
| [Events](events.md) | A property to provide a list of academic events within this container. |
| [External ID](external_id.md) | A property to provide an external id of a schema entity. |
| [Former Name](former_name.md) | The former official name of an academic event or series. Usually this will only be needed in case an academic event series has undergone a name change. |
| [GND ID](gnd_id.md) | A property to link an entity to the authority file of the German National Library. |
| [Acronym](has_acronym.md) | The official acronym of an event or event series. |
| [City](has_city.md) | The property to specify the [City](City.md) of an academic event location. |
| [Country](has_country.md) | The property to specify the [Country](Country.md) of an academic event location. |
| [Deadline](has_deadline.md) | A property to provide a deadline of an academic event. |
| [DOI](has_doi.md) | A property to provide a digital object identifier (DOI) according to https://doi.org/. |
| [Metric](has_metric.md) | A property to provide one or more metrics of an event or event series. |
| [Publication](has_publication.md) | The published works that are related to the event or event series, such as proceedings and video recordings of talks. |
| [Region](has_region.md) | The property to specify the [Region](Region.md) of an academic event location. |
| [Topic](has_topic.md) | A property to provide the theme and topics of an event or event series as free keywords, phrases or text. |
| [Venue](has_venue.md) | The property to specify the [Venue](Venue.md) of an academic event location. |
| [ID](id.md) | A property to provide an internal id of a schema entity in the ConfIDent plattform. |
| [In Series](in_series.md) | The relation used to provide the series of which an Event is a part. |
| [Metric Integer Value](int_value.md) | A property to provide an integer value for a metric. |
| [Landing Page](landing_page.md) | A property to provide the website to which a persistent identifier is resolving and which contains all the metadata about an event or event series. |
| [Lattitude](lattitude.md) | The property to specify the lattitude of an academic event location. |
| [Context License](license_str.md) | The license of the context information as text, which must be used when copying text from other sources. |
| [Context License URL](license_url.md) | The license of the context information as URL, which should be used when copying text from other sources and such a URL exists. |
| [Longitude](longitude.md) | The property to specify the longitude of an academic event location. |
| [Meeting URL](meeting_url.md) | The property to specify the URL under which a one can participate virtually in an academic event. |
| [Metric Year](metric_year.md) | A property to provide the year for which the metric value is valid. |
| [Name](name.md) | A property to provide a name of a schema entity. |
| [Official Name](official_name.md) | The official name of an event or event series. |
| [Ordinal](ordinal.md) | The ordnial number of an academic event within its series. |
| [Organizer](organized_by.md) | A property to provide the organizers of an event or event series. |
| [Other Event Format](other_format.md) | A mandatory property to provide the format of an academic event as string, in order to further specify its type in case it could not be specified according to the possible values of [Event Type](EventType.md). |
| [Metric Rate Value](rate_value.md) | A property to provide a rate value as float for a metric. |
| [Related To](related_to.md) | A property to be used to link events to each other. |
| [External formatter URI](schema_base_uri.md) | The base URI of the schema that provides the context for the schema based value. |
| [Schema Name](schema_name.md) | A property to provide the name of a schema. |
| [Schema Value](schema_value.md) | A property to provide the literal value of a schema based entity. |
| [Series](series.md) | A property to provide a list of academic event series within this container. |
| [Series Of](series_of.md) | A property to link to the events that are part of an academic event series. |
| [Sponsor](sponsored_by.md) | A property to provide the sponsor of an event or event series. |
| [Start Date](start_date.md) | The start date of an academic event or event series. Wheres the latter will in reality most likely be the start date of the first event of this series, unless there is some other source from which it is possible to derive the date of the inception of the series. |
| [Metric String Value](str_value.md) | A property to provide a string value for a metric. |
| [Street](street.md) | The street of the venue including the house number seperated by comma. |
| [Telephone](telephone.md) | The telephone number of the contact person. |
| [Context Description](text.md) | The free text used to provide more context information on an event or event series. |
| [TIBKAT ID](tibkat_id.md) | A property to link to a publication indexed in the TIB catalouge that references an event or event series. |
| [Translated Name](translated_name.md) | A translation of the official name of an event or event series to be used in different language contexts. |
| [Metric Truth Value](truth_value.md) | A property to provide a truth value for a metric. |
| [Type](type.md) | An abstract property that is reused in certain classes to differentiate their instances according to the type enums defined as the range. |
| [Official Website](website.md) | A property to provide the URL the official website of a event or event series. |
| [WikiCFP Event ID](wikicfp_event_id.md) | A property to link an event or event series with its WikiCFP identifier. |
| [WikiCFP Series ID](wikicfp_series_id.md) | A property to link an event or event series with its WikiCFP identifier. |
| [Wikidata ID](wikidata_id.md) | A property to link an entity with its Wikidata identifier. |
| [ZIP Code](zip_code.md) | The zip code of the venue. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Contributor Type](ContributorType.md) | An enumaration used to distinguish the contributors of an event or event series with regard to them being either an organization or a person. |
| [Deadline Type](DeadlineType.md) | An enum that specifies the possible kinds of deadlines of an academic event. |
| [Event Mode](EventMode.md) | An enum to specify if an academic event is in person, virtual or a hybrid of both. |
| [Event Status](EventStatus.md) | The status of the academic event which indicates if it takes place as planned. |
| [Event Type](EventType.md) | The most common minimal event types. For event types that are not in this list, you can use "other" and provide the label of this other event format using the [Event Format](event_format.md) property. |
| [Metric Type](MetricType.md) | The possible metric of an academic event. |
| [Event Relation Type](RelationType.md) | The kinds of relations that are allowed between academic events. |
| [Review Process Type](ReviewProcessType.md) | The possible values for the metric that describes the review process undertaken by the organizers of an academic event. |
