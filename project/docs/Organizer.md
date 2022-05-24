
# Class: Organizer


An organizer of an academic event or event series.

URI: [confident:Organizer](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Organizer)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ContactPerson]<contact%200..1-++[Organizer&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F],[EventSeries]++-%20organized_by%201..*>[Organizer],[Event]++-%20organized_by%201..*>[Organizer],[EventSeries]++-%20organized_by(i)%201..*>[Organizer],[Event]++-%20organized_by(i)%201..*>[Organizer],[Organizer]^-[ContactPerson],[Organizer]^-[CommitteeMember],[Contributor]^-[Organizer],[ExternalIdentifier],[EventSeries],[Event],[Contributor],[ContactPerson],[CommitteeMember])](https://yuml.me/diagram/nofunky;dir:TB/class/[ContactPerson]<contact%200..1-++[Organizer&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F],[EventSeries]++-%20organized_by%201..*>[Organizer],[Event]++-%20organized_by%201..*>[Organizer],[EventSeries]++-%20organized_by(i)%201..*>[Organizer],[Event]++-%20organized_by(i)%201..*>[Organizer],[Organizer]^-[ContactPerson],[Organizer]^-[CommitteeMember],[Contributor]^-[Organizer],[ExternalIdentifier],[EventSeries],[Event],[Contributor],[ContactPerson],[CommitteeMember])

## Parents

 *  is_a: [Contributor](Contributor.md) - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.

## Children

 * [CommitteeMember](CommitteeMember.md) - A members of an academic event committee.
 * [ContactPerson](ContactPerson.md) - The contact person of an academic event or event series.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞organized_by](EventSeries_organized_by.md)*  <sub>1..\*</sub>  **[Organizer](Organizer.md)**
 *  **[Event](Event.md)** *[Event➞organized_by](Event_organized_by.md)*  <sub>1..\*</sub>  **[Organizer](Organizer.md)**
 *  **None** *[organized_by](organized_by.md)*  <sub>1..\*</sub>  **[Organizer](Organizer.md)**

## Attributes


### Own

 * [➞contact](organizer__contact.md)  <sub>0..1</sub>
     * Description: The contact person of an academic event or event series.
     * Range: [ContactPerson](ContactPerson.md)

### Inherited from Contributor:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [String](types/String.md)
