#!/usr/bin/env python
# -*- coding: utf-8

import os
import json
import jsonschema


def validate_schema(schema, data):
    with open(schema) as schema_file:
        schema_obj = json.load(schema_file)

    with open(data) as data_file:
        data_obj = json.load(data_file)

    if not (jsonschema.validate(data_obj, schema_obj, jsonschema.Draft7Validator)):
        return True
    return False


def test_validate_blastp_schema():
    """Checks whether the given BLASTP data matches the schema"""

    schema = os.path.normpath("sss_schema.json")
    data = os.path.normpath("example_blastp.json")
    assert validate_schema(schema, data)


def test_validate_fasta36_schema():
    """ Checks whether the given FASTA36 data matches the schema"""

    schema = os.path.normpath("sss_schema.json")
    data = os.path.normpath("example_fasta36.json")
    assert validate_schema(schema, data)
