import simcx
import numpy as np
from simcx.simulators import FunctionIterator
from simcx.visuals import CobWebVisual


def eq(r):
    return lambda x: r * x * (1 - x)


def main():
    R = [0.5, 1.5, 2.8, 3.3, 3.5, 3.56, 3.835, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]
    SEEDS = list(np.arange(0.0, 1.0, 0.1))

    for r in R:
        equation = eq(r)

        display = simcx.Display()
        sim = FunctionIterator(equation, SEEDS)
        cobweb = CobWebVisual(sim, 0, 1, width=1900, height=1000)
        display.add_simulator(sim)
        display.add_visual(cobweb)
        simcx.run()


if __name__ == '__main__':
    main()
