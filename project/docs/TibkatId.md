
# Class: TibkatId


The identifier of a publication in the TIB catalog that references an event or event series.

URI: [confident:TibkatId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#TibkatId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]++-%20tibkat_id%200..*>[TibkatId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20tibkat_id(i)%200..*>[TibkatId],[ExternalIdentifier]^-[TibkatId],[ExternalIdentifier],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]++-%20tibkat_id%200..*>[TibkatId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20tibkat_id(i)%200..*>[TibkatId],[ExternalIdentifier]^-[TibkatId],[ExternalIdentifier],[Event])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[Event](Event.md)** *[Event➞tibkat_id](Event_tibkat_id.md)*  <sub>0..\*</sub>  **[TibkatId](TibkatId.md)**
 *  **None** *[tibkat_id](tibkat_id.md)*  <sub>0..\*</sub>  **[TibkatId](TibkatId.md)**

## Attributes


### Own

 * [TibkatId➞schema_name](TibkatId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [TibkatId➞schema_base_uri](TibkatId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)
