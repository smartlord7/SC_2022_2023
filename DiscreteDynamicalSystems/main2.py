import simcx
from simcx.simulators import FunctionIterator
from simcx.visuals import TimeSeries


def mortgage_left_to_pay(monthly_payment, interest_rate):
    return lambda x: x - (monthly_payment - interest_rate * x)


def main():
    LOAN_VALUE = 80000
    MONTHLY_PAYMENT = 880.37
    INTEREST_RATE = 0.01

    display = simcx.Display()
    sim = FunctionIterator(mortgage_left_to_pay(MONTHLY_PAYMENT, INTEREST_RATE), LOAN_VALUE)

    orbit = TimeSeries(sim)
    display.add_simulator(sim)
    display.add_visual(orbit)
    simcx.run()


if __name__ == '__main__':
    main()
