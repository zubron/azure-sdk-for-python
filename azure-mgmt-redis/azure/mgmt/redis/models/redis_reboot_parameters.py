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


class RedisRebootParameters(Model):
    """Specifies which redis node(s) to reboot.

    :param reboot_type: Which redis node(s) to reboot. Depending on this
     value data loss is possible. Possible values include: 'PrimaryNode',
     'SecondaryNode', 'AllNodes'
    :type reboot_type: str or :class:`RebootType
     <azure.mgmt.redis.models.RebootType>`
    :param shard_id: In case of cluster cache, this specifies shard id which
     should be rebooted.
    :type shard_id: int
    """ 

    _validation = {
        'reboot_type': {'required': True},
    }

    _attribute_map = {
        'reboot_type': {'key': 'rebootType', 'type': 'str'},
        'shard_id': {'key': 'shardId', 'type': 'int'},
    }

    def __init__(self, reboot_type, shard_id=None):
        self.reboot_type = reboot_type
        self.shard_id = shard_id
