import requests
import yaml


def get_provider(file):
    # Todo change this library to depend on moonazul-base and read the files locally instead of getting them from github
    return yaml.load(
        requests.get('https://raw.githubusercontent.com/moonazul/moonazul-data/master/%s.yaml' % file).content)


def validate_validator(runner, validator, provider):
    for postal_code, expected in provider.items():
        message = "%s fails validation incorrectly" if expected else "%s passes validation incorrectly"
        runner.assertEqual(validator(postal_code), expected, message % postal_code)


def validate_zip_validator(runner, validator):
    zip_provider = get_provider('zip')
    validate_validator(runner, validator, zip_provider)
