
# Class: Location


A container for the information about the location in which an academic event takes place.

URI: [confident:Location](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#Location)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Venue],[Region],[Venue]<has_venue%200..1-%20[Location&#124;lattitude:float%20%3F;longitude:float%20%3F;meeting_url:uriorcurie%20%3F],[Region]<has_region%200..1-%20[Location],[Country]<has_country%200..1-%20[Location],[City]<has_city%200..1-%20[Location],[Event]++-%20at_location%200..1>[Location],[Event],[Country],[City])](https://yuml.me/diagram/nofunky;dir:TB/class/[Venue],[Region],[Venue]<has_venue%200..1-%20[Location&#124;lattitude:float%20%3F;longitude:float%20%3F;meeting_url:uriorcurie%20%3F],[Region]<has_region%200..1-%20[Location],[Country]<has_country%200..1-%20[Location],[City]<has_city%200..1-%20[Location],[Event]++-%20at_location%200..1>[Location],[Event],[Country],[City])

## Referenced by Class

 *  **None** *[at_location](at_location.md)*  <sub>0..1</sub>  **[Location](Location.md)**

## Attributes


### Own

 * [➞has_city](location__has_city.md)  <sub>0..1</sub>
     * Description: The property to specify the [City](City.md) of an academic event location.
     * Range: [City](City.md)
 * [➞has_country](location__has_country.md)  <sub>0..1</sub>
     * Description: The property to specify the [Country](Country.md) of an academic event location.
     * Range: [Country](Country.md)
 * [➞has_region](location__has_region.md)  <sub>0..1</sub>
     * Description: The property to specify the [Region](Region.md) of an academic event location.
     * Range: [Region](Region.md)
 * [➞has_venue](location__has_venue.md)  <sub>0..1</sub>
     * Description: The property to specify the [Venue](Venue.md) of an academic event location.
     * Range: [Venue](Venue.md)
 * [➞lattitude](location__lattitude.md)  <sub>0..1</sub>
     * Description: The property to specify the lattitude of an academic event location.
     * Range: [Float](types/Float.md)
 * [➞longitude](location__longitude.md)  <sub>0..1</sub>
     * Description: The property to specify the longitude of an academic event location.
     * Range: [Float](types/Float.md)
 * [➞meeting_url](location__meeting_url.md)  <sub>0..1</sub>
     * Description: The property to specify the URL under which a one can participate virtually in an academic event.
     * Range: [Uriorcurie](types/Uriorcurie.md)
