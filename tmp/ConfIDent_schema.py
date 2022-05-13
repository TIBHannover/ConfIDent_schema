# Auto generated from ConfIDent_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-13T09:04:42
# Schema: ConfIDent-schema
#
# id: https://github.com/StroemPhi/ConfIDent-schema/
# description: This is a schema for the ConfIDent project that describes the necessary metadata requirements of
#              academic events and event series.
# license: https://creativecommons.org/licenses/by/4.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.3.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#AEON_')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CONFIDENT = CurieNamespace('confident', 'https://confident.org/')
DATACITE = CurieNamespace('datacite', 'http://schema.datacite.org/meta/kernel-4.4/metadata.xsd')
DBLP_SERIES = CurieNamespace('dblp_series', 'https://dblp.org/db/conf/')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
EX = CurieNamespace('ex', 'https://example.com/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
PROVO = CurieNamespace('provo', 'https://www.w3.org/TR/2013/REC-prov-o-20130430/#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ROR = CurieNamespace('ror', 'https://ror.org/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WIKIDATA = CurieNamespace('wikidata', 'https://www.wikidata.org/wiki/')
DEFAULT_ = CONFIDENT


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PlannedProcessId(URIorCURIE):
    pass


class AcademicEventSeriesId(PlannedProcessId):
    pass


class AcademicEventId(PlannedProcessId):
    pass


class CityId(URIorCURIE):
    pass


class CountryId(URIorCURIE):
    pass


class RegionId(URIorCURIE):
    pass


class VenueId(URIorCURIE):
    pass


class ContributorId(URIorCURIE):
    pass


class SponsorId(ContributorId):
    pass


class AttendeeId(ContributorId):
    pass


class ModeratorId(ContributorId):
    pass


class ReviewerId(ContributorId):
    pass


class OrganizerId(ContributorId):
    pass


class ContactPersonId(OrganizerId):
    pass


class CommitteeMemberId(OrganizerId):
    pass


class CommitteeChairId(CommitteeMemberId):
    pass


class PresenterId(ContributorId):
    pass


class KeynoteSpeakerId(PresenterId):
    pass


class PublicationId(URIorCURIE):
    pass


@dataclass
class SchemaBasedThing(YAMLRoot):
    """
    A mixin used in classes that contain schema based values, such as the classifications used to denote the academic
    field of an event or the external identifiers used to denote a thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.SchemaBasedThing
    class_class_curie: ClassVar[str] = "confident:SchemaBasedThing"
    class_name: ClassVar[str] = "SchemaBasedThing"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.SchemaBasedThing

    value: Optional[str] = None
    schema_name: Optional[str] = None
    schema_base_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A mixin used to provide the attributes needed for the identification of named class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.NamedThing
    class_class_curie: ClassVar[str] = "confident:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, "ExternalIdentifier"], List[Union[dict, "ExternalIdentifier"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(YAMLRoot):
    """
    Abstract base class for academic events and event series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "obi:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    process_name: Optional[Union[dict, "ProcessName"]] = None
    type: Optional[str] = None
    doi: Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]] = empty_list()
    landing_page: Optional[Union[str, URI]] = None
    organizers: Optional[Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]]] = empty_dict()
    contact: Optional[Union[dict, "ContactPerson"]] = None
    academic_fields: Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    sponsors: Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]] = empty_dict()
    publications: Optional[Union[str, List[str]]] = empty_list()
    wikidata_id: Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]] = empty_list()
    wikicfp_id: Optional[Union[Union[dict, "WikiCfpId"], List[Union[dict, "WikiCfpId"]]]] = empty_list()
    dpbl_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()
    gnd_id: Optional[Union[Union[dict, "GndId"], List[Union[dict, "GndId"]]]] = empty_list()
    topics: Optional[Union[str, List[str]]] = empty_list()
    metrics: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    context_info: Optional[Union[dict, "Context"]] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, "ExternalIdentifier"], List[Union[dict, "ExternalIdentifier"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self.process_name is not None and not isinstance(self.process_name, ProcessName):
            self.process_name = ProcessName(**as_dict(self.process_name))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.doi, list):
            self.doi = [self.doi] if self.doi is not None else []
        self.doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.doi]

        if self.landing_page is not None and not isinstance(self.landing_page, URI):
            self.landing_page = URI(self.landing_page)

        self._normalize_inlined_as_list(slot_name="organizers", slot_type=Organizer, key_name="id", keyed=True)

        if self.contact is not None and not isinstance(self.contact, ContactPerson):
            self.contact = ContactPerson(**as_dict(self.contact))

        if not isinstance(self.academic_fields, list):
            self.academic_fields = [self.academic_fields] if self.academic_fields is not None else []
        self.academic_fields = [v if isinstance(v, AcademicField) else AcademicField(**as_dict(v)) for v in self.academic_fields]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        self._normalize_inlined_as_list(slot_name="sponsors", slot_type=Sponsor, key_name="id", keyed=True)

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, str) else str(v) for v in self.publications]

        if not isinstance(self.wikidata_id, list):
            self.wikidata_id = [self.wikidata_id] if self.wikidata_id is not None else []
        self.wikidata_id = [v if isinstance(v, WikidataId) else WikidataId(**as_dict(v)) for v in self.wikidata_id]

        if not isinstance(self.wikicfp_id, list):
            self.wikicfp_id = [self.wikicfp_id] if self.wikicfp_id is not None else []
        self.wikicfp_id = [v if isinstance(v, WikiCfpId) else WikiCfpId(**as_dict(v)) for v in self.wikicfp_id]

        if not isinstance(self.dpbl_id, list):
            self.dpbl_id = [self.dpbl_id] if self.dpbl_id is not None else []
        self.dpbl_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.dpbl_id]

        if not isinstance(self.gnd_id, list):
            self.gnd_id = [self.gnd_id] if self.gnd_id is not None else []
        self.gnd_id = [v if isinstance(v, GndId) else GndId(**as_dict(v)) for v in self.gnd_id]

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, str) else str(v) for v in self.topics]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.metrics]

        if self.context_info is not None and not isinstance(self.context_info, Context):
            self.context_info = Context(**as_dict(self.context_info))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class AcademicEventSeries(PlannedProcess):
    """
    An academic event series describes the set of academic events which take place on a regular basis and thus have an
    established common identity. This identity is constituted, for example, through institutional continuity in the
    hosting of a series (e.g. by a specialised society), thematic focuses and/or a common label under which a series
    is defined (particularly name and acronym). Nevertheless, it is possible that each of these criteria may change
    over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000002"]
    class_class_curie: ClassVar[str] = "aeon:0000002"
    class_name: ClassVar[str] = "AcademicEventSeries"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.AcademicEventSeries

    process_name: Union[dict, "ProcessName"] = None
    id: Union[str, AcademicEventSeriesId] = "confident:SeriesID"
    series_of: Optional[Union[str, AcademicEventId]] = None
    landing_page: Optional[Union[str, URI]] = None
    doi: Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]] = empty_list()
    organizers: Optional[Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]]] = empty_dict()
    academic_fields: Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    sponsors: Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]] = empty_dict()
    publications: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    topics: Optional[Union[str, List[str]]] = empty_list()
    metrics: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    context_info: Optional[Union[dict, "Context"]] = None
    gnd_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()
    wikicfp_id: Optional[Union[Union[dict, "WikiCfpId"], List[Union[dict, "WikiCfpId"]]]] = empty_list()
    wikidata_id: Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]] = empty_list()
    dpbl_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventSeriesId):
            self.id = AcademicEventSeriesId(self.id)

        if self._is_empty(self.process_name):
            self.MissingRequiredField("process_name")
        if not isinstance(self.process_name, ProcessName):
            self.process_name = ProcessName(**as_dict(self.process_name))

        if self.series_of is not None and not isinstance(self.series_of, AcademicEventId):
            self.series_of = AcademicEventId(self.series_of)

        if self.landing_page is not None and not isinstance(self.landing_page, URI):
            self.landing_page = URI(self.landing_page)

        if not isinstance(self.doi, list):
            self.doi = [self.doi] if self.doi is not None else []
        self.doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.doi]

        self._normalize_inlined_as_list(slot_name="organizers", slot_type=Organizer, key_name="id", keyed=True)

        if not isinstance(self.academic_fields, list):
            self.academic_fields = [self.academic_fields] if self.academic_fields is not None else []
        self.academic_fields = [v if isinstance(v, AcademicField) else AcademicField(**as_dict(v)) for v in self.academic_fields]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        self._normalize_inlined_as_list(slot_name="sponsors", slot_type=Sponsor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="publications", slot_type=Publication, key_name="id", keyed=True)

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, str) else str(v) for v in self.topics]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.metrics]

        if self.context_info is not None and not isinstance(self.context_info, Context):
            self.context_info = Context(**as_dict(self.context_info))

        if not isinstance(self.gnd_id, list):
            self.gnd_id = [self.gnd_id] if self.gnd_id is not None else []
        self.gnd_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.gnd_id]

        if not isinstance(self.wikicfp_id, list):
            self.wikicfp_id = [self.wikicfp_id] if self.wikicfp_id is not None else []
        self.wikicfp_id = [v if isinstance(v, WikiCfpId) else WikiCfpId(**as_dict(v)) for v in self.wikicfp_id]

        if not isinstance(self.wikidata_id, list):
            self.wikidata_id = [self.wikidata_id] if self.wikidata_id is not None else []
        self.wikidata_id = [v if isinstance(v, WikidataId) else WikidataId(**as_dict(v)) for v in self.wikidata_id]

        if not isinstance(self.dpbl_id, list):
            self.dpbl_id = [self.dpbl_id] if self.dpbl_id is not None else []
        self.dpbl_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.dpbl_id]

        super().__post_init__(**kwargs)


@dataclass
class AcademicEvent(PlannedProcess):
    """
    An academic event is part of the established instruments of science communication as a format for conveying the
    latest scientific publications. It is defined by the meeting of researchers at a specific time and place (virtual
    or physical) and with a specific thematic focus to present, hear and discuss these publications. In contrast to
    other forms of events, academic events should primarily serve the exchange of results and methods of scientific
    research and their didactic mediation. Furthermore, a significant participation of scientific organizations in the
    realization of an academic event is constitutive for this type of event; for example, to distinguish it from
    events in which researchers mainly act as external experts or with a purely legitimising function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.AcademicEvent
    class_class_curie: ClassVar[str] = "confident:AcademicEvent"
    class_name: ClassVar[str] = "AcademicEvent"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.AcademicEvent

    start_date: Union[str, XSDDateTime] = None
    end_date: Union[str, XSDDateTime] = None
    process_name: Union[dict, "ProcessName"] = None
    event_status: Union[str, "EventStatus"] = "as scheduled"
    id: Union[str, AcademicEventId] = "confident:EventID"
    index: Optional[int] = None
    in_series: Optional[Union[str, AcademicEventSeriesId]] = None
    event_format: Optional[Union[dict, "EventFormatSpecification"]] = None
    at_location: Optional[Union[dict, "Location"]] = None
    deadlines: Optional[Union[Union[dict, "Deadline"], List[Union[dict, "Deadline"]]]] = empty_list()
    related_to: Optional[Union[Union[dict, "ProcessRelation"], List[Union[dict, "ProcessRelation"]]]] = empty_list()
    ordinal: Optional[int] = None
    event_mode: Optional[Union[str, "EventMode"]] = None
    landing_page: Optional[Union[str, URI]] = None
    doi: Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]] = empty_list()
    type: Optional[Union[str, "EventType"]] = None
    organizers: Optional[Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]]] = empty_dict()
    academic_fields: Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    sponsors: Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]] = empty_dict()
    publications: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    topics: Optional[Union[str, List[str]]] = empty_list()
    metrics: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    context_info: Optional[Union[dict, "Context"]] = None
    gnd_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()
    wikicfp_id: Optional[Union[Union[dict, "WikiCfpId"], List[Union[dict, "WikiCfpId"]]]] = empty_list()
    wikidata_id: Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]] = empty_list()
    dpbl_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventId):
            self.id = AcademicEventId(self.id)

        if self._is_empty(self.start_date):
            self.MissingRequiredField("start_date")
        if not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self._is_empty(self.end_date):
            self.MissingRequiredField("end_date")
        if not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

        if self._is_empty(self.event_status):
            self.MissingRequiredField("event_status")
        if not isinstance(self.event_status, EventStatus):
            self.event_status = EventStatus(self.event_status)

        if self._is_empty(self.process_name):
            self.MissingRequiredField("process_name")
        if not isinstance(self.process_name, ProcessName):
            self.process_name = ProcessName(**as_dict(self.process_name))

        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.in_series is not None and not isinstance(self.in_series, AcademicEventSeriesId):
            self.in_series = AcademicEventSeriesId(self.in_series)

        if self.event_format is not None and not isinstance(self.event_format, EventFormatSpecification):
            self.event_format = EventFormatSpecification(**as_dict(self.event_format))

        if self.at_location is not None and not isinstance(self.at_location, Location):
            self.at_location = Location(**as_dict(self.at_location))

        if not isinstance(self.deadlines, list):
            self.deadlines = [self.deadlines] if self.deadlines is not None else []
        self.deadlines = [v if isinstance(v, Deadline) else Deadline(**as_dict(v)) for v in self.deadlines]

        if not isinstance(self.related_to, list):
            self.related_to = [self.related_to] if self.related_to is not None else []
        self.related_to = [v if isinstance(v, ProcessRelation) else ProcessRelation(**as_dict(v)) for v in self.related_to]

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if self.event_mode is not None and not isinstance(self.event_mode, EventMode):
            self.event_mode = EventMode(self.event_mode)

        if self.landing_page is not None and not isinstance(self.landing_page, URI):
            self.landing_page = URI(self.landing_page)

        if not isinstance(self.doi, list):
            self.doi = [self.doi] if self.doi is not None else []
        self.doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.doi]

        if self.type is not None and not isinstance(self.type, EventType):
            self.type = EventType(self.type)

        self._normalize_inlined_as_list(slot_name="organizers", slot_type=Organizer, key_name="id", keyed=True)

        if not isinstance(self.academic_fields, list):
            self.academic_fields = [self.academic_fields] if self.academic_fields is not None else []
        self.academic_fields = [v if isinstance(v, AcademicField) else AcademicField(**as_dict(v)) for v in self.academic_fields]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        self._normalize_inlined_as_list(slot_name="sponsors", slot_type=Sponsor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="publications", slot_type=Publication, key_name="id", keyed=True)

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, str) else str(v) for v in self.topics]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.metrics]

        if self.context_info is not None and not isinstance(self.context_info, Context):
            self.context_info = Context(**as_dict(self.context_info))

        if not isinstance(self.gnd_id, list):
            self.gnd_id = [self.gnd_id] if self.gnd_id is not None else []
        self.gnd_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.gnd_id]

        if not isinstance(self.wikicfp_id, list):
            self.wikicfp_id = [self.wikicfp_id] if self.wikicfp_id is not None else []
        self.wikicfp_id = [v if isinstance(v, WikiCfpId) else WikiCfpId(**as_dict(v)) for v in self.wikicfp_id]

        if not isinstance(self.wikidata_id, list):
            self.wikidata_id = [self.wikidata_id] if self.wikidata_id is not None else []
        self.wikidata_id = [v if isinstance(v, WikidataId) else WikidataId(**as_dict(v)) for v in self.wikidata_id]

        if not isinstance(self.dpbl_id, list):
            self.dpbl_id = [self.dpbl_id] if self.dpbl_id is not None else []
        self.dpbl_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.dpbl_id]

        super().__post_init__(**kwargs)


