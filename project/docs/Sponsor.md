
# Class: Sponsor


A person or an organization whose role it is to sponsor an academic event or event series.

URI: [confident:Sponsor](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Sponsor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20sponsored_by%200..*>[Sponsor&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F],[Event]++-%20sponsored_by%200..*>[Sponsor],[EventSeries]++-%20sponsored_by(i)%200..*>[Sponsor],[Event]++-%20sponsored_by(i)%200..*>[Sponsor],[Contributor]^-[Sponsor],[ExternalIdentifier],[EventSeries],[Event],[Contributor])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20sponsored_by%200..*>[Sponsor&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F],[Event]++-%20sponsored_by%200..*>[Sponsor],[EventSeries]++-%20sponsored_by(i)%200..*>[Sponsor],[Event]++-%20sponsored_by(i)%200..*>[Sponsor],[Contributor]^-[Sponsor],[ExternalIdentifier],[EventSeries],[Event],[Contributor])

## Parents

 *  is_a: [Contributor](Contributor.md) - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞sponsored_by](EventSeries_sponsored_by.md)*  <sub>0..\*</sub>  **[Sponsor](Sponsor.md)**
 *  **[Event](Event.md)** *[Event➞sponsored_by](Event_sponsored_by.md)*  <sub>0..\*</sub>  **[Sponsor](Sponsor.md)**
 *  **None** *[sponsored_by](sponsored_by.md)*  <sub>0..\*</sub>  **[Sponsor](Sponsor.md)**

## Attributes


### Inherited from Contributor:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [String](types/String.md)
