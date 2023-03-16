import matplotlib
import simcx
import numpy as np
from simcx.simulators import FunctionIterator
from simcx.visuals import TimeSeries


def eq(a, b):
    return lambda x: a * x + b


def main():
    a = [i for i in np.linspace(start=-10.0, stop=0.0, num=4)]
    b = [i for i in np.linspace(start=-10.0, stop=0.0, num=5)]
    x0 = [i for i in np.arange(-200.0, 200.0, 20.0)]

    for a_val in a:
        for b_val in b:
            display = simcx.Display()
            sim = FunctionIterator(eq(a_val, b_val), x0)

            orbit = TimeSeries(sim)
            display.add_simulator(sim)
            display.add_visual(orbit)
    simcx.run()


if __name__ == '__main__':
    main()

