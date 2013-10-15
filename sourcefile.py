from sourceifc import sourceifc
import re
from string import split
import gzip


class sourcefile(sourceifc):
    multiplier={'M':1000000,'K':1000}
    def __init__(self, filename):
        sourceifc.__init__(self)
        self.sampling_file_attributes=dict() 
        file_conf=split(filename,'__')
        for attribute in file_conf[1:]:
            re_comp=re.compile('([^_\.]+)_([^\.]*)')
            re_match=re_comp.match(attribute)
            key=re_match.group(1)
            value=re_match.group(2)
            if key == 'SR' or key == 'OSC':
                re_comp_units=re.compile('([0-9]+)(.)*')
                re_match_units=re_comp_units.match(value)
                units = int(re_match_units.group(1))
                for i in range(2,re_match_units.lastindex+1):
                    multi=re_match_units.group(i)
                    if multi in self.multiplier.keys():
                        units = units*self.multiplier[multi]
                    self.sampling_file_attributes[key]=units
            elif key == 'ENC':
                self.sampling_file_attributes[key]=value
        if re.match('.*gz$',filename):
            self.fileh=gzip.open(filename,'rb')
        else:
            self.fileh=open(filename,'rb')
    def __del__(self):
        self.fileh.close()
    def get_samples_types(self):
        if 'ENC' not in self.sampling_file_attributes.keys():
            return None
        enc_string=self.sampling_file_attributes['ENC'] 
        if enc_string == 'S8':
            return self.S8_REAL
        elif enc_string == 'S8_IQ':
            return self.S8_COMPLEX
        elif enc_string == 'S16_BE':
            return self.S16_BE_REAL
        elif enc_string == 'S16_BE_IQ':
            return self.S16_BE_COMPLEX
        elif enc_string == 'S16_LE':
            return self.S16_LE_REAL
        elif enc_string == 'S16_LE_IQ':
            return self.S16_LE_COMPLEX
        elif enc_string == 'S32_LE':
            return self.S32_LE_REAL
        elif enc_string == 'S32_LE_IQ':
            return self.S32_LE_COMPLEX
        elif enc_string == 'S32_BE':
            return self.S32_BE_REAL
        elif enc_string == 'S32_BE_IQ':
            return self.S32_BE_COMPLEX
        else:
            return None
    def get_sampling_rate(self):
        if 'SR' in self.sampling_file_attributes.keys():
            return self.sampling_file_attributes['SR']
        else:
            return None
    def get_osc_freq(self):
        if 'OSC' in self.sampling_file_attributes.keys():
            return self.sampling_file_attributes['OSC']
        else:
            return None
