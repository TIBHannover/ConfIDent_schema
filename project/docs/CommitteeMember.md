
# Class: CommitteeMember


A members of an academic event committee.

URI: [confident:CommitteeMember](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#CommitteeMember)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organizer],[ExternalIdentifier],[ContactPerson],[CommitteeMember&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F]^-[CommitteeChair],[Organizer]^-[CommitteeMember],[CommitteeChair])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organizer],[ExternalIdentifier],[ContactPerson],[CommitteeMember&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F]^-[CommitteeChair],[Organizer]^-[CommitteeMember],[CommitteeChair])

## Parents

 *  is_a: [Organizer](Organizer.md) - An organizer of an academic event or event series.

## Children

 * [CommitteeChair](CommitteeChair.md) - The head of an academic event committee.

## Referenced by Class


## Attributes


### Inherited from Organizer:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [String](types/String.md)
 * [➞contact](organizer__contact.md)  <sub>0..1</sub>
     * Description: The contact person of an academic event or event series.
     * Range: [ContactPerson](ContactPerson.md)
