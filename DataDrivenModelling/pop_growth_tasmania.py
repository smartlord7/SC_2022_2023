import matplotlib
import numpy as np
from numpy.polynomial.polynomial import Polynomial as pol
import matplotlib.pyplot as plt


def main():
    matplotlib.use('TkAgg')

    DIR_DATA = 'data/'
    EXTENSION_CSV = '.csv'
    DELIMITER_CSV = ';'
    PATH_POP_GROWTH_TASMANIA = DIR_DATA + 'pop_growth_tasmania' + EXTENSION_CSV

    DOMAIN_MIN = 1700
    DOMAIN_MAX = 2000
    COLORS = ['c', 'g', 'm', 'b', 'y']

    data = np.genfromtxt(PATH_POP_GROWTH_TASMANIA,
                         delimiter=DELIMITER_CSV,
                         skip_header=1)
    x = data[:, 0]
    y = data[:, 1]

    plt.plot(x, y, marker="o", color='r')
    plt.title('Tasmania population growth')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.ylim(0)

    handles = list()
    for i in range(1, len(COLORS)):
        fit1 = np.polyfit(x, y, i)
        domain = np.linspace(DOMAIN_MIN, DOMAIN_MAX, num=300)
        trend = np.poly1d(fit1)
        handle, = plt.plot(domain, trend(domain), COLORS[i])
        handles.append(handle)
    plt.legend(handles, [str(i) for i in range(1, len(COLORS))])
    plt.show()

if __name__ == '__main__':
    main()