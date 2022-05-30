# Auto generated from confident_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-30T09:08:19
# Schema: confident_schema
#
# id: https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/%238_naming/src/linkml/ConfIDent_schema.yaml
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
version = "0.4.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#AEON_')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CONFIDENT = CurieNamespace('confident', 'https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#')
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
class EventSeriesId(URIorCURIE):
    pass


class EventId(URIorCURIE):
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


class NamedThingId(URIorCURIE):
    pass


@dataclass
class EventSeries(YAMLRoot):
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
    class_name: ClassVar[str] = "EventSeries"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.EventSeries

    official_name: str = None
    organized_by: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    id: Union[str, EventSeriesId] = "confident:SeriesID"
    has_acronym: Optional[str] = None
    academic_field: Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]] = empty_list()
    landing_page: Optional[Union[str, URI]] = None
    has_publication: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    sponsored_by: Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]] = empty_dict()
    website: Optional[Union[str, URI]] = None
    has_doi: Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]] = empty_list()
    series_of: Optional[Union[str, EventId]] = None
    alternative_name: Optional[Union[str, List[str]]] = empty_list()
    former_name: Optional[str] = None
    translated_name: Optional[Union[str, List[str]]] = empty_list()
    context_info: Optional[Union[dict, "Context"]] = None
    has_metric: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    has_topic: Optional[Union[str, List[str]]] = empty_list()
    external_id: Optional[Union[Union[dict, "ExternalIdentifier"], List[Union[dict, "ExternalIdentifier"]]]] = empty_list()
    wikidata_id: Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]] = empty_list()
    dpbl_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()
    gnd_id: Optional[Union[Union[dict, "GndId"], List[Union[dict, "GndId"]]]] = empty_list()
    wikicfp_series_id: Optional[Union[Union[dict, "WikiCfpSeriesId"], List[Union[dict, "WikiCfpSeriesId"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventSeriesId):
            self.id = EventSeriesId(self.id)

        if self._is_empty(self.official_name):
            self.MissingRequiredField("official_name")
        if not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self._is_empty(self.organized_by):
            self.MissingRequiredField("organized_by")
        self._normalize_inlined_as_list(slot_name="organized_by", slot_type=Organizer, key_name="id", keyed=True)

        if self.has_acronym is not None and not isinstance(self.has_acronym, str):
            self.has_acronym = str(self.has_acronym)

        if not isinstance(self.academic_field, list):
            self.academic_field = [self.academic_field] if self.academic_field is not None else []
        self.academic_field = [v if isinstance(v, AcademicField) else AcademicField(**as_dict(v)) for v in self.academic_field]

        if self.landing_page is not None and not isinstance(self.landing_page, URI):
            self.landing_page = URI(self.landing_page)

        self._normalize_inlined_as_list(slot_name="has_publication", slot_type=Publication, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sponsored_by", slot_type=Sponsor, key_name="id", keyed=True)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if not isinstance(self.has_doi, list):
            self.has_doi = [self.has_doi] if self.has_doi is not None else []
        self.has_doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.has_doi]

        if self.series_of is not None and not isinstance(self.series_of, EventId):
            self.series_of = EventId(self.series_of)

        if not isinstance(self.alternative_name, list):
            self.alternative_name = [self.alternative_name] if self.alternative_name is not None else []
        self.alternative_name = [v if isinstance(v, str) else str(v) for v in self.alternative_name]

        if self.former_name is not None and not isinstance(self.former_name, str):
            self.former_name = str(self.former_name)

        if not isinstance(self.translated_name, list):
            self.translated_name = [self.translated_name] if self.translated_name is not None else []
        self.translated_name = [v if isinstance(v, str) else str(v) for v in self.translated_name]

        if self.context_info is not None and not isinstance(self.context_info, Context):
            self.context_info = Context(**as_dict(self.context_info))

        if not isinstance(self.has_metric, list):
            self.has_metric = [self.has_metric] if self.has_metric is not None else []
        self.has_metric = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.has_metric]

        if not isinstance(self.has_topic, list):
            self.has_topic = [self.has_topic] if self.has_topic is not None else []
        self.has_topic = [v if isinstance(v, str) else str(v) for v in self.has_topic]

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        if not isinstance(self.wikidata_id, list):
            self.wikidata_id = [self.wikidata_id] if self.wikidata_id is not None else []
        self.wikidata_id = [v if isinstance(v, WikidataId) else WikidataId(**as_dict(v)) for v in self.wikidata_id]

        if not isinstance(self.dpbl_id, list):
            self.dpbl_id = [self.dpbl_id] if self.dpbl_id is not None else []
        self.dpbl_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.dpbl_id]

        if not isinstance(self.gnd_id, list):
            self.gnd_id = [self.gnd_id] if self.gnd_id is not None else []
        self.gnd_id = [v if isinstance(v, GndId) else GndId(**as_dict(v)) for v in self.gnd_id]

        if not isinstance(self.wikicfp_series_id, list):
            self.wikicfp_series_id = [self.wikicfp_series_id] if self.wikicfp_series_id is not None else []
        self.wikicfp_series_id = [v if isinstance(v, WikiCfpSeriesId) else WikiCfpSeriesId(**as_dict(v)) for v in self.wikicfp_series_id]

        super().__post_init__(**kwargs)


@dataclass
class Event(YAMLRoot):
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

    class_class_uri: ClassVar[URIRef] = AEON["0000001"]
    class_class_curie: ClassVar[str] = "aeon:0000001"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Event

    official_name: str = None
    organized_by: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    start_date: Union[str, XSDDateTime] = None
    end_date: Union[str, XSDDateTime] = None
    id: Union[str, EventId] = "confident:EventID"
    event_status: Union[str, "EventStatus"] = "as scheduled"
    has_acronym: Optional[str] = None
    academic_field: Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]] = empty_list()
    landing_page: Optional[Union[str, URI]] = None
    has_publication: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    sponsored_by: Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]] = empty_dict()
    website: Optional[Union[str, URI]] = None
    has_doi: Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]] = empty_list()
    type: Optional[Union[str, "EventType"]] = None
    at_location: Optional[Union[dict, "Location"]] = None
    in_series: Optional[Union[str, EventSeriesId]] = None
    has_deadline: Optional[Union[Union[dict, "Deadline"], List[Union[dict, "Deadline"]]]] = empty_list()
    related_to: Optional[Union[Union[dict, "ProcessRelation"], List[Union[dict, "ProcessRelation"]]]] = empty_list()
    alternative_name: Optional[Union[str, List[str]]] = empty_list()
    former_name: Optional[str] = None
    translated_name: Optional[Union[str, List[str]]] = empty_list()
    context_info: Optional[Union[dict, "Context"]] = None
    has_metric: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    has_topic: Optional[Union[str, List[str]]] = empty_list()
    external_id: Optional[Union[Union[dict, "ExternalIdentifier"], List[Union[dict, "ExternalIdentifier"]]]] = empty_list()
    wikidata_id: Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]] = empty_list()
    dpbl_id: Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]] = empty_list()
    gnd_id: Optional[Union[Union[dict, "GndId"], List[Union[dict, "GndId"]]]] = empty_list()
    ordinal: Optional[int] = None
    event_mode: Optional[Union[str, "EventMode"]] = None
    tibkat_id: Optional[Union[Union[dict, "TibkatId"], List[Union[dict, "TibkatId"]]]] = empty_list()
    wikicfp_event_id: Optional[Union[Union[dict, "WikiCfpEventId"], List[Union[dict, "WikiCfpEventId"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self._is_empty(self.official_name):
            self.MissingRequiredField("official_name")
        if not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self._is_empty(self.organized_by):
            self.MissingRequiredField("organized_by")
        self._normalize_inlined_as_list(slot_name="organized_by", slot_type=Organizer, key_name="id", keyed=True)

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

        if self.has_acronym is not None and not isinstance(self.has_acronym, str):
            self.has_acronym = str(self.has_acronym)

        if not isinstance(self.academic_field, list):
            self.academic_field = [self.academic_field] if self.academic_field is not None else []
        self.academic_field = [v if isinstance(v, AcademicField) else AcademicField(**as_dict(v)) for v in self.academic_field]

        if self.landing_page is not None and not isinstance(self.landing_page, URI):
            self.landing_page = URI(self.landing_page)

        self._normalize_inlined_as_list(slot_name="has_publication", slot_type=Publication, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sponsored_by", slot_type=Sponsor, key_name="id", keyed=True)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if not isinstance(self.has_doi, list):
            self.has_doi = [self.has_doi] if self.has_doi is not None else []
        self.has_doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.has_doi]

        if self.type is not None and not isinstance(self.type, EventType):
            self.type = EventType(self.type)

        if self.at_location is not None and not isinstance(self.at_location, Location):
            self.at_location = Location(**as_dict(self.at_location))

        if self.in_series is not None and not isinstance(self.in_series, EventSeriesId):
            self.in_series = EventSeriesId(self.in_series)

        if not isinstance(self.has_deadline, list):
            self.has_deadline = [self.has_deadline] if self.has_deadline is not None else []
        self.has_deadline = [v if isinstance(v, Deadline) else Deadline(**as_dict(v)) for v in self.has_deadline]

        if not isinstance(self.related_to, list):
            self.related_to = [self.related_to] if self.related_to is not None else []
        self.related_to = [v if isinstance(v, ProcessRelation) else ProcessRelation(**as_dict(v)) for v in self.related_to]

        if not isinstance(self.alternative_name, list):
            self.alternative_name = [self.alternative_name] if self.alternative_name is not None else []
        self.alternative_name = [v if isinstance(v, str) else str(v) for v in self.alternative_name]

        if self.former_name is not None and not isinstance(self.former_name, str):
            self.former_name = str(self.former_name)

        if not isinstance(self.translated_name, list):
            self.translated_name = [self.translated_name] if self.translated_name is not None else []
        self.translated_name = [v if isinstance(v, str) else str(v) for v in self.translated_name]

        if self.context_info is not None and not isinstance(self.context_info, Context):
            self.context_info = Context(**as_dict(self.context_info))

        if not isinstance(self.has_metric, list):
            self.has_metric = [self.has_metric] if self.has_metric is not None else []
        self.has_metric = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.has_metric]

        if not isinstance(self.has_topic, list):
            self.has_topic = [self.has_topic] if self.has_topic is not None else []
        self.has_topic = [v if isinstance(v, str) else str(v) for v in self.has_topic]

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(**as_dict(v)) for v in self.external_id]

        if not isinstance(self.wikidata_id, list):
            self.wikidata_id = [self.wikidata_id] if self.wikidata_id is not None else []
        self.wikidata_id = [v if isinstance(v, WikidataId) else WikidataId(**as_dict(v)) for v in self.wikidata_id]

        if not isinstance(self.dpbl_id, list):
            self.dpbl_id = [self.dpbl_id] if self.dpbl_id is not None else []
        self.dpbl_id = [v if isinstance(v, DblpId) else DblpId(**as_dict(v)) for v in self.dpbl_id]

        if not isinstance(self.gnd_id, list):
            self.gnd_id = [self.gnd_id] if self.gnd_id is not None else []
        self.gnd_id = [v if isinstance(v, GndId) else GndId(**as_dict(v)) for v in self.gnd_id]

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if self.event_mode is not None and not isinstance(self.event_mode, EventMode):
            self.event_mode = EventMode(self.event_mode)

        if not isinstance(self.tibkat_id, list):
            self.tibkat_id = [self.tibkat_id] if self.tibkat_id is not None else []
        self.tibkat_id = [v if isinstance(v, TibkatId) else TibkatId(**as_dict(v)) for v in self.tibkat_id]

        if not isinstance(self.wikicfp_event_id, list):
            self.wikicfp_event_id = [self.wikicfp_event_id] if self.wikicfp_event_id is not None else []
        self.wikicfp_event_id = [v if isinstance(v, WikiCfpEventId) else WikiCfpEventId(**as_dict(v)) for v in self.wikicfp_event_id]

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

    schema_value: Optional[str] = None
    schema_name: Optional[str] = None
    schema_base_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_value is not None and not isinstance(self.schema_value, str):
            self.schema_value = str(self.schema_value)

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
    schema_base_uri: Optional[Union[str, URIorCURIE]] = URIRef(str(DOI))

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
    The identifier of a publication in the TIB catalog that references an event or event series.
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
class WikiCfpEventId(ExternalIdentifier):
    """
    The identifier of an academic event or series in WikiCFP.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.WikiCfpEventId
    class_class_curie: ClassVar[str] = "confident:WikiCfpEventId"
    class_name: ClassVar[str] = "WikiCfpEventId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.WikiCfpEventId

    schema_name: Optional[str] = "WikiCFP"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid="

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class WikiCfpSeriesId(ExternalIdentifier):
    """
    The identifier of an academic event or series in WikiCFP.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.WikiCfpSeriesId
    class_class_curie: ClassVar[str] = "confident:WikiCfpSeriesId"
    class_name: ClassVar[str] = "WikiCfpSeriesId"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.WikiCfpSeriesId

    schema_name: Optional[str] = "WikiCFP"
    schema_base_uri: Optional[Union[str, URIorCURIE]] = "http://www.wikicfp.com/cfp/program?id=$1"

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
    gathering is to be carried out by its participants in terms of achieving certain objectives, fulfilling certain
    conditions and performing certain actions. It thus concretizes the expectations of the contributors of an academic
    event. While the explicit details are often provided as concrete parts (e.g. deadline or attendance fee
    specifications), the implicit details depend on the semantics encoded in the words used for the classification of
    academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications
    can overlap or vary to a certain degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000004"]
    class_class_curie: ClassVar[str] = "aeon:0000004"
    class_name: ClassVar[str] = "EventFormatSpecification"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.EventFormatSpecification

    other_format: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.other_format):
            self.MissingRequiredField("other_format")
        if not isinstance(self.other_format, str):
            self.other_format = str(self.other_format)

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
    A container for statistical information about an event or event series.
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
    metric_year: Optional[str] = None
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

        if self.metric_year is not None and not isinstance(self.metric_year, str):
            self.metric_year = str(self.metric_year)

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

    has_city: Optional[Union[str, CityId]] = None
    has_country: Optional[Union[str, CountryId]] = None
    has_region: Optional[Union[str, RegionId]] = None
    has_venue: Optional[Union[str, VenueId]] = None
    lattitude: Optional[float] = None
    longitude: Optional[float] = None
    meeting_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_city is not None and not isinstance(self.has_city, CityId):
            self.has_city = CityId(self.has_city)

        if self.has_country is not None and not isinstance(self.has_country, CountryId):
            self.has_country = CountryId(self.has_country)

        if self.has_region is not None and not isinstance(self.has_region, RegionId):
            self.has_region = RegionId(self.has_region)

        if self.has_venue is not None and not isinstance(self.has_venue, VenueId):
            self.has_venue = VenueId(self.has_venue)

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
    An academic field is the scientific subject of an event or event series according to some controlled vocabulary or
    thesaurus and as such requires the scheme URI.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.AcademicField
    class_class_curie: ClassVar[str] = "confident:AcademicField"
    class_name: ClassVar[str] = "AcademicField"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.AcademicField

    schema_value: str = None
    schema_name: Optional[str] = None
    schema_base_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.schema_value):
            self.MissingRequiredField("schema_value")
        if not isinstance(self.schema_value, str):
            self.schema_value = str(self.schema_value)

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
    A contributor is a person or organization that holds a contributor role which is being realized in an event or
    event series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.Contributor
    class_class_curie: ClassVar[str] = "confident:Contributor"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.Contributor

    id: Union[str, ContributorId] = None
    type: Optional[Union[str, "ContributorType"]] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorId):
            self.id = ContributorId(self.id)

        if self.type is not None and not isinstance(self.type, ContributorType):
            self.type = ContributorType(self.type)

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

    id: Union[str, ContactPersonId] = None
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
    has_doi: Optional[Union[Union[dict, DigitalObjectId], List[Union[dict, DigitalObjectId]]]] = empty_list()
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if not isinstance(self.has_doi, list):
            self.has_doi = [self.has_doi] if self.has_doi is not None else []
        self.has_doi = [v if isinstance(v, DigitalObjectId) else DigitalObjectId(**as_dict(v)) for v in self.has_doi]

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

    events: Optional[Union[Dict[Union[str, EventId], Union[dict, Event]], List[Union[dict, Event]]]] = empty_dict()
    series: Optional[Union[Dict[Union[str, EventSeriesId], Union[dict, EventSeries]], List[Union[dict, EventSeries]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="series", slot_type=EventSeries, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


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

    schema_value: Optional[str] = None
    schema_name: Optional[str] = None
    schema_base_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_value is not None and not isinstance(self.schema_value, str):
            self.schema_value = str(self.schema_value)

        if self.schema_name is not None and not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if self.schema_base_uri is not None and not isinstance(self.schema_base_uri, URIorCURIE):
            self.schema_base_uri = URIorCURIE(self.schema_base_uri)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A mixin used to provide the attributes needed for the identification of a thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIDENT.NamedThing
    class_class_curie: ClassVar[str] = "confident:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CONFIDENT.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    external_id: Optional[Union[Union[dict, ExternalIdentifier], List[Union[dict, ExternalIdentifier]]]] = empty_list()

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


# Enumerations
class EventType(EnumDefinitionImpl):
    """
    The most common minimal event types. For event types that are not in this list, you can use "other" and provide
    the label of this other event format using the [Event Format](event_format.md) property.
    """
    Colloquium = PermissibleValue(text="Colloquium",
                                           description="A colloquium is an academic meeting that usually lasts only a few hours and serves to discuss a specific topic. Colloquia are usually part of the academic exchange in everyday university life with only one speaker, but can also take place on special occasions (anniversaries, start or end of the lecture phase, etc.) and can have more than one speaker.",
                                           meaning=AEON["0000101"])
    Conference = PermissibleValue(text="Conference",
                                           description="A conference is an academic event that lasts up to several days and serves as a forum for presentations on a specific topic or subject area. In addition to subject-specific conferences, there are also interdisciplinary conferences which allow both a broader focus and more specific questions on a particular (academic) problem. Conferences often have a highly formalized structure of parallel, clearly defined sessions with several short presentations and plenary sessions with invited (keynote) speakers who are considered multipliers in their (research) field. Ideally, the selection of the speakers and their contributions is subject to a review process.",
                                           meaning=AEON["0000103"])
    Congress = PermissibleValue(text="Congress",
                                       description="A congress is a certain type of conference which is characterised by a larger number of participants (often several hundred) and is oftentimes organised jointly by large, established (e.g. specialised societies) and/or several institutions. Congresses have a broader thematic focus than simple conferences, take place in certain cycles, but can still target an exclusive group of participants (e.g. representatives of a single discipline).",
                                       meaning=AEON["0000123"])
    Session = PermissibleValue(text="Session",
                                     description="A session is a clearly defined part of a academic event in which a small number of speakers (usually 2-5) focus on a specific topic. A session is usually formally accompanied by a session chair, who assumes the function of a moderator.",
                                     meaning=AEON["0000111"])
    Talk = PermissibleValue(text="Talk",
                               description="A talk is a central part of a larger academic event, at which a specific topic is being presented in a rather short way.",
                               meaning=AEON["0000125"])
    Forum = PermissibleValue(text="Forum",
                                 description="An academic event whose sociocultural format is determined in an academic event type specification that classifies the academic event as a forum.",
                                 meaning=AEON["0000105"])
    Hackathon = PermissibleValue(text="Hackathon",
                                         description="A hackathon is a gathering of software developers with the goal to develop software collaboratively in a short timeframe.",
                                         meaning=AEON["0000107"])
    Seminar = PermissibleValue(text="Seminar",
                                     description="A seminar can serve as a term for older conference series, but in current usage the term mainly describes a specific teaching format that serves to develop content and provides space for discussion. Participation from the audience is usually encouraged.",
                                     meaning=AEON["0000109"])
    Symposium = PermissibleValue(text="Symposium",
                                         description="A symposium is a specific type of conference with a narrower thematic focus, with fewer participants and of shorter duration. The degree of structuring lies between a classic conference and a workshop, allows more discussion than the larger conference, but is usually more formalized than the workshop.",
                                         meaning=AEON["0000113"])
    Tutorial = PermissibleValue(text="Tutorial",
                                       description="An academic event that has the function to educate the audience on a certain topic. A tutorial is often realized as an academic event talk or academic event session.",
                                       meaning=AEON["0000119"])
    Workshop = PermissibleValue(text="Workshop",
                                       description="Workshops are smaller academic events that serve to exchange information on a specific topic or problem. They usually last one or two days and offer space for discussion and the development of content and solutions. Group work is often part of the event concept.",
                                       meaning=AEON["0000121"])
    other = PermissibleValue(text="other",
                                 description="This value is to be used if the event format cannot be represented using one of the other permissible values defined in the [Event Type](EventType.md) enum. If this value is chosen the use of [Other Event Format](other_format.md) is mandatory.",
                                 meaning=AEON["0000001"])

    _defn = EnumDefinition(
        name="EventType",
        description="The most common minimal event types. For event types that are not in this list, you can use \"other\" and provide the label of this other event format using the [Event Format](event_format.md) property.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Poster Session",
                PermissibleValue(text="Poster Session",
                                 description="A poster session is a session at which poster papers are presented.",
                                 meaning=AEON["0000127"]) )
        setattr(cls, "Keynote Speech",
                PermissibleValue(text="Keynote Speech",
                                 description="A keynote speech is a special talk that has the function to set the underlying tone and summarize the core message or most important revelation of the academic event at which it is given.",
                                 meaning=AEON["00001115"]) )
        setattr(cls, "Event Track",
                PermissibleValue(text="Event Track",
                                 description="An academic event that, as a part of a larger academic event, has the function to group even smaller parts of the academic event, like sessions and talks, according to a shared theme or topic. It usually has dedicated chairs and program committees.",
                                 meaning=AEON["00001117"]) )

class EventStatus(EnumDefinitionImpl):
    """
    The status of the academic event which indicates if it takes place as planned.
    """
    postponed = PermissibleValue(text="postponed",
                                         description="Used to indicate that the event has been postponed to a later date.")
    canceled = PermissibleValue(text="canceled",
                                       description="Used to indicate that the event has been canceled.")

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
                                         description="This rate metric states the time frame in which the events of a series reoccur.")

    _defn = EnumDefinition(
        name="MetricType",
        description="The possible metric of an academic event.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "submitted papers",
                PermissibleValue(text="submitted papers",
                                 description="This metric provides the number of papers that have been submitted to the organizers of an academic event.") )
        setattr(cls, "accepted papers",
                PermissibleValue(text="accepted papers",
                                 description="This metric provides the number of papers that have been accepted by the organizers of an academic event and from which an acceptance rate can be calculated.") )
        setattr(cls, "submitted short papers",
                PermissibleValue(text="submitted short papers",
                                 description="This metric provides the number of short papers that have been submitted to the organizers of an academic event.") )
        setattr(cls, "accepted short papers",
                PermissibleValue(text="accepted short papers",
                                 description="This metric provides the number of short papers that have been accepted by the organizers of an academic event and from which an acceptance rate can be calculated.") )
        setattr(cls, "submitted abstracts",
                PermissibleValue(text="submitted abstracts",
                                 description="This metric provides the number of abstracts that have been submitted to the organizers of an academic event.") )
        setattr(cls, "accepted abstracts",
                PermissibleValue(text="accepted abstracts",
                                 description="This metric provides the number of abstracts that have been accepted by the organizers of an academic event and from which an acceptance rate can be calculated.") )
        setattr(cls, "number of attendees",
                PermissibleValue(text="number of attendees",
                                 description="This metric provides the number of attendees of an academic event.") )
        setattr(cls, "number of tracks",
                PermissibleValue(text="number of tracks",
                                 description="This metric provides the number of tracks of an academic event.") )
        setattr(cls, "has childcare options",
                PermissibleValue(text="has childcare options",
                                 description="This boolean metric states whether the academic event has a childcare option for its attendees.") )
        setattr(cls, "is accessible",
                PermissibleValue(text="is accessible",
                                 description="This boolean metric states whether the event is accessible for people with impairments.") )
        setattr(cls, "CORE rank",
                PermissibleValue(text="CORE rank",
                                 description="This score metric grades academic events according to the ranking of [CORE Inc.](https://www.core.edu.au/).") )

class ContributorType(EnumDefinitionImpl):
    """
    An enumaration used to distinguish the contributors of an event or event series with regard to them being either
    an organization or a person.
    """
    organization = PermissibleValue(text="organization",
                                               description="An institution, or an association that has one or more people as members and which actsas some kind of participant in an event or event series.",
                                               meaning=OBI["0000245"])
    person = PermissibleValue(text="person",
                                   description="A human being that acts as some kind of participant in an event or event series.",
                                   meaning=NCBITAXON["9606"])

    _defn = EnumDefinition(
        name="ContributorType",
        description="An enumaration used to distinguish the contributors of an event or event series with regard to them being either an organization or a person.",
    )

# Slots
class slots:
    pass

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.type, domain=None, range=Optional[str])

slots.has_doi = Slot(uri=IAO['0000235'], name="has_doi", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.has_doi, domain=None, range=Optional[Union[Union[dict, DigitalObjectId], List[Union[dict, DigitalObjectId]]]])

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

slots.schema_value = Slot(uri=CONFIDENT.schema_value, name="schema_value", curie=CONFIDENT.curie('schema_value'),
                   model_uri=CONFIDENT.schema_value, domain=None, range=Optional[str])

slots.schema_name = Slot(uri=CONFIDENT.schema_name, name="schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.schema_name, domain=None, range=Optional[str])

slots.schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.schema_base_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.official_name = Slot(uri=SKOS.perfLabel, name="official_name", curie=SKOS.curie('perfLabel'),
                   model_uri=CONFIDENT.official_name, domain=None, range=str)

slots.organized_by = Slot(uri=CONFIDENT.organized_by, name="organized_by", curie=CONFIDENT.curie('organized_by'),
                   model_uri=CONFIDENT.organized_by, domain=None, range=Union[Dict[Union[str, OrganizerId], Union[dict, Organizer]], List[Union[dict, Organizer]]])

slots.has_acronym = Slot(uri=CONFIDENT.has_acronym, name="has_acronym", curie=CONFIDENT.curie('has_acronym'),
                   model_uri=CONFIDENT.has_acronym, domain=None, range=Optional[str])

slots.academic_field = Slot(uri=AEON['0000040'], name="academic_field", curie=AEON.curie('0000040'),
                   model_uri=CONFIDENT.academic_field, domain=None, range=Optional[Union[Union[dict, AcademicField], List[Union[dict, AcademicField]]]])

slots.landing_page = Slot(uri=CONFIDENT.landing_page, name="landing_page", curie=CONFIDENT.curie('landing_page'),
                   model_uri=CONFIDENT.landing_page, domain=None, range=Optional[Union[str, URI]])

slots.has_publication = Slot(uri=CONFIDENT.has_publication, name="has_publication", curie=CONFIDENT.curie('has_publication'),
                   model_uri=CONFIDENT.has_publication, domain=None, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, Publication]], List[Union[dict, Publication]]]])

