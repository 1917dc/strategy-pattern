from .base import Strategy

class StrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return [item + 2 for item in data]