# Overview

This sample shows how you can enable internet access from compute instances in 
a private subnet, using a NAT instance in a public subnet as discussed 
[here](https://blogs.oracle.com/cloud-infrastructure/automate-deployment-nat-instance-in-oracle-cloud-infrastructure-with-terraform) and [the whitepaper here](https://cloud.oracle.com/opc/iaas/whitepapers/nat_instance_configuration.pdf) through OCI ansible cloud modules.

The sample 
- sets up the topology described in the whitepaper by creating the VCN,
the Internet Gateway, the public and private subnets, and the necessary
security lists and route rules. A NAT instance is provisioned in the
public subnet and a private instance is provisioned in the private
subnet. 
- After the setup, the private instance would have outbound internet access
through the NAT instance in the public subnet.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI 
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`. 

Note: The sample, by default, sets up the topology, prints an information message, 
runs a few tests to show it is working, and tears down the topology. If you want
to experiment with the topology after it is setup, comment out the invocation 
to `teardown.yaml` at the end of `sample.yaml`.
