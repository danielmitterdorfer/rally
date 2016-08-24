import sys
import os


class CmdLineProgressReporter:
    """
    CmdLineProgressReporter supports displaying an updating progress indication together with an information message.
    """

    def __init__(self, width=80, plain_output=False):
        self._width = width
        self._first_print = True
        self._plain_output = plain_output
        if (os.environ.get('TERM') == 'dumb'):
            self._plain_output = True

    def print(self, message, progress):
        """
        Prints/updates a line. The message will be left aligned, and the progress message will be right aligned.

        Typically, the message is static and progress changes over time (it could show a progress indication as
         percentage).

        :param message: A message to display (will be left-aligned)
        :param progress: A progress indication (will be right-aligned)
        """
        w = self._width
        if self._first_print:
            print(" " * w, end="")
            self._first_print = False

        formatted_progress = progress.rjust(w - len(message))
        if (self._plain_output):
            print("\n{0}{1}".format(message, formatted_progress), end="")
        else:
            print("\033[{0}D{1}{2}".format(w, message, formatted_progress), end="")

        sys.stdout.flush()

    def finish(self):
        # print a final statement in order to end the progress line
        print("")
