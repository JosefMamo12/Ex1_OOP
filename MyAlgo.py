import sys

from Building import Building
from Calls import Calls
from Elevator import Elevator


def calc_elevator_pos(elev, call):
    if len(elev.queue) == 0:
        return 0
    elevator_time = elev.queue_time
    call_time = call.time
    time_different = call_time - elevator_time
    if elev.dir == 1:
        current_floor = elev.queue[0]
    elif elev.dir == -1:
        current_floor = elev.queue[-1]
    for nextFloor in elev.queue:
        tmp_time = calc_distance(elev, current_floor, nextFloor)
        if tmp_time < time_different:
            time_different = time_different - (tmp_time + elev.WAIT_TIME)
            current_floor = nextFloor
        else:
            break
        final_floor = current_floor + time_different / elev.speed
        return final_floor


def calc_distance(elev, src, dest):
    return abs(src - dest) / elev.speed


class MyAlgo:
    def __init__(self, building: Building, calls: list) -> None:
        self.building = building
        self.calls = calls

    def start_to_allocate(self):
        for call in self.calls:
            best_elev = self.building.elev[0]
            best_time = sys.maxsize
            for elev in self.building.elev:
                index = 0
                if not elev.queue:
                    temp_time = calc_distance(elev, elev.pos, call.src)
                    if temp_time < best_time:
                        best_time = temp_time
                        best_elev = elev
                        break

                pos = calc_elevator_pos(elev, call)
            if elev.dir == call.state:
                if elev.dir == 1:
                    if pos <= call.src:
                        best_elev = elev
                        break
                elif elev.dir == -1:
                    if pos >= call.src:
                        best_elev = elev
                        break
            else:
                last_floor = elev.queue[-1]
                temp_time = elev.calcAllQueue() + calc_distance(elev, last_floor, call.src)
                if temp_time < best_time:
                    best_elev = elev
                    best_time = temp_time

            best_elev.queue.add(call.src)
