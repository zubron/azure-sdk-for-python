# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExportTemplateRequest(Model):
    """Export resource group template request parameters.

    :param resources: Gets or sets the ids of the resources. The only
     supported string currently is '*' (all resources). Future api updates
     will support exporting specific resources.
    :type resources: list of str
    :param options: The export template options. Supported values include
     'IncludeParameterDefaultValue', 'IncludeComments' or
     'IncludeParameterDefaultValue, IncludeComments
    :type options: str
    """ 

    _attribute_map = {
        'resources': {'key': 'resources', 'type': '[str]'},
        'options': {'key': 'options', 'type': 'str'},
    }

    def __init__(self, resources=None, options=None):
        self.resources = resources
        self.options = options
