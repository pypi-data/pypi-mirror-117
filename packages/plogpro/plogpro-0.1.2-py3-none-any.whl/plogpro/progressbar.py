from __future__ import print_function

from abc  import ABCMeta, abstractmethod
from time import time


class ProgressBar(metaclass=ABCMeta):
    """Base class that provides an interface for progress bars
    
    To implement a new progress bar, create a class that derives from
    `ProgressBar` and implement the method `draw()`. This method should draw the
    progress bar based on the accessible member variables.

    Usage:
        To create a progress bar, create an instance of one of its
        implementations. The progressbar can then be updated by calling the
        method `update()`.
    """

    def __init__(self, nsteps: int):
        """Create an instance of `ProgressBar`
        
        Arguments:
            nsteps (int)
                The number of steps that the progressbar will go through
        """
        self.nsteps = nsteps
        self.step = 0
        self.start_time = time()
        self.current_time = time()
    
    def update(self, step: int = None) -> None:
        """Update the progressbar

        Arguments:
            step (int, optional)
                The current step of the operation, the progress will be
                increased with one step if not provided
                (default: `None`)
        """
        self.current_time = time()
        if step is None:
            self.step += 1
        else:
            self.step = step
        self.draw()

    def progress(self) -> float:
        """Get the progress as a number between 0 and 1

        Returns:
            (float) The progress
        """
        return self.step / self.nsteps
    
    @abstractmethod
    def draw(self) -> None:
        pass


class ConsoleProgressBar(ProgressBar):
    """A text-based progress bar for in a terminal or console
    """

    def __init__(self, nsteps: int, width: int = 70):
        """Create an instance of a `ConsoleProgressBar`
        
        Arguments:
            nsteps (int)
                The number of steps that the progressbar will go through
            width (int, optional)
                The width of the progress bar
                (default: 70)
        """
        super().__init__(nsteps)
        self.width = width

    def draw(self) -> None:
        nblocks = round(self.progress() * self.width)
        output_string  = "|" + ('■' * nblocks).ljust(self.width) + "|"
        output_string += " {:d}/{:d}".format(self.step, self.nsteps)

        elapsed = round(self.current_time - self.start_time)
        elapsed_hours, rem = divmod(elapsed, 3600)
        elapsed_minutes, elapsed_seconds = divmod(rem, 60)
        estimated = round(elapsed / self.progress())
        estimated_hours, rem = divmod(estimated, 3600)
        estimated_minutes, estimated_seconds = divmod(rem, 60)

        output_string += " - "
        if estimated_hours > 0:
            output_string += "{:>02d}:".format(elapsed_hours)
        if estimated_minutes > 0 or estimated_hours > 0:
            output_string += "{:02d}:".format(elapsed_minutes)
        output_string += "{:02d}".format(elapsed_seconds)
        if estimated_minutes == 0 and estimated_hours == 0:
            output_string += "s"

        output_string += "/"
        if estimated_hours > 0:
            output_string += "{:>02d}:".format(estimated_hours)
        if estimated_minutes > 0 or estimated_hours > 0:
            output_string += "{:02d}:".format(estimated_minutes)
        output_string += "{:02d}".format(estimated_seconds)
        if estimated_minutes == 0 and estimated_hours == 0:
            output_string += "s"

        end = '\r' if self.step < self.nsteps else '\n'
        print(output_string, end=end, flush=True)
