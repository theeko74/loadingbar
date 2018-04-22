# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Module for the background of the loading bar:
    - ILoadingBackground is an interface class which represents the background
      of the loading bar;
    - StandardLoadingBackground inherits from ILoadingBackground and has
      the default properties.
"""

from .indicator import ILoadingBarIndicator


class ILoadingBackground(ILoadingBarIndicator):
    """
    Interface class for the background of the loading bar.
    """

    def display(self, size):
        """
        Return string with the background.
        """
        if size == 0:
            self.done()
        return "{0}{1}\033[0m".format(self.color, self.symbol) * (self.display_size - size)

    def done(self):
        return "\033[0m"


class StandardLoadingBackground(ILoadingBackground):
    """
    Default class for the loading bar background.
    """

    def __init__(self, display_size):
        super().__init__(display_size, '\u2588', '\033[1;30m')
