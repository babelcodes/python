import unittest


class TestDict(unittest.TestCase):
    """A dictionary (or hashmap) is a class for key / value representation"""

    def setUp(self):
        pass
        self.occurances = dict(a=5, b=6, c=8)

    def test_create(self):
        self.assertEqual(self.occurances, dict(a=5, b=6, c=8))

    def test_type(self):
        self.assertEqual(type(self.occurances), dict)
        self.assertTrue(type(self.occurances) is dict)

    def test_get(self):
        self.assertEqual(self.occurances['c'], 8)
        with self.assertRaises(KeyError):  # KeyError: 'd'
            self.occurances['d']
        # safe access
        self.assertEqual(self.occurances.get('c'), 8)
        self.assertEqual(self.occurances.get('e'), None)
        self.assertEqual(self.occurances.get('e', 'some default value'), 'some default value')

    def test_set(self):
        self.occurances['d'] = 15
        self.occurances['c'] = 1
        self.assertEqual(self.occurances, dict(a=5, b=6, c=1, d=15))

    def test_delete(self):
        del self.occurances['a']
        self.assertEqual(self.occurances, dict(b=6, c=8))

    def test_keys(self):
        self.assertEqual(self.occurances.keys(), ['a', 'c', 'b'])

    def test_values(self):
        self.assertEqual(self.occurances.values(), [5, 8, 6])

    def test_items(self):
        """Returns key/value pairs as tuples"""
        self.assertEqual(self.occurances.items(), [('a', 5), ('c', 8), ('b', 6)])
        result = ''
        for (key, value) in self.occurances.items():
            result += key + "/" + str(value) + " "
        self.assertEqual(result, 'a/5 c/8 b/6 ')
