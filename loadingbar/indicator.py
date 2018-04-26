# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Module for the indicator of the loading bar:
    - ILoadingBarIndicator is an interface class which represents the indicator
      of the loading bar;
    - StandardLoadingBarIndicator inherits from ILoadingBarIndicator and has
      the default properties.
"""

# Python2 compatibility
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import super
from future import standard_library
standard_library.install_aliases()
from builtins import object


class ILoadingBarIndicator(object):
    """
    Interface for the loading bar indicator.
    """

    def __init__(self, display_size, symbol, color):
        self.display_size = display_size
        self.symbol = symbol
        self.color = color

    def display(self, size):
        """
        Return string with the loading bar indicator.
        """
        if size >= self.display_size:
            self.done()
        return "{0}{1}\033[0m".format(self.color, self.symbol) * size

    def done(self):
        return "{0}{1}\033[0m".format(self.color, self.symbol) * self.display_size


class StandardLoadingBarIndicator(ILoadingBarIndicator):
    """
    Default class for the loading bar indicator.
    """

    def __init__(self, display_size):
        super().__init__(display_size, '\u2588', '\033[31m')
