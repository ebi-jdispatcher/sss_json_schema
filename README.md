# SSS JSON Schema
This is a *WIP* [JSON schema](https://json-schema.org/) for standardising EMBL-EBI's Job Dispatcher Sequence Similarity Search (SSS) outputs. A list of tools available at EMBL-EBI that generate these outputs is provided [here](https://www.ebi.ac.uk/seqdb/confluence/display/JDSAT/Sequence+Similarity+Search).

## Overview of the proposed Schema
The first properties the schema should provide are a quick overview of the executed program. Example:

```json lines
{
  "program": "blastp",
  "version": "BLASTP 2.9.0+",
  "command": "blastp -db 'uniprotkb_swissprot' -query input.sequence -outfmt 11 -out output.archive -matrix BLOSUM62 -max_target_seqs 50 -evalue 10 -gapopen 11 -gapextend 1"
```

This is followed by information about the query sequence, including, database identifier (ID), sequence ID, sequence accession, taxonomy information (if available) and some special parsed attributes available for some sequence providers (currently only `query_uni_*` attributes are supported for UniProtKB sequences). Example:
```json lines
    "query_def": "sp|P35858|ALS_HUMAN Insulin-like growth factor-binding protein complex acid labile subunit OS=Homo sapiens GN=IGFALS PE=1 SV=1",
    "query_db": "SP",
    "query_id": "ALS_HUMAN",
    "query_acc": "P35858",
    "query_desc": "Insulin-like growth factor-binding protein complex acid labile subunit OS=Homo sapiens GN=IGFALS PE=1 SV=1",
    "query_url": "https://www.uniprot.org/uniprot/P35858",
    "query_uni_de": "Insulin-like growth factor-binding protein complex acid labile subunit",
    "query_os": "Homo sapiens",    
    "query_uni_os": "Homo sapiens",
    "query_uni_gn": "IGFALS",
    "query_uni_pe": "1",
    "query_uni_sv": "1",
    "query_stype": "protein",
    "query_len": 605,
```

This is followed by information about the 'targeted' database(s). Example:

```json lines
  "db_count": 1,
    "db_num": 561356,
    "db_len": 201858328,
    "dbs": [
        {
            "name": "uniprotkb_swissprot",
            "stype": "protein",
            "created": "2019-11-13T02:09:00+00:00"
        }
    ],
```
This is followed by information about queried options and parameters, which are entirely optional.

```json lines
    "alignments": 50,
    "scores": 50,
    "expect_upper": 10.0,
    "gap_extend": 1.0,
    "gap_open": 11.0,
    "matrix": "BLOSUM62",
```
Next, as an option, we can provide start and end time stamps, as well as a time delta for how long the `search` took. Example:

```json lines
    "start": "2019-11-28T09:40:14+00:00",
    "end": "2019-11-28T09:40:26+00:00",
    "search": "P0Y0M0DT0H0M12.000S",
```

The next main required object properties are the `hits` list. Each search hit has got an incremental identifier plus several attributes following the same convention as the those mentioned above for the query sequence. 
```json lines
    "hits": [
            {
            "hit_num": 1,
            "hit_def": "SP:P35858 ALS_HUMAN Insulin-like growth factor-binding protein complex acid labile subunit OS=Homo sapiens OX=9606 GN=IGFALS PE=1 SV=1",
            "hit_db": "SP",
            "hit_id": "ALS_HUMAN",
            "hit_acc": "P35858",
            "hit_desc": "Insulin-like growth factor-binding protein complex acid labile subunit OS=Homo sapiens OX=9606 GN=IGFALS PE=1 SV=1",
            "hit_url": "https://www.uniprot.org/uniprot/P35858",
            "hit_os": "Homo sapiens",
            "hit_xref_url": "https://www.ebi.ac.uk/ebisearch/search.ebi?db=uniprot&query=P35858",
            "hit_uni_de": "Insulin-like growth factor-binding protein complex acid labile subunit",
            "hit_uni_os": "Homo sapiens",
            "hit_uni_ox": "9606",
            "hit_uni_gn": "IGFALS",
            "hit_uni_pe": "1",
            "hit_uni_sv": "1",
            "hit_len": 605,
```

The main addition to hits is the `hits_hsps` list, which displays key information for each HSP (High-Scoring Segment - while this notation/organization makes sense for BLAST applications, we use it interchangeably for other tool outputs such as those from FASTA, even if only one "HSP" is observed for each hit). Key information provided for each HSP are scores, such as e-values, bit scores, etc. Other important attributes are sequence "from" and "to" ranges that allow us to (re)construct a parwise alignment between the query and hit sequence. Example:

```json lines
            "hit_hsps": [
                {
                    "hsp_num": 1,
                    "hsp_score": 3142,
                    "hsp_bit_score": 1214.91,
                    "hsp_expect": 0.0,
                    "hsp_align_len": 605,
                    "hsp_identity": 100.0,
                    "hsp_positive": 100.0,
                    "hsp_gaps": 0,
                    "hsp_query_frame": "0",
                    "hsp_hit_frame": "0",
                    "hsp_strand": "none/none",
                    "hsp_query_from": 1,
                    "hsp_query_to": 605,
                    "hsp_hit_from": 1,
                    "hsp_hit_to": 605,
                    "hsp_qseq": "MALRKGGLALALLLLSWV(...)RDLSEAHFAPC",
                    "hsp_mseq": "MALRKGGLALALLLLSWV(...)RDLSEAHFAPC",
                    "hsp_hseq": "MALRKGGLALALLLLSWV(...)RDLSEAHFAPC"
                }
            ]
```

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
