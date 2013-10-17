import numpy as np


class source_sample_type:
    def __init__(self,enc_string):
        if enc_string == 'S8':
            self.dtype=np.dtype([('I',np.uint8)])
        elif enc_string == 'S8_IQ':
            self.dtype=np.dtype([('I',np.uint8),('Q',np.uint8)])
        elif enc_string == 'S16_BE':
            self.dtype=np.dtype([('I','>h')])
        elif enc_string == 'S16_BE_IQ':
            self.dtype=np.dtype([('I','>h'),('Q','>h')])
        elif enc_string == 'S16_LE':
            self.dtype=np.dtype([('I','<h')])
        elif enc_string == 'S16_LE_IQ':
            self.dtype=np.dtype([('I','<h'),('Q','<h')])
        elif enc_string == 'S32_LE':
            self.dtype=np.dtype([('I','<i')])
        elif enc_string == 'S32_LE_IQ':
            self.dtype=np.dtype([('I','<i'),('Q','<i')])
        elif enc_string == 'S32_BE':
            self.dtype=np.dtype([('I','>i')])
        elif enc_string == 'S32_BE_IQ':
            self.dtype=np.dtype([('I','>i'),('Q','>i')])

    def frombuffer(self,rawdata):
        npa=np.frombuffer(rawdata,self.dtype)
        return self._convert_to_complex(npa) 

    def fromfile(self,fileh,count):
        npa=np.fromfile(fileh,self.dtype,count)
        return self._convert_to_complex(npa) 

    def nbytes(self):
        return self.dtype.nbytes

    def _is_complex_type(self):
        fields = self.dtype.fields
        if 'I' in fields and 'Q' in fields:
            return True
        else:
            return False

    def _convert_to_complex(self,buf_array):
        if not self._is_complex_type():
            return buf_array 
        else:
            return buf_array['I'] + buf_array['Q']*1j

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