@dataclass
class ProcessName(YAMLRoot):
    """
    The container for the various names denoting a planned process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000090"]
    class_class_curie: ClassVar[str] = "aeon:0000090"
    class_name: ClassVar[str] = "ProcessName"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.ProcessName

    official_name: str = None
    acronym: Optional[str] = None
    former_name: Optional[str] = None
    translated_name: Optional[Union[str, List[str]]] = empty_list()
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.official_name):
            self.MissingRequiredField("official_name")
        if not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.former_name is not None and not isinstance(self.former_name, str):
            self.former_name = str(self.former_name)

        if not isinstance(self.translated_name, list):
            self.translated_name = [self.translated_name] if self.translated_name is not None else []
        self.translated_name = [v if isinstance(v, str) else str(v) for v in self.translated_name]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class ExternalIdentifier(YAMLRoot):
    """
    An identifer of an entity declared in another schema.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.ExternalIdentifier
    class_class_curie: ClassVar[str] = "confident:ExternalIdentifier"
    class_name: ClassVar[str] = "ExternalIdentifier"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.ExternalIdentifier

    value: Optional[str] = None
    schema_name: Optional[str] = None
    schema_base_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class DigitalObjectId(ExternalIdentifier):
    """
    A centrally registered identifier symbol used to uniquely identify digital objects given by International DOI
    Foundation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0002110"]
    class_class_curie: ClassVar[str] = "obi:0002110"
    class_name: ClassVar[str] = "DigitalObjectId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.DigitalObjectId

    schema_name: Optional[str] = "DOI"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "https://doi.org"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class WikidataId(ExternalIdentifier):
    """
    The identifier of a thing (item) in Wikidata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = WIKIDATA.Q43649390
    class_class_curie: ClassVar[str] = "wikidata:Q43649390"
    class_name: ClassVar[str] = "WikidataId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.WikidataId

    schema_name: Optional[str] = "Wikidata"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "https://www.wikidata.org/entity/"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class GndId(ExternalIdentifier):
    """
    The identifier of a thing (item) in the German National authority file.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.GndId
    class_class_curie: ClassVar[str] = "confident:GndId"
    class_name: ClassVar[str] = "GndId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.GndId

    schema_name: Optional[str] = "GND"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "http://d-nb.info/gnd/"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class TibkatId(ExternalIdentifier):
    """
    The identifier of a publication in the TIB catalog.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.TibkatId
    class_class_curie: ClassVar[str] = "confident:TibkatId"
    class_name: ClassVar[str] = "TibkatId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.TibkatId

    schema_name: Optional[str] = "TIBKAT"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "https://www.tib.eu/en/search/id/TIBKAT:"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class DblpId(ExternalIdentifier):
    """
    The identifier of an academic event or series in dblp.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.DblpId
    class_class_curie: ClassVar[str] = "confident:DblpId"
    class_name: ClassVar[str] = "DblpId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.DblpId

    schema_name: Optional[str] = "dblp"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = URIRef(str(DBLP_SERIES))

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class WikiCfpId(ExternalIdentifier):
    """
    The identifier of an academic event or series in WikiCFP.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.WikiCfpId
    class_class_curie: ClassVar[str] = "confident:WikiCfpId"
    class_name: ClassVar[str] = "WikiCfpId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.WikiCfpId

    schema_name: Optional[str] = "WikiCFP"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "http://www.wikicfp.com/cfp/program?id="

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class EventFormatSpecification(YAMLRoot):
    """
    An academic event format specification is a plan specification that classifies a planned gathering of people in an
    academic context according to some sociocultural format, which provides implicit and explicit details on how this
    gathing is to be carried out by its participants in terms of achieving certain objectives, fulfiling certain
    conditions and performing certain actions. It thus concretizes the expectations of the contributors of an academic
    event. While the explicit details are often provied as concrete parts (e.g. deadline or attendance fee
    specifications), the implicit details depend on the semantics encoded in the words used for the classification of
    academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications
    can overlap or vary to a certain degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000004"]
    class_class_curie: ClassVar[str] = "aeon:0000004"
    class_name: ClassVar[str] = "EventFormatSpecification"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.EventFormatSpecification

    specified_as: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.specified_as):
            self.MissingRequiredField("specified_as")
        if not isinstance(self.specified_as, str):
            self.specified_as = str(self.specified_as)

        super().__post_init__(**kwargs)


@dataclass
class Deadline(YAMLRoot):
    """
    A container for event deadlines.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Deadline
    class_class_curie: ClassVar[str] = "confident:Deadline"
    class_name: ClassVar[str] = "Deadline"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Deadline

    type: Union[str, "DeadlineType"] = None
    deadline_date: Union[str, XSDDateTime] = None
    deadline_other: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, DeadlineType):
            self.type = DeadlineType(self.type)

        if self._is_empty(self.deadline_date):
            self.MissingRequiredField("deadline_date")
        if not isinstance(self.deadline_date, XSDDateTime):
            self.deadline_date = XSDDateTime(self.deadline_date)

        if self.deadline_other is not None and not isinstance(self.deadline_other, str):
            self.deadline_other = str(self.deadline_other)

        super().__post_init__(**kwargs)


