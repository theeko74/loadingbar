# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
Module for the label side to the loading bar that displays information:
    - IInfo is an interface class which represents the information label
    - StandardInfo inherits from IInfo and has the default properties.
"""

# Python2 compatibility
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import super
from builtins import round
from future import standard_library
standard_library.install_aliases()
from builtins import object

# Standard imports
import time


class AbstractInfo(object):
    """
    Abstract class for the info label.
    """

    def display(self, loaded):
        """
        Display the info label side to download bar.
        """
        s = ""

        # List all attributes of the class, and for
        # each of them call the display method
        for label in vars(self).keys():
            s += getattr(self, label).display(loaded) + " "
        return s


class StandardInfo(AbstractInfo):
    """
    Standard class for the info label.
    """

    def __init__(self, tot_size):
        self.size_calculator = SizeCalculator(tot_size)
        self.speed_calculator = SpeedCalculator(tot_size)
        self.eta_calculator = ETACalculator(self.speed_calculator)


class VerboseInfo(StandardInfo):
    """
    Info label that displays a message for verbose mode.
    """

    def __init__(self, tot_size):
        super().__init__(tot_size)

    def display(self, loaded, msg):
        """
        Override standard display method.
        """
        s = super().display(loaded)
        s += msg
        return s


class InternetInfo(AbstractInfo):
    """
    Infos for internet download.
    """

    def __init__(self, tot_size):
        self.size_calculator = SizeCalculator(tot_size)
        self.speed_calculator = InternetSpeedCalculator(tot_size)
        self.eta_calculator = ETACalculator(self.speed_calculator)


class PercentageOnlyInfo(AbstractInfo):
    """
    Display percentage after the loading bar.
    """
    def __init__(self, tot_size):
        self.percentage_calculator = PercentageCalculator(tot_size)


class PercentageInfo(StandardInfo):
    """
    Display percentage and verbose infos.
    """

    def __init__(self, tot_size):
        self.percentage_calculator = PercentageCalculator(tot_size)
        super().__init__(tot_size)


class SpeedCalculator(object):
    """
    Speed calculator algorithm.
    """

    def __init__(self, tot_size):
        self.tot_size = tot_size
        self.time = None
        self._calculated_speed = None

    def speed(self, loaded):
        """
        Calculate the downloading speed in KB/S.
        """
        if not self.time:
            self._calculated_speed = 0
            self.time = time.time()
        else:
            tmp_time = time.time()
            delta_time = tmp_time - self.time
            self.time = tmp_time
            if delta_time == 0:
                self._calculated_speed = 0
            else:
                self._calculated_speed = loaded / 1000 / delta_time
        return self._calculated_speed

    @staticmethod
    def speed_to_str(speed):
        """
        Convert speed to formated string with the appropriate units.
        """
        if speed < 1000:
            return "{:>4}K/s".format(round(speed))
        else:
            return "{:4.1f}M/s".format(round(speed/1000))

    def display(self, loaded):
        """
        Return a formated string of the downloading speed.
        """
        return self.speed_to_str(self.speed(loaded))

    def get_speed(self, loaded):
        """
        Get the lastest calculated speed.
        """
        if not self._calculated_speed:
            self.speed(loaded)
        return self._calculated_speed


class InternetSpeedCalculator(SpeedCalculator):
    """
    Special calculator to get an average speed of the download
    rather than an evaluation at every chunk received which not accurate.
    """

    def __init__(self, tot_size):
        super().__init__(tot_size)
        self.cumulate = 0
        self.start_time = None

    def speed(self, loaded):
        """
        Override standard speed function.
        """
        if not self.time:
            self._calculated_speed = 0
            self.time = time.time()
        else:
            if not self.start_time:
                self.start_time = time.time()
            delta_time = time.time() - self.start_time
            self.cumulate += loaded
            if delta_time == 0:
                self._calculated_speed = 0
            else:
                self._calculated_speed = self.cumulate / 1000 / delta_time
        return self._calculated_speed


class SizeCalculator(object):
    """
    Downloaded size calculator.
    """

    def __init__(self, tot_size):
        self.tot_size = tot_size
        self.loaded = 0

    def size(self, loaded):
        """
        Calculate the downloaded size.
        """
        self.loaded += loaded
        return self.loaded

    @staticmethod
    def size_to_str(size):
        """
        Convert size in bytes to string with appropriate units.
        """
        # At least display size in Ko
        size = size / 1000
        if size > 1000000:
            return "{:5.1f}G".format(size/1000000)
        elif size > 1000:
            return "{:5.1f}M".format(size/1000)
        else:
            return "{:>5}K".format(round(size))

    def display(self, loaded):
        """
        Return a formated string of the downloaded size.
        """
        return self.size_to_str(self.size(loaded))


class ETACalculator(object):
    """
    Calculate the Estimate Time to Arrival (ETA),
    or how many time before the download is complete.
    """

    def __init__(self, speed_calculator):
        self.speed_calculator = speed_calculator
        self.still_to_load = self.speed_calculator.tot_size

    def eta(self, loaded):
        """
        Calculate the ETA
        """
        if self.still_to_load == 0 or self.speed_calculator.get_speed(loaded) <= 0:
            return 0
        self.still_to_load -= loaded
        return (self.still_to_load) / (self.speed_calculator.get_speed(loaded)  * 1000)

    @staticmethod
    def time_to_str(time):
        """
        Convert time to formated string with the appropriate time units.
        """
        if time < 60:
            return "{:>2}sec ".format(round(time))
        elif time > 60 and time < 3600:
            return "{:>2}min ".format(round(time/60))
        else:
            return "{:>2}h{:>2}m".format(round(time/3600), round(time%3600/60))

    def display(self, loaded):
        """
        Return a formated string of the ETA.
        """
        return self.time_to_str(self.eta(loaded))


class PercentageCalculator(object):
    """
    Calculate the percentage of loading.
    """

    def __init__(self, tot_size):
        self.tot_size = tot_size
        self.already_loaded = 0

    @staticmethod
    def nb_to_perc_str(nb, tot_nb):
        return "{:>4}%".format(round(nb / tot_nb * 100))

    def display(self, loaded):
        self.already_loaded += loaded
        return self.nb_to_perc_str(self.already_loaded, self.tot_size)

    def done(self):
        self.already_loaded = self.tot_size
        return self.display(0)
