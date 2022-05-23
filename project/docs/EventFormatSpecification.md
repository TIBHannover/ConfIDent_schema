
# Class: EventFormatSpecification


An academic event format specification is a plan specification that classifies a planned gathering of people in an academic context according to some sociocultural format, which provides implicit and explicit details on how this gathing is to be carried out by its participants in terms of achieving certain objectives, fulfiling certain conditions and performing certain actions. It thus concretizes the expectations of the contributors of an academic event. While the explicit details are often provied as concrete parts (e.g. deadline or attendance fee specifications), the implicit details depend on the semantics encoded in the words used for the classification of academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications can overlap or vary to a certain degree.

URI: [confident:EventFormatSpecification](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#EventFormatSpecification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventFormatSpecification&#124;other_format:string])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventFormatSpecification&#124;other_format:string])

## Referenced by Class

 *  **None** *[event_format](event_format.md)*  <sub>0..1</sub>  **[EventFormatSpecification](EventFormatSpecification.md)**

## Attributes


### Own

 * [➞other_format](eventFormatSpecification__other_format.md)  <sub>1..1</sub>
     * Description: A mandatory property to provide the format of an academic event as string, in order to further specify its type in case it could not be specified according to the possible values of [Event Type](EventType.md).
     * Range: [String](types/String.md)
     * Example: ad-hoc meeting of university presidents An example to provide a format specification for special type of academic event that is not in the schema's [EventType](EventType) enum.

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | aeon:0000004 |

