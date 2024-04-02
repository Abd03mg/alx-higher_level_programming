#!/usr/bin/python3
""" Find a peak"""


def find_peak(lot):
    ''' function that finds a peak.
        Args:
            lots: List.Of.inTegers
    '''
    if len(lot) == 0:
        return None
    else:
        return max(lot)
