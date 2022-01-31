# SSS JSON Schema
This is a *WIP* [JSON schema](https://json-schema.org/) for standardising EMBL-EBI's Job Dispatcher Sequence Similarity Search (SSS) outputs. A list of tools available at EMBL-EBI that generate these outputs is provided [here](https://www.ebi.ac.uk/seqdb/confluence/display/JDSAT/Sequence+Similarity+Search).

## Validating an output against the SSS JSON schema

Validation an existing JSON can de done by running the Python module [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/).

```bash
jsonschema --validator Draft7Validator -i example_blastp.json sss_schema.json
```

or alternatively, using the custom Python script provided:

```bash
python validate_sss_json_schema.py sss_schema.json example_fasta36.json
```

## License 
The European Bioinformatics Institute - [EMBL-EBI](https://www.ebi.ac.uk/), is an Intergovernmental Organization which, as part of the European Molecular Biology Laboratory family, focuses on research and services in bioinformatics.  

Apache License 2.0. See [license](LICENSE) for details.
