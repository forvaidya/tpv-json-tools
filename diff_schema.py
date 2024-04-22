#!/usr/bin/env python3

from genson import SchemaBuilder
import json
import sys


json_xm = sys.argv[1]
json_blr = sys.argv[2]

jdata_blr = {}
with open(json_blr) as json_blr_ptr:
    jdata_blr = json.load(json_blr_ptr)

builder_blr = SchemaBuilder()
builder_blr.add_object(jdata_blr)
json_blr_schema = builder_blr.to_schema()

jdata_xm = {}
with open(json_xm) as json_xm_ptr:
    jdata_xm = json.load(json_xm_ptr)

builder_xm = SchemaBuilder()
builder_xm.add_object(jdata_xm)
json_xm_schema = builder_xm.to_schema()




json_xm_schema_file = json_xm.strip(r'.json') + "_output_schema.json"

with open(json_xm_schema_file, 'w', encoding='utf-8') as json_xm_schema_wptr:
    json.dump(json_xm_schema, json_xm_schema_wptr, ensure_ascii=False, indent=4)


json_blr_schema_file = json_blr.strip(r'.json') + "_output_schema.json"
with open(json_blr_schema_file, 'w', encoding='utf-8') as json_blr_schema_wptr:
    json.dump(json_blr_schema, json_blr_schema_wptr, ensure_ascii=False, indent=4)






