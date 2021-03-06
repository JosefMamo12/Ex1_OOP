import csv
import json


from Calls import Calls
from Elevator import Elevator
import sys



elevator_list = []
all_calls = []
output = []


def handle_files(building_file, csv_file):
    try:
        with open(csv_file, 'r+') as csv_call_file:
            line = csv.reader(csv_call_file)
            for row in line:
                call = Calls(row[0], row[1], row[2], row[3], row[4], row[5])
                all_calls.append(call)
    except IOError as e:
        print(e)
    # Opening JSON file
    try:
        with open(building_file, 'r+') as f:
            building_data = json.load(f)
        for value in building_data["_elevators"]:
            print(value)
            elevator_list.append(
                Elevator(value))
    except IOError as e:
        print(e)


def minimum_time(call):
    mini = float('inf')
    min_index = 0
    for i in range(len(elevator_list)):
        tta = elevator_list[i].time_to_arrive(call)
        if mini > tta:
            mini = tta
            min_index = i
    elevator_list[min_index].time += mini
    return min_index


# allocate calls by using a greedy algorithm:
def allocate_calls():
    for c in all_calls:  # for each call
        index = minimum_time(c)  # get the elevator with the mininaml total time
        elevator_list[index].queue.append(c)  # put the call in the elevator
        output.append(['Elevator Call', c.time, c.src, c.dest, 0, index])


def create_output_file(output_file):
    with open(output_file, 'w', newline='') as calls:
        writer = csv.writer(calls)
        for i in range(len(output)):
            writer.writerow(output[i])


if __name__ == '__main__':
    building_file = sys.argv[1]
    call_file = sys.argv[2]
    out_file = sys.argv[3]
    handle_files(building_file, call_file)
    allocate_calls()
    create_output_file(out_file)

