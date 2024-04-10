#!/usr/bin/env python3
"""
Module for testing client
"""

import json
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class

from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)


class TestGithubOrgClient(unittest.TestCase):
    """
    Test that GithubOrgClient.org returns the correct value
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mock: MagicMock) -> None:
        """Tests the `org` method."""
        mock.return_value = MagicMock(return_value=resp)
        self.assertEqual(GithubOrgClient(org).org(), resp)
        mock.assert_called_once_with("https://api.github.com/orgs/{}".format(org))
