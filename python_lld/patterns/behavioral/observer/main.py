from typing import Protocol, Type

class Observer(Protocol):

    def update(self, event) -> None:
        ...

class Observable(Protocol):

    _observers: list[Observer]

    def attach(self, observer: Observer) -> None:
        ...
    
    def detach(self, observer: Observer) -> None:
        ...
    
    def notify(self, event: str) -> None:
        ...

class OrderTracker(Observable):

    _observers: list[Observer]

    def __init__(self, *observers: Observer) -> None:
        self._observers = list(observers)
    
    def attach(self, *observers: Observer) -> None:
        self._observers += list(observers)

    def detach (self, *observers: Observer) -> None:
        self._observers = [obs for obs in self._observers if obs not in observers ]

    def notify(self, event: str):
        for obs in self._observers:
            obs.update(event)


class EmailNotifier(Observer):

    _event: str

    def update(self, event: str)->None:
        self._event = event
    
    def getEvent(self) -> None:
        print(f"EMAIL Notifier - {self._event}")

class SMSNotifier(Observer):
    _event: str
    def update(self, event: str)->None:
        self._event = event
    
    def getEvent(self) -> None:
        print(f"SMS Notifier - {self._event}")

class AnalyticsService(Observer):
    _event: str
    def update(self, event: str)->None:
        self._event = event
    
    def getEvent(self) -> None:
        print(f"Analytics Service - {self._event}")


#================main-===================

email = EmailNotifier()
sms = SMSNotifier()
analytics = AnalyticsService()

ordertracker = OrderTracker(email, sms, analytics)
ordertracker.notify("PLACED")
email.getEvent()
sms.getEvent()
analytics.getEvent()

ordertracker.notify("PACKED")
email.getEvent()
sms.getEvent()
analytics.getEvent()

ordertracker.detach(email)
ordertracker.notify("SHIPPED")
email.getEvent()
sms.getEvent()
analytics.getEvent()