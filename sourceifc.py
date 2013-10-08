class source_ifc:
    S8_REAL = 0
    S8_COMPLEX  = 1
    S16_BE_REAL = 2
    S16_BE_COMPLEX = 3
    S32_BE_REAL = 4
    S32_BE_COMPLEX = 5
    S16_LE_REAL = 6
    S16_LE_COMPLEX = 7
    S32_LE_REAL = 8
    S32_LE_COMPLEX = 9
    def __init__(self):
        pass
    def get_samples_types(self):
        return None
    def get_sampling_rate(self):
        return None
    def get_osc_freq(self):
        return None

        
