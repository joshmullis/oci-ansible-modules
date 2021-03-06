.. _oci_security_list_facts:


oci_security_list_facts - Fetches details of a specific Security List or a list of Security Lists in the specified VCN and compartment
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetches details of a specific Security List or a list of Security Lists in the specified VCN and compartment.oc



Requirements (on host that executes module)
-------------------------------------------

  * python >= 2.6
  * Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io



Options
-------

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>

    <tr>
    <td>api_user<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user's OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
    </td>
    </tr>

    <tr>
    <td>api_user_fingerprint<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair's fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
    </td>
    </tr>

    <tr>
    <td>api_user_key_file<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
    </td>
    </tr>

    <tr>
    <td>api_user_key_pass_phrase<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the compartment details about whose Security List must be retrieved</div>
    </td>
    </tr>

    <tr>
    <td>config_file_location<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
    </td>
    </tr>

    <tr>
    <td>config_profile_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>DEFAULT</td>
    <td></td>
    <td>
        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
    </td>
    </tr>

    <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
    </td>
    </tr>

    <tr>
    <td>security_list_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Security List. Required if the details of a specific Security List details needs to be fetched. Mutually exclusive with compartment_id and vcn_id.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>tenancy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
    </td>
    </tr>

    <tr>
    <td>vcn_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Virtual Cloud Network to which the Security List is attached.</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    # Note: These examples do not set authentication details.
    # Get information about all Security List
    - name: Get information about all security list within a vcn and compartment
      oci_security_list_facts:
        compartment_id: 'ocid.compartment..aa'
        vcn_id: 'ocid.vcn..aa'

    # Get information about a specific Security List
    - name: Get information about security list by id
      oci_security_list_facts:
        id: 'ocid1.securitylist.aa'


Return Values
-------------

Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

    <tr>
    <td>security_lists</td>
    <td>
        <div>Attributes of the fetched Security List(s).</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'egress_security_rules': [{'icmp_options': None, 'udp_options': None, 'is_stateless': None, 'tcp_options': None, 'destination': '0.0.0.0/0', 'protocol': 'all'}], 'display_name': 'ansible_security_list_one', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'vcn_id': 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx', 'defined_tags': {'features': {'capacity': 'medium'}}, 'freeform_tags': {'region': 'east'}, 'time_created': '2017-11-24T05:33:44.779000+00:00', 'ingress_security_rules': [{'source': '0.0.0.0/0', 'icmp_options': None, 'udp_options': None, 'is_stateless': False, 'tcp_options': {'source_port_range': None, 'destination_port_range': {'max': 22, 'min': 22}}, 'protocol': '6'}, {'source': '0.0.0.0/0', 'icmp_options': {'code': 4, 'type': 3}, 'udp_options': None, 'is_stateless': False, 'tcp_options': None, 'protocol': '1'}, {'source': '10.0.0.0/16', 'icmp_options': {'code': None, 'type': 3}, 'udp_options': None, 'is_stateless': False, 'tcp_options': None, 'protocol': '1'}], 'id': 'ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx'}, {'lifecycle_state': 'AVAILABLE', 'egress_security_rules': [{'icmp_options': None, 'udp_options': None, 'is_stateless': True, 'tcp_options': None, 'destination': '10.0.0.0/8', 'protocol': 'all'}], 'display_name': 'ansible_security_list_two', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'vcn_id': 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx', 'defined_tags': {'features': {'capacity': 'large'}}, 'freeform_tags': {'region': 'west'}, 'time_created': '2017-11-24T05:33:44.779000+00:00', 'ingress_security_rules': [{'source': '0.0.0.0/0', 'icmp_options': None, 'udp_options': None, 'is_stateless': False, 'tcp_options': {'source_port_range': None, 'destination_port_range': {'max': 45, 'min': 50}}, 'protocol': '6'}, {'source': '0.0.0.0/0', 'icmp_options': {'code': 4, 'type': 3}, 'udp_options': None, 'is_stateless': False, 'tcp_options': None, 'protocol': '1'}], 'id': 'ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx'}]</td>
    </tr>

    <tr>
    <td>contains:</td>
    <td colspan=4>
        <table border=1 cellpadding=2>

        <tr>
        <th class="head">name</th>
        <th class="head">description</th>
        <th class="head">returned</th>
        <th class="head">type</th>
        <th class="head">sample</th>
        </tr>

        <tr>
        <td>vcn_id</td>
        <td>
            <div>Identifier of the Virtual Cloud Network to which the Security List is attached.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vcn..ixcd</td>
        </tr>

        <tr>
        <td>egress_security_rules</td>
        <td>
            <div>Rules for allowing egress IP packets</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'tcp-options': None, 'protocol': 'all', 'icmp-options': None, 'udp-options': None, 'destination': '0.0.0.0/0', 'is-stateless': None}]</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>Name assigned to the Security List during creation</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_security_list</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the Security List</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>lifecycle_state</td>
        <td>
            <div>The current state of the Security List</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the Security List was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>ingress_security_rules</td>
        <td>
            <div>Rules for allowing ingress IP packets</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'source': '0.0.0.0/0', 'protocol': '6', 'icmp-options': None, 'udp-options': None, 'tcp-options': {'destination-port-range': {'max': 22, 'min': 22}, 'source-port-range': None}, 'is-stateless': None}]</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Security List</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.securitylist.oc1.axdf</td>
        </tr>

        </table>
    </td>
    </tr>

    </table>
    </br>
    </br>


Notes
-----

.. note::
    - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html


Author
~~~~~~

    * Debayan Gupta(@debayan_gupta)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
