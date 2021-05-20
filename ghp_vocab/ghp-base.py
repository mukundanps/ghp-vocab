# Auto generated from ghp-base.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-19 21:41
# Schema: ghp-vocab
#
# id: https://goodhealthpass.org/ghp-vocab
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
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


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BASE_FHIR = CurieNamespace('base-fhir', 'http://hl7.org/fhir/')
DGC = CurieNamespace('dgc', 'http://hl7.eu/fhir/ig/dgc/')
GHP = CurieNamespace('ghp', 'https://goodhealthpass.org/ghp-vocab/')
ICD_ENTITY = CurieNamespace('icd-entity', 'http://id.who.int/icd/entity/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PATHOGEN = CurieNamespace('pathogen', 'https://w3id.org/pathogen#')
SCT = CurieNamespace('sct', 'http://snomed.info/sct/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
WHO_IPS = CurieNamespace('who-ips', 'http://hl7.org/fhir/uv/ips/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GHP


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = GHP.String


# Class references
class DGCPatientId(extended_str):
    pass


@dataclass
class DGCPatient(YAMLRoot):
    """
    Minimal Person information mapped to FHIR DGC Patient
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.DGCPatient
    class_class_curie: ClassVar[str] = "pathogen:DGCPatient"
    class_name: ClassVar[str] = "DGCPatient"
    class_model_uri: ClassVar[URIRef] = GHP.DGCPatient

    id: Union[str, DGCPatientId] = None
    first_name: Union[str, List[str]] = None
    last_name: str = None
    gender: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DGCPatientId):
            self.id = DGCPatientId(self.id)

        if self._is_empty(self.first_name):
            raise ValueError("first_name must be supplied")
        if not isinstance(self.first_name, list):
            self.first_name = [self.first_name]
        self.first_name = [v if isinstance(v, str) else str(v) for v in self.first_name]

        if self._is_empty(self.last_name):
            raise ValueError("last_name must be supplied")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self._is_empty(self.gender):
            raise ValueError("gender must be supplied")
        if not isinstance(self.gender, str):
            self.gender = str(self.gender)

        super().__post_init__(**kwargs)


@dataclass
class DGCVaccine(YAMLRoot):
    """
    Minimal vaccine information mapped to FHIR DGC valuesets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.DGCVaccine
    class_class_curie: ClassVar[str] = "pathogen:DGCVaccine"
    class_name: ClassVar[str] = "DGCVaccine"
    class_model_uri: ClassVar[URIRef] = GHP.DGCVaccine

    code: str = None
    targetDisease: str = None
    marketingAuthHolder: str = None
    medicinalProductName: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.code):
            raise ValueError("code must be supplied")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self._is_empty(self.targetDisease):
            raise ValueError("targetDisease must be supplied")
        if not isinstance(self.targetDisease, str):
            self.targetDisease = str(self.targetDisease)

        if self._is_empty(self.marketingAuthHolder):
            raise ValueError("marketingAuthHolder must be supplied")
        if not isinstance(self.marketingAuthHolder, str):
            self.marketingAuthHolder = str(self.marketingAuthHolder)

        if self._is_empty(self.medicinalProductName):
            raise ValueError("medicinalProductName must be supplied")
        if not isinstance(self.medicinalProductName, str):
            self.medicinalProductName = str(self.medicinalProductName)

        super().__post_init__(**kwargs)


@dataclass
class DGCVaccinationInformation(YAMLRoot):
    """
    Minimal vaccination event information mapped to FHIR DGC profile
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.DGCVaccinationInformation
    class_class_curie: ClassVar[str] = "pathogen:DGCVaccinationInformation"
    class_name: ClassVar[str] = "DGCVaccinationInformation"
    class_model_uri: ClassVar[URIRef] = GHP.DGCVaccinationInformation

    administeringCentre: str = None
    batchNumber: str = None
    countryOfVaccination: str = None
    dateOfVaccination: str = None
    healthProfessional: str = None
    order: str = None
    vaccine: str = None
    nextVaccinationDate: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.administeringCentre):
            raise ValueError("administeringCentre must be supplied")
        if not isinstance(self.administeringCentre, str):
            self.administeringCentre = str(self.administeringCentre)

        if self._is_empty(self.batchNumber):
            raise ValueError("batchNumber must be supplied")
        if not isinstance(self.batchNumber, str):
            self.batchNumber = str(self.batchNumber)

        if self._is_empty(self.countryOfVaccination):
            raise ValueError("countryOfVaccination must be supplied")
        if not isinstance(self.countryOfVaccination, str):
            self.countryOfVaccination = str(self.countryOfVaccination)

        if self._is_empty(self.dateOfVaccination):
            raise ValueError("dateOfVaccination must be supplied")
        if not isinstance(self.dateOfVaccination, str):
            self.dateOfVaccination = str(self.dateOfVaccination)

        if self._is_empty(self.healthProfessional):
            raise ValueError("healthProfessional must be supplied")
        if not isinstance(self.healthProfessional, str):
            self.healthProfessional = str(self.healthProfessional)

        if self._is_empty(self.order):
            raise ValueError("order must be supplied")
        if not isinstance(self.order, str):
            self.order = str(self.order)

        if self._is_empty(self.vaccine):
            raise ValueError("vaccine must be supplied")
        if not isinstance(self.vaccine, str):
            self.vaccine = str(self.vaccine)

        if self.nextVaccinationDate is not None and not isinstance(self.nextVaccinationDate, str):
            self.nextVaccinationDate = str(self.nextVaccinationDate)

        super().__post_init__(**kwargs)


@dataclass
class DGCTestInformation(YAMLRoot):
    """
    Minimal Covid-19 Lab test information mapped to FHIR DGC profile
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.DGCTestInformation
    class_class_curie: ClassVar[str] = "pathogen:DGCTestInformation"
    class_name: ClassVar[str] = "DGCTestInformation"
    class_model_uri: ClassVar[URIRef] = GHP.DGCTestInformation

    testName: str = None
    testType: str = None
    sampleOriginType: str = None
    sampleCollectionDateTime: str = None
    testResult: str = None
    testCenter: str = None
    testValidatorId: str = None
    healthProfessionalAdministered: str = None
    testDetails: str = None
    countryOfTestAdminstration: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.testName):
            raise ValueError("testName must be supplied")
        if not isinstance(self.testName, str):
            self.testName = str(self.testName)

        if self._is_empty(self.testType):
            raise ValueError("testType must be supplied")
        if not isinstance(self.testType, str):
            self.testType = str(self.testType)

        if self._is_empty(self.sampleOriginType):
            raise ValueError("sampleOriginType must be supplied")
        if not isinstance(self.sampleOriginType, str):
            self.sampleOriginType = str(self.sampleOriginType)

        if self._is_empty(self.sampleCollectionDateTime):
            raise ValueError("sampleCollectionDateTime must be supplied")
        if not isinstance(self.sampleCollectionDateTime, str):
            self.sampleCollectionDateTime = str(self.sampleCollectionDateTime)

        if self._is_empty(self.testResult):
            raise ValueError("testResult must be supplied")
        if not isinstance(self.testResult, str):
            self.testResult = str(self.testResult)

        if self._is_empty(self.testCenter):
            raise ValueError("testCenter must be supplied")
        if not isinstance(self.testCenter, str):
            self.testCenter = str(self.testCenter)

        if self._is_empty(self.testValidatorId):
            raise ValueError("testValidatorId must be supplied")
        if not isinstance(self.testValidatorId, str):
            self.testValidatorId = str(self.testValidatorId)

        if self._is_empty(self.healthProfessionalAdministered):
            raise ValueError("healthProfessionalAdministered must be supplied")
        if not isinstance(self.healthProfessionalAdministered, str):
            self.healthProfessionalAdministered = str(self.healthProfessionalAdministered)

        if self._is_empty(self.testDetails):
            raise ValueError("testDetails must be supplied")
        if not isinstance(self.testDetails, str):
            self.testDetails = str(self.testDetails)

        if self._is_empty(self.countryOfTestAdminstration):
            raise ValueError("countryOfTestAdminstration must be supplied")
        if not isinstance(self.countryOfTestAdminstration, str):
            self.countryOfTestAdminstration = str(self.countryOfTestAdminstration)

        super().__post_init__(**kwargs)


@dataclass
class DGCInfectionInformation(YAMLRoot):
    """
    Minimal Covid-19 Recovery information mapped to FHIR DGC profile
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.DGCInfectionInformation
    class_class_curie: ClassVar[str] = "pathogen:DGCInfectionInformation"
    class_name: ClassVar[str] = "DGCInfectionInformation"
    class_model_uri: ClassVar[URIRef] = GHP.DGCInfectionInformation

    diseaseRecoveredFrom: str = None
    dateFirstPositive: str = None
    countryOfTest: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.diseaseRecoveredFrom):
            raise ValueError("diseaseRecoveredFrom must be supplied")
        if not isinstance(self.diseaseRecoveredFrom, str):
            self.diseaseRecoveredFrom = str(self.diseaseRecoveredFrom)

        if self._is_empty(self.dateFirstPositive):
            raise ValueError("dateFirstPositive must be supplied")
        if not isinstance(self.dateFirstPositive, str):
            self.dateFirstPositive = str(self.dateFirstPositive)

        if self._is_empty(self.countryOfTest):
            raise ValueError("countryOfTest must be supplied")
        if not isinstance(self.countryOfTest, str):
            self.countryOfTest = str(self.countryOfTest)

        super().__post_init__(**kwargs)


@dataclass
class GHPProofOfVaccination(YAMLRoot):
    """
    Proof of Covid-19 Vaccination
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.GHPProofOfVaccination
    class_class_curie: ClassVar[str] = "pathogen:GHPProofOfVaccination"
    class_name: ClassVar[str] = "GHPProofOfVaccination"
    class_model_uri: ClassVar[URIRef] = GHP.GHPProofOfVaccination

    vaccinationInformation: str = None
    personalInformation: str = None
    evidence: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.vaccinationInformation):
            raise ValueError("vaccinationInformation must be supplied")
        if not isinstance(self.vaccinationInformation, str):
            self.vaccinationInformation = str(self.vaccinationInformation)

        if self._is_empty(self.personalInformation):
            raise ValueError("personalInformation must be supplied")
        if not isinstance(self.personalInformation, str):
            self.personalInformation = str(self.personalInformation)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence]
        self.evidence = [v if isinstance(v, str) else str(v) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class GHPProofOfCovidTest(YAMLRoot):
    """
    Proof of Covid-19 Lab test
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.GHPProofOfCovidTest
    class_class_curie: ClassVar[str] = "pathogen:GHPProofOfCovidTest"
    class_name: ClassVar[str] = "GHPProofOfCovidTest"
    class_model_uri: ClassVar[URIRef] = GHP.GHPProofOfCovidTest

    testInformation: str = None
    personalInformation: str = None
    evidence: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.testInformation):
            raise ValueError("testInformation must be supplied")
        if not isinstance(self.testInformation, str):
            self.testInformation = str(self.testInformation)

        if self._is_empty(self.personalInformation):
            raise ValueError("personalInformation must be supplied")
        if not isinstance(self.personalInformation, str):
            self.personalInformation = str(self.personalInformation)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence]
        self.evidence = [v if isinstance(v, str) else str(v) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class GHPProofOfRecovery(YAMLRoot):
    """
    Proof of recovery from Covid-19
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATHOGEN.GHPProofOfRecovery
    class_class_curie: ClassVar[str] = "pathogen:GHPProofOfRecovery"
    class_name: ClassVar[str] = "GHPProofOfRecovery"
    class_model_uri: ClassVar[URIRef] = GHP.GHPProofOfRecovery

    infectionInformation: str = None
    personalInformation: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.infectionInformation):
            raise ValueError("infectionInformation must be supplied")
        if not isinstance(self.infectionInformation, str):
            self.infectionInformation = str(self.infectionInformation)

        if self._is_empty(self.personalInformation):
            raise ValueError("personalInformation must be supplied")
        if not isinstance(self.personalInformation, str):
            self.personalInformation = str(self.personalInformation)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

