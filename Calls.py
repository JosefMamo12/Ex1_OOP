from csv import reader, writer


class Calls:
    def __init__(self, name, time, src, dest, allocated_elev):
        self.name = name
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.allocated_elev = int(allocated_elev)
        if self.src > self.dest:
            self.state = -1
        else:
            self.state = 1

    def __repr__(self) -> str:
        str = "{},  {}, {}, {} , {}, {}".format(self.name, self.time,
                                                self.src, self.dest,
                                                self.state,
                                                self.allocated_elev)

        return str
