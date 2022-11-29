import numpy as np

tsize = np.log10(np.asarray([500, 1000, 2000, 4000, 6000, 8000, 9582]))

# DFT geometries, FPS int
AE_dft_int_fps_int = [
    0.452,  # 500
    0.256,  # 1000
    0.167,  # 2000
    0.128,  # 4000
    0.088,  # 6000
    0.072,  # 8000
    0.059,  # 9582
]

AE_dft_ext_fps_int = [
    0.372,  # 500
    0.24,   # 1000
    0.136,  # 2000
    0.108,  # 4000
    0.074,  # 6000
    0.061,  # 8000
    0.047,  # 9582
]
