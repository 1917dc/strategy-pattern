from context import Context
from strategy import StrategyA, StrategyB
import numpy as np

if __name__ == '__main__':
    data = np.random.randint(1, 20, 10)
    context = Context(StrategyA())
    print(data)
    print(context.run(data))

    context.strategy = StrategyB()
    print(context.run(data))