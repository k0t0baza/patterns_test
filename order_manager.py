from logging import Logger
from notify import OrderNotifier
from payments import PaymentFormat
from orders_payments import OrderProcessingFactory

class OrderManager:
    def __init__(self, factory:OrderProcessingFactory, logger:Logger):
        self._factory = factory
        self._logger = logger
        self._notifier = OrderNotifier()

    def add_notification_method(self, notification_method):
        self._notifier.add_observer(notification_method)

    def remove_notification_method(self, notification_method):
        self._notifier.remove_observer(notification_method)

    def process_order(self, order, payment_amount):
        processor = self._factory.create_order_processor()
        processor.process_order(order)
        self._logger.log(f"Обрабатывается следующий заказ: {order}")

        payment_strategy = self._factory.create_payment_strategy()
        payment_strategy.pay(payment_amount)
        self._logger.log(f"Какую опталу ожидается получить: {payment_amount}")

        self._notifier.notify_observers(f"Заказ {order} обработан и считается оплаченным {payment_amount}")
        self._logger.log(f"Отправлены уведомления для заказа: {order}")