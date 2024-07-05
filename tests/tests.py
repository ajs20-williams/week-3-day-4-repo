import sys
sys.path.append('..') # imports python file from parent directory

from unittest.mock import patch
import unittest


from is_weekday import get_famous_birthdays
from requests.exceptions import Timeout



class TestIsWeekday(unittest.TestCase):

  def test_get_famous_birthdays_timeout(self):
    @patch('is_weekday.requests')  # patches, or imitates, the requests module in `is_weekday.py`
    def test_get_famous_birthdays_timeout(self, mock_requests): #define a new parameter to pass the mock request object into our test
      mock_requests.get.side_effect = Timeout  #configure our mock object                    
      with self.assertRaises(Timeout):
        get_famous_birthdays()

if __name__ == '__main__':
  unittest.main()
    
