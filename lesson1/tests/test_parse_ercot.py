import parse_ercot
from nose.tools import *

zipfile = "tests/2013_ERCOT_Hourly_Load_Data.zip"
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def test_ercot():
    #parse_ercot.open_zip(zipfile)
    data = parse_ercot.parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    eq_(round(data['maxvalue'], 10), round(18779.02551, 10))
