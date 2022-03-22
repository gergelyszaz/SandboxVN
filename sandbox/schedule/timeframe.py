class TimeFrame:
    start: int
    end: int

    def check(self, time: int) -> bool:
        return time >= self.start and time <= self.end
