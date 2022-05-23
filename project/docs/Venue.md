
# Class: Venue


The venue at which an academic event takes place.

URI: [confident:Venue](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Venue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Location]-%20has_venue%200..1>[Venue&#124;street:string%20%3F;zip_code:string%20%3F;id:uriorcurie;name:string%20%3F],[Venue]uses%20-.->[NamedThing],[NamedThing],[Location],[ExternalIdentifier])](https://yuml.me/diagram/nofunky;dir:TB/class/[Location]-%20has_venue%200..1>[Venue&#124;street:string%20%3F;zip_code:string%20%3F;id:uriorcurie;name:string%20%3F],[Venue]uses%20-.->[NamedThing],[NamedThing],[Location],[ExternalIdentifier])

## Uses Mixin

 *  mixin: [NamedThing](NamedThing.md) - A mixin used to provide the attributes needed for the identification of a thing.

## Referenced by Class

 *  **None** *[➞has_venue](location__has_venue.md)*  <sub>0..1</sub>  **[Venue](Venue.md)**

## Attributes


### Own

 * [➞street](venue__street.md)  <sub>0..1</sub>
     * Description: The street of the venue including the house number seperated by comma.
     * Range: [String](types/String.md)
     * Example: Am Welfengarten, 1 street, hous number
 * [➞zip_code](venue__zip_code.md)  <sub>0..1</sub>
     * Description: The zip code of the venue.
     * Range: [String](types/String.md)

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
