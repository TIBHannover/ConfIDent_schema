
# Class: Event


An academic event is part of the established instruments of science communication as a format for conveying the latest scientific publications. It is defined by the meeting of researchers at a specific time and place (virtual or physical) and with a specific thematic focus to present, hear and discuss these publications. In contrast to other forms of events, academic events should primarily serve the exchange of results and methods of scientific research and their didactic mediation.  Furthermore, a significant participation of scientific organizations in the realization of an academic event is constitutive for this type of event; for example, to distinguish it from events in which researchers mainly act as external experts or with a purely legitimising function.

URI: [confident:Event](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Event)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WikidataId],[WikiCfpEventId],[TibkatId],[Sponsor],[Publication],[Organizer],[Metric],[Location],[GndId],[ExternalIdentifier],[EventSeries],[WikiCfpEventId]<wikicfp_event_id%200..*-++[Event&#124;id:uriorcurie;official_name:string;start_date:datetime;end_date:datetime;event_status:EventStatus;has_acronym:string%20%3F;type:EventType%20%3F;landing_page:uri%20%3F;website:uri%20%3F;umbrella_of:string%20%3F;has_umbrella:string%20%3F;colocated_with:string%20*;joint_venture_with:string%20*;alternative_name:string%20*;former_name:string%20*;translated_name:string%20*;has_topic:string%20*;ordinal:integer%20%3F;event_mode:EventMode%20%3F],[TibkatId]<tibkat_id%200..*-++[Event],[GndId]<gnd_id%200..*-++[Event],[DblpId]<dpbl_id%200..*-++[Event],[WikidataId]<wikidata_id%200..*-++[Event],[ExternalIdentifier]<external_id%200..*-++[Event],[Metric]<has_metric%200..*-++[Event],[Context]<context_info%200..1-++[Event],[DigitalObjectId]<has_doi%200..*-++[Event],[Sponsor]<sponsored_by%200..*-++[Event],[Publication]<has_publication%200..*-++[Event],[AcademicField]<academic_field%200..*-++[Event],[Deadline]<has_deadline%200..*-++[Event],[Event]<superevent_of%200..1-%20[Event],[Event]<subevent_of%200..1-%20[Event],[EventSeries]<in_series%200..1-%20[Event],[Location]<at_location%200..1-++[Event],[Organizer]<organized_by%201..*-++[Event],[ConfIDentRecords]++-%20events%200..*>[Event],[EventSeries]-%20series_of%200..1>[Event],[DigitalObjectId],[Deadline],[DblpId],[Context],[ConfIDentRecords],[AcademicField])](https://yuml.me/diagram/nofunky;dir:TB/class/[WikidataId],[WikiCfpEventId],[TibkatId],[Sponsor],[Publication],[Organizer],[Metric],[Location],[GndId],[ExternalIdentifier],[EventSeries],[WikiCfpEventId]<wikicfp_event_id%200..*-++[Event&#124;id:uriorcurie;official_name:string;start_date:datetime;end_date:datetime;event_status:EventStatus;has_acronym:string%20%3F;type:EventType%20%3F;landing_page:uri%20%3F;website:uri%20%3F;umbrella_of:string%20%3F;has_umbrella:string%20%3F;colocated_with:string%20*;joint_venture_with:string%20*;alternative_name:string%20*;former_name:string%20*;translated_name:string%20*;has_topic:string%20*;ordinal:integer%20%3F;event_mode:EventMode%20%3F],[TibkatId]<tibkat_id%200..*-++[Event],[GndId]<gnd_id%200..*-++[Event],[DblpId]<dpbl_id%200..*-++[Event],[WikidataId]<wikidata_id%200..*-++[Event],[ExternalIdentifier]<external_id%200..*-++[Event],[Metric]<has_metric%200..*-++[Event],[Context]<context_info%200..1-++[Event],[DigitalObjectId]<has_doi%200..*-++[Event],[Sponsor]<sponsored_by%200..*-++[Event],[Publication]<has_publication%200..*-++[Event],[AcademicField]<academic_field%200..*-++[Event],[Deadline]<has_deadline%200..*-++[Event],[Event]<superevent_of%200..1-%20[Event],[Event]<subevent_of%200..1-%20[Event],[EventSeries]<in_series%200..1-%20[Event],[Location]<at_location%200..1-++[Event],[Organizer]<organized_by%201..*-++[Event],[ConfIDentRecords]++-%20events%200..*>[Event],[EventSeries]-%20series_of%200..1>[Event],[DigitalObjectId],[Deadline],[DblpId],[Context],[ConfIDentRecords],[AcademicField])

## Referenced by Class

 *  **[ConfIDentRecords](ConfIDentRecords.md)** *[ConfIDentRecords➞events](confIDentRecords__events.md)*  <sub>0..\*</sub>  **[Event](Event.md)**
 *  **None** *[series_of](series_of.md)*  <sub>0..1</sub>  **[Event](Event.md)**
 *  **None** *[subevent_of](subevent_of.md)*  <sub>0..1</sub>  **[Event](Event.md)**
 *  **None** *[superevent_of](superevent_of.md)*  <sub>0..1</sub>  **[Event](Event.md)**

## Attributes


### Own

 * [Event➞id](Event_id.md)  <sub>1..1</sub>
     * Description: A property to provide the internal identifier of an academic event.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [Event➞official_name](Event_official_name.md)  <sub>1..1</sub>
     * Description: A property to provide the the official name of an academic event.
     * Range: [String](types/String.md)
 * [Event➞organized_by](Event_organized_by.md)  <sub>1..\*</sub>
     * Description: A property to provide the organizer of an academic event.
     * Range: [Organizer](Organizer.md)
 * [start_date](start_date.md)  <sub>1..1</sub>
     * Description: The start date of an academic event or event series. Wheres the latter will in reality most likely be the start date of the first event of this series, unless there is some other source from which it is possible to derive the date of the inception of the series.
     * Range: [Datetime](types/Datetime.md)
 * [end_date](end_date.md)  <sub>1..1</sub>
     * Description: Similar to start_date but only for the end of an academic event or event series.
     * Range: [Datetime](types/Datetime.md)
 * [event_status](event_status.md)  <sub>1..1</sub>
     * Description: A property to provide the status of an event from a controlled list (e.g. as scheduled (default), postpooned, canceld etc).
     * Range: [EventStatus](EventStatus.md)
 * [Event➞has_acronym](Event_has_acronym.md)  <sub>0..1</sub>
     * Description: The official acronym of an academic event.
     * Range: [String](types/String.md)
 * [Event➞type](Event_type.md)  <sub>0..1</sub>
     * Description: A property to provide the format of an academic event according to the possible values of the [Event Type](EventType.md) enum.
     * Range: [EventType](EventType.md)
 * [at_location](at_location.md)  <sub>0..1</sub>
     * Description: The location of the academic event.
     * Range: [Location](Location.md)
 * [in_series](in_series.md)  <sub>0..1</sub>
     * Description: The relation used to provide the series of which an Event is a part.
     * Range: [EventSeries](EventSeries.md)
 * [subevent_of](subevent_of.md)  <sub>0..1</sub>
     * Description: A relation used to link the an event part (e.g. a session) to its superordinate event (e.g. the conference in which the session takes place).
     * Range: [Event](Event.md)
 * [superevent_of](superevent_of.md)  <sub>0..1</sub>
     * Description: A relation used to link the an superordinate event (e.g. the conference in which a session takes place) to its event part (e.g. the session).
     * Range: [Event](Event.md)
 * [has_deadline](has_deadline.md)  <sub>0..\*</sub>
     * Description: A property to provide a deadline of an academic event.
     * Range: [Deadline](Deadline.md)
 * [Event➞academic_field](Event_academic_field.md)  <sub>0..\*</sub>
     * Description: A property to describe the scientific subject(s) associated with an academic event, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [schema_value](schema_value.md) and [schema_name](schema_name.md) are mandatory.
     * Range: [AcademicField](AcademicField.md)
 * [Event➞landing_page](Event_landing_page.md)  <sub>0..1</sub>
     * Description: A property to provide the website to which the DOI an academic event is resolving to.
     * Range: [Uri](types/Uri.md)
 * [Event➞has_publication](Event_has_publication.md)  <sub>0..\*</sub>
     * Description: A property to provide the publication associated with
     * Range: [Publication](Publication.md)
 * [Event➞sponsored_by](Event_sponsored_by.md)  <sub>0..\*</sub>
     * Description: A property to provide the sponsors of an academic event.
     * Range: [Sponsor](Sponsor.md)
 * [Event➞website](Event_website.md)  <sub>0..1</sub>
     * Description: A property to provide the URL the official website of an academic event.
     * Range: [Uri](types/Uri.md)
 * [Event➞has_doi](Event_has_doi.md)  <sub>0..\*</sub>
     * Description: A property to provide a digital object identifier (DOI) for an event. This is set automatically.
     * Range: [DigitalObjectId](DigitalObjectId.md)
 * [Event➞umbrella_of](Event_umbrella_of.md)  <sub>0..1</sub>
     * Description: A relation to be used to link an event that hosts several events to its subordinate parts.
     * Range: [String](types/String.md)
 * [Event➞has_umbrella](Event_has_umbrella.md)  <sub>0..1</sub>
     * Description: A relation to be used to link an event to its hosting superordinate event.
     * Range: [String](types/String.md)
 * [Event➞colocated_with](Event_colocated_with.md)  <sub>0..\*</sub>
     * Description: A relation to be used to link an event to one or more other events that share the same location but not the same schedule and that are open to all attendees.
     * Range: [String](types/String.md)
 * [Event➞joint_venture_with](Event_joint_venture_with.md)  <sub>0..\*</sub>
     * Description: A relation to be used to link a series or event to one or more other events that share the same location, have a joint schedule and that are open to all attendees.
     * Range: [String](types/String.md)
 * [Event➞alternative_name](Event_alternative_name.md)  <sub>0..\*</sub>
     * Description: A property to provide alternative names of an academic event.
     * Range: [String](types/String.md)
 * [Event➞former_name](Event_former_name.md)  <sub>0..\*</sub>
     * Description: The former official name of an academic event. Usually this will only be needed in case an academic event has undergone a name change.
     * Range: [String](types/String.md)
 * [Event➞translated_name](Event_translated_name.md)  <sub>0..\*</sub>
     * Description: A translation of the official name of an event to be used in different language contexts.
     * Range: [String](types/String.md)
 * [Event➞context_info](Event_context_info.md)  <sub>0..1</sub>
     * Description: A property to provide extra information for an academic event.
     * Range: [Context](Context.md)
 * [Event➞has_metric](Event_has_metric.md)  <sub>0..\*</sub>
     * Description: A property to provide one ore more metrics of an academic event.
     * Range: [Metric](Metric.md)
 * [Event➞has_topic](Event_has_topic.md)  <sub>0..\*</sub>
     * Description: A property to provide the theme and topics of an event as free keywords, phrases or text.
     * Range: [String](types/String.md)
 * [Event➞external_id](Event_external_id.md)  <sub>0..\*</sub>
     * Description: The property to provide external identifiers for an academic event, including their identifier scheme.
     * Range: [ExternalIdentifier](ExternalIdentifier.md)
 * [Event➞wikidata_id](Event_wikidata_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event with its Wikidata identifier.
     * Range: [WikidataId](WikidataId.md)
 * [Event➞dpbl_id](Event_dpbl_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event with its DBLP identifier.
     * Range: [DblpId](DblpId.md)
 * [Event➞gnd_id](Event_gnd_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event with its GND identifier.
     * Range: [GndId](GndId.md)
 * [ordinal](ordinal.md)  <sub>0..1</sub>
     * Description: The ordnial number of an academic event within its series.
     * Range: [Integer](types/Integer.md)
 * [event_mode](event_mode.md)  <sub>0..1</sub>
     * Description: The event mode describes whether the event is a physical, virtual or hybrid event.
     * Range: [EventMode](EventMode.md)
 * [Event➞tibkat_id](Event_tibkat_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event with its TIBKAT identifier.
     * Range: [TibkatId](TibkatId.md)
 * [Event➞wikicfp_event_id](Event_wikicfp_event_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event with its WikiCFP identifier.
     * Range: [WikiCfpEventId](WikiCfpEventId.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | aeon:0000001 |
| **Close Mappings:** | | sdo:Event |

