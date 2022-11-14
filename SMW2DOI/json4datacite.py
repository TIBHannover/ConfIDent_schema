import glob
import json
import os
import requests
import pprint
import argparse
from datacite_python import generated as dc
from datetime import date
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader

p = argparse.ArgumentParser()
p.add_argument('--user', "-u", help="sets username of DataCite account")
p.add_argument('--password', "-pw", help="sets password of DataCite account")
p.add_argument('--prefix', "-p", help="sets prefix of DataCite account")
args = p.parse_args()

TODAY = str(date.today())
pp = pprint.PrettyPrinter(indent=4)
DEBUG = False
ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")
DATA_FILES = glob.glob(os.path.join(DATA_DIR, '*.json'))
TEST_SAMPLE = glob.glob(os.path.join(DATA_DIR, "event_examples.json"))
DATACITE_DICT = {
    'data': {
        'type': 'dois',
        'attributes': {
            'prefix': args.prefix,
            'event': 'draft',
            # 'event': 'publish',
            'identifiers': [{
                'identifierType': 'DOI'
            }],
            'url': 'https://www.confident-conference.org/index.php',
            'creators': [
                {'name': 'Mustermann, Max', 'nameType': 'Personal'},
            ],
            'titles': [
                {'title': 'Test event 2345'},
            ],
            'publisher': 'Kingdom Hights LTD',
            'publicationYear': '2022',
            'types': {
                'resourceType': 'academic conference',
                'resourceTypeGeneral': 'Event'
            },
            'schemaVersion': 'http://datacite.org/schema/kernel-4',
        },
    }
}
DATA = {
    'data': {
        'type': 'dois',
        'attributes': {
            'prefix': '10.80159',
            'event': 'draft',
            'identifiers': [{
                'identifierType': 'DOI'
            }],
            "url": "https://www.confident-conference.org/index.php/Event:045081df-6756-4004-9091-3f42c0551332",
            "types": {
                "resourceType": "academic conference",
                "resourceTypeGeneral": "Event"
            },
            "creators": [
                {
                    "name": "KDZ - Centre for Public Administration Research",
                    "nameType": "Organizational",
                    "givenName": None,
                    "familyName": None,
                    "affiliation": [],
                    "nameIdentifiers": [
                        {
                            "schemeUri": "https://ror.org",
                            "nameIdentifier": "https://ror.org/03k3t0n26",
                            "nameIdentifierScheme": "ROR"
                        }
                    ]
                }
            ],
            "titles": [
                {
                    "lang": "en",
                    "title": "19th Semantic MediaWiki Conference",
                    "titleType": None
                },
                {
                    "lang": None,
                    "title": "SMWCon Fall 2022",
                    "titleType": "AlternativeTitle"
                }
            ],
            "publisher": "German National Library Of Science and Technology",
            "subjects": [],
            "contributors": [],
            "dates": [
                {
                    "date": "2022-10-26",
                    "dateType": "Valid",
                    "dateInformation": "start date"
                },
                {
                    "date": "2022-10-28",
                    "dateType": "Valid",
                    "dateInformation": "end date"
                }
            ],
            "publicationYear": 2022,
            "language": "en",
            "descriptions": [],
            "geoLocations": [
                {
                    "geoLocationPlace": "Breda, The Netherlands"
                }
            ],
            "fundingReferences": [],
            "relatedIdentifiers": [
                {
                    "schemeUri": None,
                    "schemeType": None,
                    "relationType": "IsDescribedBy",
                    "relatedIdentifier": "https://www.semantic-mediawiki.org/wiki/SMWCon_Fall_2022",
                    "resourceTypeGeneral": "Text",
                    "relatedIdentifierType": "URL",
                    "relatedMetadataScheme": None
                },
                {
                    "schemeUri": None,
                    "schemeType": None,
                    "relationType": "IsPartOf",
                    "relatedIdentifier": "10.25798/vbj2-6w50",
                    "resourceTypeGeneral": "Collection",
                    "relatedIdentifierType": "DOI",
                    "relatedMetadataScheme": None
                },
                {
                    "schemeUri": None,
                    "schemeType": None,
                    "relationType": "IsDocumentedBy",
                    "relatedIdentifier": "10.5281/zenodo.7261666",
                    "resourceTypeGeneral": "Other",
                    "relatedIdentifierType": "DOI",
                    "relatedMetadataScheme": None
                }
            ],
            "schemaVersion": "http://datacite.org/schema/kernel-4"
        }
    }
}


