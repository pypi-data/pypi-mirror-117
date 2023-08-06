from .util import findGauss, findUniform
import matplotlib.pyplot as plt
import numpy as np


def Gauss(name):
    """"
    Calls the findGauss function from util.py to return the Gauss prior for the given molecule.
    Input:      name of molecule
    Output:     Gauss prior object containing pdf, logpdf, cdf, ppf and rvs methods
    """
    prior = findGauss(name, 'v_t')
    return prior


def uniform(name):
    """
    Calls the findUniform function from util.py to return the uniform bounds for the given molecule.
    Input:      name of molecule
    Output:     array of length [2] with the upper and lower bounds for the uniform prior
    """
    prior = findUniform(name, 'v_t')
    return prior


def plotGauss(name): # pragma: no cover
    """
    Plots the prior probability distribution for the given molecule.
    Input:      name of molecule, type of prior (should either be 'Gauss' or 'uniform')
    Output:     matplotlib.pyplot graph of the given prior
    """
    # set the xrange, upper bound and lower bound for the prior
    xrange = uniform(name)
    lb = xrange[0,0]
    ub = xrange[0,1]
    xrange = np.linspace(lb, ub, 100)

    # plot the Gauss prior
    prior = Gauss(name)
    plt.xlabel('Tail Volume [Å]')
    plt.ylabel('pdf')
    plt.title(name)
    plt.plot(xrange, prior.pdf(xrange))
    plt.show()

def plotUniform(name): # pragma: no cover

    xrange = uniform(name)
    lb = xrange[0,0]
    ub = xrange[0,1]
    xrange = np.linspace(0.5 * lb, 1.3 * ub, 100)
    y = np.zeros_like(xrange)

    # plot the uniform prior
    for i, j in enumerate(xrange):
        if (lb <= j <= ub):
            y[i] = 1.0
        else:
            y[i] = 0.0
    plt.xlabel('Tail volume [Å]')
    plt.ylabel('pdf')
    plt.title(name)
    plt.plot(xrange, y)
    plt.show()

