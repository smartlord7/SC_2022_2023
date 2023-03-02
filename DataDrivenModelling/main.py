import csv

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression

'''
This data correspond the confirmed cases of covid-19 by ARS, which is the health region area. 
Use  it to create a model for each ARS. What can you conclude?

Source: https://github.com/dssg-pt
  
'''


def logistic(x):
    return 10 / (1 + np.e ** -x);

def main():
    matplotlib.use('TkAgg')

    DIR_DATA = 'data/'
    EXTENSION_CSV = '.csv'
    DELIMITER_CSV = ','
    PATH_COVID_ARS = DIR_DATA + 'covid_ars' + EXTENSION_CSV

    DOMAIN_MIN = 1
    DOMAIN_MAX = 350

    data = np.genfromtxt(PATH_COVID_ARS,
                         delimiter=DELIMITER_CSV,
                         skip_header=1)
    cases = data[:, 2:]
    x = np.arange(cases.shape[0])
    y = cases[:, 1]

    y[y == 0] = 1
    plt.figure()
    plt.plot(x, y)
    plt.show()

    x = x.reshape(-1, 1)
    y_log = np.log(y)

    # Fit a linear regression model to the transformed data
    model = LinearRegression().fit(x, y_log)

    # Generate predictions from the fitted model
    y_pred_log = model.predict(x)

    # Convert the predicted values back to the original scale
    y_pred = np.exp(y_pred_log)

    residuals = np.abs(y_pred - y)
    sse = np.sum((residuals) ** 2)
    mean = np.mean(y)
    sst = np.sum((y - mean) ** 2)
    r2 = (sst - sse) / sst
    corr = np.sqrt(r2)

    print("SSE: %.3f\n"
          "SSR: %.3f\n"
          "SST: %.3f\n"
          "R^2: %.3f\n"
          "Corr(x, y) = + %.3f\n" % (sse,
                                     sst - sse,
                                     sst,
                                     r2,
                                     corr))
    plt.figure()
    plt.scatter(x, residuals)
    plt.title("Residuals")
    plt.show()



    # Plot the original data and the regression line
    plt.scatter(x, y)
    plt.plot(x, y_pred, color='red')
    plt.xlabel('Time')
    plt.ylabel('Number of cases')
    plt.show()

if __name__ == '__main__':
    main()
