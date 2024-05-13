#!/usr/bin/env python3

"""
TestGithubOrgClient module
"""

import unittest
from parameterized import parameterized_class
from unittest.mock import patch
from fixtures import TEST_ORG_PAYLOAD, TEST_REPOS_PAYLOAD, EXPECTED_REPOS, APACHE2_REPOS
from client import GithubOrgClient


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (TEST_ORG_PAYLOAD, TEST_REPOS_PAYLOAD, EXPECTED_REPOS, APACHE2_REPOS)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            MockResponse(cls.org_payload),
            MockResponse(cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method
        """
        github_client = GithubOrgClient("testorg")
        repos = github_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with a specific license
        """
        github_client = GithubOrgClient("testorg")
        repos = github_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


class MockResponse:
    """
    MockResponse class
    """

    def __init__(self, payload):
        """
        Initialize MockResponse
        """
        self.payload = payload

    def json(self):
        """
        Return JSON payload
        """
        return self.payload


if __name__ == '__main__':
    unittest.main()
