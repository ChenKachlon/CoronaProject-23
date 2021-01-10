from django.test import TestCase
from accounts.models import *


class Test_models(TestCase):

    @classmethod
    def setUpTestData(cls):
        Patient.objects.create()
        Bed.objects.create()
        Ventilator.objects.create()
        Concentration.objects.create()
        Equipment.objects.create()
        RequestForm.objects.create()
        ReportForm.objects.create()

    def test_patient_name(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')

    def test_patient_id(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('ID').verbose_name
        self.assertEqual(field_label,'ID')

    def test_patient_phone(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('phone').verbose_name
        self.assertEqual(field_label,'phone')

    def test_patient_status(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('status').verbose_name
        self.assertEqual(field_label,'status')

    def test_patient_need_ven(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('need_ven').verbose_name
        self.assertEqual(field_label,'need ven')

    def test_patient_date_created(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('date_created').verbose_name
        self.assertEqual(field_label,'date created')

    def test_bed_name_max_length(self):
        bed = Bed.objects.get(id=1)
        max_length = bed._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_bed_department_max_length(self):
        bed = Bed.objects.get(id=1)
        max_length = bed._meta.get_field('department').max_length
        self.assertEqual(max_length, 200)

    def test_bed_room_number(self):
        bed = Bed.objects.get(id=1)
        field_label = bed._meta.get_field('room_number').verbose_name
        self.assertEqual(field_label,'room number')

    def test_ven_name_max_length(self):
        ven = Ventilator.objects.get(id=1)
        max_length = ven._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_ven_department_max_length(self):
        ven = Bed.objects.get(id=1)
        max_length = ven._meta.get_field('department').max_length
        self.assertEqual(max_length, 200)

    def test_ven_room_number(self):
        ven = Ventilator.objects.get(id=1)
        field_label = ven._meta.get_field('room_number').verbose_name
        self.assertEqual(field_label,'room number')

    def test_ven_number(self):
        ven = Ventilator.objects.get(id=1)
        field_label = ven._meta.get_field('ventilator_number').verbose_name
        self.assertEqual(field_label,'ventilator number')

    def test_ven_date_created(self):
        ven = Ventilator.objects.get(id=1)
        field_label = ven._meta.get_field('date_created').verbose_name
        self.assertEqual(field_label,'date created')

    def test_concentration_name(self):
        concentration = Concentration.objects.get(id=1)
        field_label = concentration._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')

    def test_concentration_amount(self):
        concentration = Concentration.objects.get(id=1)
        field_label = concentration._meta.get_field('Amount').verbose_name
        self.assertEqual(field_label,'Amount')

    def test_equip_name_max_length(self):
        equip = Equipment.objects.get(id=1)
        max_length = equip._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_equip_department_max_length(self):
        equip = Equipment.objects.get(id=1)
        max_length = equip._meta.get_field('department').max_length
        self.assertEqual(max_length, 264)

    def test_equip_date_registered(self):
        equip = Equipment.objects.get(id=1)
        field_label = equip._meta.get_field('date_registered').verbose_name
        self.assertEqual(field_label,'date registered')

    def test_req_name_max_length(self):
        req = RequestForm.objects.get(id=1)
        max_length = req._meta.get_field('name').max_length
        self.assertEqual(max_length, 264)

    def test_req_request_max_length(self):
        req = RequestForm.objects.get(id=1)
        max_length = req._meta.get_field('request').max_length
        self.assertEqual(max_length, 264)

    def test_req_description_max_length(self):
        req = RequestForm.objects.get(id=1)
        max_length = req._meta.get_field('description').max_length
        self.assertEqual(max_length, 264)

    def test_req_date_registered(self):
        req = RequestForm.objects.get(id=1)
        field_label = req._meta.get_field('date_registered').verbose_name
        self.assertEqual(field_label,'date registered')

    def test_rep_name_max_length(self):
        rep = ReportForm.objects.get(id=1)
        max_length = rep._meta.get_field('name').max_length
        self.assertEqual(max_length, 264)

    def test_rep_choice_max_length(self):
        rep = ReportForm.objects.get(id=1)
        max_length = rep._meta.get_field('choice').max_length
        self.assertEqual(max_length, 264)

    def test_rep_department_max_length(self):
        rep = ReportForm.objects.get(id=1)
        max_length = rep._meta.get_field('department').max_length
        self.assertEqual(max_length, 264)

    def test_rep_description_max_length(self):
        rep = ReportForm.objects.get(id=1)
        max_length = rep._meta.get_field('description').max_length
        self.assertEqual(max_length, 264)

    def test_rep_date_registered(self):
        rep = ReportForm.objects.get(id=1)
        field_label = rep._meta.get_field('date_registered').verbose_name
        self.assertEqual(field_label,'date registered')