slots.sponsored_by = Slot(uri=CONFIDENT.sponsored_by, name="sponsored_by", curie=CONFIDENT.curie('sponsored_by'),
                   model_uri=CONFIDENT.sponsored_by, domain=None, range=Optional[Union[Dict[Union[str, SponsorId], Union[dict, Sponsor]], List[Union[dict, Sponsor]]]])

slots.website = Slot(uri=CONFIDENT.website, name="website", curie=CONFIDENT.curie('website'),
                   model_uri=CONFIDENT.website, domain=None, range=Optional[Union[str, URI]])

slots.alternative_name = Slot(uri=SKOS.altLabel, name="alternative_name", curie=SKOS.curie('altLabel'),
                   model_uri=CONFIDENT.alternative_name, domain=None, range=Optional[Union[str, List[str]]])

slots.former_name = Slot(uri=CONFIDENT.former_name, name="former_name", curie=CONFIDENT.curie('former_name'),
                   model_uri=CONFIDENT.former_name, domain=None, range=Optional[str])

slots.translated_name = Slot(uri=CONFIDENT.translated_name, name="translated_name", curie=CONFIDENT.curie('translated_name'),
                   model_uri=CONFIDENT.translated_name, domain=None, range=Optional[Union[str, List[str]]])

slots.context_info = Slot(uri=CONFIDENT.context_info, name="context_info", curie=CONFIDENT.curie('context_info'),
                   model_uri=CONFIDENT.context_info, domain=None, range=Optional[Union[dict, Context]])