class DataCiteUser:
    """
    A class to hold the credentials of a DataCite Account.

    :param user The DataCite account user name.
    :param password The DataCite user account password.
    :param prefix THe DataCite user account prefix.
    """

    def __init__(self, user: str, password: str, prefix: str) -> object:
        self.user = user
        self.password = password
        self.prefix = prefix


def load(json_file_path: object, data_node: str = "results") -> dict:
    """Load a JSON file with a list of digital object records under the data_node
    that are to be registered with DataCite.

    :param json_file_path: The filepath of the JSON file
    :param data_node: Name of the JSON key that contains the data
    :return: a list of dicts that hold the data
    """
    for path in json_file_path:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)[data_node]
    return data


def translate_to_datacite_json(data: list):
    """function to translate the SMW dict into a DataSite conform JSON
    based on https://stackoverflow.com/questions/4698932/one-line-expression-to-map-dictionary-to-another"""

    confident_dict = {}
    datacite_dict = {}
    mapping_dict = {}

    # d = dict((m.get(k, k), v) for (k, v) in d.items())

    # return d


def mint_doi(datacite_conform_dict):
    # Generate DataCite XML from dictionary.
    # doc = schema42.tostring(DATACITE_DATA)
    # print(doc)

    # generate conform DataCite json
    datacite_conform_json = json.dumps(datacite_conform_dict)

    headers = {'Content-Type': 'application/vnd.api+json', }

    try:
        r = requests.post('https://api.test.datacite.org/dois',
                          headers=headers,
                          data=datacite_conform_json,
                          auth=(args.user, args.password))
        r.raise_for_status()
        response = json.loads(r.text).get("data")
        print(f'The DOI {response["id"]} was created successfully '
              f'for the  \n{response["attributes"]["titles"][0]["title"]}')
    except requests.exceptions.RequestException:
        if r.status_code == 500:
            print("ERROR: unknown prefix")
        else:
            err = json.loads(r.text)
            if "source" in err:
                wrong_field = err.get("errors")[0]["source"].replace("'", "").split(", ")[0]
                wrong_attribute = err.get("errors")[0]["source"].replace("'", "").split(", ")[1]
                error = err.get("errors")[0]["title"].split("] ")[1]
                print(f'ERROR: There is something wrong within the field: '
                      f'\n    {wrong_field} --> {wrong_attribute}'
                      f'\n    {error}'
                      )
            else:
                print("ERROR: Either the username or the password of the provided account credentials are wrong.")
    return r




if __name__ == '__main__':
    """command with which the datacite_python XSD was transformed into python dataclasses (pydantic) 
    poetry run xsdata metadata.xsd --compound-fields /
    --structure-style single-package --relative-imports --output pydantic

    # print(translate_to_datacite_json(load_json_into_dict()))
    # Validate dictionary
    # assert schema42.validate(DATACITE_DATA)
    # DATACITE_DATA['data']['attributes']['titles'][0]={'title': 'International Conference of Noobs in Coding 2022'}
    # data = load_json_into_dict()
    # print(data["results"]['Event:Db6550cc-ce04-4484-86a2-e4ccbe2c55dd']['printouts'])

    # creator = r.Creators.Creator(creator_name=r.Creators.Creator.CreatorName(value="Max Muster", name_type="Personal"))
    # data = r(identifier=r.Identifier(identifier_type="DOI"), creators=[creator])

    identifier = dc.ResourceIdentifier("", "DOI")
    person = dc.NameType.PERSONAL
    creator1_name = dc.ResourceCreatorsCreatorCreatorName("TIB", nameType="Organizational")
    creator1 = dc.ResourceCreatorsCreator(creatorName=creator1_name,
                                          affiliation=[dc.Affiliation(
                                              value="TIB",
                                              affiliationIdentifier="12345",
                                              affiliationIdentifierScheme="ROR",
                                              schemeURI="https://ror.org/")])
    creator2_name = dc.ResourceCreatorsCreatorCreatorName("Philip Strömert", nameType="Personal")
    creator2 = dc.ResourceCreatorsCreator(creatorName=creator2_name)
    creators = dc.ResourceCreators(creator=[creator1, creator2])
    data = dc.Resource(
        identifier=identifier,
        creators=creators
    )

    #x = json.dumps(dataclasses.asdict(data))
    y = dataclasses.asdict(data)

    print(y['creators']['creator'][0]['creatorName']['nameType'].value)

    pp.pprint(y)"""

    mint_doi(DATACITE_DICT)
    #print(args.user)
    # load(TEST_SAMPLE)
    # pp.pprint(load(TEST_SAMPLE))
