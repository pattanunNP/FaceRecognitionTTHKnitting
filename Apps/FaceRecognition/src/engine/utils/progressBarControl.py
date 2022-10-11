import progressbar
import time


class ProgressBar:

    def __init__(self):

        self.widgets = [' [',
                        progressbar.Timer(format='elapsed time: %(elapsed)s'), '] ', progressbar.Bar('='), ' (', progressbar.ETA(), ') ', ]

        self.bar = progressbar.ProgressBar(
            max_value=100, widgets=self.widgets).start()

    def run(self, total):
        for i in range(len(total)):
            time.sleep(0.01)
            self.bar.update(i)
