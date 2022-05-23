
# Class: SchemaBasedThing


A mixin used in classes that contain schema based values, such as the classifications used to denote the academic field of an event or the external identifiers used to denote a thing.

URI: [confident:SchemaBasedThing](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#SchemaBasedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier]uses%20-.->[SchemaBasedThing&#124;schema_value:string%20%3F;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F],[AcademicField]uses%20-.->[SchemaBasedThing],[ExternalIdentifier],[AcademicField])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier]uses%20-.->[SchemaBasedThing&#124;schema_value:string%20%3F;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F],[AcademicField]uses%20-.->[SchemaBasedThing],[ExternalIdentifier],[AcademicField])

## Mixin for

 * [AcademicField](AcademicField.md) (mixin)  - An academic field is the scientific subject of an event or event series according to some controlled vocabulary or thesaurus and as such requires the scheme URI.
 * [ExternalIdentifier](ExternalIdentifier.md) (mixin)  - An identifer of an entity declared in another schema.

## Referenced by Class


## Attributes


### Own

 * [schema_value](schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)
 * [schema_name](schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [schema_base_uri](schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)
