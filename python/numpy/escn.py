import numpy as np
datas = np.genfromtxt('escn.csv', delimiter=',' ,skip_header=1)

# datas = np.random.random([100,20000])

print(datas)
# for data in datas:
# 	print(data)