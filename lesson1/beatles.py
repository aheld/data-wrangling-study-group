# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
#import os


#
#  Three different example approaches
#


def parse_file1(DATAFILE):
    data = []
    index = []
    with open(DATAFILE, "rb") as f:
        for i in range(11):
            line = f.readline()
            data.append(line.strip().replace('\xe2\x80\x94', '-').split(','))
            f.next

    index = data[0]
    d = []
    for i in data[1:11]:
        d.append(dict(zip(index, i)))
    #print d
    return d


def parse_file2(datafile):
    data = []
    titles = "Title,Released,Label,UK Chart Position,US Chart Position,\
BPI Certification,RIAA Certification".split(',')
    with open(datafile, "rb") as f:
        for line in f:
            data.append(dict(zip(titles,
                                 line.
                                 strip().
                                 replace('\xe2\x80\x94', '-').
                                 split(','))))
            if len(data) > 11:
                break
    data.pop(0)

    return data


def parse_file(DATAFILE):
    with open(DATAFILE, "r") as f:
        titles = f.readline().strip().split(',')

        def get_ten_rows():
            for x in range(10):
                line = f.readline()
                yield line.strip().replace('\xe2\x80\x94', '-').split(',')

        data = [dict(zip(titles, row)) for row in get_ten_rows()]
    return data
