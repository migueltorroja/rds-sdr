import numpy as np


class source_sample_type:
    def __init__(self,enc_string):
        if enc_string == 'S8':
            self.encoding_bytes_per_sample = 1
            self.encoding_is_little_endian = True 
            self.encoding_is_complex = False
        elif enc_string == 'S8_IQ':
            self.encoding_bytes_per_sample = 1
            self.encoding_is_little_endian = True 
            self.encoding_is_complex = True 
        elif enc_string == 'S16_BE':
            self.encoding_bytes_per_sample = 2 
            self.encoding_is_little_endian = False 
            self.encoding_is_complex = False 
        elif enc_string == 'S16_BE_IQ':
            self.encoding_bytes_per_sample = 2 
            self.encoding_is_little_endian = False 
            self.encoding_is_complex = True 
        elif enc_string == 'S16_LE':
            self.encoding_bytes_per_sample = 2 
            self.encoding_is_little_endian = True 
            self.encoding_is_complex = False 
        elif enc_string == 'S16_LE_IQ':
            self.encoding_bytes_per_sample = 2 
            self.encoding_is_little_endian = True 
            self.encoding_is_complex = True 
        elif enc_string == 'S32_LE':
            self.encoding_bytes_per_sample = 4
            self.encoding_is_little_endian = True 
            self.encoding_is_complex = False 
        elif enc_string == 'S32_LE_IQ':
            self.encoding_bytes_per_sample = 4
            self.encoding_is_little_endian = True 
            self.encoding_is_complex = True 
        elif enc_string == 'S32_BE':
            self.encoding_bytes_per_sample = 4
            self.encoding_is_little_endian = False 
            self.encoding_is_complex = False 
        elif enc_string == 'S32_BE_IQ':
            self.encoding_bytes_per_sample = 4
            self.encoding_is_little_endian = False
            self.encoding_is_complex = True
    def raw_data_to_samples(self,rawdata):
        if self.encoding_is_complex:
            samples = np.array(rawdata[0::2]) + np.array(rawdata[1::2])*1j
        return samples
    def nsamples_in_nbytes(self,nsamples):
        nbytes=self.encoding_bytes_per_sample
        if self.encoding_is_complex:
            nbytes = nbytes*2
        return nbytes

class sourceifc:
    class out_callbacks:
        def send_samples(self, timestamp, samples):
            pass
    S8_REAL         = 0
    S8_COMPLEX      = 1
    S16_BE_REAL     = 2
    S16_BE_COMPLEX  = 3
    S32_BE_REAL     = 4
    S32_BE_COMPLEX  = 5
    S16_LE_REAL     = 6
    S16_LE_COMPLEX  = 7
    S32_LE_REAL     = 8
    S32_LE_COMPLEX  = 9
    def __init__(self):
        self.m_callbacks = []
        self.block_size = 256 
        pass
    def get_samples_types(self):
        return None
    def get_sampling_rate(self):
        return None
    def get_osc_freq(self):
        return None
    def set_block_size(self, block_size):
        self.block_size = block_size
    def register_callbacks(self, callbacks ):
        self.m_callbacks = [self.m_callbacks, callbacks]
    def read_samples(self):
        return [0, [] ]
    def _send_to_sinks(self,timestamp, samples):
        for cb in self.m_callbacks:
            cb.send_samples(timestamp, samples)
