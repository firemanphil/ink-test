#!/usr/bin/env python
import unittest
from berlin_clock import convert_to_berlin_clock_string
class TestBerlinClock(unittest.TestCase):
    
    def test_lunchtime(self):
        result = convert_to_berlin_clock_string('13:17:01')
        self.assertEqual(result,'13:17:01 O RROO RRRO YYROOOOOOOO YYOO')

    def test_just_before_midnight(self):
        result = convert_to_berlin_clock_string('23:59:59')
        self.assertEqual(result,'23:59:59 O RRRR RRRO YYRYYRYYRYY YYYY')

    def test_midnight_version_1(self):
        result = convert_to_berlin_clock_string('24:00:00')
        self.assertEqual(result,'24:00:00 Y RRRR RRRR OOOOOOOOOOO OOOO')

    def test_midnight_version_2(self):
        result = convert_to_berlin_clock_string('00:00:00')
        self.assertEqual(result,'00:00:00 Y OOOO OOOO OOOOOOOOOOO OOOO')
if __name__ == '__main__':
    unittest.main()
