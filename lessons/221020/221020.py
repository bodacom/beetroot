# import unittest
# #import function

# class Cl(unittest.TestCase):
    
#     def test_func(self):
#         self.assertEqual(12, 12)

# unittest.main()

# destinations = {
#   'BUD': 'Budapest',
#   'CMN': 'Casablanca',
#   'IST': 'Istanbul'
# }
# print('Welcome to Small World Airlines!')
# print('What is the airport code of your travel destination?')
# destination = 'HND'


# # Write your code below: 
# assert destination in destinations, 'Sorry, Small World Air currently does not fly to this destination'
# city_name = destinations[destination]
# print('Great! Retrieving information for your flight to ...' + city_name)

import unittest
import functions


class NearestExitTest(unittest.TestCase):

    def test_row_1(self):
        self.assertEqual(functions.get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
    
    def test_row_20(self):
        self.assertEqual(functions.get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
        
    def test_row_40(self):
      	self.assertEqual(functions.get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


if __name__ == '__main__':
    unittest.main()
