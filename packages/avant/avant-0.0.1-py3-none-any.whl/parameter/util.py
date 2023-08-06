from .gauss_class import Gauss
import pandas as pd
import bson



def findGauss(name, parameter):
    """
    Opens the database to extract the data, inserts it into Gauss class and returns a Gauss prior object.
    Input:      name of molecule, parameter to find
    Output:    Gauss prior object containing pdf, logpdf, cdf, ppf and rvs methods
    """
    # Open the bson_file to get the Gaussian data
    bson_file = open('../avant/db/Gaussian.bson', 'rb')
    b = bson.decode_all(bson_file.read())
    # Turn the data into a pandas dataframe so it can be filtered
    c = pd.DataFrame(list(b))
    # Filter the data by the correct name and parameter
    filtered = c[(c['name'] == name) & (c['parameter'] == parameter)]
    # Return only the loc and scale columns
    filtered2 = filtered[['loc', 'scale']]
    # Convert to numpy array
    data_arr = filtered2.to_numpy(dtype=float)

    # get the values for the lower and upper bound of the distribution
    bounds = findUniform(name,parameter)
    lb = bounds[0,0]
    ub = bounds[0,1]
    # insert the data into Gauss class to get the prior probability object
    prior_object = Gauss(data_arr,lb,ub)
    print(data_arr,lb,ub)

    return prior_object


def findUniform(name, parameter):
    """
    Opens the database to extract the data and returns an array of bounds for the uniform prior probability.
    Input:      name of molecule, parameter of interest
    Output:     array of length [2] with the upper and lower bounds for the uniform prior
    """

    # Open the bson_file to get the Uniform data
    bson_file = open('../avant/db/uniform.bson', 'rb')
    b = bson.decode_all(bson_file.read())
    # Turn the data into a pandas dataframe so it can be filtered
    c = pd.DataFrame(list(b))
    # Filter the data by the correct name and parameter
    filtered = c[(c['name'] == name) & (c['parameter'] == parameter)]
    # Return only the upper and lower bound columns
    filtered2 = filtered[['lower bound', 'upper bound']]
    # Convert to numpy array
    bounds = filtered2.to_numpy(dtype=float)

    return bounds


