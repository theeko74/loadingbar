# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Main module for the loading bar
    - ILoadingBar is an interface class which represents the loading bar;
    - StandardLoadingBar inherits from ILoadingBar and has customization.
"""

# Python 2 compatibility
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import super
from future import standard_library
standard_library.install_aliases()

# Standard imports
import sys

# Module imports
from loadingbar.aloadingbar import ILoadingBar
from loadingbar import indicator
from loadingbar import background
from loadingbar import infos


__all__ = [
    'LoadingBar', 'InfoLoadingBar', 'VerboseLoadingBar',
    'MessageLoadingBar', 'InternetLoadingBar',
    'PercentageLoadingBar', 'PercentageInfoLoadingBar',
    'PercentageBeforeLoadingBar', 'PercentageBeforeLoadingBarAndInfo'
]


DEFAULT_DISPLAY_SIZE = 50


class LoadingBar(ILoadingBar):
    """
    Default loading bar.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, None)


class InfoLoadingBar(ILoadingBar):
    """
    Loading bar with speed, ETA, size downloaded info.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.StandardInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)


class MessageLoadingBar(LoadingBar):
    """
    Loading bar with a message to display info like filename, etc.
    """

    def __init__(self, tot_size):
        super().__init__(tot_size)

    def update(self, progression, msg):
        """
        Override update method.
        """
        s = self.update_loading_bar(progression)
        if s:
            s += '  ' + msg
            self.display(s)


class VerboseLoadingBar(ILoadingBar):
    """
    Verbose mode to display msg in the info label.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.VerboseInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)

    def update(self, progression, msg):
        s = self.update_loading_bar(progression)
        s += self.update_info(progression, msg)
        self.display(s)

    def update_info(self, progression, msg):
        """
        Override update method.
        """
        return self.info.display(progression, msg)


class PercentageLoadingBar(ILoadingBar):
    """
    Loading bar that display a % indicator.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.PercentageOnlyInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)


class PercentageInfoLoadingBar(ILoadingBar):
    """
    Loading bar that display a % indicator and the standard infos.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.PercentageInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)


class PercentageBeforeLoadingBar(ILoadingBar):
    """
    Loading bar that display a % indicator before the loading bar.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        self.perc = infos.PercentageOnlyInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, None)

    def update(self, progression):
        """
        Override update method.
        """
        s = self.perc.display(progression)
        s += " "
        s += self.update_loading_bar(progression)
        if self.info:
            s += self.update_info(progression)
        self.display(s)

    def done(self):
        """
        Override done method.
        """
        s = self.perc.percentage_calculator.done()
        s += " "
        s += self.loading_indicator.done()
        s += self.background.done()
        s += '\n'
        self.display(s)


class PercentageBeforeLoadingBarAndInfo(PercentageBeforeLoadingBar):
    """
    Loading bar that display a % indicator before the loading bar,
    plus the standard additionnal infos.
    """

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.StandardInfo(tot_size)
        self.perc = infos.PercentageOnlyInfo(tot_size)
        super(PercentageBeforeLoadingBar, self).__init__(tot_size, self.display_size, default_li, default_bg, default_info)


class InternetLoadingBar(ILoadingBar):
    """
    Special loading bar for internet downloads.
    """
    display_size = DEFAULT_DISPLAY_SIZE

    def __init__(self, tot_size):
        default_li = indicator.StandardLoadingBarIndicator(self.display_size)
        default_bg = background.StandardLoadingBackground(self.display_size)
        default_info = infos.InternetInfo(tot_size)
        super().__init__(tot_size, self.display_size, default_li, default_bg, default_info)
