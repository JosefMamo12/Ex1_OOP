import csv
import json
import sys
from csv import reader, writer

from Elevator import Elevator
from Calls import Calls
import sys

elevator_list = []


def minimum_time(call):
    mini = float('inf')
    index = 0
    for i in range(len(elevator_list)):
        if (mini > elevator_list[i].timeToArrive(call)):
            mini = elevator_list[i].timeToArrive((call))
            index = i
    return index


# Opening JSON file
building_file = open('Ex1_Buildings/B2.json')
# Opening CSV files
call_file = open('Ex1_Calls/Calls_a.csv', 'r')
all_calls = reader(call_file)
# returns JSON object as
# a dictionary
building_data = json.load(building_file)

# Creating the elevator class from the Building Json file
for value in building_data["_elevators"]:
    print(value)
    elevator_list.append(
        Elevator(value["_id"], value["_speed"], value["_minFloor"], value["_maxFloor"], value["_closeTime"],
                 value["_openTime"], value["_startTime"], value["_stopTime"]))
print(elevator_list)

# Iterate over calls file and compute to which call
# The best elevator will fit.

data = []
for line in all_calls:
    c = Calls(line[1], line[2], line[3])
    index = minimum_time(c)
    elevator_list[index].queue.append(c)
    list = ['Elevator Call', c.time, c.src, c.dest, 0, index]
    data.append(list)

with open('MyCalls.csv', 'w', newline='') as calls:
    writer = csv.writer(calls)
    for i in range(len(data)):
        writer.writerow(data[i])

# if elevator is empty when allocating move to source
# Closing file
building_file.close()
call_file.close()
