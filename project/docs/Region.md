
# Class: Region


The region in which an academic event takes place. For non USA events this might often be negligible.

URI: [confident:Region](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Region)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Location]-%20has_region%200..1>[Region&#124;id:uriorcurie;name:string%20%3F],[Region]uses%20-.->[NamedThing],[NamedThing],[Location],[ExternalIdentifier])](https://yuml.me/diagram/nofunky;dir:TB/class/[Location]-%20has_region%200..1>[Region&#124;id:uriorcurie;name:string%20%3F],[Region]uses%20-.->[NamedThing],[NamedThing],[Location],[ExternalIdentifier])

## Uses Mixin

 *  mixin: [NamedThing](NamedThing.md) - A mixin used to provide the attributes needed for the identification of a thing.

## Referenced by Class

 *  **None** *[➞has_region](location__has_region.md)*  <sub>0..1</sub>  **[Region](Region.md)**

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='Texas', description='the US state Texas as an example of a region') |

