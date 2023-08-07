#!/usr/bin/env python

"""Run tests against all the *.raw files."""
import glob
import os

import pytest
import yaml

import lib
from lib.parse import parse_output

rawoutput ="""
Sun Aug  6 20:04:26.275 UTC
Cisco IOS XR Software, Version 7.3.2
Copyright (c) 2013-2021 by Cisco Systems, Inc.

Build Information:
 Built By     : ingunawa
 Built On     : Wed Oct 13 20:00:36 PDT 2021
 Built Host   : iox-ucs-017
 Workspace    : /auto/srcarchive17/prod/7.3.2/xrv9k/ws
 Version      : 7.3.2
 Location     : /opt/cisco/XR/packages/
 Label        : 7.3.2-0

cisco IOS-XRv 9000 () processor
System uptime is 3 days 4 hours 39 minutes
"""

command = "show version"
platform = "cisco_xr"

def raw_template_test(rawoutput,platform,command):
    """Return structured data along with reference data."""
    try:
        structured = parse_output(platform=platform, command=command, data=rawoutput)
        return structured
    except Exception as err:
        print(err)
    # with open(parsed_file, "r", encoding="utf-8") as data:
    #     parsed_data = yaml.safe_load(data.read())

data = raw_template_test(rawoutput,platform,command)
print(data)

