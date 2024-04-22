#!/usr/bin/env python3

from genson import SchemaBuilder
import json
import sys


json_xm = sys.argv[1]
json_blr = sys.argv[2]


json_xm_schema = json_xm.strip(r'.json') + "_schema.json

json_blr_schema = json_blr.strip(r'.json') + "_schema.json


