from abc import ABC, abstractmethod

class PaymentFormat(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentFormat):
    def pay(self, amount):
        print(f"Ожидается оплата {amount}$ используя кредитную карту")

class SBPPayment(PaymentFormat):
    def pay(self, amount):
        print(f"Ожидается оплата {amount}$ используя виртуальный счет")

class CashOnDeliveryPayment(PaymentFormat):
    def pay(self, amount):
        print(f"Ожидается оплата {amount}$ наличными при доставке")
