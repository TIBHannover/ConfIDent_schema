
# Class: WikiCfpSeriesId


The identifier of an academic event or series in WikiCFP.

URI: [confident:WikiCfpSeriesId](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#WikiCfpSeriesId)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20wikicfp_series_id%200..*>[WikiCfpSeriesId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[EventSeries]++-%20wikicfp_series_id(i)%200..*>[WikiCfpSeriesId],[ExternalIdentifier]^-[WikiCfpSeriesId],[ExternalIdentifier],[EventSeries])](https://yuml.me/diagram/nofunky;dir:TB/class/[EventSeries]++-%20wikicfp_series_id%200..*>[WikiCfpSeriesId&#124;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F;schema_value(i):string%20%3F],[EventSeries]++-%20wikicfp_series_id(i)%200..*>[WikiCfpSeriesId],[ExternalIdentifier]^-[WikiCfpSeriesId],[ExternalIdentifier],[EventSeries])

## Parents

 *  is_a: [ExternalIdentifier](ExternalIdentifier.md) - An identifer of an entity declared in another schema.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞wikicfp_series_id](EventSeries_wikicfp_series_id.md)*  <sub>0..\*</sub>  **[WikiCfpSeriesId](WikiCfpSeriesId.md)**
 *  **None** *[wikicfp_series_id](wikicfp_series_id.md)*  <sub>0..\*</sub>  **[WikiCfpSeriesId](WikiCfpSeriesId.md)**

## Attributes


### Own

 * [WikiCfpSeriesId➞schema_name](WikiCfpSeriesId_schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)
 * [WikiCfpSeriesId➞schema_base_uri](WikiCfpSeriesId_schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ExternalIdentifier:

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)
