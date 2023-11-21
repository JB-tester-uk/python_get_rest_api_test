import requests
from behave import *

@given('this url "{url_string}"')
def given_a_url_has_been_provide(context, url_string):
    context.url = str(url_string).strip()
    assert ((r"http://" in url_string) or
            (r"https://" in url_string)) == True, f"Error: {url_string} is missing either 'http://' or 'https://'"


@when('the premium user request is sent')
def send_url_get_request(context):
    try:
        context.result = requests.get(context.url)
    except Exception as e:
        print(e)
        assert False, f"Error: problem with performing a get request"


@then('we should receive a "{response_value}" response')
def check_response_value(context, response_value):
    assert context.result.status_code == int(response_value), f"Error: incorrect response value, expected {response_value},actual value {context.result.status_code}"


@then('"{list_name}" has field "{expected_field}" and should contain "{expected_string}"')
def check_get_response_contains_expected_string(context, list_name, expected_field, expected_string):
    json_response = context.result.json()
    response_name_values = []

    if json_response is not None and list_name in json_response:
        for element in json_response[list_name]:
            if expected_field in element:
                response_name_values.append(element[expected_field])
    else:
        assert False, f"Error: get response, list name missing , expected {list_name}"

    assert  expected_string in response_name_values, f"Error: get response, expected \"{expected_string}\", actual values {response_name_values} with field name \"{expected_field}\""


@then('response has field "{expected_field}" and should contain "{expected_string}"')
def check_get_response_contains_expected_string(context, expected_field, expected_string):
    json_response = context.result.json()

    assert  expected_field in json_response,  f"Error: get response, expected field \"{expected_field}\", actual response \"{json_response}\""
    assert  json_response[expected_field] == expected_string, f"Error: get response, expected \"{expected_string}\", actual \"{json_response[expected_field]}\""



@then('"{list_name}" has field "{expected_field}" and DOES NOT contain "{expected_string}"')
def check_get_response_contains_expected_string(context, list_name, expected_field, expected_string):
    json_response = context.result.json()
    response_name_values = []

    if json_response is not None and list_name in json_response:
        for element in json_response[list_name]:
            if expected_field in element:
                response_name_values.append(element[expected_field])
    else:
        assert False, f"Error: get response, list name missing , expected {list_name}"

    assert  expected_string not in response_name_values, f"Error: get response, expected value \"{expected_string}\" SHOULD NOT be present, actual values {response_name_values} with field name \"{expected_field}\""