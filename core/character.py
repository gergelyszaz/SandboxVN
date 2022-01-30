class Character:
    _habits = []
    _events = []
    
    _map
    _activeEvent
    _location

    def ReplaneDay(self):
        pass

    def Update(self, time):
        self._activeEvent = self.GetPriorityEvent(time)
        self.ProcessEvent(self._activeEvent)
        pass

    def GetPriorityEvent(self, time):    
        # filter by time, order by priority
        # find first reachable

        #TODO
        return None

    def ProcessEvent(self, event):
        #TODO

        # if current place == event destination, do action
        # if current place != event destination, go to destination

        pass

    def Move(self, destionation):
        # find shortest route between location and destination
        # move to next node
        # update map with the information from current node
        pass

    def ExtendMap(self, map):
        pass
