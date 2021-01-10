from django.test import TestCase
from django.urls import reverse

from accounts.models import *

class ListViewTest(TestCase):

    def test_register_view_url_exists_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_login_view_url_exists_by_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    # def test_home_view_url_exists_by_name(self):
    #     response = self.client.get('')
    #     self.assertEqual(response.status_code, 200)

    # def test_department_view_url_exists_by_name(self):
    #     response = self.client.get(reverse("department"))
    #     self.assertEqual(response.status_code, 200)

    def test_add_patient_view_url_exists_by_name(self):
        response = self.client.get('/add_patient')
        self.assertEqual(response.status_code, 200)
    #
    # def test_patients_view_url_exists_at_desired_location(self):
    #     response = self.client.get(reverse("patients"))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_beds_view_url_exists_at_desired_location(self):
    #     response = self.client.get(reverse("beds"))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_ven_view_url_exists_at_desired_location(self):
    #     response = self.client.get(reverse("ventilators"))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_equip_view_url_exists_at_desired_location(self):
    #     response = self.client.get(reverse("equipment"))
    #     self.assertEqual(response.status_code, 200)

