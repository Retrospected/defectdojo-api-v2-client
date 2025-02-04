# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import djclient
from djclient.api.endpoints_api import EndpointsApi  # noqa: E501
from djclient.rest import ApiException


class TestEndpointsApi(unittest.TestCase):
    """EndpointsApi unit test stubs"""

    def setUp(self):
        self.api = djclient.api.endpoints_api.EndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_endpoints_create(self):
        """Test case for endpoints_create

        """
        pass

    def test_endpoints_delete(self):
        """Test case for endpoints_delete

        """
        pass

    def test_endpoints_generate_report(self):
        """Test case for endpoints_generate_report

        """
        pass

    def test_endpoints_list(self):
        """Test case for endpoints_list

        """
        pass

    def test_endpoints_partial_update(self):
        """Test case for endpoints_partial_update

        """
        pass

    def test_endpoints_read(self):
        """Test case for endpoints_read

        """
        pass

    def test_endpoints_update(self):
        """Test case for endpoints_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
