
# Class: ExternalIdentifier


An identifer of an entity declared in another schema.

URI: [confident:ExternalIdentifier](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#ExternalIdentifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WikidataId],[WikiCfpSeriesId],[WikiCfpEventId],[TibkatId],[SchemaBasedThing],[GndId],[EventSeries]++-%20external_id%200..*>[ExternalIdentifier&#124;schema_value:string%20%3F;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F],[Event]++-%20external_id%200..*>[ExternalIdentifier],[EventSeries]++-%20external_id(i)%200..*>[ExternalIdentifier],[Event]++-%20external_id(i)%200..*>[ExternalIdentifier],[NamedThing]++-%20external_id%200..*>[ExternalIdentifier],[ExternalIdentifier]uses%20-.->[SchemaBasedThing],[ExternalIdentifier]^-[WikidataId],[ExternalIdentifier]^-[WikiCfpSeriesId],[ExternalIdentifier]^-[WikiCfpEventId],[ExternalIdentifier]^-[TibkatId],[ExternalIdentifier]^-[GndId],[ExternalIdentifier]^-[DigitalObjectId],[ExternalIdentifier]^-[DblpId],[NamedThing],[EventSeries],[Event],[DigitalObjectId],[DblpId])](https://yuml.me/diagram/nofunky;dir:TB/class/[WikidataId],[WikiCfpSeriesId],[WikiCfpEventId],[TibkatId],[SchemaBasedThing],[GndId],[EventSeries]++-%20external_id%200..*>[ExternalIdentifier&#124;schema_value:string%20%3F;schema_name:string%20%3F;schema_base_uri:uriorcurie%20%3F],[Event]++-%20external_id%200..*>[ExternalIdentifier],[EventSeries]++-%20external_id(i)%200..*>[ExternalIdentifier],[Event]++-%20external_id(i)%200..*>[ExternalIdentifier],[NamedThing]++-%20external_id%200..*>[ExternalIdentifier],[ExternalIdentifier]uses%20-.->[SchemaBasedThing],[ExternalIdentifier]^-[WikidataId],[ExternalIdentifier]^-[WikiCfpSeriesId],[ExternalIdentifier]^-[WikiCfpEventId],[ExternalIdentifier]^-[TibkatId],[ExternalIdentifier]^-[GndId],[ExternalIdentifier]^-[DigitalObjectId],[ExternalIdentifier]^-[DblpId],[NamedThing],[EventSeries],[Event],[DigitalObjectId],[DblpId])

## Uses Mixin

 *  mixin: [SchemaBasedThing](SchemaBasedThing.md) - A mixin used in classes that contain schema based values, such as the classifications used to denote the academic field of an event or the external identifiers used to denote a thing.

## Children

 * [DblpId](DblpId.md) - The identifier of an academic event or series in dblp.
 * [DigitalObjectId](DigitalObjectId.md) - A centrally registered identifier symbol used to uniquely identify digital objects given by International DOI Foundation.
 * [GndId](GndId.md) - The identifier of a thing (item) in the German National authority file.
 * [TibkatId](TibkatId.md) - The identifier of a publication in the TIB catalog that references an event or event series.
 * [WikiCfpEventId](WikiCfpEventId.md) - The identifier of an academic event or series in WikiCFP.
 * [WikiCfpSeriesId](WikiCfpSeriesId.md) - The identifier of an academic event or series in WikiCFP.
 * [WikidataId](WikidataId.md) - The identifier of a thing (item) in Wikidata.

## Referenced by Class

 *  **[EventSeries](EventSeries.md)** *[EventSeries➞external_id](EventSeries_external_id.md)*  <sub>0..\*</sub>  **[ExternalIdentifier](ExternalIdentifier.md)**
 *  **[Event](Event.md)** *[Event➞external_id](Event_external_id.md)*  <sub>0..\*</sub>  **[ExternalIdentifier](ExternalIdentifier.md)**
 *  **None** *[external_id](external_id.md)*  <sub>0..\*</sub>  **[ExternalIdentifier](ExternalIdentifier.md)**

## Attributes


### Own

 * [ExternalIdentifier➞schema_value](ExternalIdentifier_schema_value.md)  <sub>0..1</sub>
     * Description: A property to provide the literal value of a schema based entity.
     * Range: [String](types/String.md)

### Mixed in from SchemaBasedThing:

 * [schema_name](schema_name.md)  <sub>0..1</sub>
     * Description: A property to provide the name of a schema.
     * Range: [String](types/String.md)

### Mixed in from SchemaBasedThing:

 * [schema_base_uri](schema_base_uri.md)  <sub>0..1</sub>
     * Description: The base URI of the schema that provides the context for the schema based value.
     * Range: [Uriorcurie](types/Uriorcurie.md)
