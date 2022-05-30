
# Class: Reviewer


A person that has the role to review the submissions of an academic event.

URI: [confident:Reviewer](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Reviewer)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Contributor]^-[Reviewer&#124;type(i):ContributorType%20%3F;id(i):uriorcurie;name(i):string%20%3F],[ExternalIdentifier],[Contributor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Contributor]^-[Reviewer&#124;type(i):ContributorType%20%3F;id(i):uriorcurie;name(i):string%20%3F],[ExternalIdentifier],[Contributor])

## Parents

 *  is_a: [Contributor](Contributor.md) - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.

## Attributes


### Inherited from Contributor:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [ContributorType](ContributorType.md)
 * [Contributor➞id](Contributor_id.md)  <sub>1..1</sub>
     * Description: The internal ConfIDent identifier for a contibutor
     * Range: [Uriorcurie](types/Uriorcurie.md)
