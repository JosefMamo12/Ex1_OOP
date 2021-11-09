from Calls import Calls


class Elevator:
    def __repr__(self) -> str:
        return "ID: " + str(self.id) + ", Speed: " + str(self.speed)

    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.id = int(id)
        self.speed = float(speed)
        self.minFloor = int(minFloor)
        self.maxFloor = int(maxFloor)
        self.closeTime = float(closeTime)
        self.openTime = float(openTime)
        self.startTime = float(startTime)
        self.stopTime = float(stopTime)
        self.queue = []
        self.pos = 0
        self.state = 0

    def timeToArrive(self, call):
        time = 0
        time += (self.openTime + self.closeTime) * 2
        if self.pos != call.src:
            time += self.startTime + self.stopTime + abs(self.pos - call.src) / self.speed
        time += self.startTime + self.stopTime + abs(call.src - call.dest) / self.speed
        return time
