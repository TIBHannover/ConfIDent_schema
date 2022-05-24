
# Class: DblpId


The identifier of an academic event or series in dblp.

URI: [confident:DblpId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#DblpId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[EventSeries],[Event],[EventSeries]++-%20dpbl_id%200..*>[DblpId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20dpbl_id%200..*>[DblpId],[EventSeries]++-%20dpbl_id(i)%200..*>[DblpId],[Event]++-%20dpbl_id(i)%200..*>[DblpId],[ExternalIdentifier]^-[DblpId])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[EventSeries],[Event],[EventSeries]++-%20dpbl_id%200..*>[DblpId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20dpbl_id%200..*>[DblpId],[EventSeries]++-%20dpbl_id(i)%200..*>[DblpId],[Event]++-%20dpbl_id(i)%200..*>[DblpId],[ExternalIdentifier]^-[DblpId])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞dpbl_id](EventSeries_dpbl_id.md)*  <sub>0..\*</sub>  **[DblpId](DblpId.md)**
 *  **[Event](Event.md)** *[Event➞dpbl_id](Event_dpbl_id.md)*  <sub>0..\*</sub>  **[DblpId](DblpId.md)**
 *  **None** *[dpbl_id](dpbl_id.md)*  <sub>0..\*</sub>  **[DblpId](DblpId.md)**

## Attributes


### Own

 * [DblpId➞schema_name](DblpId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [DblpId➞schema_base_uri](DblpId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)
