from pymongo import MongoClient
from dataclasses import dataclass
from typing import List

client = MongoClient('mongodb+srv://bertstein:Es2gA5S9sjGi!MU@cluster0.trbutmg.mongodb.net/')
db = client['InfoMapify']
collection = db['Countries']


@dataclass
class CountryEntity:
    name: str
    code: str
    curr_gdp: int


def _country_dict_to_entity(country_dict: dict) -> CountryEntity:
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
    country_dict = collection.find_one({'Country Code': code.upper()})
    country = _country_dict_to_entity(country_dict)
    return country


def get_country_by_name(name: str) -> CountryEntity:
    country_dict = collection.find_one({'Country Name': name})
    country = _country_dict_to_entity(country_dict)
    return country


def get_countries() -> List[CountryEntity]:
    countries = []
    cursor = collection.find().limit(10)
    for country in cursor:
        countries.append(_country_dict_to_entity(country))
    return countries
