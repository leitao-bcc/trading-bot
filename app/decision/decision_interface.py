import abc
from order_type import OrderType


class DecisionInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return True

    @abc.abstractmethod
    def make_a_decision(self, last_order_type: OrderType, current_price: float, price_history: list) -> OrderType:
        """"Decides the next operation to be performed"""
        raise NotImplementedError
