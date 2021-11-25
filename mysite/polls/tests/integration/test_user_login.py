from rest_framework.test import APIClient
from polls.tests.base_test import NewTestCase


class UserLoginTestCase(NewTestCase):
    r"""Login functionality and check if a user is successfully getting logged"""
    def setUp(self) -> None:
        super().setUp()

    def test_user_login(self):
        client = APIClient()
        result = client.post("/admin/auth/user/add/",
                             {"username": self.username, "password": self.password},
                             format="json")
        self.assertEquals(result.status_code, 200)
        self.assertTrue("access" in result.json())
        self.assertEquals("refresh" in result.json())

    def tearDown(self) -> None:
        self.client.logout()
        super().tearDown()
