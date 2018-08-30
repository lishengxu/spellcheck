import unittest
from main.all_mail_info import *

class TestAllMailInfo(unittest.TestCase):

    def test_init(self):
        test = AllMailInfo('hello', 'world')
        self.assertEqual('hello', test.get_file())
        self.assertEqual('world', test.get_name())