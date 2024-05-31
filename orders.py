from abc import ABC, abstractmethod

class OrderProcessor(ABC):
    @abstractmethod
    def process_order(self, order):
        pass

class WebsiteOrderProcessor(OrderProcessor):
    def process_order(self, order):
        print(f"С вебсайта получен следующий заказ: {order}")

class MobileAppOrderProcessor(OrderProcessor):
    def process_order(self, order):
        print(f"От мобильного приложения получен следующий заказ: {order}")
        
