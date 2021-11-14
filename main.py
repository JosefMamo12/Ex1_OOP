import csv
import json
from _csv import reader

from Calls import Calls
from Building import Building
from MyAlgo import MyAlgo
import pathlib

call_file = r'C:\Users\yosim\PycharmProjects\Ex1\Ex1_Calls\BoazCalls.csv'


def create_call_list():
    calls = []
    try:
        with open(call_file, 'r') as csv_call_file:
            line = csv.reader(csv_call_file)
            for row in line:
                call = Calls(row[0], row[1], row[2], row[3], row[5])
                calls.append(call)
    except IOError as e:
        print(e)
    return calls


building_file = r'C:\Users\yosim\PycharmProjects\Ex1\Ex1_Buildings\B2.json'

b = Building(building_file)
c = create_call_list()
algo = MyAlgo(b, c)
algo.start_to_allocate()