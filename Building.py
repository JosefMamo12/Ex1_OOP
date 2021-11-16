import json
from Elevator import Elevator


class Building:

    def __init__(self, building_file):
        try:
            with open(building_file, 'r') as f:
                building = json.load(f)
                self.minFloor = building['_minFloor']
                self.maxFloor = building['_maxFloor']
                self.elevs = []
                for elev_dict in building['_elevators']:
                    elev = Elevator(elev_dict)
                    self.elevs.append(elev)
        except IOError as e:
            print(e)

    def toString(self):
        st = "minFloor = {} maxFloor = {} ".format(self.minFloor, self.maxFloor)
        st += "elevators = {"
        for elev in self.elevators:
            st += elev.toString()
        return st + "}"
