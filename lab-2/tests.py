from Calendar import Calendar
import unittest


class TestCalendar(unittest.TestCase):
    def test_optimize(self):
        test_list = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        calendar = Calendar(test_list)
        calendar.optimize()
        self.assertEqual(calendar.output_list, [(0, 1), (3, 8), (9, 12)])

    def test_empty(self):
        calendar = Calendar([])
        calendar.optimize()
        self.assertEqual(calendar.output_list, [])


if __name__ == '__main__':
    unittest.main()
