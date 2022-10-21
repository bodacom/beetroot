import unittest
import functions_2


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = functions_2.get_daily_movie()
        licensed_movies = functions_2.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)
    
    def test_wifi_status(self):
        wifi_enabled = functions_2.get_wifi_status()
        self.assertTrue(wifi_enabled)



if __name__ == '__main__':
    unittest.main()
