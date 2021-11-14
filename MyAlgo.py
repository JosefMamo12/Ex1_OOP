import math
import sys

from Building import Building
from Calls import Calls
from Elevator import Elevator


def calc_elevator_pos(elev, call):
    if len(elev.floor) == 0:
        return 0
    elevator_time = elev.elev_time
    call_time = call.time
    time_different = call_time - elevator_time
    current_floor = elev.floor[0]
    for nextFloor in elev.floor:
        if nextFloor != elev.pos:
            tmp_time = calc_distance(elev, current_floor, nextFloor)
            if tmp_time < time_different:
                time_different = tmp_time + elev.WAIT_TIME - time_different
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
            best_elev = self.building.elevs[0]
            best_time = sys.maxsize
            for elev in self.building.elevs:
                index = 0
                if not elev.floor:
                    temp_time = calc_distance(elev, elev.pos, call.src)
                    if temp_time < best_time:
                        best_time = temp_time
                        best_elev = elev

                else:
                    pos = calc_elevator_pos(elev, call)
                    if elev.dir == call.state:
                        if elev.dir == 1:
                            if pos <= call.src:
                                best_elev = elev
                                break
                        elif elev.dir == -1:
                            if pos >= call.src:
                                best_elev = elev
                                index += 1
                                break
                    else:
                        last_floor = elev.queue[-1]
                        temp_time = elev.calcAllQueue() + calc_distance(elev, last_floor, call.src)
                        if temp_time < best_time:
                            best_elev = elev
                            best_time = temp_time

            best_elev.dir = call.state
            best_elev.floor.append(call.src)
            best_elev.floor.append(call.dest)
            best_elev.pos = math.floor(calc_elevator_pos(best_elev, call))
            best_elev.floor_time = best_time