slots.has_metric = Slot(uri=CONFIDENT.has_metric, name="has_metric", curie=CONFIDENT.curie('has_metric'),
                   model_uri=CONFIDENT.has_metric, domain=None, range=Optional[Union[Union[dict, Metric], List[Union[dict, Metric]]]])

slots.has_topic = Slot(uri=CONFIDENT.has_topic, name="has_topic", curie=CONFIDENT.curie('has_topic'),
                   model_uri=CONFIDENT.has_topic, domain=None, range=Optional[Union[str, List[str]]])

slots.dpbl_id = Slot(uri=IAO['0000235'], name="dpbl_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.dpbl_id, domain=None, range=Optional[Union[Union[dict, DblpId], List[Union[dict, DblpId]]]])

slots.start_date = Slot(uri=AEON.start_date, name="start_date", curie=AEON.curie('start_date'),
                   model_uri=CONFIDENT.start_date, domain=None, range=Union[str, XSDDateTime])

slots.end_date = Slot(uri=AEON.end_date, name="end_date", curie=AEON.curie('end_date'),
                   model_uri=CONFIDENT.end_date, domain=None, range=Union[str, XSDDateTime])

slots.event_status = Slot(uri=AEON.event_status, name="event_status", curie=AEON.curie('event_status'),
                   model_uri=CONFIDENT.event_status, domain=None, range=Union[str, "EventStatus"])

slots.in_series = Slot(uri=CONFIDENT.in_series, name="in_series", curie=CONFIDENT.curie('in_series'),
                   model_uri=CONFIDENT.in_series, domain=None, range=Optional[Union[str, EventSeriesId]])

slots.event_format = Slot(uri=AEON['0000032'], name="event_format", curie=AEON.curie('0000032'),
                   model_uri=CONFIDENT.event_format, domain=None, range=Optional[Union[dict, EventFormatSpecification]])

slots.at_location = Slot(uri=CONFIDENT.at_location, name="at_location", curie=CONFIDENT.curie('at_location'),
                   model_uri=CONFIDENT.at_location, domain=None, range=Optional[Union[dict, Location]])

slots.has_deadline = Slot(uri=CONFIDENT.has_deadline, name="has_deadline", curie=CONFIDENT.curie('has_deadline'),
                   model_uri=CONFIDENT.has_deadline, domain=None, range=Optional[Union[Union[dict, Deadline], List[Union[dict, Deadline]]]])

slots.related_to = Slot(uri=CONFIDENT.related_to, name="related_to", curie=CONFIDENT.curie('related_to'),
                   model_uri=CONFIDENT.related_to, domain=None, range=Optional[Union[Union[dict, ProcessRelation], List[Union[dict, ProcessRelation]]]])

slots.ordinal = Slot(uri=AEON.event_number, name="ordinal", curie=AEON.curie('event_number'),
                   model_uri=CONFIDENT.ordinal, domain=None, range=Optional[int])

slots.event_mode = Slot(uri=CONFIDENT.event_mode, name="event_mode", curie=CONFIDENT.curie('event_mode'),
                   model_uri=CONFIDENT.event_mode, domain=None, range=Optional[Union[str, "EventMode"]])

slots.tibkat_id = Slot(uri=IAO['0000235'], name="tibkat_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.tibkat_id, domain=None, range=Optional[Union[Union[dict, TibkatId], List[Union[dict, TibkatId]]]])

slots.wikicfp_event_id = Slot(uri=IAO['0000235'], name="wikicfp_event_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.wikicfp_event_id, domain=None, range=Optional[Union[Union[dict, WikiCfpEventId], List[Union[dict, WikiCfpEventId]]]])

slots.series_of = Slot(uri=CONFIDENT.series_of, name="series_of", curie=CONFIDENT.curie('series_of'),
                   model_uri=CONFIDENT.series_of, domain=None, range=Optional[Union[str, EventId]])

slots.wikicfp_series_id = Slot(uri=IAO['0000235'], name="wikicfp_series_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.wikicfp_series_id, domain=None, range=Optional[Union[Union[dict, WikiCfpSeriesId], List[Union[dict, WikiCfpSeriesId]]]])

slots.eventFormatSpecification__other_format = Slot(uri=OBI['0002815'], name="eventFormatSpecification__other_format", curie=OBI.curie('0002815'),
                   model_uri=CONFIDENT.eventFormatSpecification__other_format, domain=None, range=str)

slots.deadline__deadline_date = Slot(uri=CONFIDENT.deadline_date, name="deadline__deadline_date", curie=CONFIDENT.curie('deadline_date'),
                   model_uri=CONFIDENT.deadline__deadline_date, domain=None, range=Union[str, XSDDateTime])

slots.deadline__deadline_other = Slot(uri=CONFIDENT.deadline_other, name="deadline__deadline_other", curie=CONFIDENT.curie('deadline_other'),
                   model_uri=CONFIDENT.deadline__deadline_other, domain=None, range=Optional[str])

slots.metric__int_value = Slot(uri=CONFIDENT.int_value, name="metric__int_value", curie=CONFIDENT.curie('int_value'),
                   model_uri=CONFIDENT.metric__int_value, domain=None, range=Optional[int])

slots.metric__str_value = Slot(uri=CONFIDENT.str_value, name="metric__str_value", curie=CONFIDENT.curie('str_value'),
                   model_uri=CONFIDENT.metric__str_value, domain=None, range=Optional[str])

slots.metric__rate_value = Slot(uri=CONFIDENT.rate_value, name="metric__rate_value", curie=CONFIDENT.curie('rate_value'),
                   model_uri=CONFIDENT.metric__rate_value, domain=None, range=Optional[float])

slots.metric__truth_value = Slot(uri=CONFIDENT.truth_value, name="metric__truth_value", curie=CONFIDENT.curie('truth_value'),
                   model_uri=CONFIDENT.metric__truth_value, domain=None, range=Optional[Union[bool, Bool]])

slots.metric__metric_year = Slot(uri=CONFIDENT.metric_year, name="metric__metric_year", curie=CONFIDENT.curie('metric_year'),
                   model_uri=CONFIDENT.metric__metric_year, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{4}$'))

slots.metric__description = Slot(uri=CONFIDENT.description, name="metric__description", curie=CONFIDENT.curie('description'),
                   model_uri=CONFIDENT.metric__description, domain=None, range=Optional[str])

slots.location__has_city = Slot(uri=CONFIDENT.has_city, name="location__has_city", curie=CONFIDENT.curie('has_city'),
                   model_uri=CONFIDENT.location__has_city, domain=None, range=Optional[Union[str, CityId]])

slots.location__has_country = Slot(uri=CONFIDENT.has_country, name="location__has_country", curie=CONFIDENT.curie('has_country'),
                   model_uri=CONFIDENT.location__has_country, domain=None, range=Optional[Union[str, CountryId]])

slots.location__has_region = Slot(uri=CONFIDENT.has_region, name="location__has_region", curie=CONFIDENT.curie('has_region'),
                   model_uri=CONFIDENT.location__has_region, domain=None, range=Optional[Union[str, RegionId]])

slots.location__has_venue = Slot(uri=CONFIDENT.has_venue, name="location__has_venue", curie=CONFIDENT.curie('has_venue'),
                   model_uri=CONFIDENT.location__has_venue, domain=None, range=Optional[Union[str, VenueId]])

slots.location__lattitude = Slot(uri=CONFIDENT.lattitude, name="location__lattitude", curie=CONFIDENT.curie('lattitude'),
                   model_uri=CONFIDENT.location__lattitude, domain=None, range=Optional[float])

slots.location__longitude = Slot(uri=CONFIDENT.longitude, name="location__longitude", curie=CONFIDENT.curie('longitude'),
                   model_uri=CONFIDENT.location__longitude, domain=None, range=Optional[float])

slots.location__meeting_url = Slot(uri=CONFIDENT.meeting_url, name="location__meeting_url", curie=CONFIDENT.curie('meeting_url'),
                   model_uri=CONFIDENT.location__meeting_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.venue__street = Slot(uri=CONFIDENT.street, name="venue__street", curie=CONFIDENT.curie('street'),
                   model_uri=CONFIDENT.venue__street, domain=None, range=Optional[str])

slots.venue__zip_code = Slot(uri=CONFIDENT.zip_code, name="venue__zip_code", curie=CONFIDENT.curie('zip_code'),
                   model_uri=CONFIDENT.venue__zip_code, domain=None, range=Optional[str])

slots.context__text = Slot(uri=CONFIDENT.text, name="context__text", curie=CONFIDENT.curie('text'),
                   model_uri=CONFIDENT.context__text, domain=None, range=Optional[str])

slots.context__license_str = Slot(uri=CONFIDENT.license_str, name="context__license_str", curie=CONFIDENT.curie('license_str'),
                   model_uri=CONFIDENT.context__license_str, domain=None, range=Optional[str])

slots.context__license_url = Slot(uri=CONFIDENT.license_url, name="context__license_url", curie=CONFIDENT.curie('license_url'),
                   model_uri=CONFIDENT.context__license_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.organizer__contact = Slot(uri=CONFIDENT.contact, name="organizer__contact", curie=CONFIDENT.curie('contact'),
                   model_uri=CONFIDENT.organizer__contact, domain=None, range=Optional[Union[dict, ContactPerson]])

slots.contactPerson__email = Slot(uri=SDO.email, name="contactPerson__email", curie=SDO.curie('email'),
                   model_uri=CONFIDENT.contactPerson__email, domain=None, range=Optional[str],
                   pattern=re.compile(r'\b[-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'))

slots.contactPerson__telephone = Slot(uri=SDO.telephone, name="contactPerson__telephone", curie=SDO.curie('telephone'),
                   model_uri=CONFIDENT.contactPerson__telephone, domain=None, range=Optional[str])

slots.confIDentRecords__events = Slot(uri=CONFIDENT.events, name="confIDentRecords__events", curie=CONFIDENT.curie('events'),
                   model_uri=CONFIDENT.confIDentRecords__events, domain=ConfIDentRecords, range=Optional[Union[Dict[Union[str, EventId], Union[dict, Event]], List[Union[dict, Event]]]])

slots.confIDentRecords__series = Slot(uri=CONFIDENT.series, name="confIDentRecords__series", curie=CONFIDENT.curie('series'),
                   model_uri=CONFIDENT.confIDentRecords__series, domain=ConfIDentRecords, range=Optional[Union[Dict[Union[str, EventSeriesId], Union[dict, EventSeries]], List[Union[dict, EventSeries]]]])

slots.EventSeries_id = Slot(uri=CONFIDENT.id, name="EventSeries_id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.EventSeries_id, domain=EventSeries, range=Union[str, EventSeriesId])

slots.EventSeries_official_name = Slot(uri=SKOS.perfLabel, name="EventSeries_official_name", curie=SKOS.curie('perfLabel'),
                   model_uri=CONFIDENT.EventSeries_official_name, domain=EventSeries, range=str)

slots.EventSeries_organized_by = Slot(uri=CONFIDENT.organized_by, name="EventSeries_organized_by", curie=CONFIDENT.curie('organized_by'),
                   model_uri=CONFIDENT.EventSeries_organized_by, domain=EventSeries, range=Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]])

slots.EventSeries_has_acronym = Slot(uri=CONFIDENT.has_acronym, name="EventSeries_has_acronym", curie=CONFIDENT.curie('has_acronym'),
                   model_uri=CONFIDENT.EventSeries_has_acronym, domain=EventSeries, range=Optional[str])

slots.EventSeries_landing_page = Slot(uri=CONFIDENT.landing_page, name="EventSeries_landing_page", curie=CONFIDENT.curie('landing_page'),
                   model_uri=CONFIDENT.EventSeries_landing_page, domain=EventSeries, range=Optional[Union[str, URI]])

slots.EventSeries_has_doi = Slot(uri=IAO['0000235'], name="EventSeries_has_doi", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.EventSeries_has_doi, domain=EventSeries, range=Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]])

slots.EventSeries_academic_field = Slot(uri=AEON['0000040'], name="EventSeries_academic_field", curie=AEON.curie('0000040'),
                   model_uri=CONFIDENT.EventSeries_academic_field, domain=EventSeries, range=Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]])

slots.EventSeries_website = Slot(uri=CONFIDENT.website, name="EventSeries_website", curie=CONFIDENT.curie('website'),
                   model_uri=CONFIDENT.EventSeries_website, domain=EventSeries, range=Optional[Union[str, URI]])

slots.EventSeries_sponsored_by = Slot(uri=CONFIDENT.sponsored_by, name="EventSeries_sponsored_by", curie=CONFIDENT.curie('sponsored_by'),
                   model_uri=CONFIDENT.EventSeries_sponsored_by, domain=EventSeries, range=Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]])

