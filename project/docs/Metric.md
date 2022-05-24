
# Class: Metric


A container for statistical information about an event or event series.

URI: [confident:Metric](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Metric)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20has_metric%200..*>[Metric&#124;type:MetricType%20%3F;int_value:integer%20%3F;str_value:string%20%3F;rate_value:float%20%3F;truth_value:boolean%20%3F;metric_year:string%20%3F;description:string%20%3F],[Event]++-%20has_metric%200..*>[Metric],[EventSeries]++-%20has_metric(i)%200..*>[Metric],[Event]++-%20has_metric(i)%200..*>[Metric],[EventSeries],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20has_metric%200..*>[Metric&#124;type:MetricType%20%3F;int_value:integer%20%3F;str_value:string%20%3F;rate_value:float%20%3F;truth_value:boolean%20%3F;metric_year:string%20%3F;description:string%20%3F],[Event]++-%20has_metric%200..*>[Metric],[EventSeries]++-%20has_metric(i)%200..*>[Metric],[Event]++-%20has_metric(i)%200..*>[Metric],[EventSeries],[Event])

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞has_metric](EventSeries_has_metric.md)*  <sub>0..\*</sub>  **[Metric](Metric.md)**
 *  **[Event](Event.md)** *[Event➞has_metric](Event_has_metric.md)*  <sub>0..\*</sub>  **[Metric](Metric.md)**
 *  **None** *[has_metric](has_metric.md)*  <sub>0..\*</sub>  **[Metric](Metric.md)**

## Attributes


### Own

 * [Metric➞type](Metric_type.md)  <sub>0..1</sub>
     * Description: A property to provide the type of relation between academic events.
     * Range: [MetricType](MetricType.md)
 * [➞int_value](metric__int_value.md)  <sub>0..1</sub>
     * Description: A property to provide an integer value for a metric.
     * Range: [Integer](types/Integer.md)
 * [➞str_value](metric__str_value.md)  <sub>0..1</sub>
     * Description: A property to provide a string value for a metric.
     * Range: [String](types/String.md)
 * [➞rate_value](metric__rate_value.md)  <sub>0..1</sub>
     * Description: A property to provide a rate value as float for a metric.
     * Range: [Float](types/Float.md)
 * [➞truth_value](metric__truth_value.md)  <sub>0..1</sub>
     * Description: A property to provide a truth value for a metric.
     * Range: [Boolean](types/Boolean.md)
 * [➞metric_year](metric__metric_year.md)  <sub>0..1</sub>
     * Description: A property to provide the year for which the metric value is valid.
     * Range: [String](types/String.md)
 * [➞description](metric__description.md)  <sub>0..1</sub>
     * Description: A property to provide a description of a metric.
     * Range: [String](types/String.md)
