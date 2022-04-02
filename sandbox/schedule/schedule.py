from sandbox.schedule.calendarevent import CalendarEvent


class Schedule:
    events: list[CalendarEvent] = []

    def add_event(self, event: CalendarEvent):
        self.events.append(event)

    def get_current_events(self, time: int) -> list[CalendarEvent]:
        events: list[CalendarEvent] = [
            e for e in self.events if e.timeframe.check(time)
        ]

        return events
