#! /usr/bin/python

import sys
import pylab as pl


sampling_rate=200000
local_osc=57000
cycles_per_bit=24
total_bits=50
samples_per_cycle=float(sampling_rate)/float(local_osc)
samples_per_bit=cycles_per_bit*samples_per_cycle
len_iq_samples=int(float(total_bits)*samples_per_bit)
total_samples_to_read=len_iq_samples*2
fileh=open(sys.argv[1],'rb')
samples=bytearray(fileh.read(total_samples_to_read))
print len(samples)
iq_samples=pl.array([complex(samples[i*2]-128, samples[i*2+1]-128) for i in range(0,len_iq_samples) ])
dc_component=pl.sum(iq_samples)/len_iq_samples
for i in range(-5,5):
    lo=pl.exp(-1j*pl.frange(0,len_iq_samples-1)*(local_osc+i*1000)*2*pl.pi/sampling_rate)
#pl.plot(iq_samples)
    down_convert=iq_samples*lo
    decimated_samples=[pl.sum(down_convert[i:i+samples_per_bit-1]) for i in range(0,len_iq_samples-int(samples_per_bit))]
    x_axis_range=pl.frange(len(decimated_samples)-1)/samples_per_bit
    print len(x_axis_range), len(decimated_samples)
    pl.subplot(211)
    pl.plot(x_axis_range,pl.real(decimated_samples),'b',
            x_axis_range,pl.imag(decimated_samples),'r')
    pl.title('IQ Samples')
    pl.subplot(212)
    pl.plot(x_axis_range,pl.arctan(pl.imag(decimated_samples)/pl.real(decimated_samples)))
    pl.title('Phase')
    pl.figure(2)
    f_range=pl.frange(-sampling_rate/2 , sampling_rate/2 ,(sampling_rate)/len_iq_samples)
    print len(f_range), len_iq_samples
    pl.plot(f_range[0:len_iq_samples],abs(pl.fft(iq_samples)))
    pl.plot('FFT of IQ Samples')
    pl.show()
