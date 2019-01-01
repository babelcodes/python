import unittest


class TestTuple(unittest.TestCase):
    """Several values separated by a coma, immutable"""

    def setUp(self):
        pass
        # self.occurances = dict(a=5, b=6, c=8)

    def test_create(self):
        """With or without parentheses"""
        ranga = 'Ranga', 1981, 'India'
        self.assertEqual(ranga, ('Ranga', 1981, 'India'))
        ranga = ('Ranga', 1981, 'India')
        self.assertEqual(ranga, ('Ranga', 1981, 'India'))

    def test_create__withOneValue(self):
        a_value = (1)
        self.assertTrue(type(a_value) is int)
        a_tuple = (1,)
        self.assertTrue(type(a_tuple) is tuple)

    def test_type(self):
        ranga = 'Ranga', 1981, 'India'
        self.assertEqual(type(ranga), tuple)
        self.assertTrue(type(ranga) is tuple)

    def test_get(self):
        ranga = 'Ranga', 1981, 'India'
        #
        self.assertEqual(ranga[0], 'Ranga')
        self.assertEqual(ranga[1], 1981)
        self.assertEqual(ranga[2], 'India')
        #
        name, year, country = ranga
        self.assertEqual(name, 'Ranga')
        self.assertEqual(year, 1981)
        self.assertEqual(country, 'India')
        with self.assertRaises(ValueError):  # ValueError: too many values to unpack
            first, second = ranga
        # Swipe values
        a, b = 1, 2
        a, b = b, a
        self.assertEqual(a, 2)
        self.assertEqual(b, 1)

    def test_set(self):
        """Not possible as tuples are not mutable"""
        ranga = 'Ranga', 1981, 'India'
        with self.assertRaises(TypeError):  # TypeError: 'tuple' object does not support item assignment
            ranga[1] = 15

    def test_len(self):
        ranga = 'Ranga', 1981, 'India'
        self.assertEqual(len(ranga), 3)
