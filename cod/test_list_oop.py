import unittest


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    def __repr__(self):
        return repr((self.name, self.population, self.area))

class TestListOOP(unittest.TestCase):

    def setUp(self):
        self.countries = [
            Country('India', 1200, 100),
            Country('China', 1400, 200),
            Country('USA', 100, 300),
        ]
        # with self.assertRaises(IndexError):
        #     animals[3]

    def test_len(self):
        self.assertEqual(len(self.countries), 3)
        self.assertEqual(len(self.countries[0:1]), 1)
        self.assertEqual(self.countries[0:1][0].name, 'India')

    def test_sort(self):
        from operator import attrgetter
        self.countries.sort(key=attrgetter('population'))
        self.assertEqual(self.countries[0:1][0].name, 'USA')
        self.assertEqual(self.countries[1:2][0].name, 'India')
        self.assertEqual(self.countries[2:3][0].name, 'China')
        self.assertTrue(self.countries[0:1][0].population <= self.countries[1:2][0].population)
        self.assertTrue(self.countries[1:2][0].population <= self.countries[2:3][0].population)

    def test_sort_reverse(self):
        from operator import attrgetter
        self.countries.sort(key=attrgetter('population'), reverse=True)
        self.assertEqual(self.countries[0:1][0].name, 'China')
        self.assertEqual(self.countries[1:2][0].name, 'India')
        self.assertEqual(self.countries[2:3][0].name, 'USA')
        self.assertTrue(self.countries[0:1][0].population >= self.countries[1:2][0].population)
        self.assertTrue(self.countries[1:2][0].population >= self.countries[2:3][0].population)

    def test_max(self):
        from operator import attrgetter
        m = max(self.countries, key=attrgetter('population'))
        self.assertEqual(m.name, 'China')
        self.assertEqual(m.population, 1400)

    def test_min(self):
        from operator import attrgetter
        m = min(self.countries, key=attrgetter('area'))
        self.assertEqual(m.name, 'India')
        self.assertEqual(m.area, 100)


if __name__ == '__main__':
    unittest.main()