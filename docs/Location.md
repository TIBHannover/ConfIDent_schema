# Class: Subobject Location
_A container for the information about the location in which an academic event takes place._






<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | 
| ---  | --- | --- | --- | 
| [City](has_city.md) | [City](City.md) | 0..1 _recommended_ | The property to specify the [City](City.md) of an academic event location.  | 
| [Country](has_country.md) | [Country](Country.md) | 0..1 _recommended_ | The property to specify the [Country](Country.md) of an academic event location.  | 
| [Region](has_region.md) | [Region](Region.md) | 0..1 | The property to specify the [Region](Region.md) of an academic event location.  | 
| [Venue](has_venue.md) | [Venue](Venue.md) | 0..1 | The property to specify the [Venue](Venue.md) of an academic event location.  | 
| [Lattitude](lattitude.md) | [xsd:float](http://www.w3.org/2001/XMLSchema#float) | 0..1 | The property to specify the lattitude of an academic event location.  | 
| [Longitude](longitude.md) | [xsd:float](http://www.w3.org/2001/XMLSchema#float) | 0..1 | The property to specify the longitude of an academic event location.  | 
| [Meeting URL](meeting_url.md) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | 0..1 | The property to specify the URL under which a one can participate virtually in an academic event.  | 


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [Location](at_location.md) | range | Location |












## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['confident:Location'] |
| native | ['confident:Location'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Location
description: A container for the information about the location in which an academic
  event takes place.
title: Subobject Location
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
attributes:
  has_city:
    name: has_city
    description: The property to specify the [City](City.md) of an academic event
      location.
    title: City
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: City
    recommended: true
  has_country:
    name: has_country
    description: The property to specify the [Country](Country.md) of an academic
      event location.
    title: Country
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: Country
    recommended: true
  has_region:
    name: has_region
    description: The property to specify the [Region](Region.md) of an academic event
      location.
    title: Region
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: Region
  has_venue:
    name: has_venue
    description: The property to specify the [Venue](Venue.md) of an academic event
      location.
    title: Venue
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: Venue
  lattitude:
    name: lattitude
    description: The property to specify the lattitude of an academic event location.
    title: Lattitude
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: float
  longitude:
    name: longitude
    description: The property to specify the longitude of an academic event location.
    title: Longitude
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: float
  meeting_url:
    name: meeting_url
    description: The property to specify the URL under which a one can participate
      virtually in an academic event.
    title: Meeting URL
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    range: uriorcurie

```
</details>

### Induced

<details>
```yaml
name: Location
description: A container for the information about the location in which an academic
  event takes place.
title: Subobject Location
from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
attributes:
  has_city:
    name: has_city
    description: The property to specify the [City](City.md) of an academic event
      location.
    title: City
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: has_city
    owner: Location
    range: City
    recommended: true
  has_country:
    name: has_country
    description: The property to specify the [Country](Country.md) of an academic
      event location.
    title: Country
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: has_country
    owner: Location
    range: Country
    recommended: true
  has_region:
    name: has_region
    description: The property to specify the [Region](Region.md) of an academic event
      location.
    title: Region
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: has_region
    owner: Location
    range: Region
  has_venue:
    name: has_venue
    description: The property to specify the [Venue](Venue.md) of an academic event
      location.
    title: Venue
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: has_venue
    owner: Location
    range: Venue
  lattitude:
    name: lattitude
    description: The property to specify the lattitude of an academic event location.
    title: Lattitude
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: lattitude
    owner: Location
    range: float
  longitude:
    name: longitude
    description: The property to specify the longitude of an academic event location.
    title: Longitude
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: longitude
    owner: Location
    range: float
  meeting_url:
    name: meeting_url
    description: The property to specify the URL under which a one can participate
      virtually in an academic event.
    title: Meeting URL
    from_schema: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/ConfIDent_schema.yaml
    alias: meeting_url
    owner: Location
    range: uriorcurie

```
</details>