@dataclass
class Metric(YAMLRoot):
    """
    A container for statistical information about a planned process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Metric
    class_class_curie: ClassVar[str] = "confident:Metric"
    class_name: ClassVar[str] = "Metric"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Metric

    type: Optional[Union[str, "MetricType"]] = None
    int_value: Optional[int] = None
    str_value: Optional[str] = None
    rate_value: Optional[float] = None
    truth_value: Optional[Union[bool, Bool]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, MetricType):
            self.type = MetricType(self.type)

        if self.int_value is not None and not isinstance(self.int_value, int):
            self.int_value = int(self.int_value)

        if self.str_value is not None and not isinstance(self.str_value, str):
            self.str_value = str(self.str_value)

        if self.rate_value is not None and not isinstance(self.rate_value, float):
            self.rate_value = float(self.rate_value)

        if self.truth_value is not None and not isinstance(self.truth_value, Bool):
            self.truth_value = Bool(self.truth_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ProcessRelation(YAMLRoot):
    """
    A container for relations between academic events.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.ProcessRelation
    class_class_curie: ClassVar[str] = "confident:ProcessRelation"
    class_name: ClassVar[str] = "ProcessRelation"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.ProcessRelation

    type: Optional[Union[str, "RelationType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, RelationType):
            self.type = RelationType(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Location(YAMLRoot):
    """
    A container for the information about the location in which an academic event takes place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Location
    class_class_curie: ClassVar[str] = "confident:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Location

    city: Optional[Union[str, CityId]] = None
    country: Optional[Union[str, CountryId]] = None
    region: Optional[Union[str, RegionId]] = None
    venue: Optional[Union[str, VenueId]] = None
    lattitude: Optional[float] = None
    longitude: Optional[float] = None
    meeting_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.city is not None and not isinstance(self.city, CityId):
            self.city = CityId(self.city)

        if self.country is not None and not isinstance(self.country, CountryId):
            self.country = CountryId(self.country)

        if self.region is not None and not isinstance(self.region, RegionId):
            self.region = RegionId(self.region)

        if self.venue is not None and not isinstance(self.venue, VenueId):
            self.venue = VenueId(self.venue)

        if self.lattitude is not None and not isinstance(self.lattitude, float):
            self.lattitude = float(self.lattitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.meeting_url is not None and not isinstance(self.meeting_url, URIorCURIE):
            self.meeting_url = URIorCURIE(self.meeting_url)

        super().__post_init__(**kwargs)


@dataclass
class City(YAMLRoot):
    """
    The city in which an academic event takes place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.City
    class_class_curie: ClassVar[str] = "confident:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.City

    id: Union[str, CityId] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CityId):
            self.id = CityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class Country(YAMLRoot):
    """
    The country in which an academic event takes place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Country
    class_class_curie: ClassVar[str] = "confident:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Country

    id: Union[str, CountryId] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountryId):
            self.id = CountryId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class Region(YAMLRoot):
    """
    The region in which an academic event takes place. For non USA events this might often be negligible.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Region
    class_class_curie: ClassVar[str] = "confident:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Region

    id: Union[str, RegionId] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegionId):
            self.id = RegionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class Venue(YAMLRoot):
    """
    The venue at which an academic event takes place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Venue
    class_class_curie: ClassVar[str] = "confident:Venue"
    class_name: ClassVar[str] = "Venue"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Venue

    id: Union[str, VenueId] = None
    street: Optional[str] = None
    zip_code: Optional[str] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VenueId):
            self.id = VenueId(self.id)

        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        if self.zip_code is not None and not isinstance(self.zip_code, str):
            self.zip_code = str(self.zip_code)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class AcademicField(YAMLRoot):
    """
    An academic field is the scientific subject of a planned process according to some controlled vocabulary or
    thesaurus and as such requires the scheme URI.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.AcademicField
    class_class_curie: ClassVar[str] = "confident:AcademicField"
    class_name: ClassVar[str] = "AcademicField"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.AcademicField

    value: str = None
    schema_name: Optional[str] = None
    schema_base_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class Context(YAMLRoot):
    """
    A container to provide extra information, such as call of papers event description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Context
    class_class_curie: ClassVar[str] = "confident:Context"
    class_name: ClassVar[str] = "Context"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Context

    text: Optional[str] = None
    license_str: Optional[str] = None
    license_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        if self.license_str is not None and not isinstance(self.license_str, str):
            self.license_str = str(self.license_str)

        if self.license_url is not None and not isinstance(self.license_url, URIorCURIE):
            self.license_url = URIorCURIE(self.license_url)

        super().__post_init__(**kwargs)


@dataclass
class Contributor(YAMLRoot):
    """
    A contributor is a person or organization that holds a contributor role which is being realized in a planned
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Contributor
    class_class_curie: ClassVar[str] = "confident:Contributor"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Contributor

    id: Union[str, ContributorId] = None
    type: Optional[str] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorId):
            self.id = ContributorId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class Sponsor(Contributor):
    """
    A person or an organization whose role it is to sponsor an academic event or event series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Sponsor
    class_class_curie: ClassVar[str] = "confident:Sponsor"
    class_name: ClassVar[str] = "Sponsor"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Sponsor

    id: Union[str, SponsorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SponsorId):
            self.id = SponsorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Attendee(Contributor):
    """
    A person whose only role it is to attend an academic event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Attendee
    class_class_curie: ClassVar[str] = "confident:Attendee"
    class_name: ClassVar[str] = "Attendee"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Attendee

    id: Union[str, AttendeeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttendeeId):
            self.id = AttendeeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Moderator(Contributor):
    """
    A person that has the role to moderate an academic event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Moderator
    class_class_curie: ClassVar[str] = "confident:Moderator"
    class_name: ClassVar[str] = "Moderator"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Moderator

    id: Union[str, ModeratorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModeratorId):
            self.id = ModeratorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Reviewer(Contributor):
    """
    A person that has the role to review the submissions of an academic event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Reviewer
    class_class_curie: ClassVar[str] = "confident:Reviewer"
    class_name: ClassVar[str] = "Reviewer"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Reviewer

    id: Union[str, ReviewerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReviewerId):
            self.id = ReviewerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Organizer(Contributor):
    """
    An organizer of an academic event or event series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Organizer
    class_class_curie: ClassVar[str] = "confident:Organizer"
    class_name: ClassVar[str] = "Organizer"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Organizer

    id: Union[str, OrganizerId] = None
    contact: Optional[Union[dict, "ContactPerson"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizerId):
            self.id = OrganizerId(self.id)

        if self.contact is not None and not isinstance(self.contact, ContactPerson):
            self.contact = ContactPerson(**as_dict(self.contact))

        super().__post_init__(**kwargs)


@dataclass
class ContactPerson(Organizer):
    """
    The contact person of an academic event or event series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.ContactPerson
    class_class_curie: ClassVar[str] = "confident:ContactPerson"
    class_name: ClassVar[str] = "ContactPerson"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.ContactPerson

    id: Union[str, ContactPersonId] = EX.ContactPerson
    email: Optional[str] = None
    telephone: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContactPersonId):
            self.id = ContactPersonId(self.id)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.telephone is not None and not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        super().__post_init__(**kwargs)