slots.EventSeries_has_publication = Slot(uri=CONFIDENT.has_publication, name="EventSeries_has_publication", curie=CONFIDENT.curie('has_publication'),
                   model_uri=CONFIDENT.EventSeries_has_publication, domain=EventSeries, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.EventSeries_alternative_name = Slot(uri=SKOS.altLabel, name="EventSeries_alternative_name", curie=SKOS.curie('altLabel'),
                   model_uri=CONFIDENT.EventSeries_alternative_name, domain=EventSeries, range=Optional[Union[str, List[str]]])

slots.EventSeries_former_name = Slot(uri=CONFIDENT.former_name, name="EventSeries_former_name", curie=CONFIDENT.curie('former_name'),
                   model_uri=CONFIDENT.EventSeries_former_name, domain=EventSeries, range=Optional[str])

slots.EventSeries_translated_name = Slot(uri=CONFIDENT.translated_name, name="EventSeries_translated_name", curie=CONFIDENT.curie('translated_name'),
                   model_uri=CONFIDENT.EventSeries_translated_name, domain=EventSeries, range=Optional[Union[str, List[str]]])

slots.EventSeries_has_topic = Slot(uri=CONFIDENT.has_topic, name="EventSeries_has_topic", curie=CONFIDENT.curie('has_topic'),
                   model_uri=CONFIDENT.EventSeries_has_topic, domain=EventSeries, range=Optional[Union[str, List[str]]])

slots.EventSeries_has_metric = Slot(uri=CONFIDENT.has_metric, name="EventSeries_has_metric", curie=CONFIDENT.curie('has_metric'),
                   model_uri=CONFIDENT.EventSeries_has_metric, domain=EventSeries, range=Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]])

