from .base import Strategy

class StrategyA(Strategy):
    def do_algorithm(self, data: list) -> list:
        return [item + 1 for item in data]