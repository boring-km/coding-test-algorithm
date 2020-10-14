import time


class TimeCheck:
    def __init__(self):
        self.start_time, self.end_time = 0, 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        result_time = self.end_time - self.start_time
        print("time :", result_time)
