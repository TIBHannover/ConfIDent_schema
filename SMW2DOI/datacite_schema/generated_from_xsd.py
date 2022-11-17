from dataclasses import field
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union


@dataclass(order=True)
class Affiliation:
    """
    Uniquely identifies an affiliation, according to various identifier
    schemes.
    """
    class Meta:
        name = "affiliation"
        target_namespace = "http://datacite.org/schema/kernel-4"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    affiliationIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    affiliationIdentifierScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class Box:
    class Meta:
        name = "box"
        target_namespace = "http://datacite.org/schema/kernel-4"

    westBoundLongitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    eastBoundLongitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    southBoundLatitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )
    northBoundLatitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )


class ContributorType(Enum):
    """
    The type of contributor of the resource.
    """
    CONTACT_PERSON = "ContactPerson"
    DATA_COLLECTOR = "DataCollector"
    DATA_CURATOR = "DataCurator"
    DATA_MANAGER = "DataManager"
    DISTRIBUTOR = "Distributor"
    EDITOR = "Editor"
    HOSTING_INSTITUTION = "HostingInstitution"
    OTHER = "Other"
    PRODUCER = "Producer"
    PROJECT_LEADER = "ProjectLeader"
    PROJECT_MANAGER = "ProjectManager"
    PROJECT_MEMBER = "ProjectMember"
    REGISTRATION_AGENCY = "RegistrationAgency"
    REGISTRATION_AUTHORITY = "RegistrationAuthority"
    RELATED_PERSON = "RelatedPerson"
    RESEARCH_GROUP = "ResearchGroup"
    RIGHTS_HOLDER = "RightsHolder"
    RESEARCHER = "Researcher"
    SPONSOR = "Sponsor"
    SUPERVISOR = "Supervisor"
    WORK_PACKAGE_LEADER = "WorkPackageLeader"


class DateType(Enum):
    """The type of date.

    Use RKMS‐ISO8601 standard for depicting date ranges.To indicate the
    end of an embargo period, use Available. To indicate the start of an
    embargo period, use Submitted or Accepted, as appropriate.
    """
    ACCEPTED = "Accepted"
    AVAILABLE = "Available"
    COLLECTED = "Collected"
    COPYRIGHTED = "Copyrighted"
    CREATED = "Created"
    ISSUED = "Issued"
    OTHER = "Other"
    SUBMITTED = "Submitted"
    UPDATED = "Updated"
    VALID = "Valid"
    WITHDRAWN = "Withdrawn"


class DescriptionType(Enum):
    """
    The type of the description.
    """
    ABSTRACT = "Abstract"
    METHODS = "Methods"
    SERIES_INFORMATION = "SeriesInformation"
    TABLE_OF_CONTENTS = "TableOfContents"
    TECHNICAL_INFO = "TechnicalInfo"
    OTHER = "Other"


class FunderIdentifierType(Enum):
    """
    The type of the funderIdentifier.
    """
    ISNI = "ISNI"
    GRID = "GRID"
    ROR = "ROR"
    CROSSREF_FUNDER_ID = "Crossref Funder ID"
    OTHER = "Other"


@dataclass(order=True)
class NameIdentifier:
    """
    Uniquely identifies a creator or contributor, according to various
    identifier schemes.
    """
    class Meta:
        name = "nameIdentifier"
        target_namespace = "http://datacite.org/schema/kernel-4"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    nameIdentifierScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class NameType(Enum):
    ORGANIZATIONAL = "Organizational"
    PERSONAL = "Personal"


class NumberType(Enum):
    ARTICLE = "Article"
    CHAPTER = "Chapter"
    REPORT = "Report"
    OTHER = "Other"


@dataclass(order=True)
class Point:
    class Meta:
        name = "point"
        target_namespace = "http://datacite.org/schema/kernel-4"

    pointLongitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    pointLatitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )


class RelatedIdentifierType(Enum):
    """
    The type of the RelatedIdentifier.
    """
    ARK = "ARK"
    AR_XIV = "arXiv"
    BIBCODE = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    HANDLE = "Handle"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    W3ID = "w3id"


