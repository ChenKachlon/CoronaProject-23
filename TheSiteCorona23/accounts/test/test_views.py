from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from accounts.models import *

class ListViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.user = User.objects.create_user('john','lennon@thebeatles.com' ,'johnpassword')

    def test_register_view_url_exists_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_login_view_url_exists_by_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_add_patient_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('add_patient'))
        self.assertEqual(response.status_code,200)

    def test_add_bed_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('add_bed'))
        self.assertEqual(response.status_code,200)

    def test_add_ven_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('add_ven'))
        self.assertEqual(response.status_code,200)

    def test_add_Equipment_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('add_equip'))
        self.assertEqual(response.status_code,200)

    def test_create_request_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('create_request'))
        self.assertEqual(response.status_code,200)

    def test_create_report_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('create_report'))
        self.assertEqual(response.status_code,200)

    def test_patients_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('patients'))
        self.assertEqual(response.status_code,302)

    def test_beds_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('beds'))
        self.assertEqual(response.status_code,302)

    def test_ventilators_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('ventilators'))
        self.assertEqual(response.status_code,302)

    def test_equipment_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('equipment'))
        self.assertEqual(response.status_code,302)

    def test_req_rep_view_url_exists_by_name(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('request_report'))
        self.assertEqual(response.status_code, 302)