from typing import Protocol

class Notification(Protocol):
    def send(message:str) -> None:
        ...

class EmailNotification(Notification):
    def send(message:str) -> None:
        print("message sent from email")
    
class SMSNotification(Notification):
    def send(message:str) -> None:
        print("message sent from sms")

class PushNotification(Notification):
    def send(message:str) -> None:
        print("message sent from push")


class NotifcationFactory:

    #simple hardcoded if else statement. decent factory but does violate open closed principle.
    
    def create_notification(self, channel: str):
        
        _notification_channel: Notification

        if(channel == "email"):
            self.notification_channel = EmailNotification()
        
        elif(channel == "sms"):
            self.notification_channel = SMSNotification()
        
        elif(channel == "push"):
            self.notification_channel = PushNotification()

        raise ValueError("Unknown Channel")
    
    def send(self, message:str):
        self.notification_channel.send(message)

factory = NotifcationFactory()
n1 = factory.create_notification("email")
n1.send("hi there")