
# Class: WikidataId


The identifier of a thing (item) in Wikidata.

URI: [confident:WikidataId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#WikidataId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20wikidata_id%200..*>[WikidataId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20wikidata_id%200..*>[WikidataId],[EventSeries]++-%20wikidata_id(i)%200..*>[WikidataId],[Event]++-%20wikidata_id(i)%200..*>[WikidataId],[ExternalIdentifier]^-[WikidataId],[ExternalIdentifier],[EventSeries],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20wikidata_id%200..*>[WikidataId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20wikidata_id%200..*>[WikidataId],[EventSeries]++-%20wikidata_id(i)%200..*>[WikidataId],[Event]++-%20wikidata_id(i)%200..*>[WikidataId],[ExternalIdentifier]^-[WikidataId],[ExternalIdentifier],[EventSeries],[Event])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞wikidata_id](EventSeries_wikidata_id.md)*  <sub>0..\*</sub>  **[WikidataId](WikidataId.md)**
 *  **[Event](Event.md)** *[Event➞wikidata_id](Event_wikidata_id.md)*  <sub>0..\*</sub>  **[WikidataId](WikidataId.md)**
 *  **None** *[wikidata_id](wikidata_id.md)*  <sub>0..\*</sub>  **[WikidataId](WikidataId.md)**

## Attributes


### Own

 * [WikidataId➞schema_name](WikidataId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [WikidataId➞schema_base_uri](WikidataId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | wikidata:Q43649390 |

