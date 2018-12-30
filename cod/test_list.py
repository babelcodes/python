import unittest


class TestList(unittest.TestCase):

    def test_create(self):
        marks = [23, 56, 67]
        self.assertEqual(marks, [23, 56, 67])

    def test_sum(self):
        self.assertEqual(sum([23, 56, 67]), 146)

    def test_min(self):
        self.assertEqual(min([23, 56, 67]), 23)

    def test_max(self):
        self.assertEqual(max([23, 56, 67]), 67)

    def test_append(self):
        marks = [23, 56, 67]
        self.assertEqual(marks.append(76), None)
        self.assertEqual(marks, [23, 56, 67, 76])

    def test_insert(self):
        marks = [23, 56, 67]
        self.assertEqual(marks.insert(2, 60), None)
        self.assertEqual(marks, [23, 56, 60, 67])

    def test_remove(self):
        marks = [23, 56, 67]
        self.assertEqual(marks.remove(56), None)
        self.assertEqual(marks, [23, 67])

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


if __name__ == '__main__':
    unittest.main()