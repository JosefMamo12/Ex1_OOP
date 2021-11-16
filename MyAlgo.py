import math
import sys

from Building import Building
from Calls import Calls
from Elevator import Elevator

UP = 1
DOWN = -1


def calc_elevator_pos(elev: Elevator, call: Calls):
    if not elev.floor:
        return elev.pos
    time_different = call.time - elev.startingTime
    call_time = call.time
    elevator_time = call_time - time_different
    if elevator_time > elev.timeToEnd:
        current_floor = elev.floor[-1]
        return current_floor
    current_floor = elev.pos
    for nextFloor in elev.floor:
        tmp_time = calc_distance(elev, current_floor, nextFloor) * elev.STOP_TIME
        if tmp_time < time_different:
            time_different = time_different - tmp_time
            current_floor = nextFloor
        else:
            break
    if time_different < elev.STOP_TIME:
        return math.floor(current_floor)
    final_floor = current_floor + time_different / elev.speed
    return math.floor(final_floor)


def calc_distance(elev: Elevator, src, dest):
    return abs(src - dest) / elev.speed


def calc_time_to_end(elev: Elevator, c: Calls, pos: int) -> float:
    dist = calc_distance(elev, pos, c.src) + len(elev.floor) * elev.STOP_TIME + calc_distance(elev, c.src, c.dest)
    return dist


class MyAlgo:
    def __init__(self, building: Building, calls: list) -> None:
        self.building = building
        self.calls = calls

    def start_to_allocate(self):
        for c in self.calls:
            best_elev = self.building.elevs[0]
            bestElevDist = sys.maxsize
            for elev in self.building.elevs:
                pos = elev.pos = calc_elevator_pos(elev, c)
                if not elev.floor and not elev.pqUp and not elev.pqDown:  # Means the elevator is not busy
                    elevDistance = calc_distance(elev, elev.pos, c.src)
                    if elevDistance < bestElevDist:
                        bestElevDist = elevDistance
                        best_elev = elev
                        best_elev.flag = True

                else:  # This specific elevator is busy
                    if elev.startingTime <= c.time <= elev.timeToEnd:
                        if elev.dir == UP and elev.pos <= c.src:
                            best_elev = elev
                            break

                        elif elev.dir == DOWN and elev.pos >= c.src:
                            best_elev = elev
                            break
                        elif elev.dir == UP and elev.pos > c.src:
                            if elev.pqDown:
                                elevDistance = elev.calcAllQueue() + calc_distance(elev, elev.floor[0],
                                                                                   elev.floor[-1]) + calc_distance(
                                    elev, elev.pqDown[0], elev.pqDown[-1]) + len(
                                    elev.pqDown) * elev.WAIT_TIME + calc_distance(elev, elev.pqDown[-1], c.src)
                            else:
                                elevDistance = elev.calcAllQueue() + calc_distance(elev, elev.floor[0],
                                                                                   elev.floor[-1]) + calc_distance(
                                    elev.floor[-1], c.src)
                        else:
                            if elev.pqUp:
                                elevDistance = elev.calcAllQueue() + calc_distance(elev, elev.pos,
                                                                                   elev.floor[-1]) + calc_distance(
                                    elev, elev.pqUp[0], elev.pqUp[-1]) + len(
                                    elev.pqUp) * elev.WAIT_TIME + calc_distance(elev, elev.pqDown[-1], c.src)
                            else:
                                elevDistance = elev.calcAllQueue() + calc_distance(elev, elev.pos,
                                                                                   elev.floor[-1]) + calc_distance(elev, elev.floor[-1], c.src)
                        if bestElevDist > elevDistance:
                            bestElevDist = elevDistance
                            best_elev = elev

                    else:
                        elev.floor.clear()
                        elev.flag = False
                        elevDistance = calc_distance(elev, elev.pos, c.src)
                        if elevDistance < bestElevDist:
                            bestElevDist = elevDistance
                            best_elev = elev

            if best_elev.flag:
                best_elev.startingTime = c.time
                best_elev.flag = False
            best_elev.dir = c.state
            if best_elev.pos != c.src and c.src not in best_elev.floor:
                best_elev.floor.append(c.src)
            if c.dest not in best_elev.floor:
                best_elev.floor.append(c.dest)
            best_elev.timeToEnd = best_elev.startingTime + calc_time_to_end(best_elev, c, best_elev.pos)
            c.allocated_elev = best_elev.id - 1
