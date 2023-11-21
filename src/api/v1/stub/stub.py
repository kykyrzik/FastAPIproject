from typing import Callable, Any


class Stub:
    """
    https://gist.github.com/Tishka17/9b2625753c80681e8ba688c84d834bb6
    It's fabric, with calling Class and returning bool

    """
    def __init__(self, dependency: Callable, **kwargs):
        self._dependency = dependency
        self._kwargs = kwargs

    def __call__(self):
        raise NotImplementedError

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Stub):
            return (self._dependency == other._dependency
                    and self._kwargs == other._kwargs
                    )
        else:
            if not self._kwargs:
                return self._dependency == other
            return False

    def __hash__(self):
        if not self._kwargs:
            return hash(self._dependency)
        serial = (self._dependency, *self._kwargs.items())
        return hash(serial)
