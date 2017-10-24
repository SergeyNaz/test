# -*- coding: utf-8 -*-
from lettuce import *
import requests


API_ADDRESS = 'https://api.hh.ru'


@step('I request available countries')
def request_countries(step):
    response = requests.get(API_ADDRESS + "/areas/countries")
    world.last_request = response


@step('Returned code is (\d+)')
def check_returned_code(step, wished_code):
    assert world.last_request.status_code == int(wished_code),\
        'Returned codes are not match, expected - {}, actual - {}'.format(wished_code, world.last_code)


@step('Returned items have (.*) fields')
def check_returned_items_have_fields(step, wished_fields):
    wished_fields_list = [field.strip() for field in wished_fields.split(',')]
    country_items = world.last_request.json()
    for country_item in country_items:
        for field in wished_fields_list:
            assert field in country_item, \
                'Not found {} field for country with {} id'.format(field, country_item['id'])


@step('Each country url follows to the area with the same name and id')
def country_urls_follows_to_same_areas(step):
    for country in world.last_request.json():
        area = requests.get(country['url']).json()
        assert area['id'] == country['id'], \
            'Id of {} country does not match with area id'.format(country['name'])
        assert area['name'] == country['name'], \
            'Name of {} country does not match with area name'.format(country['name'])


@step('I create initial (\w+) searching request')
def create_search_company_request(step, entity):
    entity = entity.encode('utf8')
    if entity.endswith('y'):
        entity = entity[:len(entity) - 1] + 'ie'
    world.request_string = API_ADDRESS + "/{}s".format(entity)


@step('I add (\w+) parameter with "(.*)" value as GET parameter to request string')
def add_get_parameter(step, parameter, value):
    if '?' not in world.request_string:
        world.request_string += '?{}={}'.format(parameter, value.encode('utf8'))
    else:
        world.request_string += '&{}={}'.format(parameter, value.encode('utf8'))


@step('I execute request string')
def execute_request_string(step):
    world.last_request = requests.get(world.request_string)


@step('Response contains (\d+) count of items by "(\w+)" key')
def check_response_by_key(step, items_count, key_name):
    assert int(items_count) == len(world.last_request.json()[key_name]), \
        "Count of items is not match with expected"


@step('Item contains "(.*)" value for "(\w+)" key')
def item_contains_value_for_key(step, value, key):
    assert value == world.last_request.json()['items'][0][key], \
        "Name of item does not match with expected"


@step('Item contains "(.*)" value for "(\w+)" key')
def item_contains_value_for_key(step, value, key):
    assert value == world.last_request.json()['items'][0][key], \
        "Name of item does not match with expected"


@step('Response contains item where "(\w+)" key has "(.*)" value')
def find_item_with_key_and_value(step, key, value):
    print key, value
    found = False
    for item in world.last_request.json()['items']:
        if item[key] == value:
            found = True
            break
    assert found, 'Not found vacancy with {} name'.format(value)