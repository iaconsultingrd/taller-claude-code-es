import unittest

from itbis import calcular_itbis, desglosar_itbis, total_con_itbis


class TestItbis(unittest.TestCase):
    def test_calcular_itbis(self):
        self.assertEqual(calcular_itbis(1000), 180.0)

    def test_total_con_itbis(self):
        self.assertEqual(total_con_itbis(1000), 1180.0)

    def test_desglosar_itbis(self):
        self.assertEqual(desglosar_itbis(1180), {"base": 1000.0, "itbis": 180.0})


if __name__ == "__main__":
    unittest.main()
