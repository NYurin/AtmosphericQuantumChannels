import cupy
import numpy as np


def pp(x, digits=3):
  if x == 0 or x is np.nan or np.isinf(x):
    return x
  return round(x, -int(np.floor(np.log10(x))) + (digits - 1))

def fft2(x, delta):
  xp = cupy.get_array_module(x)
  return xp.fft.fftshift(xp.fft.fft2(xp.fft.fftshift(x))) * delta**2

def ifft2(x, delta):
  xp = cupy.get_array_module(x)
  N = x.shape[0]
  return xp.fft.ifftshift(xp.fft.ifft2(xp.fft.ifftshift(x))) * (N * delta)**2
