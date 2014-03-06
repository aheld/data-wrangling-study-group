#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min and max values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""
import datetime

import xlrd
from zipfile import ZipFile


def open_zip(datafile):
    with ZipFile('{0}'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    #print sheet_data
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    #exceltime = sheet.cell_value(1, 0)
    #print "Time in Excel format:",
    #print exceltime
    #print "Convert time to a Python datetime tuple, from the Excel float:",
    #print xlrd.xldate_as_tuple(exceltime, 0)

    # *******************
    # load all the data and key it by date, then send back just the requested date
    # *******************

    def get_data():
        for rownum in range(1, sheet.nrows):
            silly_excel_date = sheet.cell_value(rownum, 0)
            better_python_tuple = xlrd.xldate_as_tuple(silly_excel_date, 0)
            best_python_date = datetime.datetime(*better_python_tuple)

            #range(1,9) gives [1,2,3,4,5,6,7,8]
            loads = [sheet.cell_value(rownum, col) for col in range(1, 9)]

            data = {
                'maxtime': better_python_tuple,
                'maxvalue': max(loads),
                'minvalue': min(loads),
                'avgcoast': sum(loads) / float(len(loads))
            }
            yield (best_python_date, data)

    data = {date: data for date, data in get_data()}
    return data[datetime.datetime(2013, 8, 13, 17, 0, 0)]
