# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Module for the indicator of the loading bar:
    - ILoadingBarIndicator is an interface class which represents the indicator
      of the loading bar;
    - StandardLoadingBarIndicator inherits from ILoadingBarIndicator and has
      the default properties.
"""


class ILoadingBarIndicator:
    """
    Interface for the loading bar indicator.
    """

    def __init__(self, tot_size, symbol, color):
        self.tot_size = tot_size
        self.symbol = symbol
        self.color = color

    def display(self, size):
        """
        Return string with the loading bar indicator.
        """
        if size >= self.tot_size:
            self.done()
        return "{0}{1}\033[0m".format(self.color, self.symbol) * size

    def done(self):
        return "{0}{1}\033[0m".format(self.color, self.symbol) * self.tot_size


class StandardLoadingBarIndicator(ILoadingBarIndicator):
    """
    Default class for the loading bar indicator.
    """

    def __init__(self, tot_size):
        super().__init__(tot_size, '\u2588', '\033[31m')
