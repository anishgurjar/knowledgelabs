from typing import Protocol, Dict, List, Type


class Notification(Protocol):
    def send(self, message: str) -> None:
        ...

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"{message} [SENT FROM EMAIL]")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"{message} [SENT FROM SMS]")

class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"{message} [SENT FROM PUSH]")

notificationRegistry: Dict[str, Notification] = {
    "email": EmailNotification,
    "sms": SMSNotification,
    "push": PushNotification
}

class NotificationFactory():

    _notificationType: Notification

    def createNotification(self, notificationRegistry: Dict[str, Notification], type: str):
        if type not in notificationRegistry:
            raise ValueError("no such value")
        return notificationRegistry[type]()

n1 = NotificationFactory()
sender = n1.createNotification(notificationRegistry, "email")
sender.send("hi my name is anish")
