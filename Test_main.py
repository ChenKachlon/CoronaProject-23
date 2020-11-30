import unittest
import main

class test_main(unittest.TestCase):
    def test_ConvertToStr(self):
        self.assertIsInstance(main.ConvertToStr(322, 289), str, "The function ConvertToStr don't return a str")

    def test_amount_of_beds_in_given_hospital(self):
         self.assertEqual(main.amount_of_beds_in_given_hospital(),main.ws_beds.max_row-2,"The DB and the function are not syncing")
         self.assertNotEqual(main.amount_of_beds_in_given_hospital(),main.ws_beds.max_row,"The DB and the function are not syncing")
         self.assertNotEqual(main.amount_of_beds_in_given_hospital(),main.ws_beds.max_row-4,"The DB and the function are not syncing")

    def test_amount_of_beds_in_given_department(self):
         self.assertEqual(main.amount_of_beds_in_given_department(),main.ws_beds.max_row-main.Sub_Amounts_Beds()-2)
         self.assertEqual(main.amount_of_beds_in_given_department(),main.ws_beds.max_row-main.Sub_Amounts_Beds()-2)
         self.assertNotEqual(main.amount_of_beds_in_given_department(),main.ws_beds.max_row-main.Sub_Amounts_Beds())

    def test_amount_of_patients_in_given_hospital(self):
        self.assertEqual(main.amount_of_patients_in_given_hospital(),main.ws.max_row-1,"The DB and the function are not syncing")
        self.assertNotEqual(main.amount_of_patients_in_given_hospital(),main.ws.max_row-4,"The DB and the function are not syncing")

    def test_amount_of_patients_in_given_department(self):
         self.assertEqual(main.amount_of_patients_in_given_department(),main.ws.max_row-main.Sub_Amounts_Patients()-1)
         self.assertEqual(main.amount_of_patients_in_given_department(),main.ws.max_row-main.Sub_Amounts_Patients()-1)
         self.assertNotEqual(main.amount_of_patients_in_given_department(),main.ws_beds.max_row-main.Sub_Amounts_Patients())


if __name__ == '__main__':
    unittest.main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
