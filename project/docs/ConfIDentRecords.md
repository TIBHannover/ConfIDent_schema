
# Class: ConfIDentRecords


A container to be able to bundle academic event data and series in one data file (e.g. YAML or JSON).

URI: [confident:ConfIDentRecords](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#ConfIDentRecords)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries],[Event],[EventSeries]<series%200..*-++[ConfIDentRecords],[Event]<events%200..*-++[ConfIDentRecords])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries],[Event],[EventSeries]<series%200..*-++[ConfIDentRecords],[Event]<events%200..*-++[ConfIDentRecords])

## Referenced by Class


## Attributes


### Own

 * [ConfIDentRecords➞events](confIDentRecords__events.md)  <sub>0..\*</sub>
     * Description: A property to provide a list of academic events within this container.
     * Range: [Event](Event.md)
 * [ConfIDentRecords➞series](confIDentRecords__series.md)  <sub>0..\*</sub>
     * Description: A property to provide a list of academic event series within this container.
     * Range: [EventSeries](EventSeries.md)
