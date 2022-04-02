import abc


class Character:
    @abc.abstractmethod
    def update(self, time: int) -> None:
        raise NotImplementedError
