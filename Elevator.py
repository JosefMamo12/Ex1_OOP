from Calls import Calls


class Elevator:
    def __repr__(self) -> str:
        return "ID: " + str(self.id) + ", Speed: " + str(self.speed)

    def __init__(self, value):
        self.id = int(value['_id'])
        self.speed = float(value['_speed'])
        self.minFloor = int(value['_minFloor'])
        self.maxFloor = int(value['_maxFloor'])
        self.closeTime = float(value['_closeTime'])
        self.openTime = float(value['_openTime'])
        self.startTime = float(value['_startTime'])
        self.stopTime = float(value['_stopTime'])
        self.avg_floor = (self.minFloor + self.maxFloor) / 2
        self.queue = []
        self.time = float(0)

    def time_to_arrive(self, c: Calls):
        time = 0
        time += (self.openTime + self.closeTime) * 2
        # if the call dest isnt the current floor add the travel time
        if self.avg_floor != c.src:
            time += self.startTime + self.stopTime + abs(self.avg_floor - c.src) / self.speed
        # add the travel time to dest
        time += self.startTime + self.stopTime + abs(c.src - c.dest) / self.speed
        if not self.time < c.time:  # if the call doesn't happens after the current elevator queue will finish
            time += c.time  # add to time the difference
        return time

