
# confident_schema


**metamodel version:** 1.7.0

**version:** 0.4.0


This is a schema for the ConfIDent project that describes the necessary metadata requirements of academic events and event series.


### Classes

 * [AcademicField](AcademicField.md) - An academic field is the scientific subject of an event or event series according to some controlled vocabulary or thesaurus and as such requires the scheme URI.
 * [City](City.md) - The city in which an academic event takes place.
 * [ConfIDentRecords](ConfIDentRecords.md) - A container to be able to bundle academic event data and series in one data file (e.g. YAML or JSON).
 * [Context](Context.md) - A container to provide extra information, such as call of papers event description.
 * [Contributor](Contributor.md) - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.
     * [Attendee](Attendee.md) - A person whose only role it is to attend an academic event.
     * [Moderator](Moderator.md) - A person that has the role to moderate an academic event.
     * [Organizer](Organizer.md) - An organizer of an academic event or event series.
         * [CommitteeMember](CommitteeMember.md) - A members of an academic event committee.
             * [CommitteeChair](CommitteeChair.md) - The head of an academic event committee.
         * [ContactPerson](ContactPerson.md) - The contact person of an academic event or event series.
     * [Presenter](Presenter.md) - A person that presents its work at an academic event.
         * [KeynoteSpeaker](KeynoteSpeaker.md) - A 'keynote speaker' is a presenter that is an invited person - often a multiplier in his or her (research) field - responsible for delivering a keynote speech.
     * [Reviewer](Reviewer.md) - A person that has the role to review the submissions of an academic event.
     * [Sponsor](Sponsor.md) - A person or an organization whose role it is to sponsor an academic event or event series.
 * [Country](Country.md) - The country in which an academic event takes place.
 * [Deadline](Deadline.md) - A container for event deadlines.
 * [Event](Event.md) - An academic event is part of the established instruments of science communication as a format for conveying the latest scientific publications. It is defined by the meeting of researchers at a specific time and place (virtual or physical) and with a specific thematic focus to present, hear and discuss these publications. In contrast to other forms of events, academic events should primarily serve the exchange of results and methods of scientific research and their didactic mediation.  Furthermore, a significant participation of scientific organizations in the realization of an academic event is constitutive for this type of event; for example, to distinguish it from events in which researchers mainly act as external experts or with a purely legitimising function.
 * [EventFormatSpecification](EventFormatSpecification.md) - An academic event format specification is a plan specification that classifies a planned gathering of people in an academic context according to some sociocultural format, which provides implicit and explicit details on how this gathering is to be carried out by its participants in terms of achieving certain objectives, fulfilling certain conditions and performing certain actions. It thus concretizes the expectations of the contributors of an academic event. While the explicit details are often provided as concrete parts (e.g. deadline or attendance fee specifications), the implicit details depend on the semantics encoded in the words used for the classification of academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications can overlap or vary to a certain degree.
 * [EventSeries](EventSeries.md) - An academic event series describes the set of academic events which take place on a regular basis and thus have an established common identity. This identity is constituted, for example, through institutional continuity in the hosting of a series (e.g. by a specialised society), thematic focuses and/or a common label under which a series is defined (particularly name and acronym). Nevertheless, it is possible that each of these criteria may change over time.
 * [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.
     * [DblpId](DblpId.md) - The identifier of an academic event or series in dblp.
     * [DigitalObjectId](DigitalObjectId.md) - A centrally registered identifier symbol used to uniquely identify digital objects given by International DOI Foundation.
     * [GndId](GndId.md) - The identifier of a thing (item) in the German National authority file.
     * [TibkatId](TibkatId.md) - The identifier of a publication in the TIB catalog that references an event or event series.
     * [WikiCfpEventId](WikiCfpEventId.md) - The identifier of an academic event or series in WikiCFP.
     * [WikiCfpSeriesId](WikiCfpSeriesId.md) - The identifier of an academic event or series in WikiCFP.
     * [WikidataId](WikidataId.md) - The identifier of a thing (item) in Wikidata.
 * [Location](Location.md) - A container for the information about the location in which an academic event takes place.
 * [Metric](Metric.md) - A container for statistical information about an event or event series.
 * [ProcessRelation](ProcessRelation.md) - A container for relations between academic events.
 * [Publication](Publication.md) - A published work, e.g. proceedings or conferenc paper, that is the output of an academic event or series.
 * [Region](Region.md) - The region in which an academic event takes place. For non USA events this might often be negligible.
 * [Venue](Venue.md) - The venue at which an academic event takes place.

### Mixins

 * [NamedThing](NamedThing.md) - A mixin used to provide the attributes needed for the identification of a thing.
 * [SchemaBasedThing](SchemaBasedThing.md) - A mixin used in classes that contain schema based values, such as the classifications used to denote the academic field of an event or the external identifiers used to denote a thing.

### Slots

 * [academic_field](academic_field.md) - A property to describe the scientific subject(s) of an event or event series, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [Schema Value](schema_value.md) and [Schema Name](schema_name.md) are mandatory.
     * [EventSeries➞academic_field](EventSeries_academic_field.md) - A property to describe the scientific subject(s) associated with an academic event series, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [Schema Value](schema_value.md) and [Schema Name](schema_name.md) are mandatory.
     * [Event➞academic_field](Event_academic_field.md) - A property to describe the scientific subject(s) associated with an academic event, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [schema_value](schema_value.md) and [schema_name](schema_name.md) are mandatory.
 * [at_location](at_location.md) - The location of the academic event.
 * [ConfIDentRecords➞events](confIDentRecords__events.md) - A property to provide a list of academic events within this container.
 * [ConfIDentRecords➞series](confIDentRecords__series.md) - A property to provide a list of academic event series within this container.
 * [➞email](contactPerson__email.md) - The email address of the contact person.
 * [➞telephone](contactPerson__telephone.md) - The telephone number of the contact person.
 * [➞license_str](context__license_str.md) - The license of the context information as text, which must be used when copying text from other sources.
 * [➞license_url](context__license_url.md) - The license of the context information as URL, which should be used when copying text from other sources and such a URL exists.
 * [➞text](context__text.md) - The free text used to provide more context information on an event or event series.
 * [context_info](context_info.md) - A property to provide extra information, such as call of papers summary,  event or event series description.
     * [EventSeries➞context_info](EventSeries_context_info.md) - A property to provide extra information for an academic event series.
     * [Event➞context_info](Event_context_info.md) - A property to provide extra information for an academic event.
 * [➞deadline_date](deadline__deadline_date.md) - The date of a deadline.
 * [➞deadline_other](deadline__deadline_other.md) - A property to specify another type of deadline, if this type of deadline is not within the allowed values of [DeadlineType](DeadlineType.md).
 * [end_date](end_date.md) - Similar to start_date but only for the end of an academic event or event series.
 * [➞other_format](eventFormatSpecification__other_format.md) - A mandatory property to provide the format of an academic event as string, in order to further specify its type in case it could not be specified according to the possible values of [Event Type](EventType.md).
 * [event_format](event_format.md) - A property to provide an event format specification, if none of the [Event Types](EventType.md) are applicable to specify the format of an academic event.
 * [event_mode](event_mode.md) - The event mode describes whether the event is a physical, virtual or hybrid event.
 * [event_status](event_status.md) - A property to provide the status of an event from a controlled list (e.g. as scheduled (default), postpooned, canceld etc).
 * [external_id](external_id.md) - A property to provide an external id of a schema entity.
     * [EventSeries➞external_id](EventSeries_external_id.md) - The property to provide external identifiers for an academic event series, including their identifier scheme.
     * [Event➞external_id](Event_external_id.md) - The property to provide external identifiers for an academic event, including their identifier scheme.
     * [dpbl_id](dpbl_id.md) - A property to link the an event or event series with its DBLP identifier.
         * [EventSeries➞dpbl_id](EventSeries_dpbl_id.md) - A property to link an academic event series with its DBLP identifier.
         * [Event➞dpbl_id](Event_dpbl_id.md) - A property to link an academic event with its DBLP identifier.
     * [gnd_id](gnd_id.md) - A property to link an entity to the authority file of the German National Library.
         * [EventSeries➞gnd_id](EventSeries_gnd_id.md) - A property to link an academic event series with its GND identifier.
         * [Event➞gnd_id](Event_gnd_id.md) - A property to link an academic event with its GND identifier.
     * [has_doi](has_doi.md) - A property to provide a digital object identifier (DOI) according to https://doi.org/.
         * [EventSeries➞has_doi](EventSeries_has_doi.md) - A property to provide a digital object identifier (DOI) for an event series. This is set automatically.
         * [Event➞has_doi](Event_has_doi.md) - A property to provide a digital object identifier (DOI) for an event. This is set automatically.
     * [tibkat_id](tibkat_id.md) - A property to link to a publication indexed in the TIB catalouge that references an event or event series.
         * [Event➞tibkat_id](Event_tibkat_id.md) - A property to link an academic event with its TIBKAT identifier.
     * [wikicfp_event_id](wikicfp_event_id.md) - A property to link an event or event series with its WikiCFP identifier.
         * [Event➞wikicfp_event_id](Event_wikicfp_event_id.md) - A property to link an academic event with its WikiCFP identifier.
     * [wikicfp_series_id](wikicfp_series_id.md) - A property to link an event or event series with its WikiCFP identifier.
         * [EventSeries➞wikicfp_series_id](EventSeries_wikicfp_series_id.md) - A property to link an academic event series with its WikiCFP identifier.
     * [wikidata_id](wikidata_id.md) - A property to link an entity with its Wikidata identifier.
         * [EventSeries➞wikidata_id](EventSeries_wikidata_id.md) - A property to link an academic event series with its Wikidata identifier.
         * [Event➞wikidata_id](Event_wikidata_id.md) - A property to link an academic event with its Wikidata identifier.
 * [has_deadline](has_deadline.md) - A property to provide a deadline of an academic event.
 * [has_metric](has_metric.md) - A property to provide one or more metrics of an event or event series.
     * [EventSeries➞has_metric](EventSeries_has_metric.md) - A property to provide one ore more metrics of an academic event series.
     * [Event➞has_metric](Event_has_metric.md) - A property to provide one ore more metrics of an academic event.
 * [has_publication](has_publication.md) - The published works that are related to the event or event series, such as proceedings and video recordings of talks.
     * [EventSeries➞has_publication](EventSeries_has_publication.md) - A property to provide the publication associated with
     * [Event➞has_publication](Event_has_publication.md) - A property to provide the publication associated with
 * [has_topic](has_topic.md) - A property to provide the theme and topics of an event or event series as free keywords, phrases or text.
     * [EventSeries➞has_topic](EventSeries_has_topic.md) - A property to provide the theme and topics of an event series as free keywords, phrases or text.
     * [Event➞has_topic](Event_has_topic.md) - A property to provide the theme and topics of an event as free keywords, phrases or text.
 * [id](id.md) - A property to provide an internal id of a schema entity in the ConfIDent plattform.
     * [Contributor➞id](Contributor_id.md) - The internal ConfIDent identifier for a contibutor
     * [EventSeries➞id](EventSeries_id.md) - A property to provide the internal identifier of an academic event series.
     * [Event➞id](Event_id.md) - A property to provide the internal identifier of an academic event.
 * [in_series](in_series.md) - The relation used to provide the series of which an Event is a part.
 * [landing_page](landing_page.md) - A property to provide the website to which a persistent identifier is resolving and which contains all the metadata about an event or event series.
     * [EventSeries➞landing_page](EventSeries_landing_page.md) - A property to provide the website to which the DOI an academic event series is resolving to.
     * [Event➞landing_page](Event_landing_page.md) - A property to provide the website to which the DOI an academic event is resolving to.
 * [➞has_city](location__has_city.md) - The property to specify the [City](City.md) of an academic event location.
 * [➞has_country](location__has_country.md) - The property to specify the [Country](Country.md) of an academic event location.
 * [➞has_region](location__has_region.md) - The property to specify the [Region](Region.md) of an academic event location.
 * [➞has_venue](location__has_venue.md) - The property to specify the [Venue](Venue.md) of an academic event location.
 * [➞lattitude](location__lattitude.md) - The property to specify the lattitude of an academic event location.
 * [➞longitude](location__longitude.md) - The property to specify the longitude of an academic event location.
 * [➞meeting_url](location__meeting_url.md) - The property to specify the URL under which a one can participate virtually in an academic event.
 * [➞description](metric__description.md) - A property to provide a description of a metric.
 * [➞int_value](metric__int_value.md) - A property to provide an integer value for a metric.
 * [➞metric_year](metric__metric_year.md) - A property to provide the year for which the metric value is valid.
 * [➞rate_value](metric__rate_value.md) - A property to provide a rate value as float for a metric.
 * [➞str_value](metric__str_value.md) - A property to provide a string value for a metric.
 * [➞truth_value](metric__truth_value.md) - A property to provide a truth value for a metric.
 * [name](name.md) - A property to provide a name of a schema entity.
     * [alternative_name](alternative_name.md) - A property to provide alternative names of an event or event series.
         * [EventSeries➞alternative_name](EventSeries_alternative_name.md) - A property to provide alternative names of an academic event series.
         * [Event➞alternative_name](Event_alternative_name.md) - A property to provide alternative names of an academic event.
     * [former_name](former_name.md) - The former official name of an academic event or series. Usually this will only be needed in case an academic event series has undergone a name change.
         * [EventSeries➞former_name](EventSeries_former_name.md) - The former official name of an academic event series. Usually this will only be needed in case an academic event series has undergone a name change.
         * [Event➞former_name](Event_former_name.md) - The former official name of an academic event. Usually this will only be needed in case an academic event has undergone a name change.
     * [has_acronym](has_acronym.md) - The official acronym of an event or event series.
         * [EventSeries➞has_acronym](EventSeries_has_acronym.md) - The official acronym of an academic event series.
         * [Event➞has_acronym](Event_has_acronym.md) - The official acronym of an academic event.
     * [official_name](official_name.md) - The official name of an event or event series.
         * [EventSeries➞official_name](EventSeries_official_name.md) - A property to provide the the official name of an academic event series.
         * [Event➞official_name](Event_official_name.md) - A property to provide the the official name of an academic event.
     * [translated_name](translated_name.md) - A translation of the official name of an event or event series to be used in different language contexts.
         * [EventSeries➞translated_name](EventSeries_translated_name.md) - A translation of the official name of an event series to be used in different language contexts.
         * [Event➞translated_name](Event_translated_name.md) - A translation of the official name of an event to be used in different language contexts.
 * [ordinal](ordinal.md) - The ordnial number of an academic event within its series.
 * [organized_by](organized_by.md) - A property to provide the organizers of an event or event series.
     * [EventSeries➞organized_by](EventSeries_organized_by.md) - A property to provide the organizer of an academic event series.
     * [Event➞organized_by](Event_organized_by.md) - A property to provide the organizer of an academic event.
 * [➞contact](organizer__contact.md) - The contact person of an academic event or event series.
 * [related_to](related_to.md) - A property to be used to link events to each other.
 * [schema_base_uri](schema_base_uri.md) - The base URI of the schema that provides the context for the schema based value.
     * [DblpId➞schema_base_uri](DblpId_schema_base_uri.md)
     * [DigitalObjectId➞schema_base_uri](DigitalObjectId_schema_base_uri.md)
     * [GndId➞schema_base_uri](GndId_schema_base_uri.md)
     * [TibkatId➞schema_base_uri](TibkatId_schema_base_uri.md)
     * [WikiCfpEventId➞schema_base_uri](WikiCfpEventId_schema_base_uri.md)
     * [WikiCfpSeriesId➞schema_base_uri](WikiCfpSeriesId_schema_base_uri.md)
     * [WikidataId➞schema_base_uri](WikidataId_schema_base_uri.md)
 * [schema_name](schema_name.md) - A property to provide the name of a schema.
     * [DblpId➞schema_name](DblpId_schema_name.md)
     * [DigitalObjectId➞schema_name](DigitalObjectId_schema_name.md)
     * [GndId➞schema_name](GndId_schema_name.md)
     * [TibkatId➞schema_name](TibkatId_schema_name.md)
     * [WikiCfpEventId➞schema_name](WikiCfpEventId_schema_name.md)
     * [WikiCfpSeriesId➞schema_name](WikiCfpSeriesId_schema_name.md)
     * [WikidataId➞schema_name](WikidataId_schema_name.md)
 * [schema_value](schema_value.md) - A property to provide the literal value of a schema based entity.
     * [AcademicField➞schema_value](AcademicField_schema_value.md) - The classification label of a certain classification schema.
     * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)
 * [series_of](series_of.md) - A property to link to the events that are part of an academic event series.
 * [sponsored_by](sponsored_by.md) - A property to provide the sponsor of an event or event series.
     * [EventSeries➞sponsored_by](EventSeries_sponsored_by.md) - A property to provide the sponsors of an academic event series.
     * [Event➞sponsored_by](Event_sponsored_by.md) - A property to provide the sponsors of an academic event.
 * [start_date](start_date.md) - The start date of an academic event or event series. Wheres the latter will in reality most likely be the start date of the first event of this series, unless there is some other source from which it is possible to derive the date of the inception of the series.
 * [type](type.md) - An abstract property that is reused in certain classes to differentiate their instances according to the type enums defined as the range.
     * [Contributor➞type](Contributor_type.md) - A property to provide the information whether the contributor is an organization or person.
     * [Deadline➞type](Deadline_type.md) - A propery to provide the type of the deadline.
     * [Event➞type](Event_type.md) - A property to provide the format of an academic event according to the possible values of the [Event Type](EventType.md) enum.
     * [Metric➞type](Metric_type.md) - A property to provide the type of relation between academic events.
     * [ProcessRelation➞type](ProcessRelation_type.md) - A property to provide the type of process relation.
 * [➞street](venue__street.md) - The street of the venue including the house number seperated by comma.
 * [➞zip_code](venue__zip_code.md) - The zip code of the venue.
 * [website](website.md) - A property to provide the URL the official website of a event or event series.
     * [EventSeries➞website](EventSeries_website.md) - A property to provide the URL the official website of an academic event series.
     * [Event➞website](Event_website.md) - A property to provide the URL the official website of an academic event.

### Enums

 * [ContributorType](ContributorType.md) - An enumaration used to distinguish the contributors of an event or event series with regard to them being either an organization or a person.
 * [DeadlineType](DeadlineType.md) - An enum that specifies the possible kinds of deadlines of an academic event.
 * [EventMode](EventMode.md) - An enum to specify if an academic event is in person, virtual or a hybrid of both.
 * [EventStatus](EventStatus.md) - The status of the academic event which indicates if it takes place as planned.
 * [EventType](EventType.md) - The most common minimal event types. For event types that are not in this list, you can use "other" and provide the label of this other event format using the [Event Format](event_format.md) property.
 * [MetricType](MetricType.md) - The possible metric of an academic event.
 * [RelationType](RelationType.md) - The kinds of relations that are allowed between academic events.

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
