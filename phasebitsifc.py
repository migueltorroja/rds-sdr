class phasebitsifc:
    class out_callbacks:
        def send_phases(self, phases_out)
    def __init__(self):
        self.m_callbacks = []
    def register_callbacks(self, callback):
        self.m_callbacks = [self.m_callbacks, callbacks]
