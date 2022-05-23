
# Class: GndId


The identifier of a thing (item) in the German National authority file.

URI: [confident:GndId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#GndId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20gnd_id%200..*>[GndId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20gnd_id%200..*>[GndId],[EventSeries]++-%20gnd_id(i)%200..*>[GndId],[Event]++-%20gnd_id(i)%200..*>[GndId],[ExternalIdentifier]^-[GndId],[ExternalIdentifier],[EventSeries],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20gnd_id%200..*>[GndId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20gnd_id%200..*>[GndId],[EventSeries]++-%20gnd_id(i)%200..*>[GndId],[Event]++-%20gnd_id(i)%200..*>[GndId],[ExternalIdentifier]^-[GndId],[ExternalIdentifier],[EventSeries],[Event])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞gnd_id](EventSeries_gnd_id.md)*  <sub>0..\*</sub>  **[GndId](GndId.md)**
 *  **[Event](Event.md)** *[Event➞gnd_id](Event_gnd_id.md)*  <sub>0..\*</sub>  **[GndId](GndId.md)**
 *  **None** *[gnd_id](gnd_id.md)*  <sub>0..\*</sub>  **[GndId](GndId.md)**

## Attributes


### Own

 * [GndId➞schema_name](GndId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [GndId➞schema_base_uri](GndId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)
