#!/usr/bin/python
import random


def generate(n_points=10000):

    # make the toy data-set for terrain
    random.seed(42)
    grade = [random.random() for ii in range(0, n_points)]
    bumpy = [random.random() for ii in range(0, n_points)]
    error = [random.random() for ii in range(0, n_points)]
    y = [round(grade[ii] * bumpy[ii] + 0.3 + 0.1 * error[ii]) for ii in range(0, n_points)]
    for ii in range(0, len(y)):
        if grade[ii] > 0.8 or bumpy[ii] > 0.8:
            y[ii] = 1.0

    for ii in range(0, len(y)):
        if y[ii] == 0.0:
            y[ii] = 'slow'
        else:
            y[ii] = 'fast'

    x = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    split = int(0.75*n_points)
    x_train = x[0:split]
    x_test = x[split:]
    y_train = y[0:split]
    y_test = y[split:]

    return x_train, y_train, x_test, y_test