slots.EventSeries_context_info = Slot(uri=CONFIDENT.context_info, name="EventSeries_context_info", curie=CONFIDENT.curie('context_info'),
                   model_uri=CONFIDENT.EventSeries_context_info, domain=EventSeries, range=Optional[Union[dict, "Context"]])

slots.EventSeries_external_id = Slot(uri=IAO['0000235'], name="EventSeries_external_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.EventSeries_external_id, domain=EventSeries, range=Optional[Union[Union[dict, "ExternalIdentifier"], List[Union[dict, "ExternalIdentifier"]]]])

slots.EventSeries_wikidata_id = Slot(uri=IAO['0000235'], name="EventSeries_wikidata_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.EventSeries_wikidata_id, domain=EventSeries, range=Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]])

slots.EventSeries_gnd_id = Slot(uri=IAO['0000235'], name="EventSeries_gnd_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.EventSeries_gnd_id, domain=EventSeries, range=Optional[Union[Union[dict, "GndId"], List[Union[dict, "GndId"]]]])

slots.EventSeries_dpbl_id = Slot(uri=IAO['0000235'], name="EventSeries_dpbl_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.EventSeries_dpbl_id, domain=EventSeries, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.EventSeries_wikicfp_series_id = Slot(uri=IAO['0000235'], name="EventSeries_wikicfp_series_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.EventSeries_wikicfp_series_id, domain=EventSeries, range=Optional[Union[Union[dict, "WikiCfpSeriesId"], List[Union[dict, "WikiCfpSeriesId"]]]])

slots.Event_id = Slot(uri=CONFIDENT.id, name="Event_id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.Event_id, domain=Event, range=Union[str, EventId])

slots.Event_official_name = Slot(uri=SKOS.perfLabel, name="Event_official_name", curie=SKOS.curie('perfLabel'),
                   model_uri=CONFIDENT.Event_official_name, domain=Event, range=str)

slots.Event_organized_by = Slot(uri=CONFIDENT.organized_by, name="Event_organized_by", curie=CONFIDENT.curie('organized_by'),
                   model_uri=CONFIDENT.Event_organized_by, domain=Event, range=Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]])

slots.Event_has_acronym = Slot(uri=CONFIDENT.has_acronym, name="Event_has_acronym", curie=CONFIDENT.curie('has_acronym'),
                   model_uri=CONFIDENT.Event_has_acronym, domain=Event, range=Optional[str])

slots.Event_landing_page = Slot(uri=CONFIDENT.landing_page, name="Event_landing_page", curie=CONFIDENT.curie('landing_page'),
                   model_uri=CONFIDENT.Event_landing_page, domain=Event, range=Optional[Union[str, URI]])

slots.Event_has_doi = Slot(uri=IAO['0000235'], name="Event_has_doi", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_has_doi, domain=Event, range=Optional[Union[Union[dict, "DigitalObjectId"], List[Union[dict, "DigitalObjectId"]]]])

slots.Event_academic_field = Slot(uri=AEON['0000040'], name="Event_academic_field", curie=AEON.curie('0000040'),
                   model_uri=CONFIDENT.Event_academic_field, domain=Event, range=Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]])

