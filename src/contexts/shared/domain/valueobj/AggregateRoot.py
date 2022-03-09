from abc import abstractmethod, ABC
from typing import Dict, List, Union

from src.contexts.shared.domain.DomainEvent import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self._domain_events: List[DomainEvent] = []

    @abstractmethod
    def to_primitives(self) -> Union[Dict, List]:
        raise NotImplementedError()

    def pull_domain_events(self):
        events = self._domain_events
        self._domain_events = []
        return events

    def record_event(self, event: DomainEvent):
        self._domain_events.append(event)
