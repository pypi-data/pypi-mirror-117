# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
# Copyright (C) 2021 Graz University of Technology.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Record response serializers."""

from .csl import CSLJSONSerializer, StringCitationSerializer
from .datacite import DataCite43JSONSerializer, DataCite43XMLSerializer
from .dublincore import DublinCoreJSONSerializer, DublinCoreXMLSerializer
from .ui import UIJSONSerializer

__all__ = (
    "CSLJSONSerializer",
    "DataCite43JSONSerializer",
    "DataCite43XMLSerializer",
    "DublinCoreJSONSerializer",
    "DublinCoreXMLSerializer",
    "StringCitationSerializer",
    "UIJSONSerializer",
)