slots.Event_website = Slot(uri=CONFIDENT.website, name="Event_website", curie=CONFIDENT.curie('website'),
                   model_uri=CONFIDENT.Event_website, domain=Event, range=Optional[Union[str, URI]])

slots.Event_sponsored_by = Slot(uri=CONFIDENT.sponsored_by, name="Event_sponsored_by", curie=CONFIDENT.curie('sponsored_by'),
                   model_uri=CONFIDENT.Event_sponsored_by, domain=Event, range=Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]])

slots.Event_has_publication = Slot(uri=CONFIDENT.has_publication, name="Event_has_publication", curie=CONFIDENT.curie('has_publication'),
                   model_uri=CONFIDENT.Event_has_publication, domain=Event, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.Event_type = Slot(uri=RDF.type, name="Event_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.Event_type, domain=Event, range=Optional[Union[str, "EventType"]])

slots.Event_alternative_name = Slot(uri=SKOS.altLabel, name="Event_alternative_name", curie=SKOS.curie('altLabel'),
                   model_uri=CONFIDENT.Event_alternative_name, domain=Event, range=Optional[Union[str, List[str]]])

slots.Event_former_name = Slot(uri=CONFIDENT.former_name, name="Event_former_name", curie=CONFIDENT.curie('former_name'),
                   model_uri=CONFIDENT.Event_former_name, domain=Event, range=Optional[str])

slots.Event_translated_name = Slot(uri=CONFIDENT.translated_name, name="Event_translated_name", curie=CONFIDENT.curie('translated_name'),
                   model_uri=CONFIDENT.Event_translated_name, domain=Event, range=Optional[Union[str, List[str]]])

slots.Event_has_topic = Slot(uri=CONFIDENT.has_topic, name="Event_has_topic", curie=CONFIDENT.curie('has_topic'),
                   model_uri=CONFIDENT.Event_has_topic, domain=Event, range=Optional[Union[str, List[str]]])

slots.Event_has_metric = Slot(uri=CONFIDENT.has_metric, name="Event_has_metric", curie=CONFIDENT.curie('has_metric'),
                   model_uri=CONFIDENT.Event_has_metric, domain=Event, range=Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]])

