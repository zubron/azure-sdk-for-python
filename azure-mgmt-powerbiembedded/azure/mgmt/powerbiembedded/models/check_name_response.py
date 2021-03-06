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


class CheckNameResponse(Model):
    """CheckNameResponse.

    :param name_available: Specifies a Boolean value that indicates whether
     the specified Power BI Workspace Collection name is available to use.
    :type name_available: bool
    :param reason: Reason why the workspace collection name cannot be used.
     Possible values include: 'Unavailable', 'Invalid'
    :type reason: str or :class:`CheckNameReason
     <azure.mgmt.powerbiembedded.models.CheckNameReason>`
    :param message: Message indicating an unavailable name due to a conflict
     or a description of the naming rules that are violated.
    :type message: str
    """ 

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, name_available=None, reason=None, message=None):
        self.name_available = name_available
        self.reason = reason
        self.message = message
