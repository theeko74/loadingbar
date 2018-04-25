# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Main module for the loading bar abstract class.
    - ILoadingBar is an interface class which represents the loading bar.
"""

# Python2 compatibility
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import round
from future import standard_library
standard_library.install_aliases()
from builtins import object

# Standard imports
import sys


#-----------------------------------------------------------------
# ABSTRACT CLASS
#-----------------------------------------------------------------

class ILoadingBar(object):
    """
    Interface class for the loading bar.
    """

    def __init__(self, tot_size, display_size, loading_indicator, background, info):
        self.tot_size = tot_size
        self.display_size = display_size
        self.progress = 0
        self.loading_indicator = loading_indicator
        self.info = info
        self.background = background

    def update(self, progression):
        """
        Move the loading bar according to the progression.
        """
        s = self.update_loading_bar(progression)
        if self.info:
            s += self.update_info(progression)
        # Display everything
        self.display(s)

    def update_loading_bar(self, progression):
        """
        Method to draw the loading bar.
        """
        self.progress += (progression * self.display_size) / self.tot_size
        if self.progress >= self.display_size:
            self.progress = self.display_size

        s = self.loading_indicator.display(round(self.progress))
        s += self.background.display(round(self.progress))
        return s

    def update_info(self, progression):
        """
        Method to draw the info panel.
        """
        s = self.info.display(progression)
        return s

    def done(self):
        """
        Update the loading bar when complete.
        """
        s = self.loading_indicator.done()
        s += self.background.done()
        s += '\n'
        self.display(s)

    def display(self, s):
        """
        Display string with return cariage
        """
        s = "\r" + s
        sys.stdout.flush()
        sys.stdout.write(s)
