
# Class: CommitteeChair


The head of an academic event committee.

URI: [confident:CommitteeChair](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#CommitteeChair)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[ContactPerson],[CommitteeMember],[CommitteeMember]^-[CommitteeChair&#124;type(i):ContributorType%20%3F;id(i):uriorcurie;name(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[ContactPerson],[CommitteeMember],[CommitteeMember]^-[CommitteeChair&#124;type(i):ContributorType%20%3F;id(i):uriorcurie;name(i):string%20%3F])

## Parents

 *  is_a: [CommitteeMember](CommitteeMember.md) - A members of an academic event committee.

## Attributes


### Inherited from CommitteeMember:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [ContributorType](ContributorType.md)
 * [Contributor➞id](Contributor_id.md)  <sub>1..1</sub>
     * Description: The internal ConfIDent identifier for a contibutor
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞contact](organizer__contact.md)  <sub>0..1</sub>
     * Description: The contact person of an academic event or event series.
     * Range: [ContactPerson](ContactPerson.md)
