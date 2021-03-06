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


class JobPreparationTask(Model):
    """A Job Preparation task to run before any tasks of the job on any given
    compute node.

    :param id: A string that uniquely identifies the job preparation task
     within the job. The id can contain any combination of alphanumeric
     characters including hyphens and underscores and cannot contain more
     than 64 characters.
    :type id: str
    :param command_line: The command line of the Job Preparation task.
    :type command_line: str
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line.
    :type resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the Job Preparation task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param constraints: Constraints that apply to the Job Preparation task.
    :type constraints: :class:`TaskConstraints
     <azure.batch.models.TaskConstraints>`
    :param wait_for_success: Whether the Batch service should wait for the
     Job Preparation task to complete successfully before scheduling any
     other tasks of the job on the compute node.
    :type wait_for_success: bool
    :param run_elevated: Whether to run the Job Preparation task in elevated
     mode. The default value is false.
    :type run_elevated: bool
    :param rerun_on_node_reboot_after_success: Whether the Batch service
     should rerun the Job Preparation task after a compute node reboots. Note
     that the Job Preparation task should still be written to be idempotent
     because it can be rerun if the compute node is rebooted while Job
     Preparation task is still running. The default value is true.
    :type rerun_on_node_reboot_after_success: bool
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'wait_for_success': {'key': 'waitForSuccess', 'type': 'bool'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
        'rerun_on_node_reboot_after_success': {'key': 'rerunOnNodeRebootAfterSuccess', 'type': 'bool'},
    }

    def __init__(self, id=None, command_line=None, resource_files=None, environment_settings=None, constraints=None, wait_for_success=None, run_elevated=None, rerun_on_node_reboot_after_success=None):
        self.id = id
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.constraints = constraints
        self.wait_for_success = wait_for_success
        self.run_elevated = run_elevated
        self.rerun_on_node_reboot_after_success = rerun_on_node_reboot_after_success
