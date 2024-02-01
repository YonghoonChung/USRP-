import numpy as np
import matplotlib.pyplot as plt

rx = np.load('20.0dB data.npy')
##
# rx = np.load('rx_data.npy')
# rx = rx.reshape(-1)
scope = rx[6662000:6722000]
plt.figure()
plt.plot(rx.real)
plt.show()

plt.figure()
plt.plot(scope.real)
plt.show()

##
wifi6 = scope[16060:18200-100-20]
plt.figure()
plt.plot(wifi6.real)
plt.show()
dvbt2 = scope[22000:31100]
plt.figure()
plt.plot(dvbt2.real)
plt.show()

##
# lookupTable = np.zeros((7,2,4))
# for idx in range(len(lookupTable)):
#     lookupTable[idx,:,0] = idx*5
#
# np.save('lookupTable', lookupTable)

##
lookupTable = np.load('lookupTable.npy')
lookupTable[4,0,1] = wifi6.mean().real
lookupTable[4,0,2] = wifi6.mean().imag
lookupTable[4,0,3] = wifi6.std()
lookupTable[4,1,1] = dvbt2.mean().real
lookupTable[4,1,2] = dvbt2.mean().imag
lookupTable[4,1,3] = dvbt2.std()

np.save('lookupTable', lookupTable)