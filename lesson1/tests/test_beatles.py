import os

from beatles import *

import unittest

DATADIR = "tests"
DATAFILE = "beatles-diskography.csv"


class BeatlesTest(unittest.TestCase):
    def test(self):
        # a simple test of your implemetation
        datafile = os.path.join(DATADIR, DATAFILE)
        firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1',
                     'Label': 'Parlophone(UK)', 'Released': '22 March 1963',
                     'US Chart Position': '-',
                     'RIAA Certification': 'Platinum',
                     'BPI Certification': 'Gold'}
        tenthline = {'Title': '', 'UK Chart Position': '1',
                     'Label': 'Parlophone(UK)',
                     'Released': '10 July 1964', 'US Chart Position': '-',
                     'RIAA Certification': '',
                     'BPI Certification': 'Gold'}

        d = parse_file(datafile)
        assert d[0] == firstline
        assert d[9] == tenthline

        d = parse_file1(datafile)
        self.assertTrue(d[0] == firstline)
        self.assertTrue(d[9] == tenthline)

        d = parse_file2(datafile)
        self.assertEqual(d[0], firstline)
        self.assertEqual(d[9], tenthline)
