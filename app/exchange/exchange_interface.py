import abc


class ExchangeInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_balance') and
                callable(subclass.get_balance) and
                hasattr(subclass, 'get_market_price') and
                callable(subclass.get_market_price) and
                hasattr(subclass, 'sell_order') and
                callable(subclass.sell_order) and
                hasattr(subclass, 'buy_order') and
                callable(subclass.buy_order) and
                hasattr(subclass, 'get_order_detail') and
                callable(subclass.get_order_detail))

    @abc.abstractmethod
    def get_balance(self) -> float:
        """GET request to exchange API for account balance"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_market_price(self) -> float:
        """"GET request to exchange API for current price of the asset"""
        raise NotImplementedError

    @abc.abstractmethod
    def sell_order(self, amount: int) -> str:
        """"POST request to exchange API to do a sell operation"""
        raise NotImplementedError

    @abc.abstractmethod
    def buy_order(self, amount: int) -> str:
        """"POST request to exchange API to do a buy operation"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_order_detail(self, order_id: str) -> str:
        """"GET request to exchange API for the details of an order"""
        raise NotImplementedError
