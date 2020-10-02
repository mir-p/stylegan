# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Global configuration."""

# ADDED 
from google.colab import drive
drive.mount('/content/gdrive')

#----------------------------------------------------------------------------
# Paths.

result_dir = '/content/gdrive/My Drive/stylegan/results'
data_dir = '/content/gdrive/My Drive/stylegan/datasets'
cache_dir = 'cache'
run_dir_ignore = ['/content/gdrive/My Drive/stylegan/results', '/content/gdrive/My Drive/stylegan/datasets', '/stylegan/cache']

#----------------------------------------------------------------------------

