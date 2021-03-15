from rest_framework.test import APITestCase

from core.models import Department


class DemoTests(APITestCase):
    def setUp(self) -> None:
        self.department = Department.objects.create(department_name='Chemistry')

    def test_create_class(self):
        url = "/api/classes/"

        payload = {
            "department": self.department.id,
            "class_name": "Chemistry 101"
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
