# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 22:29:25 2018

@author: kaleid
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

#plt.imshow
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')

# 添加一个colorbar ，其中我们添加一个shrink参数，使colorbar的长度变短为原来的92%
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()


