#-------------------------------------------------------------------------------
# Name:        basics
# Purpose:
#
# Author:      prashant.ullegaddi
#
# Created:     05-06-2013
# Copyright:   (c) prashant.ullegaddi 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import sys


def binvals(values, num_of_bins=10):
    """ Bins the list and returns the corresponding bins for the same. """
    bins = np.linspace(min(values), max(values), num_of_bins)
    digitized = []

    for indx, val in enumerate(np.digitize(values, bins)):
        begin = bins[val-1]
        if val == len(bins):
            end = sys.maxint
        else:
            end = bins[val]
        digitized.append((values[indx], begin, end))

    return digitized


def main():
    pass

if __name__ == '__main__':
    main()
