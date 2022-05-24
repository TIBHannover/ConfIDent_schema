
# Class: Publication


A published work, e.g. proceedings or conferenc paper, that is the output of an academic event or series.

URI: [confident:Publication](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DigitalObjectId]<has_doi%200..*-++[Publication&#124;id:uriorcurie;name:string%20%3F],[EventSeries]++-%20has_publication%200..*>[Publication],[Event]++-%20has_publication%200..*>[Publication],[EventSeries]++-%20has_publication(i)%200..*>[Publication],[Event]++-%20has_publication(i)%200..*>[Publication],[Publication]uses%20-.->[NamedThing],[NamedThing],[ExternalIdentifier],[EventSeries],[Event],[DigitalObjectId])](https://yuml.me/diagram/nofunky;dir:TB/class/[DigitalObjectId]<has_doi%200..*-++[Publication&#124;id:uriorcurie;name:string%20%3F],[EventSeries]++-%20has_publication%200..*>[Publication],[Event]++-%20has_publication%200..*>[Publication],[EventSeries]++-%20has_publication(i)%200..*>[Publication],[Event]++-%20has_publication(i)%200..*>[Publication],[Publication]uses%20-.->[NamedThing],[NamedThing],[ExternalIdentifier],[EventSeries],[Event],[DigitalObjectId])

## Uses Mixin

 *  mixin: [NamedThing](NamedThing.md) - A mixin used to provide the attributes needed for the identification of a thing.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞has_publication](EventSeries_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **[Event](Event.md)** *[Event➞has_publication](Event_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **None** *[has_publication](has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [has_doi](has_doi.md)  <sub>0..\*</sub>
     * Description: A property to provide a digital object identifier (DOI) according to https://doi.org/.
     * Range: [DigitalObjectId](DigitalObjectId.md)

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
