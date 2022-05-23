
# Class: Attendee


A person whose only role it is to attend an academic event.

URI: [confident:Attendee](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Attendee)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[Contributor],[Contributor]^-[Attendee&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalIdentifier],[Contributor],[Contributor]^-[Attendee&#124;type(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F])

## Parents

 *  is_a: [Contributor](Contributor.md) - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.

## Attributes


### Inherited from Contributor:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [String](types/String.md)