class RelationType(Enum):
    """
    Description of the relationship of the resource being registered (A) and
    the related resource (B).
    """
    IS_CITED_BY = "IsCitedBy"
    CITES = "Cites"
    IS_SUPPLEMENT_TO = "IsSupplementTo"
    IS_SUPPLEMENTED_BY = "IsSupplementedBy"
    IS_CONTINUED_BY = "IsContinuedBy"
    CONTINUES = "Continues"
    IS_NEW_VERSION_OF = "IsNewVersionOf"
    IS_PREVIOUS_VERSION_OF = "IsPreviousVersionOf"
    IS_PART_OF = "IsPartOf"
    HAS_PART = "HasPart"
    IS_PUBLISHED_IN = "IsPublishedIn"
    IS_REFERENCED_BY = "IsReferencedBy"
    REFERENCES = "References"
    IS_DOCUMENTED_BY = "IsDocumentedBy"
    DOCUMENTS = "Documents"
    IS_COMPILED_BY = "IsCompiledBy"
    COMPILES = "Compiles"
    IS_VARIANT_FORM_OF = "IsVariantFormOf"
    IS_ORIGINAL_FORM_OF = "IsOriginalFormOf"
    IS_IDENTICAL_TO = "IsIdenticalTo"
    HAS_METADATA = "HasMetadata"
    IS_METADATA_FOR = "IsMetadataFor"
    REVIEWS = "Reviews"
    IS_REVIEWED_BY = "IsReviewedBy"
    IS_DERIVED_FROM = "IsDerivedFrom"
    IS_SOURCE_OF = "IsSourceOf"
    DESCRIBES = "Describes"
    IS_DESCRIBED_BY = "IsDescribedBy"
    HAS_VERSION = "HasVersion"
    IS_VERSION_OF = "IsVersionOf"
    REQUIRES = "Requires"
    IS_REQUIRED_BY = "IsRequiredBy"
    OBSOLETES = "Obsoletes"
    IS_OBSOLETED_BY = "IsObsoletedBy"


class ResourceType(Enum):
    """
    The general type of a resource.
    """
    AUDIOVISUAL = "Audiovisual"
    BOOK = "Book"
    BOOK_CHAPTER = "BookChapter"
    COLLECTION = "Collection"
    COMPUTATIONAL_NOTEBOOK = "ComputationalNotebook"
    CONFERENCE_PAPER = "ConferencePaper"
    CONFERENCE_PROCEEDING = "ConferenceProceeding"
    DATA_PAPER = "DataPaper"
    DATASET = "Dataset"
    DISSERTATION = "Dissertation"
    EVENT = "Event"
    IMAGE = "Image"
    INTERACTIVE_RESOURCE = "InteractiveResource"
    JOURNAL = "Journal"
    JOURNAL_ARTICLE = "JournalArticle"
    MODEL = "Model"
    OUTPUT_MANAGEMENT_PLAN = "OutputManagementPlan"
    PEER_REVIEW = "PeerReview"
    PHYSICAL_OBJECT = "PhysicalObject"
    PREPRINT = "Preprint"
    REPORT = "Report"
    SERVICE = "Service"
    SOFTWARE = "Software"
    SOUND = "Sound"
    STANDARD = "Standard"
    TEXT = "Text"
    WORKFLOW = "Workflow"
    OTHER = "Other"


@dataclass(order=True)
class ResourceAlternateIdentifiersAlternateIdentifier:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    alternateIdentifierType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(order=True)
class ResourceDescriptionsDescriptionBr:
    class Meta:
        global_type = False


@dataclass(order=True)
class ResourceFormats:
    """
    :ivar format: Technical format of the resource. Use file extension
        or MIME type where possible.
    """
    class Meta:
        global_type = False

    format: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceFundingReferencesFundingReferenceAwardNumber:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    awardURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class ResourceIdentifier:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    identifierType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(order=True)
class ResourceSizes:
    """
    :ivar size: Unstructures size information about the resource.
    """
    class Meta:
        global_type = False

    size: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


class TitleType(Enum):
    ALTERNATIVE_TITLE = "AlternativeTitle"
    SUBTITLE = "Subtitle"
    TRANSLATED_TITLE = "TranslatedTitle"
    OTHER = "Other"


class LangValue(Enum):
    VALUE = ""


