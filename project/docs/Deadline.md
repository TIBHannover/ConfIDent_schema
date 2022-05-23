
# Class: Deadline


A container for event deadlines.

URI: [confident:Deadline](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Deadline)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]++-%20has_deadline%200..*>[Deadline&#124;type:DeadlineType;deadline_date:datetime;deadline_other:string%20%3F],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]++-%20has_deadline%200..*>[Deadline&#124;type:DeadlineType;deadline_date:datetime;deadline_other:string%20%3F],[Event])

## Referenced by Class

 *  **None** *[has_deadline](has_deadline.md)*  <sub>0..\*</sub>  **[Deadline](Deadline.md)**

## Attributes


### Own

 * [Deadline➞type](Deadline_type.md)  <sub>1..1</sub>
     * Description: A propery to provide the type of the deadline.
     * Range: [DeadlineType](DeadlineType.md)
 * [➞deadline_date](deadline__deadline_date.md)  <sub>1..1</sub>
     * Description: The date of a deadline.
     * Range: [Datetime](types/Datetime.md)
 * [➞deadline_other](deadline__deadline_other.md)  <sub>0..1</sub>
     * Description: A property to specify another type of deadline, if this type of deadline is not within the allowed values of [DeadlineType](DeadlineType.md).
     * Range: [String](types/String.md)
