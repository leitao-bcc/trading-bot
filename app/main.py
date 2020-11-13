from time import sleep
from trade_bot import TradeBot
from exchange.exchange_interface import ExchangeInterface
from decision.decision_interface import DecisionInterface


def main():
    # It doesn't work
    decision = DecisionInterface()
    # It doesn't work
    exchange = ExchangeInterface()

    trade_bot = TradeBot(decision, exchange, 100)

    while True:
        trade_bot.attempt_market_trade()
        sleep(30)


if __name__ == '__main__':
    main()
