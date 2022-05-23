
# Class: ContactPerson


The contact person of an academic event or event series.

URI: [confident:ContactPerson](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#ContactPerson)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organizer],[ExternalIdentifier],[Organizer]++-%20contact%200..1>[ContactPerson&#124;email:string%20%3F;telephone:string%20%3F;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F],[Organizer]^-[ContactPerson])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organizer],[ExternalIdentifier],[Organizer]++-%20contact%200..1>[ContactPerson&#124;email:string%20%3F;telephone:string%20%3F;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F],[Organizer]^-[ContactPerson])

## Parents

 *  is_a: [Organizer](Organizer.md) - An organizer of an academic event or event series.

## Referenced by Class

 *  **None** *[➞contact](organizer__contact.md)*  <sub>0..1</sub>  **[ContactPerson](ContactPerson.md)**

## Attributes


### Own

 * [➞email](contactPerson__email.md)  <sub>0..1</sub>
     * Description: The email address of the contact person.
     * Range: [String](types/String.md)
 * [➞telephone](contactPerson__telephone.md)  <sub>0..1</sub>
     * Description: The telephone number of the contact person.
     * Range: [String](types/String.md)

### Inherited from Organizer:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [String](types/String.md)
 * [➞contact](organizer__contact.md)  <sub>0..1</sub>
     * Description: The contact person of an academic event or event series.
     * Range: [ContactPerson](ContactPerson.md)
