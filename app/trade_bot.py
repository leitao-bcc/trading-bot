from order_type import OrderType
from decision.decision_interface import DecisionInterface
from exchange.exchange_interface import ExchangeInterface

HISTORY_LEN = 10


class TradeBot:
    def __init__(self, decision: DecisionInterface, exchange: ExchangeInterface, initial_price: float = None):
        self.decision = decision
        self.exchange = exchange
        self.last_order_type = OrderType.SELL
        self.price_history = TradeBot._get_price_history(initial_price)

    def attempt_market_trade(self):
        """Tries to make a trade operation"""
        current_price = self.exchange.get_market_price()
        order_type = self.decision.make_a_decision(self.last_order_type, current_price, self.price_history)

        if order_type.SELL:
            self.exchange.sell_order(1)
        elif order_type.BUY:
            self.exchange.buy_order(1)

        if order_type != OrderType.HOLD:
            self.last_order_type = order_type

        self.update_price_history(current_price)

    def update_price_history(self, current_price: float):
        """Updates the price history respecting the size limit"""
        self.price_history.append(current_price)
        if len(self.price_history) > HISTORY_LEN:
            self.price_history = self.price_history[1:]

    @staticmethod
    def _get_price_history(initial_price: float = None) -> list:
        """Fill the price history array (can be used to recover the history in case of failure)"""
        return [initial_price] if initial_price else []
