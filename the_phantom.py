import unittest
from splinter import Browser


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = Browser('phantomjs')
        self.browser.visit('http://google.com')

    def test_check_title(self):
        assert self.browser.title == 'Google'

if __name__ in ('main', '__main__'):
    unittest.main()
