import simcx
from simcx.simulators import FunctionIterator
from simcx.visuals import TimeSeries


def eq1():
    return lambda x: x ** 2


def eq2():
    return lambda x: x ** 3


def eq3():
    return lambda x: 2 * x - 1


def main():
    seeds = [0.8, 0.9, 1.1, 1.2]
    equations = [eq1, eq2, eq3]

    for eq in equations:
        display = simcx.Display()
        sim = FunctionIterator(eq(  ), seeds)

        orbit = TimeSeries(sim)
        display.add_simulator(sim)
        display.add_visual(orbit)
        simcx.run()


if __name__ == '__main__':
    main()
