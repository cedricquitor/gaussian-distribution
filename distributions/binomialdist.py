import math
import matplotlib.pyplot as plt
from .generaldist import Distribution

class Binomial(Distribution):
    """
    Binomial distribution class for calculating and visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) number of trials
    """

    def __init__(self, prob=.5, size=20):
        self.n = size
        self.p = prob

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())


    def calculate_mean(self):
        """
        Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set
        """

        self.mean = self.p * self.n

        return self.mean


    def calculate_stdev(self):
        """
        Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set
        """

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev


    def replace_stats_with_data(self):
        """
        Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value
        """

        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def __add__(self, other):
        """
        Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution
        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):
        """
        Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian
        """

        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