@dataclass
class CommitteeMember(Organizer):
    """
    A members of an academic event committee.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.CommitteeMember
    class_class_curie: ClassVar[str] = "confident:CommitteeMember"
    class_name: ClassVar[str] = "CommitteeMember"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.CommitteeMember

    id: Union[str, CommitteeMemberId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommitteeMemberId):
            self.id = CommitteeMemberId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CommitteeChair(CommitteeMember):
    """
    The head of an academic event committee.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.CommitteeChair
    class_class_curie: ClassVar[str] = "confident:CommitteeChair"
    class_name: ClassVar[str] = "CommitteeChair"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.CommitteeChair

    id: Union[str, CommitteeChairId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommitteeChairId):
            self.id = CommitteeChairId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Presenter(Contributor):
    """
    A person that presents its work at an academic event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Presenter
    class_class_curie: ClassVar[str] = "confident:Presenter"
    class_name: ClassVar[str] = "Presenter"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Presenter

    id: Union[str, PresenterId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PresenterId):
            self.id = PresenterId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KeynoteSpeaker(Presenter):
    """
    A 'keynote speaker' is a presenter that is an invited person - often a multiplier in his or her (research) field -
    responsible for delivering a keynote speech.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.KeynoteSpeaker
    class_class_curie: ClassVar[str] = "confident:KeynoteSpeaker"
    class_name: ClassVar[str] = "KeynoteSpeaker"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.KeynoteSpeaker

    id: Union[str, KeynoteSpeakerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeynoteSpeakerId):
            self.id = KeynoteSpeakerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    """
    A published work, e.g. proceedings or conferenc paper, that is the output of an academic event or series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Publication
    class_class_curie: ClassVar[str] = "confident:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Publication

    id: Union[str, PublicationId] = None
    doi: Optional[Union[Union[dict, DigitalObjectId], List[Union[dict, DigitalObjectId]]]] = empty_list()
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if not isinstance(self.doi, list):
            self.doi = [self.doi] if self.doi is not None else []
        self.doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.doi]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass
class ConfIDentRecords(YAMLRoot):
    """
    A container to be able to bundle academic event data and series in one data file (e.g. YAML or JSON).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.ConfIDentRecords
    class_class_curie: ClassVar[str] = "confident:ConfIDentRecords"
    class_name: ClassVar[str] = "ConfIDentRecords"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.ConfIDentRecords

    events: Optional[Union[Dict[Union[str, AcademicEventId], Union[dict, AcademicEvent]], List[Union[dict, AcademicEvent]]]] = empty_dict()
    series: Optional[Union[Dict[Union[str, AcademicEventSeriesId], Union[dict, AcademicEventSeries]], List[Union[dict, AcademicEventSeries]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="events", slot_type=AcademicEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="series", slot_type=AcademicEventSeries, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class EventType(EnumDefinitionImpl):
    """
    The most common minimal event types. For event types that are not in this list, you can use "other" and provide
    the label of this other event format using the [event_format](event_format) property.
    """
    colloquium = PermissibleValue(text="colloquium",
                                           description="A colloquium is an academic meeting that usually lasts only a few hours and serves to discuss a specific topic. Colloquia are usually part of the academic exchange in everyday university life with only one speaker, but can also take place on special occasions (anniversaries, start or end of the lecture phase, etc.) and can have more than one speaker.",
                                           meaning=AEON["0000101"])
    conference = PermissibleValue(text="conference",
                                           description="A conference is an academic event that lasts up to several days and serves as a forum for presentations on a specific topic or subject area. In addition to subject-specific conferences, there are also interdisciplinary conferences which allow both a broader focus and more specific questions on a particular (academic) problem. Conferences often have a highly formalized structure of parallel, clearly defined sessions with several short presentations and plenary sessions with invited (keynote) speakers who are considered multipliers in their (research) field. Ideally, the selection of the speakers and their contributions is subject to a review process.",
                                           meaning=AEON["0000103"])
    congress = PermissibleValue(text="congress",
                                       description="A congress is a certain type of conference which is characterised by a larger number of participants (often several hundred) and is oftentimes organised jointly by large, established (e.g. specialised societies) and/or several institutions. Congresses have a broader thematic focus than simple conferences, take place in certain cycles, but can still target an exclusive group of participants (e.g. representatives of a single discipline).",
                                       meaning=AEON["0000123"])
    session = PermissibleValue(text="session",
                                     description="A session is a clearly defined part of a academic event in which a small number of speakers (usually 2-5) focus on a specific topic. A session is usually formally accompanied by a session chair, who assumes the function of a moderator.",
                                     meaning=AEON["0000111"])
    talk = PermissibleValue(text="talk",
                               description="A talk is a central part of a larger academic event, at which a specific topic is being presented in a rather short way.",
                               meaning=AEON["0000125"])
    forum = PermissibleValue(text="forum",
                                 description="An academic event whose sociocultural format is determined in an academic event type specification that classifies the academic event as a forum.",
                                 meaning=AEON["0000105"])
    hackathon = PermissibleValue(text="hackathon",
                                         description="A hackathon is a gathering of software developers with the goal to develop software collaboratively in a short timeframe.",
                                         meaning=AEON["0000107"])
    seminar = PermissibleValue(text="seminar",
                                     description="A seminar can serve as a term for older conference series, but in current usage the term mainly describes a specific teaching format that serves to develop content and provides space for discussion. Participation from the audience is usually encouraged.",
                                     meaning=AEON["0000109"])
    symposium = PermissibleValue(text="symposium",
                                         description="A symposium is a specific type of conference with a narrower thematic focus, with fewer participants and of shorter duration. The degree of structuring lies between a classic conference and a workshop, allows more discussion than the larger conference, but is usually more formalized than the workshop.",
                                         meaning=AEON["0000113"])
    tutorial = PermissibleValue(text="tutorial",
                                       description="An academic event that has the function to educate the audience on a certain topic. A tutorial is often realized as an academic event talk or academic event session.",
                                       meaning=AEON["0000119"])
    workshop = PermissibleValue(text="workshop",
                                       description="Workshops are smaller academic events that serve to exchange information on a specific topic or problem. They usually last one or two days and offer space for discussion and the development of content and solutions. Group work is often part of the event concept.",
                                       meaning=AEON["0000121"])
    other = PermissibleValue(text="other",
                                 description="This value is to be used if the event format cannot be represented using one of the other permissible values defined in the [EventFormat](https://stroemphi.github.io/ConfIDent-schema/EventFormat/) enum. If this value is chosen the use of [other_format](https://stroemphi.github.io/ConfIDent-schema/academicEvent__other_format/) is mandatory.",
                                 meaning=AEON["0000001"])

    _defn = EnumDefinition(
        name="EventType",
        description="The most common minimal event types. For event types that are not in this list, you can use \"other\" and provide the label of this other event format using the [event_format](event_format) property.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "poster session",
                PermissibleValue(text="poster session",
                                 description="A poster session is a session at which poster papers are presented.",
                                 meaning=AEON["0000127"]) )
        setattr(cls, "keynote speech",
                PermissibleValue(text="keynote speech",
                                 description="A keynote speech is a special talk that has the function to set the underlying tone and summarize the core message or most important revelation of the academic event at which it is given.",
                                 meaning=AEON["00001115"]) )
        setattr(cls, "event track",
                PermissibleValue(text="event track",
                                 description="An academic event that, as a part of a larger academic event, has the function to group even smaller parts of the academic event, like sessions and talks, according to a shared theme or topic. It usually has dedicated chairs and program committees.",
                                 meaning=AEON["00001117"]) )

class EventStatus(EnumDefinitionImpl):
    """
    The status of the academic event which indicates if it takes place as planned.
    """
    postponed = PermissibleValue(text="postponed")
    delayed = PermissibleValue(text="delayed")
    canceled = PermissibleValue(text="canceled")
    planned = PermissibleValue(text="planned")

    _defn = EnumDefinition(
        name="EventStatus",
        description="The status of the academic event which indicates if it takes place as planned.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "as scheduled",
                PermissibleValue(text="as scheduled",
                                 description="Default: used to indicate that the event takes place as planned.") )

class EventMode(EnumDefinitionImpl):
    """
    An enum to specify if an academic event is in person, virtual or a hybrid of both.
    """
    online = PermissibleValue(text="online",
                                   description="The event takes place in a virtual location.")
    hybrid = PermissibleValue(text="hybrid",
                                   description="The event takes place physically and virtually.")

    _defn = EnumDefinition(
        name="EventMode",
        description="An enum to specify if an academic event is in person, virtual or a hybrid of both.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "on site",
                PermissibleValue(text="on site",
                                 description="The event takes place in a physical location.") )

class DeadlineType(EnumDefinitionImpl):
    """
    An enum that specifies the possible kinds of deadlines of an academic event.
    """
    other = PermissibleValue(text="other",
                                 description="This value is to be used, if the other allowed values are not applicable.")

    _defn = EnumDefinition(
        name="DeadlineType",
        description="An enum that specifies the possible kinds of deadlines of an academic event.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "submission deadline",
                PermissibleValue(text="submission deadline",
                                 meaning=AEON["0000067"]) )
        setattr(cls, "notification deadline",
                PermissibleValue(text="notification deadline",
                                 meaning=AEON["0000064"]) )
        setattr(cls, "abstract deadline",
                PermissibleValue(text="abstract deadline",
                                 meaning=AEON["0000061"]) )
        setattr(cls, "camera-ready deadline",
                PermissibleValue(text="camera-ready deadline",
                                 meaning=AEON["0000062"]) )
        setattr(cls, "demo deadline",
                PermissibleValue(text="demo deadline",
                                 meaning=AEON["0000063"]) )
        setattr(cls, "paper deadline",
                PermissibleValue(text="paper deadline",
                                 meaning=AEON["0000065"]) )
        setattr(cls, "poster deadline",
                PermissibleValue(text="poster deadline",
                                 meaning=AEON["0000066"]) )
        setattr(cls, "tutorial deadline",
                PermissibleValue(text="tutorial deadline",
                                 meaning=AEON["0000068"]) )
        setattr(cls, "workshop deadline",
                PermissibleValue(text="workshop deadline",
                                 meaning=AEON["0000069"]) )

class RelationType(EnumDefinitionImpl):
    """
    The kinds of relations that are allowed between academic events.
    """
    isUmbrellaEventOf = PermissibleValue(text="isUmbrellaEventOf")
    hasUmbrellaEvent = PermissibleValue(text="hasUmbrellaEvent")
    isJointEventOf = PermissibleValue(text="isJointEventOf")
    isColocatedEventOf = PermissibleValue(text="isColocatedEventOf")
    isSubEventOf = PermissibleValue(text="isSubEventOf")
    hasSubEvent = PermissibleValue(text="hasSubEvent")

    _defn = EnumDefinition(
        name="RelationType",
        description="The kinds of relations that are allowed between academic events.",
    )

class MetricType(EnumDefinitionImpl):
    """
    The possible metric of an academic event.
    """
    frequency = PermissibleValue(text="frequency",
                                         description="The time frame in which the events of a series reoccur.")

    _defn = EnumDefinition(
        name="MetricType",
        description="The possible metric of an academic event.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "submitted papers",
                PermissibleValue(text="submitted papers") )
        setattr(cls, "accepted papers",
                PermissibleValue(text="accepted papers") )
        setattr(cls, "accepted short papers",
                PermissibleValue(text="accepted short papers") )
        setattr(cls, "number of attendees",
                PermissibleValue(text="number of attendees") )
        setattr(cls, "number of tracks",
                PermissibleValue(text="number of tracks") )
        setattr(cls, "has childcare options",
                PermissibleValue(text="has childcare options") )
        setattr(cls, "is accessible",
                PermissibleValue(text="is accessible",
                                 description="If true then the event is accessible for people with impairments.") )

class ContributorType(EnumDefinitionImpl):
    """
    An enumaration used to distinguish the contributors of a planned process with regard to them being either an
    organization or a person.
    """
    organization = PermissibleValue(text="organization",
                                               description="An institution, or an association that has one or more people as members and which actsas some kind of participant in a planned process.")
    person = PermissibleValue(text="person",
                                   description="A human being that acts as some kind of participant in a planned process.")

    _defn = EnumDefinition(
        name="ContributorType",
        description="An enumaration used to distinguish the contributors of a planned process with regard to them being either an organization or a person.",
    )

# Slots
class slots:
    pass

slots.type = Slot(uri=CONFIDENT.type, name="type", curie=CONFIDENT.curie('type'),
                   model_uri=CONFIDENT.type, domain=None, range=Optional[str])

slots.doi = Slot(uri=IAO['0000235'], name="doi", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.doi, domain=None, range=Optional[Union[Union[dict, DigitalObjectId], List[Union[dict, DigitalObjectId]]]])

slots.gnd_id = Slot(uri=IAO['0000235'], name="gnd_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.gnd_id, domain=None, range=Optional[Union[Union[dict, GndId], List[Union[dict, GndId]]]])

slots.wikidata_id = Slot(uri=IAO['0000235'], name="wikidata_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.wikidata_id, domain=None, range=Optional[Union[Union[dict, WikidataId], List[Union[dict, WikidataId]]]])

slots.name = Slot(uri=SDO.name, name="name", curie=SDO.curie('name'),
                   model_uri=CONFIDENT.name, domain=None, range=Optional[str])

slots.id = Slot(uri=CONFIDENT.id, name="id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=IAO['0000235'], name="external_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.external_id, domain=None, range=Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]])

slots.value = Slot(uri=CONFIDENT.value, name="value", curie=CONFIDENT.curie('value'),
                   model_uri=CONFIDENT.value, domain=None, range=Optional[str])

slots.schema_name = Slot(uri=CONFIDENT.schema_name, name="schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.schema_name, domain=None, range=Optional[str])

slots.schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.schema_base_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.process_name = Slot(uri=IAO['0000235'], name="process_name", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.process_name, domain=PlannedProcess, range=Optional[Union[dict, "ProcessName"]])

slots.landing_page = Slot(uri=CONFIDENT.landing_page, name="landing_page", curie=CONFIDENT.curie('landing_page'),
                   model_uri=CONFIDENT.landing_page, domain=PlannedProcess, range=Optional[Union[str, URI]])

slots.organizers = Slot(uri=CONFIDENT.organizers, name="organizers", curie=CONFIDENT.curie('organizers'),
                   model_uri=CONFIDENT.organizers, domain=PlannedProcess, range=Optional[Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]]])

slots.academic_fields = Slot(uri=AEON['0000040'], name="academic_fields", curie=AEON.curie('0000040'),
                   model_uri=CONFIDENT.academic_fields, domain=PlannedProcess, range=Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]])

