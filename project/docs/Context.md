
# Class: Context


A container to provide extra information, such as call of papers event description.

URI: [confident:Context](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Context)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries],[Event],[EventSeries]++-%20context_info%200..1>[Context&#124;text:string%20%3F;license_str:string%20%3F;license_url:uriorcurie%20%3F],[Event]++-%20context_info%200..1>[Context],[EventSeries]++-%20context_info(i)%200..1>[Context],[Event]++-%20context_info(i)%200..1>[Context])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries],[Event],[EventSeries]++-%20context_info%200..1>[Context&#124;text:string%20%3F;license_str:string%20%3F;license_url:uriorcurie%20%3F],[Event]++-%20context_info%200..1>[Context],[EventSeries]++-%20context_info(i)%200..1>[Context],[Event]++-%20context_info(i)%200..1>[Context])

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞context_info](EventSeries_context_info.md)*  <sub>0..1</sub>  **[Context](Context.md)**
 *  **[Event](Event.md)** *[Event➞context_info](Event_context_info.md)*  <sub>0..1</sub>  **[Context](Context.md)**
 *  **None** *[context_info](context_info.md)*  <sub>0..1</sub>  **[Context](Context.md)**

## Attributes


### Own

 * [➞text](context__text.md)  <sub>0..1</sub>
     * Description: The free text used to provide more context information on an event or event series.
     * Range: [String](types/String.md)
 * [➞license_str](context__license_str.md)  <sub>0..1</sub>
     * Description: The license of the context information as text, which must be used when copying text from other sources.
     * Range: [String](types/String.md)
 * [➞license_url](context__license_url.md)  <sub>0..1</sub>
     * Description: The license of the context information as URL, which should be used when copying text from other sources and such a URL exists.
     * Range: [Uriorcurie](types/Uriorcurie.md)
