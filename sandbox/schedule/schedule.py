from asyncio import events
from typing import List
from sandbox.schedule.calendarevent import CalendarEvent
class Schedule:
    events: List[CalendarEvent]

    def addEvent(self, event: CalendarEvent):
        self.events.append(event)

    def getCurrentEvents(self, time: int) -> List[CalendarEvent]:
        return [e for e in events if e.timeframe.check(time)].sort(key="priority", reverse=True)
