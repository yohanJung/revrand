import pytest
import numpy as np


@pytest.fixture
def make_quadratic():

    # Find quadratic parameters y = a*x**2 + b*x + c
    a = 3.  # Keep these positive for the log-trick tests!!
    b = 2.
    c = 1.
    N = 1000

    bounds = [(None, None), (None, None), (1.1, None)]

    x = np.linspace(-1, 1, N)
    y = a * x**2 + b * x + c
    data = np.vstack((y, x)).T

    return a, b, c, data, bounds
