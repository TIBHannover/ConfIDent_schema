
# Class: Presenter


A person that presents its work at an academic event.

URI: [confident:Presenter](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Presenter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Presenter&#124;type(i):ContributorType%20%3F;id(i):uriorcurie;name(i):string%20%3F]^-[KeynoteSpeaker],[Contributor]^-[Presenter],[KeynoteSpeaker],[ExternalIdentifier],[Contributor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Presenter&#124;type(i):ContributorType%20%3F;id(i):uriorcurie;name(i):string%20%3F]^-[KeynoteSpeaker],[Contributor]^-[Presenter],[KeynoteSpeaker],[ExternalIdentifier],[Contributor])

## Parents

 *  is_a: [Contributor](Contributor.md) - A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.

## Children

 * [KeynoteSpeaker](KeynoteSpeaker.md) - A 'keynote speaker' is a presenter that is an invited person - often a multiplier in his or her (research) field - responsible for delivering a keynote speech.

## Referenced by Class


## Attributes


### Inherited from Contributor:

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [ContributorType](ContributorType.md)
 * [Contributor➞id](Contributor_id.md)  <sub>1..1</sub>
     * Description: The internal ConfIDent identifier for a contibutor
     * Range: [Uriorcurie](types/Uriorcurie.md)
