#!/usr/bin/env python3
""" Module for testing client """

import json
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    Test that GithubOrgClient.org returns the correct value
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        GithubOrgClient(input).org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
