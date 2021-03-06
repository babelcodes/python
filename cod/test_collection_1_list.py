import unittest


class TestList(unittest.TestCase):

    def setUp(self):
        self.numbers0to5 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
        self.numbers0to9 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    def test_create(self):
        marks = [23, 56, 67]
        self.assertEqual(marks, [23, 56, 67])

    def test_create_with_range(self):
        numbers = range(1, 6)
        self.assertEqual(numbers, [1, 2, 3, 4, 5])

    def test_create_with_function(self):
        squares = [ i*i for i in range(1, 6) ]
        self.assertEqual(squares, [1, 4, 9, 16, 25])

    def test_type(self):
        self.assertEqual(type([1, 2, 3]),  list)
        self.assertTrue(type([1, 2, 3]) is list)

    def test_slicing__get(self):
        """Lower bound is included, Upper bound is exluded."""
        animals = ['cat', 'dog', 'elephant']
        self.assertEqual(animals[0], 'cat')
        self.assertEqual(animals[2], 'elephant')
        with self.assertRaises(IndexError):
            animals[3]
        self.assertEqual(self.numbers0to9[2], 'Two')
        self.assertEqual(self.numbers0to9[2:6], ['Two', 'Three', 'Four', 'Five']) # Lower bound included,  Upper bound is exluded
        self.assertEqual(self.numbers0to9[ :6], ['Zero', 'One', 'Two', 'Three', 'Four', 'Five'])
        self.assertEqual(self.numbers0to9[3: ], ['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'])
        self.assertEqual(self.numbers0to9[1:8:2], ['One', 'Three', 'Five', 'Seven'])
        self.assertEqual(self.numbers0to9[1:8:3], ['One', 'Four', 'Seven'])
        self.assertEqual(self.numbers0to9[ : :3], ['Zero', 'Three', 'Six', 'Nine'])
        self.assertEqual(self.numbers0to9[ : :-1], ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero'])
        self.assertEqual(self.numbers0to9[ : :-3], ['Nine', 'Six', 'Three', 'Zero'])

    def test_slicing__delete(self):
        """Lower bound is included, Upper bound is exluded."""
        numbers = [] + self.numbers0to9
        del numbers[3:]
        self.assertEqual(numbers, ['Zero', 'One', 'Two'])
        numbers = [] + self.numbers0to9
        del numbers[5:7]
        self.assertEqual(numbers, ['Zero', 'One', 'Two', 'Three', 'Four', 'Seven', 'Eight', 'Nine'])

    def test_slicing__replace(self):
        """Lower bound is included, Upper bound is exluded."""
        self.numbers0to9[3:7] = [3, 4, 5, 6]
        self.assertEqual(self.numbers0to9, ['Zero', 'One', 'Two', 3, 4, 5, 6, 'Seven', 'Eight', 'Nine'])

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
        self.assertEqual(len(self.numbers0to9), 10)

    def test_reverse(self):
        # array not modified, new array
        numbers = [] + self.numbers0to5
        self.assertEqual(numbers[ : :-1], ['Five', 'Four', 'Three', 'Two', 'One', 'Zero'])
        # array modified
        numbers = [] + self.numbers0to5
        self.assertEqual(numbers.reverse(), None)
        self.assertEqual(numbers, ['Five', 'Four', 'Three', 'Two', 'One', 'Zero'])
        # array not modified, new iterator
        numbers = [] + self.numbers0to5
        result = ''
        for n in reversed(numbers):
            result += n
        self.assertEqual(result, 'FiveFourThreeTwoOneZero')

    def test_sort(self):
        # array modified
        numbers = [] + self.numbers0to9
        self.assertEqual(numbers.sort(), None)
        self.assertEqual(numbers, ['Eight', 'Five', 'Four', 'Nine', 'One', 'Seven', 'Six', 'Three', 'Two', 'Zero'])
        # array modified, with key
        numbers = [] + self.numbers0to9
        self.assertEqual(numbers.sort(key=len), None)
        self.assertEqual(numbers, ['One', 'Two', 'Six', 'Zero', 'Four', 'Five', 'Nine', 'Three', 'Seven', 'Eight'])
        # array modified, with key and reverse
        numbers = [] + self.numbers0to9
        self.assertEqual(numbers.sort(key=len, reverse=True), None)
        self.assertEqual(numbers, ['Three', 'Seven', 'Eight', 'Zero', 'Four', 'Five', 'Nine', 'One', 'Two', 'Six'])
        # array not modified, new iterator
        numbers = [] + self.numbers0to9
        result = ''
        for n in sorted(numbers):
            result += n + ' '
        self.assertEqual(result, 'Eight Five Four Nine One Seven Six Three Two Zero ')
        # array not modified, new iterator with key
        numbers = [] + self.numbers0to9
        result = ''
        for n in sorted(numbers, key=len):
            result += n + ' '
        self.assertEqual(result, 'One Two Six Zero Four Five Nine Three Seven Eight ')
        # array not modified, new iterator with key and reverse
        result = ''
        for n in sorted(([] + self.numbers0to9), key=len, reverse=True):
            result += n + ' '
        self.assertEqual(result, 'Three Seven Eight Zero Four Five Nine One Two Six ')

    def test_stack_filo(self):
        numbers = []
        numbers.append(1)
        numbers.append(2)
        numbers.append(3)
        numbers.append(4)
        self.assertEqual(numbers, [1, 2, 3, 4])
        self.assertEqual(numbers.pop(), 4)
        self.assertEqual(numbers, [1, 2, 3])
        self.assertEqual(numbers.pop(), 3)
        self.assertEqual(numbers, [1, 2])
        numbers.append(33)
        self.assertEqual(numbers, [1, 2, 33])
        self.assertEqual(numbers.pop(), 33)
        self.assertEqual(numbers, [1, 2])

    def test_queue_fifo(self):
        numbers = []
        numbers.append(1)
        numbers.append(2)
        numbers.append(3)
        numbers.append(4)
        self.assertEqual(numbers, [1, 2, 3, 4])
        self.assertEqual(numbers.pop(0), 1)
        self.assertEqual(numbers, [2, 3, 4])
        self.assertEqual(numbers.pop(0), 2)
        self.assertEqual(numbers, [3, 4])
        numbers.append(33)
        self.assertEqual(numbers, [3, 4, 33])
        self.assertEqual(numbers.pop(0), 3)
        self.assertEqual(numbers, [4, 33])

    def test_list_comprehension(self):
        numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
        self.assertEqual([len(number) for number in numbers], [4, 3, 3, 5, 4, 4])
        self.assertEqual([number.upper() for number in numbers], ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'])
        self.assertEqual([ number for number in numbers if len(number)==4 ], ['Zero', 'Four', 'Five'])
        values = [3, 6, 9, 1, 4, 15, 6, 3]
        self.assertEqual([ value for value in values if value%2==1 ], [3, 9, 1, 15, 3])


if __name__ == '__main__':
    unittest.main()