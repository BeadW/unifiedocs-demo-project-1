import requests
import json
import yaml
from pathlib import Path

UNIFIEDOCS_URL = "https://ogbmmjda0f.execute-api.ap-southeast-2.amazonaws.com/prod/coredocs"

def _read_project_yaml() -> dict:
    """
    Read the project yaml from the top level
    of the dbt project.
    """
    with open('dbt_project.yml', 'r') as file:
        project_yaml = yaml.safe_load(file)
    return project_yaml

def _get_metadata_locations(project_yaml) -> dict:
    """
    Create a dictionary containing all target file
    locations.
    """
    target_path = project_yaml['target-path']
    return {
        "manifest_location": Path(target_path, 'manifest.json'),
        "catalog_location": Path(target_path, "catalog.json")
    }

def _get_project_name(project_yaml) -> str:
    """
    Get the project mane and ensure it:
        - Has no illigal characters
        - Is formatted properly
    """
    return project_yaml['name'].lower()

def _read_json(location) -> dict:
    """
    Read json file and return a dictionary
    """
    with open(location) as file: 
        return json.load(file)

def _read_manifest_json() -> dict:
    pass

def _read_catalog_json() -> dict:
    pass

def _create_api_payload(project_name, manifest, catalog):
    return {
        project_name: {
            'manifest': manifest,
            'catalog': catalog
        }
    }

def _create_api_headers():
    return {}

def _push_metadata(api_headers, api_payload):
    response = requests.post(UNIFIEDOCS_URL, json=api_payload)
    print(response)

if __name__ == '__main__':
    project_yaml = _read_project_yaml()
    project_name = _get_project_name(project_yaml)
    metadata_locations = _get_metadata_locations(project_yaml)
    print(metadata_locations)
    manifest = _read_json(metadata_locations['manifest_location'])
    catalog = _read_json(metadata_locations['catalog_location'])
    api_payload = _create_api_payload(project_name, manifest, catalog)
    api_headers = _create_api_headers()
    _push_metadata(api_headers, api_payload)

