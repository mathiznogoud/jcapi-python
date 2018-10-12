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
from jcapiv2.api.radius_servers_api import RADIUSServersApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestRADIUSServersApi(unittest.TestCase):
    """RADIUSServersApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.radius_servers_api.RADIUSServersApi()  # noqa: E501

    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()
