#!/usr/bin/python3
""" Find a peak"""


def find_peak(lot):
    ''' function that finds a peak.
        Args:
            lots: List.Of.inTegers
    if len(lot) == 0:
        return None
    else:
        peak = lot[0]
        for i in lot:
            if peak < i:
                peak = i
        return peak
