from pylab import *
from sourceifc import sourceifc

class plotsamples:
    class out_plot(sourceifc.out_callbacks):
        def send_samples(self, timestamp, samples):
            plot(samples)
            show()
    def __init__(self, src):
        src.register_callbacks(plotsamples.out_plot())
    def __del__(self):
        pass
