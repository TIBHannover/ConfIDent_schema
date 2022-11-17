from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional


@dataclass(order=True)
class Affiliation:
    class Meta:
        name = "affiliation"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    schemeUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    affiliationIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    affiliationIdentifierScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Dates:
    class Meta:
        name = "dates"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dateType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dateInformation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Descriptions:
    class Meta:
        name = "descriptions"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    descriptionType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class FundingReferences:
    class Meta:
        name = "fundingReferences"

    awardUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    awardTitle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    funderName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    awardNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    funderIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    funderIdentifierType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class GeoLocationPoint:
    class Meta:
        name = "geoLocationPoint"

    pointLatitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pointLongitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Identifiers:
    class Meta:
        name = "identifiers"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    identifierType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class NameIdentifiers:
    class Meta:
        name = "nameIdentifiers"

    schemeUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    nameIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    nameIdentifierScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class RelatedIdentifiers:
    class Meta:
        name = "relatedIdentifiers"

    schemeUri: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    schemeType: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    relationType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    relatedIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    resourceTypeGeneral: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    relatedIdentifierType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    relatedMetadataScheme: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Subjects:
    class Meta:
        name = "subjects"

    subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    valueUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    schemeUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subjectScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Titles:
    class Meta:
        name = "titles"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    titleType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Types:
    class Meta:
        name = "types"

    resourceType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    resourceTypeGeneral: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Contributors:
    class Meta:
        name = "contributors"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    nameType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    givenName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    familyName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    affiliation: List[Affiliation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    contributorType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    nameIdentifiers: List[NameIdentifiers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Creators:
    class Meta:
        name = "creators"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    nameType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    givenName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    familyName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    affiliation: List[Affiliation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    nameIdentifiers: List[NameIdentifiers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class GeoLocations:
    class Meta:
        name = "geoLocations"

    geoLocationPlace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    geoLocationPoint: Optional[GeoLocationPoint] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Attributes:
    class Meta:
        name = "attributes"

    doi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    identifiers: List[Identifiers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    types: Optional[Types] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    creators: List[Creators] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    titles: List[Titles] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    publisher: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subjects: List[Subjects] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    contributors: List[Contributors] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    dates: List[Dates] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    publicationYear: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    descriptions: List[Descriptions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    geoLocations: List[GeoLocations] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fundingReferences: List[FundingReferences] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    relatedIdentifiers: List[RelatedIdentifiers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True)
class Generated:
    class Meta:
        name = "generated"

    attributes: Optional[Attributes] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
