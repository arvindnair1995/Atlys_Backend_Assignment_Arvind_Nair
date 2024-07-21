from typing import Dict, List

from notification.base import BaseNotification


class NotificationService:
    
    def __init__(self, notifier: BaseNotification):
        self.notifier = notifier


    def send_notification(self, message: str):
        self.notifier.notify(message)
