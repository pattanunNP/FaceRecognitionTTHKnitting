import progressbar
import time


class CustomProgressBar:

    def __init__(self):


        self.widgets = [' [',
                progressbar.Timer(format= 'elapsed time: %(elapsed)s'),'] ',progressbar.Bar('='),' (',progressbar.ETA(), ') ',]
  
        self.bar = progressbar.ProgressBar(max_value=100, widgets=self.widgets).start()
  

    def run(self, times):
        for i in range(times):
            time.sleep(0.01)
            self.bar.update(i)