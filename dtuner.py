class source_ifc:
    class out_callbacks:
        def send_samples(self, samples):
            pass
    def __init__(self):
        self.m_callbacks = []
        pass
    def get_samples_types(self):
        return None
    def get_sampling_rate(self):
        return None
    def get_osc_freq(self):
        return None
    def register_callbacks(self, callbacks ):
        self.m_callbacks = [self.m_callbacks callbacks] 
