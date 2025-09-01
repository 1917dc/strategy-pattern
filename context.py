from __future__ import annotations
from strategy import Strategy

class Context():
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def run(self, data: list) -> list:
        return self._strategy.do_algorithm(data)