class TimeFrame:
    start: int
    end: int

    def check(self, time: int) -> bool:
        return self.start <= time <= self.end
