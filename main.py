import csv

from Calls import Calls
from Building import Building
from MyAlgo import MyAlgo

calls = []
if __name__ == '__main__':
    building = Building.getBuilding('Ex1_Buildings/B2.json')
    calls = Calls.getCalls('BoazCall')
    MyAlgo(building, calls)

# Opening CSV files

# Output to file
with open('MyCalls.csv', 'w', newline='') as calls:
    calls_writer = csv.writer(calls)
    for i in range(len(data)):
        calls_writer.writerow(data[i])


