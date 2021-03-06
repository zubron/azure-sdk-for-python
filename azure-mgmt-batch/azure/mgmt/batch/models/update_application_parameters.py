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


class UpdateApplicationParameters(Model):
    """Parameters for an ApplicationOperations.UpdateApplication request.

    :param allow_updates: A value indicating whether packages within the
     application may be overwritten using the same version string.
    :type allow_updates: bool
    :param default_version: The package to use if a client requests the
     application but does not specify a version.
    :type default_version: str
    :param display_name: The display name for the application.
    :type display_name: str
    """ 

    _attribute_map = {
        'allow_updates': {'key': 'allowUpdates', 'type': 'bool'},
        'default_version': {'key': 'defaultVersion', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, allow_updates=None, default_version=None, display_name=None):
        self.allow_updates = allow_updates
        self.default_version = default_version
        self.display_name = display_name
