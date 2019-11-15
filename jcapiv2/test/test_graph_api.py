# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv2
from jcapiv2.api.graph_api import GraphApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestGraphApi(unittest.TestCase):
    """GraphApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.graph_api.GraphApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_graph_active_directory_associations_list(self):
        """Test case for graph_active_directory_associations_list

        List the associations of an Active Directory instance  # noqa: E501
        """
        pass

    def test_graph_active_directory_associations_post(self):
        """Test case for graph_active_directory_associations_post

        Manage the associations of an Active Directory instance  # noqa: E501
        """
        pass

    def test_graph_active_directory_traverse_user(self):
        """Test case for graph_active_directory_traverse_user

        List the Users bound to an Active Directory instance  # noqa: E501
        """
        pass

    def test_graph_active_directory_traverse_user_group(self):
        """Test case for graph_active_directory_traverse_user_group

        List the User Groups bound to an Active Directory instance  # noqa: E501
        """
        pass

    def test_graph_application_associations_list(self):
        """Test case for graph_application_associations_list

        List the associations of an Application  # noqa: E501
        """
        pass

    def test_graph_application_associations_post(self):
        """Test case for graph_application_associations_post

        Manage the associations of an Application  # noqa: E501
        """
        pass

    def test_graph_application_traverse_user(self):
        """Test case for graph_application_traverse_user

        List the Users bound to an Application  # noqa: E501
        """
        pass

    def test_graph_application_traverse_user_group(self):
        """Test case for graph_application_traverse_user_group

        List the User Groups bound to an Application  # noqa: E501
        """
        pass

    def test_graph_command_associations_list(self):
        """Test case for graph_command_associations_list

        List the associations of a Command  # noqa: E501
        """
        pass

    def test_graph_command_associations_post(self):
        """Test case for graph_command_associations_post

        Manage the associations of a Command  # noqa: E501
        """
        pass

    def test_graph_command_traverse_system(self):
        """Test case for graph_command_traverse_system

        List the Systems bound to a Command  # noqa: E501
        """
        pass

    def test_graph_command_traverse_system_group(self):
        """Test case for graph_command_traverse_system_group

        List the System Groups bound to a Command  # noqa: E501
        """
        pass

    def test_graph_g_suite_associations_list(self):
        """Test case for graph_g_suite_associations_list

        List the associations of a G Suite instance  # noqa: E501
        """
        pass

    def test_graph_g_suite_associations_post(self):
        """Test case for graph_g_suite_associations_post

        Manage the associations of a G Suite instance  # noqa: E501
        """
        pass

    def test_graph_g_suite_traverse_user(self):
        """Test case for graph_g_suite_traverse_user

        List the Users bound to a G Suite instance  # noqa: E501
        """
        pass

    def test_graph_g_suite_traverse_user_group(self):
        """Test case for graph_g_suite_traverse_user_group

        List the User Groups bound to a G Suite instance  # noqa: E501
        """
        pass

    def test_graph_ldap_server_associations_list(self):
        """Test case for graph_ldap_server_associations_list

        List the associations of a LDAP Server  # noqa: E501
        """
        pass

    def test_graph_ldap_server_associations_post(self):
        """Test case for graph_ldap_server_associations_post

        Manage the associations of a LDAP Server  # noqa: E501
        """
        pass

    def test_graph_ldap_server_traverse_user(self):
        """Test case for graph_ldap_server_traverse_user

        List the Users bound to a LDAP Server  # noqa: E501
        """
        pass

    def test_graph_ldap_server_traverse_user_group(self):
        """Test case for graph_ldap_server_traverse_user_group

        List the User Groups bound to a LDAP Server  # noqa: E501
        """
        pass

    def test_graph_office365_associations_list(self):
        """Test case for graph_office365_associations_list

        List the associations of an Office 365 instance  # noqa: E501
        """
        pass

    def test_graph_office365_associations_post(self):
        """Test case for graph_office365_associations_post

        Manage the associations of an Office 365 instance  # noqa: E501
        """
        pass

    def test_graph_office365_traverse_user(self):
        """Test case for graph_office365_traverse_user

        List the Users bound to an Office 365 instance  # noqa: E501
        """
        pass

    def test_graph_office365_traverse_user_group(self):
        """Test case for graph_office365_traverse_user_group

        List the User Groups bound to an Office 365 instance  # noqa: E501
        """
        pass

    def test_graph_policy_associations_list(self):
        """Test case for graph_policy_associations_list

        List the associations of a Policy  # noqa: E501
        """
        pass

    def test_graph_policy_associations_post(self):
        """Test case for graph_policy_associations_post

        Manage the associations of a Policy  # noqa: E501
        """
        pass

    def test_graph_policy_traverse_system(self):
        """Test case for graph_policy_traverse_system

        List the Systems bound to a Policy  # noqa: E501
        """
        pass

    def test_graph_policy_traverse_system_group(self):
        """Test case for graph_policy_traverse_system_group

        List the System Groups bound to a Policy  # noqa: E501
        """
        pass

    def test_graph_radius_server_associations_list(self):
        """Test case for graph_radius_server_associations_list

        List the associations of a RADIUS  Server  # noqa: E501
        """
        pass

    def test_graph_radius_server_associations_post(self):
        """Test case for graph_radius_server_associations_post

        Manage the associations of a RADIUS Server  # noqa: E501
        """
        pass

    def test_graph_radius_server_traverse_user(self):
        """Test case for graph_radius_server_traverse_user

        List the Users bound to a RADIUS  Server  # noqa: E501
        """
        pass

    def test_graph_radius_server_traverse_user_group(self):
        """Test case for graph_radius_server_traverse_user_group

        List the User Groups bound to a RADIUS  Server  # noqa: E501
        """
        pass

    def test_graph_system_associations_list(self):
        """Test case for graph_system_associations_list

        List the associations of a System  # noqa: E501
        """
        pass

    def test_graph_system_associations_post(self):
        """Test case for graph_system_associations_post

        Manage associations of a System  # noqa: E501
        """
        pass

    def test_graph_system_group_associations_list(self):
        """Test case for graph_system_group_associations_list

        List the associations of a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_associations_post(self):
        """Test case for graph_system_group_associations_post

        Manage the associations of a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_member_of(self):
        """Test case for graph_system_group_member_of

        List the System Group's parents  # noqa: E501
        """
        pass

    def test_graph_system_group_members_list(self):
        """Test case for graph_system_group_members_list

        List the members of a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_members_post(self):
        """Test case for graph_system_group_members_post

        Manage the members of a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_membership(self):
        """Test case for graph_system_group_membership

        List the System Group's membership  # noqa: E501
        """
        pass

    def test_graph_system_group_traverse_command(self):
        """Test case for graph_system_group_traverse_command

        List the Commands bound to a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_traverse_policy(self):
        """Test case for graph_system_group_traverse_policy

        List the Policies bound to a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_traverse_user(self):
        """Test case for graph_system_group_traverse_user

        List the Users bound to a System Group  # noqa: E501
        """
        pass

    def test_graph_system_group_traverse_user_group(self):
        """Test case for graph_system_group_traverse_user_group

        List the User Groups bound to a System Group  # noqa: E501
        """
        pass

    def test_graph_system_member_of(self):
        """Test case for graph_system_member_of

        List the parent Groups of a System  # noqa: E501
        """
        pass

    def test_graph_system_traverse_command(self):
        """Test case for graph_system_traverse_command

        List the Commands bound to a System  # noqa: E501
        """
        pass

    def test_graph_system_traverse_policy(self):
        """Test case for graph_system_traverse_policy

        List the Policies bound to a System  # noqa: E501
        """
        pass

    def test_graph_system_traverse_user(self):
        """Test case for graph_system_traverse_user

        List the Users bound to a System  # noqa: E501
        """
        pass

    def test_graph_system_traverse_user_group(self):
        """Test case for graph_system_traverse_user_group

        List the User Groups bound to a System  # noqa: E501
        """
        pass

    def test_graph_user_associations_list(self):
        """Test case for graph_user_associations_list

        List the associations of a User  # noqa: E501
        """
        pass

    def test_graph_user_associations_post(self):
        """Test case for graph_user_associations_post

        Manage the associations of a User  # noqa: E501
        """
        pass

    def test_graph_user_group_associations_list(self):
        """Test case for graph_user_group_associations_list

        List the associations of a User Group.  # noqa: E501
        """
        pass

    def test_graph_user_group_associations_post(self):
        """Test case for graph_user_group_associations_post

        Manage the associations of a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_member_of(self):
        """Test case for graph_user_group_member_of

        List the User Group's parents  # noqa: E501
        """
        pass

    def test_graph_user_group_members_list(self):
        """Test case for graph_user_group_members_list

        List the members of a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_members_post(self):
        """Test case for graph_user_group_members_post

        Manage the members of a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_membership(self):
        """Test case for graph_user_group_membership

        List the User Group's membership  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_active_directory(self):
        """Test case for graph_user_group_traverse_active_directory

        List the Active Directories bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_application(self):
        """Test case for graph_user_group_traverse_application

        List the Applications bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_directory(self):
        """Test case for graph_user_group_traverse_directory

        List the Directories bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_g_suite(self):
        """Test case for graph_user_group_traverse_g_suite

        List the G Suite instances bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_ldap_server(self):
        """Test case for graph_user_group_traverse_ldap_server

        List the LDAP Servers bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_office365(self):
        """Test case for graph_user_group_traverse_office365

        List the Office 365 instances bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_radius_server(self):
        """Test case for graph_user_group_traverse_radius_server

        List the RADIUS Servers bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_system(self):
        """Test case for graph_user_group_traverse_system

        List the Systems bound to a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_traverse_system_group(self):
        """Test case for graph_user_group_traverse_system_group

        List the System Groups bound to User Groups  # noqa: E501
        """
        pass

    def test_graph_user_member_of(self):
        """Test case for graph_user_member_of

        List the parent Groups of a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_active_directory(self):
        """Test case for graph_user_traverse_active_directory

        List the Active Directory instances bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_application(self):
        """Test case for graph_user_traverse_application

        List the Applications bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_directory(self):
        """Test case for graph_user_traverse_directory

        List the Directories bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_g_suite(self):
        """Test case for graph_user_traverse_g_suite

        List the G Suite instances bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_ldap_server(self):
        """Test case for graph_user_traverse_ldap_server

        List the LDAP servers bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_office365(self):
        """Test case for graph_user_traverse_office365

        List the Office 365 instances bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_radius_server(self):
        """Test case for graph_user_traverse_radius_server

        List the RADIUS Servers bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_system(self):
        """Test case for graph_user_traverse_system

        List the Systems bound to a User  # noqa: E501
        """
        pass

    def test_graph_user_traverse_system_group(self):
        """Test case for graph_user_traverse_system_group

        List the System Groups bound to a User  # noqa: E501
        """
        pass

    def test_policystatuses_list(self):
        """Test case for policystatuses_list

        List the policy statuses for a system  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
