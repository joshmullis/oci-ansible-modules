#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: oci_db_home_facts
short_description: Fetches details of one or more OCI DB Homes
description:
    - Fetches details of the OCI DB Home.
version_added: "2.x"
options:
    compartment_id:
        description: Identifier of the compartment in which the specified DB System exists
        required: false
    db_system_id:
        description: Identifier of the DB System under which the DB Home is available.
        required: false
    db_home_id:
        description: Identifier of the DB Home whose details needs to be fetched.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
'''

EXAMPLES = '''
#Fetch DB Home
- name: List all DB Homes in a DB System
  oci_db_home_facts:
      compartment_id: 'ocid1.compartment..xcds'
      db_system_id: 'ocid1.dbsystem..xcds'
#Fetch a specific DB Home
- name: List a specific DB Home
  oci_db_home_facts:
      db_home_id: 'ocid1.dbhome..xcds'
'''

RETURN = '''
    db_homes:
        description: Attributes of the Fetched DB Homes
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the DB Home
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            db_system_id:
                description: Identifier of the  DB System under which the DB Home should exists.
                returned: always
                type: string
                sample: ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx
            db_version:
                description: Oracle database version.
                returned: always
                type: string
                sample: 12.2.0.1.1
            display_name:
                description: The user-friendly name for the DB Home.
                returned: always
                type: string
                sample: ansible-db-home
            id:
                description: Identifier of the DB Home.
                returned: always
                type: string
                sample: ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the DB System was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            last_patch_history_entry_id:
                description: The OCID of the last patch history. This is updated
                             as soon as a patch operation is started.
                returned: always
                type: string
                sample: ocid1.lastpatchhistory.aaaa
            lifecycle_state:
                description: The current state of the DB System.
                returned: always
                type: string
                sample: AVAILABLE
        sample: [{
                   "compartment_id":"ocid1.compartment.aaaa",
                   "db_system_id":"ocid1.dbsystem.aaaa",
                   "db_version":"12.2.0.1.1",
                   "display_name":"ansible-db-one",
                   "id":"ocid1.dbhome.aaaa",
                   "last_patch_history_entry_id":"ocid1.dbpatchhistory.aaaa",
                   "lifecycle_state":"AVAILABLE",
                   "time_created":"2018-02-16T08:44:32.779000+00:00"
                 },
                {
                   "compartment_id":"ocid1.compartment.aaaa",
                   "db_system_id":"ocid1.dbsystem.aaaa",
                   "db_version":"12.2.0.1.1",
                   "display_name":"ansible-db-two",
                   "id":"ocid1.dbhome.aaaa",
                   "last_patch_history_entry_id":"ocid1.dbpatchhistory.aaaa",
                   "lifecycle_state":"AVAILABLE",
                   "time_created":"2018-02-16T08:44:32.779000+00:00"
                 }]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_db_homes(db_client, module):
    result = dict(
        db_homes=''
    )
    compartment_id = module.params.get('compartment_id')
    db_home_id = module.params.get('db_home_id')
    db_system_id = module.params.get('db_system_id')
    try:
        if compartment_id and db_system_id:
            get_logger().debug("Listing all DB Homes under compartment %s and db system %s",
                               compartment_id, db_system_id)
            existing_db_homes = oci_utils.list_all_resources(
                db_client.list_db_homes,
                compartment_id=compartment_id, db_system_id=db_system_id)
        elif db_home_id:
            get_logger().debug("Listing DB Home %s", db_home_id)
            response = oci_utils.call_with_backoff(
                db_client.get_db_home, db_home_id=db_home_id)
            existing_db_homes = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list DB Homes due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result['db_homes'] = to_dict(existing_db_homes)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_home_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(
        compartment_id=dict(type='str', required=False),
        db_system_id=dict(type='str', required=False),
        db_home_id=dict(type='str', required=False, aliases=['id'])
    ))
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[
            ['compartment_id', 'db_home_id'],
            ['db_system_id', 'db_home_id']
        ]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module')

    oci_config = oci_utils.get_oci_config(module)
    db_client = DatabaseClient(oci_config)
    result = list_db_homes(db_client, module)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