slots.website = Slot(uri=CONFIDENT.website, name="website", curie=CONFIDENT.curie('website'),
                   model_uri=CONFIDENT.website, domain=PlannedProcess, range=Optional[Union[str, URI]])

slots.contact = Slot(uri=CONFIDENT.contact, name="contact", curie=CONFIDENT.curie('contact'),
                   model_uri=CONFIDENT.contact, domain=PlannedProcess, range=Optional[Union[dict, "ContactPerson"]])

slots.sponsors = Slot(uri=CONFIDENT.sponsors, name="sponsors", curie=CONFIDENT.curie('sponsors'),
                   model_uri=CONFIDENT.sponsors, domain=PlannedProcess, range=Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]])

slots.publications = Slot(uri=CONFIDENT.publications, name="publications", curie=CONFIDENT.curie('publications'),
                   model_uri=CONFIDENT.publications, domain=PlannedProcess, range=Optional[Union[str, List[str]]])

slots.topics = Slot(uri=CONFIDENT.topics, name="topics", curie=CONFIDENT.curie('topics'),
                   model_uri=CONFIDENT.topics, domain=PlannedProcess, range=Optional[Union[str, List[str]]])

slots.metrics = Slot(uri=CONFIDENT.metrics, name="metrics", curie=CONFIDENT.curie('metrics'),
                   model_uri=CONFIDENT.metrics, domain=PlannedProcess, range=Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]])

