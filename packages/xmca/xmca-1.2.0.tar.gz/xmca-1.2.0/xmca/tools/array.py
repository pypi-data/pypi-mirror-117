#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Collection of tools for numpy.array modifications. '''

import warnings

import numpy as np


# =============================================================================
# Tools
# =============================================================================
def remove_mean(arr):
    '''Remove the mean of an array along the first dimension.

    If a variable (column) has at least 1 errorneous observation (row)
    the entire column will be set to NaN.

    '''
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        return arr - arr.mean(axis=0)


def get_nan_cols(arr: np.ndarray) -> np.ndarray:
    '''Get NaN columns from an array.

    Parameters
    ----------
    arr : ndarray
        Array to be scanned.

    Returns
    -------
    index : 1darray
        Index of columns with NaN entries from original data

    '''
    nan_index = np.isnan(arr).any(axis=0)

    return nan_index


def remove_nan_cols(arr: np.ndarray) -> np.ndarray:
    '''Remove NaN columns in array.

    Parameters
    ----------
    arr : ndarray
        Array to be cleaned.

    Returns
    -------
    new_data : ndarray
        Array without NaN columns.

    '''
    idx = get_nan_cols(arr)
    new_arr  = arr[:, ~idx]

    return new_arr


def has_nan_time_steps(array):
    ''' Checks if an array has NaN time steps.

    Time is assumed to be on axis=0. The array is then reshaped to be 2D with
    time along axis 0 and variables along axis 1. A NaN time step is a row
    which contain NaN only.
    '''

    return (np.isnan(array).all(axis=tuple(range(1, array.ndim))).any())
