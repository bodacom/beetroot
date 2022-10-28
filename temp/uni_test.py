import unittest

def square(n):
    return n * n

def cube(n):
    return n ** 3

class Tests(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(3), 9, 'Should be 9')

    def test_cube(self):
        self.assertEqual(cube('abc'), 8, 'Should be 8')

if __name__ == '__main__':
    unittest.main()