slots.context_info = Slot(uri=CONFIDENT.context_info, name="context_info", curie=CONFIDENT.curie('context_info'),
                   model_uri=CONFIDENT.context_info, domain=PlannedProcess, range=Optional[Union[dict, "Context"]])

slots.wikicfp_id = Slot(uri=IAO['0000235'], name="wikicfp_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.wikicfp_id, domain=PlannedProcess, range=Optional[Union[Union[dict, "WikiCfpId"], List[Union[dict, "WikiCfpId"]]]])

slots.dpbl_id = Slot(uri=IAO['0000235'], name="dpbl_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.dpbl_id, domain=PlannedProcess, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.academicEventSeries__series_of = Slot(uri=CONFIDENT.series_of, name="academicEventSeries__series_of", curie=CONFIDENT.curie('series_of'),
                   model_uri=CONFIDENT.academicEventSeries__series_of, domain=AcademicEventSeries, range=Optional[Union[str, AcademicEventId]])

slots.academicEvent__index = Slot(uri=CONFIDENT.index, name="academicEvent__index", curie=CONFIDENT.curie('index'),
                   model_uri=CONFIDENT.academicEvent__index, domain=None, range=Optional[int])

slots.academicEvent__start_date = Slot(uri=AEON.start_date, name="academicEvent__start_date", curie=AEON.curie('start_date'),
                   model_uri=CONFIDENT.academicEvent__start_date, domain=AcademicEvent, range=Union[str, XSDDateTime])

slots.academicEvent__end_date = Slot(uri=AEON.end_date, name="academicEvent__end_date", curie=AEON.curie('end_date'),
                   model_uri=CONFIDENT.academicEvent__end_date, domain=AcademicEvent, range=Union[str, XSDDateTime])

slots.academicEvent__event_status = Slot(uri=AEON.event_status, name="academicEvent__event_status", curie=AEON.curie('event_status'),
                   model_uri=CONFIDENT.academicEvent__event_status, domain=AcademicEvent, range=Union[str, "EventStatus"])

slots.academicEvent__in_series = Slot(uri=CONFIDENT.in_series, name="academicEvent__in_series", curie=CONFIDENT.curie('in_series'),
                   model_uri=CONFIDENT.academicEvent__in_series, domain=AcademicEvent, range=Optional[Union[str, AcademicEventSeriesId]])

slots.academicEvent__event_format = Slot(uri=AEON['0000032'], name="academicEvent__event_format", curie=AEON.curie('0000032'),
                   model_uri=CONFIDENT.academicEvent__event_format, domain=AcademicEvent, range=Optional[Union[dict, "EventFormatSpecification"]])

slots.academicEvent__at_location = Slot(uri=CONFIDENT.at_location, name="academicEvent__at_location", curie=CONFIDENT.curie('at_location'),
                   model_uri=CONFIDENT.academicEvent__at_location, domain=AcademicEvent, range=Optional[Union[dict, "Location"]])

slots.academicEvent__deadlines = Slot(uri=CONFIDENT.deadlines, name="academicEvent__deadlines", curie=CONFIDENT.curie('deadlines'),
                   model_uri=CONFIDENT.academicEvent__deadlines, domain=AcademicEvent, range=Optional[Union[Union[dict, "Deadline"], List[Union[dict, "Deadline"]]]])

slots.academicEvent__related_to = Slot(uri=CONFIDENT.related_to, name="academicEvent__related_to", curie=CONFIDENT.curie('related_to'),
                   model_uri=CONFIDENT.academicEvent__related_to, domain=AcademicEvent, range=Optional[Union[Union[dict, "ProcessRelation"], List[Union[dict, "ProcessRelation"]]]])

slots.academicEvent__ordinal = Slot(uri=AEON.event_number, name="academicEvent__ordinal", curie=AEON.curie('event_number'),
                   model_uri=CONFIDENT.academicEvent__ordinal, domain=AcademicEvent, range=Optional[int])

slots.academicEvent__event_mode = Slot(uri=CONFIDENT.event_mode, name="academicEvent__event_mode", curie=CONFIDENT.curie('event_mode'),
                   model_uri=CONFIDENT.academicEvent__event_mode, domain=AcademicEvent, range=Optional[Union[str, "EventMode"]])

slots.processName__official_name = Slot(uri=SKOS.perfLabel, name="processName__official_name", curie=SKOS.curie('perfLabel'),
                   model_uri=CONFIDENT.processName__official_name, domain=ProcessName, range=str)

slots.processName__acronym = Slot(uri=AEON['0000091'], name="processName__acronym", curie=AEON.curie('0000091'),
                   model_uri=CONFIDENT.processName__acronym, domain=ProcessName, range=Optional[str])

slots.processName__former_name = Slot(uri=CONFIDENT.former_name, name="processName__former_name", curie=CONFIDENT.curie('former_name'),
                   model_uri=CONFIDENT.processName__former_name, domain=ProcessName, range=Optional[str])

slots.processName__translated_name = Slot(uri=SKOS.altLabel, name="processName__translated_name", curie=SKOS.curie('altLabel'),
                   model_uri=CONFIDENT.processName__translated_name, domain=ProcessName, range=Optional[Union[str, List[str]]])

slots.processName__aliases = Slot(uri=SKOS.altLabel, name="processName__aliases", curie=SKOS.curie('altLabel'),
                   model_uri=CONFIDENT.processName__aliases, domain=ProcessName, range=Optional[Union[str, List[str]]])

slots.eventFormatSpecification__specified_as = Slot(uri=OBI['0002815'], name="eventFormatSpecification__specified_as", curie=OBI.curie('0002815'),
                   model_uri=CONFIDENT.eventFormatSpecification__specified_as, domain=EventFormatSpecification, range=str)

slots.deadline__deadline_date = Slot(uri=CONFIDENT.deadline_date, name="deadline__deadline_date", curie=CONFIDENT.curie('deadline_date'),
                   model_uri=CONFIDENT.deadline__deadline_date, domain=Deadline, range=Union[str, XSDDateTime])

slots.deadline__deadline_other = Slot(uri=CONFIDENT.deadline_other, name="deadline__deadline_other", curie=CONFIDENT.curie('deadline_other'),
                   model_uri=CONFIDENT.deadline__deadline_other, domain=Deadline, range=Optional[str])

slots.metric__int_value = Slot(uri=CONFIDENT.int_value, name="metric__int_value", curie=CONFIDENT.curie('int_value'),
                   model_uri=CONFIDENT.metric__int_value, domain=Metric, range=Optional[int])

slots.metric__str_value = Slot(uri=CONFIDENT.str_value, name="metric__str_value", curie=CONFIDENT.curie('str_value'),
                   model_uri=CONFIDENT.metric__str_value, domain=Metric, range=Optional[str])

slots.metric__rate_value = Slot(uri=CONFIDENT.rate_value, name="metric__rate_value", curie=CONFIDENT.curie('rate_value'),
                   model_uri=CONFIDENT.metric__rate_value, domain=Metric, range=Optional[float])

slots.metric__truth_value = Slot(uri=CONFIDENT.truth_value, name="metric__truth_value", curie=CONFIDENT.curie('truth_value'),
                   model_uri=CONFIDENT.metric__truth_value, domain=Metric, range=Optional[Union[bool, Bool]])

slots.metric__description = Slot(uri=CONFIDENT.description, name="metric__description", curie=CONFIDENT.curie('description'),
                   model_uri=CONFIDENT.metric__description, domain=Metric, range=Optional[str])

slots.location__city = Slot(uri=CONFIDENT.city, name="location__city", curie=CONFIDENT.curie('city'),
                   model_uri=CONFIDENT.location__city, domain=Location, range=Optional[Union[str, CityId]])

slots.location__country = Slot(uri=CONFIDENT.country, name="location__country", curie=CONFIDENT.curie('country'),
                   model_uri=CONFIDENT.location__country, domain=Location, range=Optional[Union[str, CountryId]])

slots.location__region = Slot(uri=CONFIDENT.region, name="location__region", curie=CONFIDENT.curie('region'),
                   model_uri=CONFIDENT.location__region, domain=Location, range=Optional[Union[str, RegionId]])

slots.location__venue = Slot(uri=CONFIDENT.venue, name="location__venue", curie=CONFIDENT.curie('venue'),
                   model_uri=CONFIDENT.location__venue, domain=Location, range=Optional[Union[str, VenueId]])

slots.location__lattitude = Slot(uri=CONFIDENT.lattitude, name="location__lattitude", curie=CONFIDENT.curie('lattitude'),
                   model_uri=CONFIDENT.location__lattitude, domain=Location, range=Optional[float])

slots.location__longitude = Slot(uri=CONFIDENT.longitude, name="location__longitude", curie=CONFIDENT.curie('longitude'),
                   model_uri=CONFIDENT.location__longitude, domain=Location, range=Optional[float])

slots.location__meeting_url = Slot(uri=CONFIDENT.meeting_url, name="location__meeting_url", curie=CONFIDENT.curie('meeting_url'),
                   model_uri=CONFIDENT.location__meeting_url, domain=Location, range=Optional[Union[str, URIorCURIE]])

slots.venue__street = Slot(uri=CONFIDENT.street, name="venue__street", curie=CONFIDENT.curie('street'),
                   model_uri=CONFIDENT.venue__street, domain=Venue, range=Optional[str])

slots.venue__zip_code = Slot(uri=CONFIDENT.zip_code, name="venue__zip_code", curie=CONFIDENT.curie('zip_code'),
                   model_uri=CONFIDENT.venue__zip_code, domain=Venue, range=Optional[str])

slots.context__text = Slot(uri=CONFIDENT.text, name="context__text", curie=CONFIDENT.curie('text'),
                   model_uri=CONFIDENT.context__text, domain=Context, range=Optional[str])

slots.context__license_str = Slot(uri=CONFIDENT.license_str, name="context__license_str", curie=CONFIDENT.curie('license_str'),
                   model_uri=CONFIDENT.context__license_str, domain=Context, range=Optional[str])

slots.context__license_url = Slot(uri=CONFIDENT.license_url, name="context__license_url", curie=CONFIDENT.curie('license_url'),
                   model_uri=CONFIDENT.context__license_url, domain=Context, range=Optional[Union[str, URIorCURIE]])

slots.organizer__contact = Slot(uri=CONFIDENT.contact, name="organizer__contact", curie=CONFIDENT.curie('contact'),
                   model_uri=CONFIDENT.organizer__contact, domain=None, range=Optional[Union[dict, ContactPerson]])

slots.contactPerson__email = Slot(uri=SDO.email, name="contactPerson__email", curie=SDO.curie('email'),
                   model_uri=CONFIDENT.contactPerson__email, domain=ContactPerson, range=Optional[str],
                   pattern=re.compile(r'\b[-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'))

slots.contactPerson__telephone = Slot(uri=SDO.telephone, name="contactPerson__telephone", curie=SDO.curie('telephone'),
                   model_uri=CONFIDENT.contactPerson__telephone, domain=ContactPerson, range=Optional[str])

slots.confIDentRecords__events = Slot(uri=CONFIDENT.events, name="confIDentRecords__events", curie=CONFIDENT.curie('events'),
                   model_uri=CONFIDENT.confIDentRecords__events, domain=ConfIDentRecords, range=Optional[Union[Dict[Union[str, AcademicEventId], Union[dict, AcademicEvent]], List[Union[dict, AcademicEvent]]]])

slots.confIDentRecords__series = Slot(uri=CONFIDENT.series, name="confIDentRecords__series", curie=CONFIDENT.curie('series'),
                   model_uri=CONFIDENT.confIDentRecords__series, domain=ConfIDentRecords, range=Optional[Union[Dict[Union[str, AcademicEventSeriesId], Union[dict, AcademicEventSeries]], List[Union[dict, AcademicEventSeries]]]])

slots.AcademicEventSeries_id = Slot(uri=CONFIDENT.id, name="AcademicEventSeries_id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.AcademicEventSeries_id, domain=AcademicEventSeries, range=Union[str, AcademicEventSeriesId])

slots.AcademicEventSeries_process_name = Slot(uri=IAO['0000235'], name="AcademicEventSeries_process_name", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEventSeries_process_name, domain=AcademicEventSeries, range=Union[dict, "ProcessName"])

slots.AcademicEventSeries_landing_page = Slot(uri=CONFIDENT.landing_page, name="AcademicEventSeries_landing_page", curie=CONFIDENT.curie('landing_page'),
                   model_uri=CONFIDENT.AcademicEventSeries_landing_page, domain=AcademicEventSeries, range=Optional[Union[str, URI]])

slots.AcademicEventSeries_doi = Slot(uri=IAO['0000235'], name="AcademicEventSeries_doi", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEventSeries_doi, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]])

