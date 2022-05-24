
# Class: AcademicField


An academic field is the scientific subject of an event or event series according to some controlled vocabulary or thesaurus and as such requires the scheme URI.

URI: [confident:AcademicField](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#AcademicField)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SchemaBasedThing],[EventSeries],[Event],[EventSeries]++-%20academic_field%200..*>[AcademicField&#124;schema_value:string;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F],[Event]++-%20academic_field%200..*>[AcademicField],[EventSeries]++-%20academic_field(i)%200..*>[AcademicField],[Event]++-%20academic_field(i)%200..*>[AcademicField],[AcademicField]uses%20-.->[SchemaBasedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[SchemaBasedThing],[EventSeries],[Event],[EventSeries]++-%20academic_field%200..*>[AcademicField&#124;schema_value:string;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F],[Event]++-%20academic_field%200..*>[AcademicField],[EventSeries]++-%20academic_field(i)%200..*>[AcademicField],[Event]++-%20academic_field(i)%200..*>[AcademicField],[AcademicField]uses%20-.->[SchemaBasedThing])

## Uses Mixin

 *  mixin: [SchemaBasedThing](SchemaBasedThing.md) - A mixin used in classes that contain schema based values, such as the classifications used to denote the academic field of an event or the external identifiers used to denote a thing.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞academic_field](EventSeries_academic_field.md)*  <sub>0..\*</sub>  **[AcademicField](AcademicField.md)**
 *  **[Event](Event.md)** *[Event➞academic_field](Event_academic_field.md)*  <sub>0..\*</sub>  **[AcademicField](AcademicField.md)**
 *  **None** *[academic_field](academic_field.md)*  <sub>0..\*</sub>  **[AcademicField](AcademicField.md)**

## Attributes


### Own

 * [AcademicField➞schema_value](AcademicField_schema_value.md)  <sub>1..1</sub>
     * Description: The classification label of a certain classification schema.
     * Range: [String](types/String.md)

### Mixed in from SchemaBasedThing:

 * [schema_name](schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)

### Mixed in from SchemaBasedThing:

 * [schema_base_uri](schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)
