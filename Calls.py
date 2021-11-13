from csv import reader, writer


class Calls:
    def __init__(self, time, src, dest):
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        if src > dest:
            self.call_state = -1
        else:
            self.call_state = 1

    def getCalls(self, calls_file):
        my_calls = []
        index = 0
        with open(calls_file, 'r') as call_file:
            all_calls = reader(call_file)
        for call in all_calls:
            my_calls[index] = Calls(call[1], call[2], call[3])
            index = index + 1