slots.AcademicEventSeries_organizers = Slot(uri=CONFIDENT.organizers, name="AcademicEventSeries_organizers", curie=CONFIDENT.curie('organizers'),
                   model_uri=CONFIDENT.AcademicEventSeries_organizers, domain=AcademicEventSeries, range=Optional[Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]]])

slots.AcademicEventSeries_academic_fields = Slot(uri=AEON['0000040'], name="AcademicEventSeries_academic_fields", curie=AEON.curie('0000040'),
                   model_uri=CONFIDENT.AcademicEventSeries_academic_fields, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]])

slots.AcademicEventSeries_website = Slot(uri=CONFIDENT.website, name="AcademicEventSeries_website", curie=CONFIDENT.curie('website'),
                   model_uri=CONFIDENT.AcademicEventSeries_website, domain=AcademicEventSeries, range=Optional[Union[str, URI]])

slots.AcademicEventSeries_sponsors = Slot(uri=CONFIDENT.sponsors, name="AcademicEventSeries_sponsors", curie=CONFIDENT.curie('sponsors'),
                   model_uri=CONFIDENT.AcademicEventSeries_sponsors, domain=AcademicEventSeries, range=Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]])

slots.AcademicEventSeries_publications = Slot(uri=CONFIDENT.publications, name="AcademicEventSeries_publications", curie=CONFIDENT.curie('publications'),
                   model_uri=CONFIDENT.AcademicEventSeries_publications, domain=AcademicEventSeries, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.AcademicEventSeries_topics = Slot(uri=CONFIDENT.topics, name="AcademicEventSeries_topics", curie=CONFIDENT.curie('topics'),
                   model_uri=CONFIDENT.AcademicEventSeries_topics, domain=AcademicEventSeries, range=Optional[Union[str, List[str]]])

slots.AcademicEventSeries_metrics = Slot(uri=CONFIDENT.metrics, name="AcademicEventSeries_metrics", curie=CONFIDENT.curie('metrics'),
                   model_uri=CONFIDENT.AcademicEventSeries_metrics, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]])

slots.AcademicEventSeries_context_info = Slot(uri=CONFIDENT.context_info, name="AcademicEventSeries_context_info", curie=CONFIDENT.curie('context_info'),
                   model_uri=CONFIDENT.AcademicEventSeries_context_info, domain=AcademicEventSeries, range=Optional[Union[dict, "Context"]])

