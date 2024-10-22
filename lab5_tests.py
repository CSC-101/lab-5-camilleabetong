import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        t1 = data.Time(0, 59, 50)
        t2 = data.Time(0, 0, 20)
        result = lab5.time_add(t1, t2)
        expected = data.Time(1, 0,10)
        self.assertEqual(result,expected)

    def test_time_add2(self):
        t1 = data.Time(0, 43, 70)
        t2 = data.Time(1, 0, 15)
        result = lab5.time_add(t1, t2)
        expected = data.Time(1, 44,25)
        self.assertEqual(result,expected)

    # Part 4
    def test_descending(self):
        list1 = [4,3,2,1]
        result = lab5.is_descending(list1)
        expected = True
        self.assertEqual(result,expected)

    def test_descending2(self):
        list1 = [1,2,3,4]
        result = lab5.is_descending(list1)
        expected = False
        self.assertEqual(result,expected)

    # Part 5
    def test_largest(self):
        list1 = [1,6,3,2,7]
        result = lab5.largest_between(list1,0,3)
        expected = 1
        self.assertEqual(result,expected)

    def test_largest2(self):
        list1 = [1,6,3,2,7]
        result = lab5.largest_between(list1,0,4)
        expected = 4
        self.assertEqual(result,expected)

    def test_largest3(self):
        list1 = [1,6,3,2,7]
        result = lab5.largest_between(list1,4,0)
        expected = None
        self.assertEqual(result,expected)

    # Part 6
    def test_origin(self):
        points = [data.Point(1, 1), data.Point(3, 4), data.Point(-5, -5)]
        result = lab5.furthest_from_origin(points)
        expected = 2
        self.assertEqual(result,expected)

    def test_origin2(self):
        points = []
        result = lab5.furthest_from_origin(points)
        expected = None
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
