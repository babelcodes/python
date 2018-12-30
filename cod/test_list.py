import unittest


class TestList(unittest.TestCase):

    def test_create(self):
        marks = [23, 56, 67]
        self.assertEqual(marks, [23, 56, 67])

    def test_get(self):
        animals = ['cat', 'dog', 'elephant']
        self.assertEqual(animals[0], 'cat')
        self.assertEqual(animals[2], 'elephant')
        with self.assertRaises(IndexError):
            animals[3]

    def test_sum(self):
        self.assertEqual(sum([23, 56, 67]), 146)
        with self.assertRaises(TypeError):
            sum(['cat', 'dog', 'elephant'])

    def test_min(self):
        self.assertEqual(min([23, 56, 67]), 23)

    def test_max(self):
        self.assertEqual(max([23, 56, 67]), 67)

    def test_append(self):
        marks = [23, 56, 67]
        self.assertEqual(marks.append(76), None)
        self.assertEqual(marks, [23, 56, 67, 76])
        marks.append('animal') # No type restriction
        self.assertEqual(marks, [23, 56, 67, 76, 'animal'])

    def test_insert(self):
        marks = [23, 56, 67]
        self.assertEqual(marks.insert(2, 60), None)
        self.assertEqual(marks, [23, 56, 60, 67])

    def test_extend(self):
        animals = ['cat', 'dog', 'elephant']
        self.assertEqual(animals.extend('fish'), None)
        self.assertEqual(animals, ['cat', 'dog', 'elephant', 'f', 'i', 's', 'h'])
        self.assertEqual(animals.extend(['chicken', 'bird']), None)
        self.assertEqual(animals, ['cat', 'dog', 'elephant', 'f', 'i', 's', 'h', 'chicken', 'bird'])

    def test_plus(self):
        animals = ['cat', 'dog', 'elephant']
        with self.assertRaises(TypeError): # TypeError: can only concatenate list (not "str") to list
            animals + 'fish'
        self.assertEqual(animals + ['chicken', 'bird'], ['cat', 'dog', 'elephant', 'chicken', 'bird'])
        animals += ['chicken', 'bird']
        self.assertEqual(animals, ['cat', 'dog', 'elephant', 'chicken', 'bird'])

    def test_remove__byElement(self):
        marks = [23, 56, 67]
        self.assertEqual(marks.remove(56), None)
        self.assertEqual(marks, [23, 67])

    def test_del__byIndex(self):
        animals = ['cat', 'dog', 'elephant']
        del animals[1]
        self.assertEqual(animals, ['cat', 'elephant'])

    def test_in(self):
        self.assertFalse(55 in [23, 56, 67])
        self.assertTrue(56 in [23, 56, 67])

    def test_index(self):
        self.assertEqual([23, 56, 67].index(56), 1)
        with self.assertRaises(ValueError):
            [23, 56, 67].index(55)

    def test_for(self):
        sum = 0
        for mark in [23, 56, 67]:
            sum += mark
        self.assertEqual(sum, 146)

    def test_len(self):
        self.assertEqual(len(['cat', 'dog', 'elephant']), 3)


if __name__ == '__main__':
    unittest.main()