slots.AcademicEventSeries_gnd_id = Slot(uri=IAO['0000235'], name="AcademicEventSeries_gnd_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEventSeries_gnd_id, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.AcademicEventSeries_wikicfp_id = Slot(uri=IAO['0000235'], name="AcademicEventSeries_wikicfp_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEventSeries_wikicfp_id, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "WikiCfpId"], List[Union[dict, "WikiCfpId"]]]])

slots.AcademicEventSeries_wikidata_id = Slot(uri=IAO['0000235'], name="AcademicEventSeries_wikidata_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEventSeries_wikidata_id, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]])

slots.AcademicEventSeries_dpbl_id = Slot(uri=IAO['0000235'], name="AcademicEventSeries_dpbl_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEventSeries_dpbl_id, domain=AcademicEventSeries, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.AcademicEvent_id = Slot(uri=CONFIDENT.id, name="AcademicEvent_id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.AcademicEvent_id, domain=AcademicEvent, range=Union[str, AcademicEventId])

slots.AcademicEvent_process_name = Slot(uri=IAO['0000235'], name="AcademicEvent_process_name", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEvent_process_name, domain=AcademicEvent, range=Union[dict, "ProcessName"])

slots.AcademicEvent_landing_page = Slot(uri=CONFIDENT.landing_page, name="AcademicEvent_landing_page", curie=CONFIDENT.curie('landing_page'),
                   model_uri=CONFIDENT.AcademicEvent_landing_page, domain=AcademicEvent, range=Optional[Union[str, URI]])

slots.AcademicEvent_doi = Slot(uri=IAO['0000235'], name="AcademicEvent_doi", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEvent_doi, domain=AcademicEvent, range=Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]])

slots.AcademicEvent_type = Slot(uri=RDF.type, name="AcademicEvent_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.AcademicEvent_type, domain=AcademicEvent, range=Optional[Union[str, "EventType"]])

slots.AcademicEvent_organizers = Slot(uri=CONFIDENT.organizers, name="AcademicEvent_organizers", curie=CONFIDENT.curie('organizers'),
                   model_uri=CONFIDENT.AcademicEvent_organizers, domain=AcademicEvent, range=Optional[Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]]])

slots.AcademicEvent_academic_fields = Slot(uri=AEON['0000040'], name="AcademicEvent_academic_fields", curie=AEON.curie('0000040'),
                   model_uri=CONFIDENT.AcademicEvent_academic_fields, domain=AcademicEvent, range=Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]])

slots.AcademicEvent_website = Slot(uri=CONFIDENT.website, name="AcademicEvent_website", curie=CONFIDENT.curie('website'),
                   model_uri=CONFIDENT.AcademicEvent_website, domain=AcademicEvent, range=Optional[Union[str, URI]])

slots.AcademicEvent_sponsors = Slot(uri=CONFIDENT.sponsors, name="AcademicEvent_sponsors", curie=CONFIDENT.curie('sponsors'),
                   model_uri=CONFIDENT.AcademicEvent_sponsors, domain=AcademicEvent, range=Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]])

slots.AcademicEvent_publications = Slot(uri=CONFIDENT.publications, name="AcademicEvent_publications", curie=CONFIDENT.curie('publications'),
                   model_uri=CONFIDENT.AcademicEvent_publications, domain=AcademicEvent, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.AcademicEvent_topics = Slot(uri=CONFIDENT.topics, name="AcademicEvent_topics", curie=CONFIDENT.curie('topics'),
                   model_uri=CONFIDENT.AcademicEvent_topics, domain=AcademicEvent, range=Optional[Union[str, List[str]]])

slots.AcademicEvent_metrics = Slot(uri=CONFIDENT.metrics, name="AcademicEvent_metrics", curie=CONFIDENT.curie('metrics'),
                   model_uri=CONFIDENT.AcademicEvent_metrics, domain=AcademicEvent, range=Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]])

slots.AcademicEvent_context_info = Slot(uri=CONFIDENT.context_info, name="AcademicEvent_context_info", curie=CONFIDENT.curie('context_info'),
                   model_uri=CONFIDENT.AcademicEvent_context_info, domain=AcademicEvent, range=Optional[Union[dict, "Context"]])

slots.AcademicEvent_gnd_id = Slot(uri=IAO['0000235'], name="AcademicEvent_gnd_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEvent_gnd_id, domain=AcademicEvent, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.AcademicEvent_wikicfp_id = Slot(uri=IAO['0000235'], name="AcademicEvent_wikicfp_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEvent_wikicfp_id, domain=AcademicEvent, range=Optional[Union[Union[dict, "WikiCfpId"], List[Union[dict, "WikiCfpId"]]]])

slots.AcademicEvent_wikidata_id = Slot(uri=IAO['0000235'], name="AcademicEvent_wikidata_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEvent_wikidata_id, domain=AcademicEvent, range=Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]])

slots.AcademicEvent_dpbl_id = Slot(uri=IAO['0000235'], name="AcademicEvent_dpbl_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.AcademicEvent_dpbl_id, domain=AcademicEvent, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.ExternalIdentifier_value = Slot(uri=OBI['0002815'], name="ExternalIdentifier_value", curie=OBI.curie('0002815'),
                   model_uri=CONFIDENT.ExternalIdentifier_value, domain=ExternalIdentifier, range=Optional[str])

slots.DigitalObjectId_schema_name = Slot(uri=CONFIDENT.schema_name, name="DigitalObjectId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.DigitalObjectId_schema_name, domain=DigitalObjectId, range=Optional[str])

slots.DigitalObjectId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="DigitalObjectId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.DigitalObjectId_schema_base_uri, domain=DigitalObjectId, range=Optional[Union[str, URIorCURIE]])

slots.WikidataId_schema_name = Slot(uri=CONFIDENT.schema_name, name="WikidataId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.WikidataId_schema_name, domain=WikidataId, range=Optional[str])

slots.WikidataId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="WikidataId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.WikidataId_schema_base_uri, domain=WikidataId, range=Optional[Union[str, URIorCURIE]])

slots.GndId_schema_name = Slot(uri=CONFIDENT.schema_name, name="GndId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.GndId_schema_name, domain=GndId, range=Optional[str])

slots.GndId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="GndId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.GndId_schema_base_uri, domain=GndId, range=Optional[Union[str, URIorCURIE]])

slots.TibkatId_schema_name = Slot(uri=CONFIDENT.schema_name, name="TibkatId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.TibkatId_schema_name, domain=TibkatId, range=Optional[str])

slots.TibkatId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="TibkatId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.TibkatId_schema_base_uri, domain=TibkatId, range=Optional[Union[str, URIorCURIE]])

slots.DblpId_schema_name = Slot(uri=CONFIDENT.schema_name, name="DblpId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.DblpId_schema_name, domain=DblpId, range=Optional[str])

slots.DblpId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="DblpId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.DblpId_schema_base_uri, domain=DblpId, range=Optional[Union[str, URIorCURIE]])

slots.WikiCfpId_schema_name = Slot(uri=CONFIDENT.schema_name, name="WikiCfpId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.WikiCfpId_schema_name, domain=WikiCfpId, range=Optional[str])

slots.WikiCfpId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="WikiCfpId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.WikiCfpId_schema_base_uri, domain=WikiCfpId, range=Optional[Union[str, URIorCURIE]])

slots.Deadline_type = Slot(uri=CONFIDENT.type, name="Deadline_type", curie=CONFIDENT.curie('type'),
                   model_uri=CONFIDENT.Deadline_type, domain=Deadline, range=Union[str, "DeadlineType"])

slots.Metric_type = Slot(uri=CONFIDENT.type, name="Metric_type", curie=CONFIDENT.curie('type'),
                   model_uri=CONFIDENT.Metric_type, domain=Metric, range=Optional[Union[str, "MetricType"]])

slots.ProcessRelation_type = Slot(uri=CONFIDENT.type, name="ProcessRelation_type", curie=CONFIDENT.curie('type'),
                   model_uri=CONFIDENT.ProcessRelation_type, domain=ProcessRelation, range=Optional[Union[str, "RelationType"]])

slots.AcademicField_value = Slot(uri=CONFIDENT.value, name="AcademicField_value", curie=CONFIDENT.curie('value'),
                   model_uri=CONFIDENT.AcademicField_value, domain=AcademicField, range=str)

slots.Contributor_type = Slot(uri=RDF.type, name="Contributor_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.Contributor_type, domain=Contributor, range=Optional[str])

slots.ContactPerson_id = Slot(uri=CONFIDENT.id, name="ContactPerson_id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.ContactPerson_id, domain=ContactPerson, range=Union[str, ContactPersonId])