import abc

from sandbox.location.location import Location


class LocationSelector:
    @abc.abstractmethod
    def check(self, location: Location) -> bool:
        pass
