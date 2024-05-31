from abc import ABC, abstractmethod

class NotificationObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailNotification(NotificationObserver):
    def update(self, message):
        print(f"Отправляем оповещение по эмейлу: {message}")

class SMSNotification(NotificationObserver):
    def update(self, message):
        print(f"Отправляем SMS оповещение: {message}")

class PushNotification(NotificationObserver):
    def update(self, message):
        print(f"ОТправляем Push-уведомление: {message}")

class OrderNotifier:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)
