from Calls import Calls


class Elevator:
    def __repr__(self) -> str:
        return "ID: " + str(self.id) + ", Speed: " + str(self.speed)

    def __init__(self, elevator_data):
        self.id = int(elevator_data['_id'])
        self.speed = float(elevator_data['_speed'])
        self.minFloor = int(elevator_data['_minFloor'])
        self.maxFloor = int(elevator_data['_maxFloor'])
        self.closeTime = float(elevator_data['_closeTime'])
        self.openTime = float(elevator_data['_openTime'])
        self.startTime = float(elevator_data['_startTime'])
        self.stopTime = float(elevator_data['_stopTime'])

        self.WAIT_TIME = self.stopTime + self.startTime + self.closeTime + self.openTime
        self.floor = []
        self.dir = 0
        self.pos = int(0)
        self.elev_time = 0
        self.nextFloor = 0

    # Calculate the distance include stops
    def calcAllQueue(self) -> float:
        dif = abs(self.floor[0] - self.floor[-1])
        return dif / self.speed + len(self.floor) * (self.startTime + self.stopTime + self.closeTime + self.openTime)
