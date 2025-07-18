#!/usr/bin/env python3
""" defines Poisson class that represents Poisson distribution """

class Poisson:
    """Represents a Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initialize with data or a given lambda"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the PMF value for a given number of 'successes'"""
        k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        factorial = 1
        for i in range(k):
            factorial *= (i + 1)
        return ((self.lambtha ** k) * (e ** -self.lambtha)) / factorial

    def cdf(self, k):
        """Calculates the CDF value for a given number of 'successes'"""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(0, k + 1))
