"""
Module to display a loading bar indicator in a
terminal window.
"""

import sys
import time


__all__ = ['LoadingBar']


class LoadingBar:

    def __init__(self, tot_size, size=50, symbol='\u2588', empty_symbol='\u2588',
                 color_bar='\033[31m', color_bg='\033[1;30m', verbose=True):
        self.tot_size = tot_size
        self.loaded = 0
        self.progress = 0
        self.start_time = None

        # Styling
        self.symbol = symbol
        self.empty_symbol = empty_symbol
        self.color_bar = color_bar
        self.color_bg = color_bg
        self.size = size
        self.verbose = verbose

    def speed(self):
        if not self.start_time:
            return 0
        # Calculate speed in ko/s
        return (self.loaded / (time.time() - self.start_time)) / 1000

    @staticmethod
    def speed_to_str(speed):
        if speed < 1000:
            return "{:>3}K/s".format(int(speed))
        else:
            return "{:>3}M/s".format(int(speed/1000))

    def time_remain(self):
        if self.speed() == 0:
            return 0
        else:
            return self.tot_size / 1000 / self.speed()

    @staticmethod
    def time_to_str(time):
        if time < 60:
            return "{:>2}sec ".format(int(time))
        elif time > 60 and time < 3600:
            return "{:>2}min ".format(int(time/60))
        else:
            return "{:>2}h{:>2}m".format(int(time/3600), int(time%3600/60))

    @staticmethod
    def size_to_str(size):
        # At least display size in Ko
        size = size / 1000
        if size > 1000000:
            return "{:5.1f}G".format(size/1000000)
        elif size > 1000:
            return "{:5.1f}M".format(size/1000)
        else:
            return "{:>5}K".format(int(size))

    def output(self, progress):
        if self.verbose:
            s = '\r' + self.color_bar + self.symbol * progress + \
                self.color_bg + self.empty_symbol * (self.size - progress) + \
                '\033[0m '
        else:
            s = '\r' + self.color_bar + self.symbol * progress + \
                self.color_bg + self.empty_symbol * (self.size - progress) + \
                '\033[0m ' + self.size_to_str(self.loaded) + '    ' + \
                self.speed_to_str(self.speed()) + '   ' + \
                self.time_to_str(self.time_remain())
        return s

    def update(self, len_data):
        self.loaded += len_data
        progress = int(self.loaded * self.size / self.tot_size)
        # Output to console
        sys.stdout.write(self.output(progress))
        sys.stdout.flush()
        if not self.start_time:
            self.start_time = time.time()

    def done(self):
        sys.stdout.write(self.output(self.size))
        sys.stdout.write('\n')
        sys.stdout.flush()
