""" defines Normal class that represents normal distribution """


class Normal:
    """Represents a normal (Gaussian) distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            n = len(data)
            self.mean = sum(data) / n
            summation = 0
            for x in data:
                summation += ((x - mean) ** 2)
            stddev = (summation / len(data)) ** (1 / 2)
            self.stddev = stddev

    def z_score(self, x):
        """Calculates z-score for x"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates x-value from z-score"""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the PDF for x"""
        e = 2.7182818285
        pi = 3.1415926536
        power = -0.5 * (self.z_score(x) ** 2)
        coefficient = 1 / (self.stddev * ((2 * pi) ** (1 / 2)))
        pdf = coefficient * (e ** power)
        return pdf
    
    def cdf(self, x):
        """Calculates the CDF for x"""
        pi = 3.1415926536
        value = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + erf)
        return cdf
