

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):

    def test_add_num(self):
        res = calc.add(4,5)

        self.assertEqual(res,9)

