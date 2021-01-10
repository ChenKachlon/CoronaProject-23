from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import *


class Test_urls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        log_in_url=reverse('login')
        print(resolve(log_in_url))
        self.assertEqual(resolve(log_in_url).func,loginPage)

    def test_register_url_is_resolved(self):
        register_url = reverse('register')
        print(resolve(register_url))
        self.assertEqual(resolve(register_url).func, registerPage)

    def test_logout_url_is_resolved(self):
        logout_url = reverse('logout')
        print(resolve(logout_url))
        self.assertEqual(resolve(logout_url).func, logoutUser)

    def test_home_url_is_resolved(self):
        home_url = reverse('home')
        print(resolve(home_url))
        self.assertEqual(resolve(home_url).func, home)

    def test_patients_url_is_resolved(self):
        patients_url = reverse('patients')
        print(resolve(patients_url))
        self.assertEqual(resolve(patients_url).func, patients)

    def test_beds_url_is_resolved(self):
        beds_url = reverse('beds')
        print(resolve(beds_url))
        self.assertEqual(resolve(beds_url).func, beds)

    def test_equipment_url_is_resolved(self):
        equipment_url = reverse('equipment')
        print(resolve(equipment_url))
        self.assertEqual(resolve(equipment_url).func, equipmentPage)

    def test_ventilators_url_is_resolved(self):
        vent_url = reverse('ventilators')
        print(resolve(vent_url))
        self.assertEqual(resolve(vent_url).func, ventilators)

    def test_add_patient_url_is_resolved(self):
        add_p_url = reverse('add_patient')
        print(resolve(add_p_url))
        self.assertEqual(resolve(add_p_url).func, addPatients)

    def test_add_bed_url_is_resolved(self):
        add_b_url = reverse('add_bed')
        print(resolve(add_b_url))
        self.assertEqual(resolve(add_b_url).func, addBeds)

    def test_add_ven_url_is_resolved(self):
        add_ven_url = reverse('add_ven')
        print(resolve(add_ven_url))
        self.assertEqual(resolve(add_ven_url).func, addVen)

    def test_add_eq_url_is_resolved(self):
        add_eq_url = reverse('add_equip')
        print(resolve(add_eq_url))
        self.assertEqual(resolve(add_eq_url).func, addEquipment)

    def test_create_request_url_is_resolved(self):
        creat_req_url = reverse('create_request')
        print(resolve(creat_req_url))
        self.assertEqual(resolve(creat_req_url).func, createRequest)

    def test_create_report_url_is_resolved(self):
        creat_rep_url = reverse('create_report')
        print(resolve(creat_rep_url))
        self.assertEqual(resolve(creat_rep_url).func,createReport)

    def test_request_report_url_is_resolved(self):
        req_rep_url = reverse('request_report')
        print(resolve(req_rep_url))
        self.assertEqual(resolve(req_rep_url).func, ReqANDRep)