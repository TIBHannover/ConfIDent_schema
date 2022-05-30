
# Class: Contributor


A contributor is a person or organization that holds a contributor role which is being realized in an event or event series.

URI: [confident:Contributor](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Contributor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sponsor],[Reviewer],[Presenter],[Organizer],[NamedThing],[Moderator],[ExternalIdentifier],[Contributor&#124;type:ContributorType%20%3F;id:uriorcurie;name:string%20%3F]uses%20-.->[NamedThing],[Contributor]^-[Sponsor],[Contributor]^-[Reviewer],[Contributor]^-[Presenter],[Contributor]^-[Organizer],[Contributor]^-[Moderator],[Contributor]^-[Attendee],[Attendee])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sponsor],[Reviewer],[Presenter],[Organizer],[NamedThing],[Moderator],[ExternalIdentifier],[Contributor&#124;type:ContributorType%20%3F;id:uriorcurie;name:string%20%3F]uses%20-.->[NamedThing],[Contributor]^-[Sponsor],[Contributor]^-[Reviewer],[Contributor]^-[Presenter],[Contributor]^-[Organizer],[Contributor]^-[Moderator],[Contributor]^-[Attendee],[Attendee])

## Uses Mixin

 *  mixin: [NamedThing](NamedThing.md) - A mixin used to provide the attributes needed for the identification of a thing.

## Children

 * [Attendee](Attendee.md) - A person whose only role it is to attend an academic event.
 * [Moderator](Moderator.md) - A person that has the role to moderate an academic event.
 * [Organizer](Organizer.md) - An organizer of an academic event or event series.
 * [Presenter](Presenter.md) - A person that presents its work at an academic event.
 * [Reviewer](Reviewer.md) - A person that has the role to review the submissions of an academic event.
 * [Sponsor](Sponsor.md) - A person or an organization whose role it is to sponsor an academic event or event series.

## Referenced by Class


## Attributes


### Own

 * [Contributor➞type](Contributor_type.md)  <sub>0..1</sub>
     * Description: A property to provide the information whether the contributor is an organization or person.
     * Range: [ContributorType](ContributorType.md)
 * [Contributor➞id](Contributor_id.md)  <sub>1..1</sub>
     * Description: The internal ConfIDent identifier for a contibutor
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from NamedThing:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A property to provide a name of a schema entity.
     * Range: [String](types/String.md)

### Mixed in from NamedThing:

 * [external_id](external_id.md)  <sub>0..\*</sub>
     * Description: A property to provide an external id of a schema entity.
     * Range: [ExternalIdentifier](ExternalIdentifier.md)
