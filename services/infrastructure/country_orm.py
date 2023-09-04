from pymongo import MongoClient
from dataclasses import dataclass
from typing import List
import os
from dotenv import load_dotenv


load_dotenv()
client = MongoClient(os.environ.get('MONGO_CLIENT'))
db = client[os.environ.get('MONGO_DB_NAME')]
collection = db[os.environ.get('MONGO_COLLECTION_NAME')]


@dataclass
class CountryEntity:
    """An entity of a country, representing a dictionary from MongoDB."""
    name: str
    code: str
    curr_gdp: int


def _country_dict_to_entity(country_dict: dict) -> CountryEntity:
    """This function converts dict, that represents a country, to a CountryEntity.

    :param country_dict: Dictionary received from MongoDB with data on a certain country.
    :type country_dict: dict
    :return: Instance of CountryEntity converted from the country_dict.
    :rtype: CountryEntity
    """
    year = 2022
    gdp = country_dict.get(str(year), None)

    while not gdp:
        year -= 1
        gdp = country_dict.get(str(year), None)

    return CountryEntity(
        name=country_dict['Country Name'],
        code=country_dict['Country Code'],
        curr_gdp=gdp
    )


def get_country_by_code(code: str) -> CountryEntity:
    """This function receives a country code, returns a CountryEntity by it.

    :param code: The code that is used to extract a certain country, associated with this code.
    :type code: str
    :return: Instance of CountryEntity associated with the code.
    :rtype: CountryEntity
    """
    country_dict = collection.find_one({'Country Code': code.upper()})
    country = _country_dict_to_entity(country_dict)
    return country


def get_country_by_name(name: str) -> CountryEntity:
    """This function receives a country name, returns a CountryEntity by it.

    :param name: The name that is used to extract a certain country, associated with this code.
    :type name: str
    :return: Instance of CountryEntity associated with the name.
    :rtype: CountryEntity
    """
    country_dict = collection.find_one({'Country Name': name})
    country = _country_dict_to_entity(country_dict)
    return country


def get_countries() -> List[CountryEntity]:
    """This function returns a list of last ten countries.

    :return: List of CountryEntity instances.
    :rtype: List[CountryEntity]
    """
    countries = []
    cursor = collection.find().limit(10)
    for country in cursor:
        countries.append(_country_dict_to_entity(country))
    return countries
