import simcx
from simcx.simulators import FunctionIterator2D
from simcx.visuals import PhaseSpace2D, TimeSeries, Lines


def eq(k1: float, k2: float, k3: float, k4: float):
    def eq_(o, h):
        o_next = (1 + k1) * o - k3 * o * h
        h_next = (1 + k2) * h - k4 * o * h

        if o_next <= 0 or h_next <= 0:
            o_next = o
            h_next = h

        return o_next, h_next

    return eq_


def main():
    K1 = 0.2
    K2 = 0.3
    K3 = 0.001
    K4 = 0.002

    equation = eq(K1, K2, K3, K4)

    display = simcx.Display()
    sim = FunctionIterator2D(equation, [100, 200])
    orbits = Lines(sim)
    display.add_simulator(sim)
    display.add_visual(orbits)
    simcx.run()


if __name__ == '__main__':
    main()