slots.Event_context_info = Slot(uri=CONFIDENT.context_info, name="Event_context_info", curie=CONFIDENT.curie('context_info'),
                   model_uri=CONFIDENT.Event_context_info, domain=Event, range=Optional[Union[dict, "Context"]])

slots.Event_external_id = Slot(uri=IAO['0000235'], name="Event_external_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_external_id, domain=Event, range=Optional[Union[Union[dict, "ExternalIdentifier"], List[Union[dict, "ExternalIdentifier"]]]])

slots.Event_wikidata_id = Slot(uri=IAO['0000235'], name="Event_wikidata_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_wikidata_id, domain=Event, range=Optional[Union[Union[dict, "WikidataId"], List[Union[dict, "WikidataId"]]]])

slots.Event_gnd_id = Slot(uri=IAO['0000235'], name="Event_gnd_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_gnd_id, domain=Event, range=Optional[Union[Union[dict, "GndId"], List[Union[dict, "GndId"]]]])

slots.Event_dpbl_id = Slot(uri=IAO['0000235'], name="Event_dpbl_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_dpbl_id, domain=Event, range=Optional[Union[Union[dict, "DblpId"], List[Union[dict, "DblpId"]]]])

slots.Event_wikicfp_event_id = Slot(uri=IAO['0000235'], name="Event_wikicfp_event_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_wikicfp_event_id, domain=Event, range=Optional[Union[Union[dict, "WikiCfpEventId"], List[Union[dict, "WikiCfpEventId"]]]])

slots.Event_tibkat_id = Slot(uri=IAO['0000235'], name="Event_tibkat_id", curie=IAO.curie('0000235'),
                   model_uri=CONFIDENT.Event_tibkat_id, domain=Event, range=Optional[Union[Union[dict, "TibkatId"], List[Union[dict, "TibkatId"]]]])

slots.ExternalIdentifier_schema_value = Slot(uri=OBI['0002815'], name="ExternalIdentifier_schema_value", curie=OBI.curie('0002815'),
                   model_uri=CONFIDENT.ExternalIdentifier_schema_value, domain=ExternalIdentifier, range=Optional[str])

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

slots.WikiCfpEventId_schema_name = Slot(uri=CONFIDENT.schema_name, name="WikiCfpEventId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.WikiCfpEventId_schema_name, domain=WikiCfpEventId, range=Optional[str])

slots.WikiCfpEventId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="WikiCfpEventId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.WikiCfpEventId_schema_base_uri, domain=WikiCfpEventId, range=Optional[Union[str, URIorCURIE]])

slots.WikiCfpSeriesId_schema_name = Slot(uri=CONFIDENT.schema_name, name="WikiCfpSeriesId_schema_name", curie=CONFIDENT.curie('schema_name'),
                   model_uri=CONFIDENT.WikiCfpSeriesId_schema_name, domain=WikiCfpSeriesId, range=Optional[str])

slots.WikiCfpSeriesId_schema_base_uri = Slot(uri=CONFIDENT.schema_base_uri, name="WikiCfpSeriesId_schema_base_uri", curie=CONFIDENT.curie('schema_base_uri'),
                   model_uri=CONFIDENT.WikiCfpSeriesId_schema_base_uri, domain=WikiCfpSeriesId, range=Optional[Union[str, URIorCURIE]])

slots.Deadline_type = Slot(uri=RDF.type, name="Deadline_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.Deadline_type, domain=Deadline, range=Union[str, "DeadlineType"])

slots.Metric_type = Slot(uri=RDF.type, name="Metric_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.Metric_type, domain=Metric, range=Optional[Union[str, "MetricType"]])

slots.ProcessRelation_type = Slot(uri=RDF.type, name="ProcessRelation_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.ProcessRelation_type, domain=ProcessRelation, range=Optional[Union[str, "RelationType"]])

slots.AcademicField_schema_value = Slot(uri=CONFIDENT.schema_value, name="AcademicField_schema_value", curie=CONFIDENT.curie('schema_value'),
                   model_uri=CONFIDENT.AcademicField_schema_value, domain=AcademicField, range=str)

slots.Contributor_type = Slot(uri=RDF.type, name="Contributor_type", curie=RDF.curie('type'),
                   model_uri=CONFIDENT.Contributor_type, domain=Contributor, range=Optional[Union[str, "ContributorType"]])

slots.Contributor_id = Slot(uri=CONFIDENT.id, name="Contributor_id", curie=CONFIDENT.curie('id'),
                   model_uri=CONFIDENT.Contributor_id, domain=Contributor, range=Union[str, ContributorId])