import unittest
import base_sort

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.sorted_arr = [1, 2, 3, 4, 5]
        self.one_out_order = [1, 2, 3, 5, 4]
        self.two_out_order = [2, 1, 3, 5, 4] 
    def test_sort_iteration(self):
        result = base_sort.sort_iteration(self.two_out_order)
        self.assertEqual(result, self.one_out_order)
    def test_is_sorted_positive(self):
        result = base_sort.is_sorted(self.sorted_arr)
        self.assertTrue(result)
    def test_is_sorted_negative(self):
        result = base_sort.is_sorted(self.one_out_order)
        self.assertFalse(result)
    def test_get_first_sorted_positive(self):
        one_sorted_arr = [self.one_out_order, self.two_out_order, self.sorted_arr]
        result = base_sort.get_first_sorted(one_sorted_arr)
        self.assertEqual(result, self.sorted_arr)
    def test_get_first_sorted_negative(self):
        one_sorted_arr = [self.one_out_order, self.two_out_order]
        result = base_sort.get_first_sorted(one_sorted_arr)
        self.assertEqual(result, [])
        
    def test_main(self):
        result = base_sort.main(self.two_out_order)
        self.assertEqual(result, self.sorted_arr)
    def test_main_empty(self):
        result = base_sort.main([])
        self.assertEqual(result, [])
              
if __name__ == '__main__':
    unittest.main()