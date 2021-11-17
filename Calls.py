class Calls:
    def __init__(self, name, time, src, dest, state, allocated_elev):
        self.name = name
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.state = int(state)
        self.allocated_elev = int(allocated_elev)


def __repr__(self) -> str:
    str = "{},  {}, {}, {} , {}, {}".format(self.name, self.time,
                                            self.src, self.dest,
                                            self.state,
                                            self.allocated_elev)

    return str
