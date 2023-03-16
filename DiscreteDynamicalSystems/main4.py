import simcx
from simcx.simulators import FunctionIterator


def eq():
    return lambda x: x ** 2


def main():
    seeds = [0.1, 0.2, 0.5, 0.8, 1.0]
    equations = [eq()]

    for equ in equations:
        display = simcx.Display()
        sim = FunctionIterator (equ, seeds)
        cobweb = simcx.visuals.CobWebVisual(sim, 0, 1, '$3.2 x {x} (1 - {x})$',
                                             width=800, height=400)
        display.add_simulator(sim)
        display.add_visual(cobweb)
        simcx.run()


if __name__ == '__main__':
    main()
