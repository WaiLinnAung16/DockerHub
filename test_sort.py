import unittest
from bubble_sort import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def test_sort_by_age(self):
        data = [(1, "A", 30), (2, "B", 20), (3, "C", 40)]
        sorted_data = BubbleSort.sort(data, type="age")
        self.assertEqual(sorted_data, [(2, "B", 20), (1, "A", 30), (3, "C", 40)])

    def test_sort_by_id(self):
        data = [(2, "B", 20), (1, "A", 30), (3, "C", 40)]
        sorted_data = BubbleSort.sort(data, type="id")
        self.assertEqual(sorted_data, [(1, "A", 30), (2, "B", 20), (3, "C", 40)])

if __name__ == '__main__':
    unittest.main()
