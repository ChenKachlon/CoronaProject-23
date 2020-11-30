import unittest
import Main

class test_Main(unittest.TestCase):
    def test_ConvertToStr(self):
        self.assertIsInstance(Main.ConvertToStr(322, 289), str, "The function ConvertToStr don't return a str")

    def test_amount_of_beds_in_given_hospital(self):
         self.assertEqual(Main.amount_of_beds_in_given_hospital(),Main.ws_beds.max_row-2,"The DB and the function are not syncing")
         self.assertNotEqual(Main.amount_of_beds_in_given_hospital(),Main.ws_beds.max_row,"The DB and the function are not syncing")
         self.assertNotEqual(Main.amount_of_beds_in_given_hospital(),Main.ws_beds.max_row-4,"The DB and the function are not syncing")

    def test_amount_of_beds_in_given_department(self):
        self.assertEqual(Main.amount_of_beds_in_given_department(),Main.ws_beds.max_row-39)
        self.assertEqual(Main.amount_of_beds_in_given_department(),Main.ws_beds.max_row-13)
        self.assertNotEqual(Main.amount_of_beds_in_given_department(),Main.ws_beds.max_row-12)

    def test_amount_of_patients_in_given_hospital(self):
        self.assertEqual(Main.amount_of_patients_in_given_hospital(),Main.ws.max_row-1,"The DB and the function are not syncing")
        self.assertNotEqual(Main.amount_of_patients_in_given_hospital(),Main.ws.max_row-4,"The DB and the function are not syncing")

    def test_amount_of_patients_in_given_department(self):
         self.assertEqual(Main.amount_of_beds_in_given_department(),Main.ws.max_row-39)
         self.assertEqual(Main.amount_of_beds_in_given_department(),Main.ws.max_row-13)
         self.assertNotEqual(Main.amount_of_beds_in_given_department(),Main.ws_beds.max_row-12)


if __name__ == '__main__':
    unittest.main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
