import json
from Elevator import Elevator


class Building:
    def __init__(self, maxFloor, minFloor):
        self.maxFloor = maxFloor
        self.minFloor = minFloor
        self.elev = []

    def getBuilding(self, building_file):
        with open(building_file, 'r') as f:
            building_data = json.load(f)
        for value in building_data["_elevators"]:
            Elevator(value)
