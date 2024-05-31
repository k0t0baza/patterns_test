from abc import ABC, abstractmethod
from orders import WebsiteOrderProcessor, MobileAppOrderProcessor, OrderProcessor
from payments import CreditCardPayment, SBPPayment, PaymentFormat

class OrderProcessingFactory(ABC):
    @abstractmethod
    def create_order_processor(self) -> OrderProcessor:
        pass

    @abstractmethod
    def create_payment_strategy(self) -> PaymentFormat:
        pass

class WebsiteOrderProcessingFactory(OrderProcessingFactory):
    def create_order_processor(self):
        return WebsiteOrderProcessor()

    def create_payment_strategy(self):
        return CreditCardPayment()

class MobileAppOrderProcessingFactory(OrderProcessingFactory):
    def create_order_processor(self):
        return MobileAppOrderProcessor()

    def create_payment_strategy(self):
        return SBPPayment()