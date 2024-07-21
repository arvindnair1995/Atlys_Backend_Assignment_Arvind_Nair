from notification.base import BaseNotification


class ConsoleNotification(BaseNotification):
    
    def notify(self, message: str):
        print(message)
