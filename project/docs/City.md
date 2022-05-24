
# Class: City


The city in which an academic event takes place.

URI: [confident:City](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#City)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ExternalIdentifier],[Location]-%20has_city%200..1>[City&#124;id:uriorcurie;name:string%20%3F],[City]uses%20-.->[NamedThing],[Location])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ExternalIdentifier],[Location]-%20has_city%200..1>[City&#124;id:uriorcurie;name:string%20%3F],[City]uses%20-.->[NamedThing],[Location])

## Uses Mixin

 *  mixin: [NamedThing](NamedThing.md) - A mixin used to provide the attributes needed for the identification of a thing.

## Referenced by Class

 *  **None** *[➞has_city](location__has_city.md)*  <sub>0..1</sub>  **[City](City.md)**

## Attributes


### Mixed in from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A property to provide an internal id of a schema entity in the ConfIDent plattform.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from NamedThing:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A property to provide a name of a schema entity.
     * Range: [String](types/String.md)

### Mixed in from NamedThing:

 * [external_id](external_id.md)  <sub>0..\*</sub>
     * Description: A property to provide an external id of a schema entity.
     * Range: [ExternalIdentifier](ExternalIdentifier.md)