@dataclass(order=True)
class ResourceAlternateIdentifiers:
    """
    :ivar alternateIdentifier: An identifier or identifiers other than
        the primary Identifier applied to the resource being registered.
        This may be any alphanumeric string which is unique within its
        domain of issue. May be used for local identifiers.
        AlternateIdentifier should be used for another identifier of the
        same instance (same location, same file).
    """
    class Meta:
        global_type = False

    alternateIdentifier: List[ResourceAlternateIdentifiersAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceContributorsContributorContributorName:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    nameType: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceCreatorsCreatorCreatorName:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    nameType: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceDatesDate:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    dateType: Optional[DateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    dateInformation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class ResourceDescriptionsDescription:
    class Meta:
        global_type = False

    descriptionType: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": ResourceDescriptionsDescriptionBr,
                    "namespace": "http://datacite.org/schema/kernel-4",
                },
            ),
        }
    )


@dataclass(order=True)
class ResourceFundingReferencesFundingReferenceFunderIdentifier:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    funderIdentifierType: Optional[FunderIdentifierType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class ResourceGeoLocationsGeoLocationGeoLocationPolygon:
    class Meta:
        global_type = False

    polygonPoint: List[Point] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "min_occurs": 4,
        }
    )
    inPolygonPoint: Optional[Point] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourcePublisher:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceRelatedIdentifiersRelatedIdentifier:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    resourceTypeGeneral: Optional[ResourceType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    relatedIdentifierType: Optional[RelatedIdentifierType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    relationType: Optional[RelationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    relatedMetadataScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemContributorsContributorContributorName:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    nameType: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemCreatorsCreatorCreatorName:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    nameType: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemNumber:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    numberType: Optional[NumberType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemRelatedItemIdentifier:
    """
    :ivar value:
    :ivar relatedItemIdentifierType: The type of the Identifier for the
        related item e.g. DOI.
    :ivar relatedMetadataScheme: The name of the scheme.
    :ivar schemeURI: The URI of the relatedMetadataScheme.
    :ivar schemeType: The type of the relatedMetadataScheme, linked with
        the schemeURI.
    """
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    relatedItemIdentifierType: Optional[RelatedIdentifierType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    relatedMetadataScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemTitlesTitle:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    titleType: Optional[TitleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceResourceType:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    resourceTypeGeneral: Optional[ResourceType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(order=True)
class ResourceRightsListRights:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    rightsURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rightsIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rightsIdentifierScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceSubjectsSubject:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    subjectScheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schemeURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valueURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    classificationCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceTitlesTitle:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    titleType: Optional[TitleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass(order=True)
class ResourceContributorsContributor:
    class Meta:
        global_type = False

    contributorName: Optional[ResourceContributorsContributorContributorName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
        }
    )
    givenName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    familyName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    nameIdentifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    affiliation: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    contributorType: Optional[ContributorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(order=True)
class ResourceCreatorsCreator:
    class Meta:
        global_type = False

    creatorName: Optional[ResourceCreatorsCreatorCreatorName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
        }
    )
    givenName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    familyName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    nameIdentifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    affiliation: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceDates:
    """
    :ivar date: Different dates relevant to the work. YYYY,YYYY-MM-DD,
        YYYY-MM-DDThh:mm:ssTZD or any other format or level of
        granularity described in W3CDTF. Use RKMS-ISO8601 standard for
        depicting date ranges.
    """
    class Meta:
        global_type = False

    date: List[ResourceDatesDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceDescriptions:
    """
    :ivar description: All additional information that does not fit in
        any of the other categories. May be used for technical
        information. It is a best practice to supply a description.
    """
    class Meta:
        global_type = False

    description: List[ResourceDescriptionsDescription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceFundingReferencesFundingReference:
    """
    :ivar funderName: Name of the funding provider.
    :ivar funderIdentifier: Uniquely identifies a funding entity,
        according to various types.
    :ivar awardNumber: The code assigned by the funder to a sponsored
        award (grant).
    :ivar awardTitle: The human readable title of the award (grant).
    """
    class Meta:
        global_type = False

    funderName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
        }
    )
    funderIdentifier: Optional[ResourceFundingReferencesFundingReferenceFunderIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    awardNumber: Optional[ResourceFundingReferencesFundingReferenceAwardNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    awardTitle: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceGeoLocationsGeoLocation:
    class Meta:
        global_type = False

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "geoLocationPlace",
                    "type": object,
                    "namespace": "http://datacite.org/schema/kernel-4",
                },
                {
                    "name": "geoLocationPoint",
                    "type": Point,
                    "namespace": "http://datacite.org/schema/kernel-4",
                },
                {
                    "name": "geoLocationBox",
                    "type": Box,
                    "namespace": "http://datacite.org/schema/kernel-4",
                },
                {
                    "name": "geoLocationPolygon",
                    "type": ResourceGeoLocationsGeoLocationGeoLocationPolygon,
                    "namespace": "http://datacite.org/schema/kernel-4",
                },
            ),
        }
    )


@dataclass(order=True)
class ResourceRelatedIdentifiers:
    """
    :ivar relatedIdentifier: Identifiers of related resources. Use this
        property to indicate subsets of properties, as appropriate.
    """
    class Meta:
        global_type = False

    relatedIdentifier: List[ResourceRelatedIdentifiersRelatedIdentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemContributorsContributor:
    """
    :ivar contributorName:
    :ivar givenName:
    :ivar familyName:
    :ivar contributorType: The type of contributor of the resource.
    """
    class Meta:
        global_type = False

    contributorName: Optional[ResourceRelatedItemsRelatedItemContributorsContributorContributorName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
        }
    )
    givenName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    familyName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    contributorType: Optional[ContributorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemCreatorsCreator:
    class Meta:
        global_type = False

    creatorName: Optional[ResourceRelatedItemsRelatedItemCreatorsCreatorCreatorName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
        }
    )
    givenName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    familyName: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemTitles:
    """
    :ivar title: Title of the related item.
    """
    class Meta:
        global_type = False

    title: List[ResourceRelatedItemsRelatedItemTitlesTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceRightsList:
    """
    :ivar rights: Any rights information for this resource. Provide a
        rights management statement for the resource or reference a
        service providing such information. Include embargo information
        if applicable. Use the complete title of a license and include
        version information if applicable.
    """
    class Meta:
        global_type = False

    rights: List[ResourceRightsListRights] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceSubjects:
    """
    :ivar subject: Subject, keywords, classification codes, or key
        phrases describing the resource.
    """
    class Meta:
        global_type = False

    subject: List[ResourceSubjectsSubject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceTitles:
    """
    :ivar title: A name or title by which a resource is known.
    """
    class Meta:
        global_type = False

    title: List[ResourceTitlesTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "min_occurs": 1,
        }
    )


@dataclass(order=True)
class ResourceContributors:
    """
    :ivar contributor: The institution or person responsible for
        collecting, creating, or otherwise contributing to the
        developement of the dataset. The personal name format should be:
        Family, Given.
    """
    class Meta:
        global_type = False

    contributor: List[ResourceContributorsContributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceCreators:
    """
    :ivar creator: The main researchers involved working on the data, or
        the authors of the publication in priority order. May be a
        corporate/institutional or personal name. Format: Family, Given.
        Personal names can be further specified using givenName and
        familyName.
    """
    class Meta:
        global_type = False

    creator: List[ResourceCreatorsCreator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "min_occurs": 1,
        }
    )


@dataclass(order=True)
class ResourceFundingReferences:
    """
    :ivar fundingReference: Information about financial support
        (funding) for the resource being registered.
    """
    class Meta:
        global_type = False

    fundingReference: List[ResourceFundingReferencesFundingReference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceGeoLocations:
    class Meta:
        global_type = False

    geoLocation: List[ResourceGeoLocationsGeoLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemContributors:
    """
    :ivar contributor: The institution or person responsible for
        collecting, managing, distributing, or otherwise contributing to
        the development of the resource.
    """
    class Meta:
        global_type = False

    contributor: List[ResourceRelatedItemsRelatedItemContributorsContributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItemCreators:
    """
    :ivar creator: The institution or person responsible for creating
        the related resource. To supply multiple creators, repeat this
        property.
    """
    class Meta:
        global_type = False

    creator: List[ResourceRelatedItemsRelatedItemCreatorsCreator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class ResourceRelatedItemsRelatedItem:
    """
    :ivar relatedItemIdentifier: The identifier for the related item.
    :ivar creators:
    :ivar titles:
    :ivar publicationYear: The year when the item was or will be made
        publicly available.
    :ivar volume: Volume of the related item.
    :ivar issue: Issue number or name of the related item.
    :ivar number: Number of the related item e.g. report number of
        article number.
    :ivar firstPage: First page of the related item e.g. of the chapter,
        article, or conference paper.
    :ivar lastPage: Last page of the related item e.g. of the chapter,
        article, or conference paper.
    :ivar publisher: The name of the entity that holds, archives,
        publishes prints, distributes, releases, issues, or produces the
        resource. This property will be used to formulate the citation,
        so consider the prominence of the role.
    :ivar edition: Edition or version of the related item.
    :ivar contributors:
    :ivar relatedItemType: The type of the related item, e.g. journal
        article, book or chapter.
    :ivar relationType: Description of the relationship of the resource
        being registered (A) and the related resource (B).
    """
    class Meta:
        global_type = False

    relatedItemIdentifier: Optional[ResourceRelatedItemsRelatedItemRelatedItemIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    creators: Optional[ResourceRelatedItemsRelatedItemCreators] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    titles: Optional[ResourceRelatedItemsRelatedItemTitles] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    publicationYear: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "pattern": r"[\d]{4}",
        }
    )
    volume: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    issue: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    number: Optional[ResourceRelatedItemsRelatedItemNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    firstPage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    lastPage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    publisher: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    edition: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    contributors: Optional[ResourceRelatedItemsRelatedItemContributors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )
    relatedItemType: Optional[ResourceType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    relationType: Optional[RelationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(order=True)
class ResourceRelatedItems:
    """
    :ivar relatedItem: Information about a resource related to the one
        being registered e.g. a journal or book of which the article or
        chapter is part.
    """
    class Meta:
        global_type = False

    relatedItem: List[ResourceRelatedItemsRelatedItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
        }
    )


@dataclass(order=True)
class Resource:
    """Root element of a single record.

    This wrapper element is for XML implementation only and is not defined in the DataCite DOI standard.
    Note: This is the case for all wrapper elements within this schema.
    No content in this wrapper element.

    :ivar identifier: A persistent identifier that identifies a
        resource.
    :ivar creators:
    :ivar titles:
    :ivar publisher: The name of the entity that holds, archives,
        publishes prints, distributes, releases, issues, or produces the
        resource. This property will be used to formulate the citation,
        so consider the prominence of the role. In the case of datasets,
        "publish" is understood to mean making the data available to the
        community of researchers.
    :ivar publicationYear: Year when the data is made publicly
        available. If an embargo period has been in effect, use the date
        when the embargo period ends. In the case of datasets, "publish"
        is understood to mean making the data available on a specific
        date to the community of researchers. If there is no standard
        publication year value, use the date that would be preferred
        from a citation perspective. YYYY
    :ivar resourceType: The type of a resource. You may enter an
        additional free text description. The format is open, but the
        preferred format is a single term of some detail so that a pair
        can be formed with the sub-property.
    :ivar subjects:
    :ivar contributors:
    :ivar dates:
    :ivar language: Primary language of the resource. Allowed values are
        taken from  IETF BCP 47, ISO 639-1 language codes.
    :ivar alternateIdentifiers:
    :ivar relatedIdentifiers:
    :ivar sizes:
    :ivar formats:
    :ivar version: Version number of the resource. If the primary
        resource has changed the version number increases. Register a
        new identifier for a major version change. Individual stewards
        need to determine which are major vs. minor versions. May be
        used in conjunction with properties 11 and 12
        (AlternateIdentifier and RelatedIdentifier) to indicate various
        information updates. May be used in conjunction with property 17
        (Description) to indicate the nature and file/record range of
        version.
    :ivar rightsList:
    :ivar descriptions:
    :ivar geoLocations:
    :ivar fundingReferences:
    :ivar relatedItems:
    """
    class Meta:
        name = "resource"
        namespace = "http://datacite.org/schema/kernel-4"

    identifier: Optional[ResourceIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    creators: Optional[ResourceCreators] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    titles: Optional[ResourceTitles] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    publisher: Optional[ResourcePublisher] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    publicationYear: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[\d]{4}",
        }
    )
    resourceType: Optional[ResourceResourceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    subjects: Optional[ResourceSubjects] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contributors: Optional[ResourceContributors] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dates: Optional[ResourceDates] = field(
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
    alternateIdentifiers: Optional[ResourceAlternateIdentifiers] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    relatedIdentifiers: Optional[ResourceRelatedIdentifiers] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sizes: Optional[ResourceSizes] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    formats: Optional[ResourceFormats] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rightsList: Optional[ResourceRightsList] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    descriptions: Optional[ResourceDescriptions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    geoLocations: Optional[ResourceGeoLocations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingReferences: Optional[ResourceFundingReferences] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    relatedItems: Optional[ResourceRelatedItems] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
