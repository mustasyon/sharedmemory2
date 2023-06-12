from datetime import datetime

class FPS:
    def __init__(self):
        # store the start time, end time, and total number of frames
        # that were examined between the start and end intervals
        self._start = datetime.now().timestamp()
        self._numFrames = 0
        self._elapsedTime = None
        self.fps = 0.0
    def start(self):
        # start the timer
        self._start = datetime.now().timestamp()
        return self
    def update(self):
        # increment the total number of frames examined during the
        # start and end intervals
        self._numFrames += 1
        self.elapsed()
        if(self._elapsedTime>5):
            self._start = datetime.now().timestamp()
            self.fps = self._numFrames / self._elapsedTime
            self._numFrames = 0
            print(f"self.fps:{self.fps}")
    def elapsed(self):
        # return the total number of seconds between the start and
        # end interval
        self._elapsedTime=datetime.now().timestamp()-self._start