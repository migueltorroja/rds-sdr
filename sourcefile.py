from sourceifc import sourceifc,source_sample_type
import re
from string import split
import gzip


class sourcefile(sourceifc):
    multiplier={'M':1000000,'K':1000}
    def __init__(self, filename):
        sourceifc.__init__(self)
        self.sampling_file_attributes=dict() 
        file_conf=split(filename,'__')
        self.index_file=0
        self.src_samp_type=source_sample_type('S8_IQ')
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
                self.src_samp_type=source_sample_type(value)
        if re.match('.*gz$',filename):
            self.fileh=gzip.open(filename,'rb')
        else:
            self.fileh=open(filename,'rb')
    def __del__(self):
        #self.fileh.close()
        pass
    def get_samples_type(self):
        return self.src_samp_type 
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

    def read_samples(self):
        prev_index=self.index_file
        #buff=self.fileh.read(self.block_size*self.src_samp_type.nbytes())
        #samples=self.src_samp_type.frombuffer(buff)
        samples=self.src_samp_type.fromfile(self.fileh,self.block_size)
        self.index_file += self.block_size
        self._send_to_sinks(prev_index, samples)
        return [prev_index, samples]
