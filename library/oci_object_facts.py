#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_object_facts
short_description: Retrieve details of an object or all the objects in a specific namespace and bucket in OCI Object \
                    Storage Service
description:
    - This module retrieves details of an object or all the objects present in a specified namespace and bucket in OCI \
      Object Storage Service.
version_added: "2.x"
options:
    namespace_name:
        description: Name of the namespace from which facts of objects need to be fetched.
        required: true
        aliases: [ 'namespace' ]
    bucket_name:
        description: Name of the bucket from which facts of objects need to be fetched.
        required: true
        aliases: [ 'bucket' ]
    object_name:
        description: Name of the object. Required to fetch details of a specific object.
        required: false
        aliases: [ 'object', 'name' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
'''

EXAMPLES = '''
- name: Get details of all the objects in namespace 'mynamespace' and bucket 'mybucket'
  oci_object_facts:
    namespace: mynamespace
    bucket: mybucket

- name: Get details of a specific object
  oci_object_facts:
    name: mynamespace
    bucket: mybucket
    object: myobject
'''

RETURN = '''
objects:
    description: List of object details
    returned: On success
    type: complex
    contains:
        md5:
            description: Base64-encoded MD5 hash of the object data
            returned: always
            type: string
            sample: 3zBENq6MBnedDrpl2+SttQ==
        name:
            description: Name of the object
            returned: always
            type: string
            sample: image2a343.png
        size:
            description: Size of the object in bytes
            returned: always
            type: int
            sample: 165661
        time_created:
            description: Date and time of object creation
            returned: always
            type: datetime
            sample: 2017-10-09T08:39:17.411000+00:00
    sample: [
        {
            "md5": "3zBENq6MBnedDrpl2+SttQ==",
            "name": "image2a343.png",
            "size": 165661,
            "time_created": "2017-10-09T10:27:53.688000+00:00"
        },
        {
            "md5": "LWX13se0YFa6VVlv0R3hqA==",
            "name": "info1.txt",
            "size": 1084,
            "time_created": "2017-10-09T08:39:17.411000+00:00"
        }
    ]
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from oci.object_storage.object_storage_client import ObjectStorageClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError
    from ansible.module_utils.oracle import oci_utils

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(
        namespace_name=dict(type='str', required=True, aliases=['namespace']),
        bucket_name=dict(type='str', required=True, aliases=['bucket']),
        object_name=dict(type='str', required=False, aliases=['name', 'object'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module')

    config = oci_utils.get_oci_config(module)
    object_storage_client = ObjectStorageClient(config)

    namespace = module.params['namespace_name']
    bucket = module.params['bucket_name']
    object_name = module.params['object_name']
    fields_to_retrieve = 'name,size,timeCreated,md5'
    try:
        if object_name is not None:
            result = to_dict(oci_utils.list_all_resources(object_storage_client.list_objects, namespace_name=namespace,
                                                          bucket_name=bucket, prefix=object_name,
                                                          fields=fields_to_retrieve).objects)
        else:
            result = to_dict(oci_utils.
                             list_all_resources(object_storage_client.list_objects, namespace_name=namespace,
                                                bucket_name=bucket, fields=fields_to_retrieve).objects)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(objects=result)


if __name__ == '__main__':
    main()
