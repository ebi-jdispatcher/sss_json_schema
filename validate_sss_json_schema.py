#!/usr/bin/env python
# -*- coding: utf-8

import json
import easyargs
import jsonschema


@easyargs
def validate_schema(schema, data):
    with open(schema) as schema_file:
        schema_obj = json.load(schema_file)

    with open(data) as data_file:
        data_obj = json.load(data_file)

    if not (jsonschema.validate(data_obj, schema_obj, jsonschema.Draft7Validator)):
        print(f"JSON '{data}' validated against JSON schema '{schema}' ...")
        print("Validated - JSON has all the required fields and expected data types!")


if __name__ == '__main__':
    validate_schema()
