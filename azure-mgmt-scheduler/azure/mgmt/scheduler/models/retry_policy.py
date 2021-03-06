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


class RetryPolicy(Model):
    """RetryPolicy.

    :param retry_type: Gets or sets the retry strategy to be used. Possible
     values include: 'None', 'Fixed'
    :type retry_type: str or :class:`RetryType
     <azure.mgmt.scheduler.models.RetryType>`
    :param retry_interval: Gets or sets the retry interval between retries.
    :type retry_interval: timedelta
    :param retry_count: Gets or sets the number of times a retry should be
     attempted.
    :type retry_count: int
    """ 

    _attribute_map = {
        'retry_type': {'key': 'retryType', 'type': 'RetryType'},
        'retry_interval': {'key': 'retryInterval', 'type': 'duration'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
    }

    def __init__(self, retry_type=None, retry_interval=None, retry_count=None):
        self.retry_type = retry_type
        self.retry_interval = retry_interval
        self.retry_count = retry_count
