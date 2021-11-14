from csv import reader, writer


class Calls:
    def __init__(self, name, time, src, dest, allocated_elev):
        self.name = name
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.allocated_elev = allocated_elev
        if src > dest:
            self.state = -1
        else:
            self.call_state = 1


