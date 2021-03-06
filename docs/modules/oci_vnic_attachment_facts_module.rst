.. _oci_vnic_attachment_facts:


oci_vnic_attachment_facts - Retrieve details about one or more VNIC attachments in the specified compartment
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves details about a VNIC attachment, or all VNIC attachments in a specified Compartment in OCI Compute Service. A VNIC attachment resides in the same compartment as the attached instance.



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
    <td>availability_domain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Availability Domain.</div>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the compartment (either the tenancy or another compartment in the tenancy). Required for retrieving information about all VNIC attachments in a Compartment/Tenancy, or a compute instance.</div>
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
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the instance to which a VNIC attachment is attached to. Required for retrieving information about all VNIC attachments of a compute instance.</div>
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
    <td>tenancy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
    </td>
    </tr>

    <tr>
    <td>vnic_attachment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the VNIC attachment. Required for retrieving information about a specific VNIC attachment</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get details of all the VNIC attachments in a specified compartment
      oci_vnic_attachment_facts:
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'

    - name: Get VNIC attachments of a specific instance
      oci_vnic_attachment_facts:
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
        instance_id: 'ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq'

    - name: Get details of a specific VNIC attachment
      oci_vnic_attachment_facts:
        id: 'ocid1.vnic.oc1..xxxxxEXAMPLExxxxx...vm62asdaxq'


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
    <td>vnic_attachments</td>
    <td>
        <div>Information about one or more VNIC attachments</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'DETACHED', 'availability_domain': 'BnQb:PHX-AD-1', 'display_name': 'sec_vnic_1_for_my_instance', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...wbvm62xq', 'subnet_id': 'ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...smpqpaoa', 'time_created': '2017-11-26T16:24:35.487000+00:00', 'instance_id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...qkwr6q', 'vnic_id': 'ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...v2beqa', 'vlan_tag': 41, 'id': 'ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx...b3momq'}]</td>
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
        <td>lifecycle_state</td>
        <td>
            <div>The current state of the VNIC attachment</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ATTACHED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain of the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>Uocm:PHX-AD-1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the image. It does not have to be unique, and it's changeable.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>sec-vnic1-to-instance1</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment  the VNIC attachment is in, which is the same compartment the instance is in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'</td>
        </tr>

        <tr>
        <td>subnet_id</td>
        <td>
            <div>The OCID of the VNIC's subnet.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the image was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the VNIC attachment</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...asdadv3qca</td>
        </tr>

        <tr>
        <td>instance_id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...asdgrrv3qca</td>
        </tr>

        <tr>
        <td>vnic_id</td>
        <td>
            <div>The OCID of the VNIC. Available after the attachment process is complete.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpasdadsaoa</td>
        </tr>

        <tr>
        <td>vlan_tag</td>
        <td>
            <div>The Oracle-assigned VLAN tag of the attached VNIC. Available after the attachment process is complete.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>0</td>
        </tr>

        <tr>
        <td>nic_index</td>
        <td>
            <div>The physical network interface card (NIC) the VNIC is using in a bare metal instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>0</td>
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

    * Sivakumar Thyagarajan (@sivakumart)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
