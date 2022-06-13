
# Class: DigitalObjectId


A centrally registered identifier symbol used to uniquely identify digital objects given by International DOI Foundation.

URI: [confident:DigitalObjectId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#DigitalObjectId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[EventSeries],[Event],[EventSeries]++-%20has_doi%200..*>[DigitalObjectId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20has_doi%200..*>[DigitalObjectId],[EventSeries]++-%20has_doi(i)%200..*>[DigitalObjectId],[Event]++-%20has_doi(i)%200..*>[DigitalObjectId],[Publication]++-%20has_doi%200..*>[DigitalObjectId],[ExternalIdentifier]^-[DigitalObjectId],[Publication])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[EventSeries],[Event],[EventSeries]++-%20has_doi%200..*>[DigitalObjectId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20has_doi%200..*>[DigitalObjectId],[EventSeries]++-%20has_doi(i)%200..*>[DigitalObjectId],[Event]++-%20has_doi(i)%200..*>[DigitalObjectId],[Publication]++-%20has_doi%200..*>[DigitalObjectId],[ExternalIdentifier]^-[DigitalObjectId],[Publication])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞has_doi](EventSeries_has_doi.md)*  <sub>0..\*</sub>  **[DigitalObjectId](DigitalObjectId.md)**
 *  **[Event](Event.md)** *[Event➞has_doi](Event_has_doi.md)*  <sub>0..\*</sub>  **[DigitalObjectId](DigitalObjectId.md)**
 *  **None** *[has_doi](has_doi.md)*  <sub>0..\*</sub>  **[DigitalObjectId](DigitalObjectId.md)**

## Attributes


### Own

 * [DigitalObjectId➞schema_name](DigitalObjectId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [DigitalObjectId➞schema_base_uri](DigitalObjectId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | OBI:0002110 |

