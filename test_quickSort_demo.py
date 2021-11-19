from unittest import TestCase
from quickSort_demo import *


class Test(TestCase):
	
	def setUp(self) -> None:
		super().setUp()
		self.test = [748928, 44542, 55653, 67865, 346543, 45665467, 33, 2, 1, 224, 5, 6, 7]
	
	def test_quick_sort(self):
		t_1 = self.test
		t_2 = self.test
		# sorted(t_2)
		quickSort(t_1)
		# self.assertEqual(t_1, t_2)
