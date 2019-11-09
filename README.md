SLE Compliance Checker
======================

Until approximately the middle of 2019 it was possible to accidentally loose the billing meter information in AWS when creating a custom image from an on-demand
image or running instance. The problem was addressed in the AWS infrastructure such that an accidental drop of the billing construct is no longer possible.

The change in AWS is effective on a going forward basis only and therefore it is possible that instances are running that are not in compliance with the SLE usage policy. The policy requires that any instance accessing the SUSE operated update infrastructure is an on-demand instance with the proper billing construct.

The slecompliancereport code will inspect all running instances in an account for compliance to the use policy. In addition the compliance checker will warn if the code that is responsible for the connection between the update infrastructure and the running instance is outdated and needs to be updated in order to ensure proper access to the update infrastructure once strict access controls are enabled server side. All warnings about out dated client code must be fixed in order to ensure continued access to the update infrastructure after access rules are enforced.
