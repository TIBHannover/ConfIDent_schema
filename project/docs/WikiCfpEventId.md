
# Class: WikiCfpEventId


The identifier of an academic event or series in WikiCFP.

URI: [confident:WikiCfpEventId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#WikiCfpEventId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]++-%20wikicfp_event_id%200..*>[WikiCfpEventId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20wikicfp_event_id(i)%200..*>[WikiCfpEventId],[ExternalIdentifier]^-[WikiCfpEventId],[ExternalIdentifier],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]++-%20wikicfp_event_id%200..*>[WikiCfpEventId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[Event]++-%20wikicfp_event_id(i)%200..*>[WikiCfpEventId],[ExternalIdentifier]^-[WikiCfpEventId],[ExternalIdentifier],[Event])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[Event](Event.md)** *[Event➞wikicfp_event_id](Event_wikicfp_event_id.md)*  <sub>0..\*</sub>  **[WikiCfpEventId](WikiCfpEventId.md)**
 *  **None** *[wikicfp_event_id](wikicfp_event_id.md)*  <sub>0..\*</sub>  **[WikiCfpEventId](WikiCfpEventId.md)**

## Attributes


### Own

 * [WikiCfpEventId➞schema_name](WikiCfpEventId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [WikiCfpEventId➞schema_base_uri](WikiCfpEventId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)
