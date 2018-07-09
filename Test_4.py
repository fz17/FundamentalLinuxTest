import platform
import numpy as np

a = 0
for i in np.arange(100):
    a += i
    
print(a)

print(platform.system())
