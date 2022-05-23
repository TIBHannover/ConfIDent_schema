
# Class: EventSeries


An academic event series describes the set of academic events which take place on a regular basis and thus have an established common identity. This identity is constituted, for example, through institutional continuity in the hosting of a series (e.g. by a specialised society), thematic focuses and/or a common label under which a series is defined (particularly name and acronym). Nevertheless, it is possible that each of these criteria may change over time.

URI: [confident:EventSeries](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#EventSeries)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WikidataId],[WikiCfpSeriesId],[Sponsor],[Publication],[Organizer],[Metric],[GndId],[ExternalIdentifier],[WikiCfpSeriesId]<wikicfp_series_id%200..*-++[EventSeries&#124;id:uriorcurie;official_name:string;has_acronym:string%20%3F;landing_page:uri%20%3F;website:uri%20%3F;alternative_name:string%20*;former_name:string%20%3F;translated_name:string%20*;has_topic:string%20*],[GndId]<gnd_id%200..*-++[EventSeries],[DblpId]<dpbl_id%200..*-++[EventSeries],[WikidataId]<wikidata_id%200..*-++[EventSeries],[ExternalIdentifier]<external_id%200..*-++[EventSeries],[Metric]<has_metric%200..*-++[EventSeries],[Context]<context_info%200..1-++[EventSeries],[Event]<series_of%200..1-%20[EventSeries],[DigitalObjectId]<has_doi%200..*-++[EventSeries],[Sponsor]<sponsored_by%200..*-++[EventSeries],[Publication]<has_publication%200..*-++[EventSeries],[AcademicField]<academic_field%200..*-++[EventSeries],[Organizer]<organized_by%201..*-++[EventSeries],[ConfIDentRecords]++-%20series%200..*>[EventSeries],[Event]-%20in_series%200..1>[EventSeries],[Event],[DigitalObjectId],[DblpId],[Context],[ConfIDentRecords],[AcademicField])](https://yuml.me/diagram/nofunky;dir:TB/class/[WikidataId],[WikiCfpSeriesId],[Sponsor],[Publication],[Organizer],[Metric],[GndId],[ExternalIdentifier],[WikiCfpSeriesId]<wikicfp_series_id%200..*-++[EventSeries&#124;id:uriorcurie;official_name:string;has_acronym:string%20%3F;landing_page:uri%20%3F;website:uri%20%3F;alternative_name:string%20*;former_name:string%20%3F;translated_name:string%20*;has_topic:string%20*],[GndId]<gnd_id%200..*-++[EventSeries],[DblpId]<dpbl_id%200..*-++[EventSeries],[WikidataId]<wikidata_id%200..*-++[EventSeries],[ExternalIdentifier]<external_id%200..*-++[EventSeries],[Metric]<has_metric%200..*-++[EventSeries],[Context]<context_info%200..1-++[EventSeries],[Event]<series_of%200..1-%20[EventSeries],[DigitalObjectId]<has_doi%200..*-++[EventSeries],[Sponsor]<sponsored_by%200..*-++[EventSeries],[Publication]<has_publication%200..*-++[EventSeries],[AcademicField]<academic_field%200..*-++[EventSeries],[Organizer]<organized_by%201..*-++[EventSeries],[ConfIDentRecords]++-%20series%200..*>[EventSeries],[Event]-%20in_series%200..1>[EventSeries],[Event],[DigitalObjectId],[DblpId],[Context],[ConfIDentRecords],[AcademicField])

## Referenced by Class

 *  **[ConfIDentRecords](ConfIDentRecords.md)** *[ConfIDentRecords➞series](confIDentRecords__series.md)*  <sub>0..\*</sub>  **[EventSeries](EventSeries.md)**
 *  **None** *[in_series](in_series.md)*  <sub>0..1</sub>  **[EventSeries](EventSeries.md)**

## Attributes


### Own

 * [EventSeries➞id](EventSeries_id.md)  <sub>1..1</sub>
     * Description: A property to provide the internal identifier of an academic event series.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [EventSeries➞official_name](EventSeries_official_name.md)  <sub>1..1</sub>
     * Description: A property to provide the the official name of an academic event series.
     * Range: [String](types/String.md)
 * [EventSeries➞organized_by](EventSeries_organized_by.md)  <sub>1..\*</sub>
     * Description: A property to provide the organizer of an academic event series.
     * Range: [Organizer](Organizer.md)
 * [EventSeries➞has_acronym](EventSeries_has_acronym.md)  <sub>0..1</sub>
     * Description: The official acronym of an academic event series.
     * Range: [String](types/String.md)
 * [EventSeries➞academic_field](EventSeries_academic_field.md)  <sub>0..\*</sub>
     * Description: A property to describe the scientific subject(s) associated with an academic event series, according to some controlled vocabulary or thesaurus. If this is used, its subproperties [Schema Value](schema_value.md) and [Schema Name](schema_name.md) are mandatory.
     * Range: [AcademicField](AcademicField.md)
 * [EventSeries➞landing_page](EventSeries_landing_page.md)  <sub>0..1</sub>
     * Description: A property to provide the website to which the DOI an academic event series is resolving to.
     * Range: [Uri](types/Uri.md)
 * [EventSeries➞has_publication](EventSeries_has_publication.md)  <sub>0..\*</sub>
     * Description: A property to provide the publication associated with
     * Range: [Publication](Publication.md)
 * [EventSeries➞sponsored_by](EventSeries_sponsored_by.md)  <sub>0..\*</sub>
     * Description: A property to provide the sponsors of an academic event series.
     * Range: [Sponsor](Sponsor.md)
 * [EventSeries➞website](EventSeries_website.md)  <sub>0..1</sub>
     * Description: A property to provide the URL the official website of an academic event series.
     * Range: [Uri](types/Uri.md)
 * [EventSeries➞has_doi](EventSeries_has_doi.md)  <sub>0..\*</sub>
     * Description: A property to provide a digital object identifier (DOI) for an event series. This is set automatically.
     * Range: [DigitalObjectId](DigitalObjectId.md)
 * [series_of](series_of.md)  <sub>0..1</sub>
     * Description: A property to link to the events that are part of an academic event series.
     * Range: [Event](Event.md)
 * [EventSeries➞alternative_name](EventSeries_alternative_name.md)  <sub>0..\*</sub>
     * Description: A property to provide alternative names of an academic event series.
     * Range: [String](types/String.md)
 * [EventSeries➞former_name](EventSeries_former_name.md)  <sub>0..1</sub>
     * Description: The former official name of an academic event series. Usually this will only be needed in case an academic event series has undergone a name change.
     * Range: [String](types/String.md)
 * [EventSeries➞translated_name](EventSeries_translated_name.md)  <sub>0..\*</sub>
     * Description: A translation of the official name of an event series to be used in different language contexts.
     * Range: [String](types/String.md)
 * [EventSeries➞context_info](EventSeries_context_info.md)  <sub>0..1</sub>
     * Description: A property to provide extra information for an academic event series.
     * Range: [Context](Context.md)
 * [EventSeries➞has_metric](EventSeries_has_metric.md)  <sub>0..\*</sub>
     * Description: A property to provide one ore more metrics of an academic event series.
     * Range: [Metric](Metric.md)
 * [EventSeries➞has_topic](EventSeries_has_topic.md)  <sub>0..\*</sub>
     * Description: A property to provide the theme and topics of an event series as free keywords, phrases or text.
     * Range: [String](types/String.md)
 * [EventSeries➞external_id](EventSeries_external_id.md)  <sub>0..\*</sub>
     * Description: The property to provide external identifiers for an academic event series, including their identifier scheme.
     * Range: [ExternalIdentifier](ExternalIdentifier.md)
 * [EventSeries➞wikidata_id](EventSeries_wikidata_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event series with its Wikidata identifier.
     * Range: [WikidataId](WikidataId.md)
 * [EventSeries➞dpbl_id](EventSeries_dpbl_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event series with its DBLP identifier.
     * Range: [DblpId](DblpId.md)
 * [EventSeries➞gnd_id](EventSeries_gnd_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event series with its GND identifier.
     * Range: [GndId](GndId.md)
 * [EventSeries➞wikicfp_series_id](EventSeries_wikicfp_series_id.md)  <sub>0..\*</sub>
     * Description: A property to link an academic event series with its WikiCFP identifier.
     * Range: [WikiCfpSeriesId](WikiCfpSeriesId.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | aeon:0000002 |
| **Close Mappings:** | | sdo:EventSeries |

