import unittest


class TestSet(unittest.TestCase):
    """A set do not contains duplicate"""

    def setUp(self):
        self._1_2_3_4_5_ = set(range(1, 6))
        self._4_5_6_7_8_9_10_ = set(range(4, 11))

    def test_create(self):
        numbers_list = [1, 2, 1, 3, 2]
        numbers_set = set(numbers_list)
        self.assertEqual(numbers_set, {1, 2, 3})
        #
        numbers_set = set([1, 2, 3])
        self.assertEqual(numbers_set, {1, 2, 3})
        #
        numbers_set = {1, 2, 3}
        self.assertEqual(numbers_set, {1, 2, 3})
        #
        numbers_set = {}
        self.assertTrue(type(numbers_set) is dict)
        with self.assertRaises(AttributeError):
            numbers_set.add(2)

    def test_create_with_range(self):
        numbers = set(range(1, 6))
        self.assertEqual(numbers, {1, 2, 3, 4, 5})

    def test_type(self):
        self.assertEqual(type({1, 2, 3}),  set)
        self.assertTrue(type({1, 2, 3}) is set)

    def test_add(self):
        numbers = set()
        numbers.add(3)
        numbers.add(4)
        numbers.add(0)
        numbers.add(4)
        self.assertEqual(numbers, {0, 3, 4})

    def test_remove(self):
        numbers = {1, 2, 3}
        numbers.add(4)
        self.assertEqual(numbers.remove(2), None)
        self.assertEqual(numbers, {1, 3, 4})

    def test_get(self):
        numbers = {1, 2, 3}
        with self.assertRaises(TypeError): # 'set' object does not support indexing
            numbers[0]

    def test_in(self):
        self.assertTrue(1 in {1, 2, 3})
        self.assertTrue(9 not in {1, 2, 3})

    def test_min(self):
        self.assertEqual(min({1, 2, 3}), 1)

    def test_max(self):
        self.assertEqual(max({1, 2, 3}), 3)

    def test_sum(self):
        self.assertEqual(sum({1, 2, 3}), 6)

    def test_len(self):
        self.assertEqual(len({1, 2, 3}), 3)

    def test_plus(self):
        with self.assertRaises(TypeError): # unsupported operand type(s) for +: 'set' and 'set'
            self._1_2_3_4_5_ + self._4_5_6_7_8_9_10_

    def test_union(self):
        self.assertEqual(self._1_2_3_4_5_ | self._4_5_6_7_8_9_10_, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

    def test_intersection(self):
        self.assertEqual(self._1_2_3_4_5_ & self._4_5_6_7_8_9_10_, {4, 5})

    def test_minus(self):
        self.assertEqual(self._1_2_3_4_5_ - self._4_5_6_7_8_9_10_, {1, 2, 3})
        self.assertEqual(self._4_5_6_7_8_9_10_ - self._1_2_3_4_5_, {6, 7, 8, 9, 10})
