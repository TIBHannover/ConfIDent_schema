
# Class: NamedThing


A mixin used to provide the attributes needed for the identification of a thing.

URI: [confident:NamedThing](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier]<external_id%200..*-++[NamedThing&#124;id:uriorcurie;name:string%20%3F],[Venue]uses%20-.->[NamedThing],[Region]uses%20-.->[NamedThing],[Publication]uses%20-.->[NamedThing],[Country]uses%20-.->[NamedThing],[Contributor]uses%20-.->[NamedThing],[City]uses%20-.->[NamedThing],[Venue],[Region],[Publication],[ExternalIdentifier],[Country],[Contributor],[City])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier]<external_id%200..*-++[NamedThing&#124;id:uriorcurie;name:string%20%3F],[Venue]uses%20-.->[NamedThing],[Region]uses%20-.->[NamedThing],[Publication]uses%20-.->[NamedThing],[Country]uses%20-.->[NamedThing],[Contributor]uses%20-.->[NamedThing],[City]uses%20-.->[NamedThing],[Venue],[Region],[Publication],[ExternalIdentifier],[Country],[Contributor],[City])

## Mixin for

 * [City](City.md) (mixin)  - The city in which an academic event takes place.
 * [Contributor](Contributor.md) (mixin)  - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.
 * [Country](Country.md) (mixin)  - The country in which an academic event takes place.
 * [Publication](Publication.md) (mixin)  - A published work, e.g. proceedings or conferenc paper, that is the output of an academic event or series.
 * [Region](Region.md) (mixin)  - The region in which an academic event takes place. For non USA events this might often be negligible.
 * [Venue](Venue.md) (mixin)  - The venue at which an academic event takes place.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A property to provide an internal id of a schema entity in the ConfIDent plattform.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A property to provide a name of a schema entity.
     * Range: [String](types/String.md)
 * [external_id](external_id.md)  <sub>0..\*</sub>
     * Description: A property to provide an external id of a schema entity.
     * Range: [ExternalIdentifier](ExternalIdentifier.md)
