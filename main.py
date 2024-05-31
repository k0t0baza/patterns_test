from orders_payments import WebsiteOrderProcessingFactory
from logging import SuperConsoleLogger
from notify import EmailNotification, SMSNotification
from order_manager import OrderManager


if __name__ == "__main__":
    order_manager = OrderManager(WebsiteOrderProcessingFactory(), SuperConsoleLogger())
    
    order_manager.add_notification_method(EmailNotification())
    order_manager.add_notification_method(SMSNotification())

    order_manager.process_order('Заказ #1234', 100.0)