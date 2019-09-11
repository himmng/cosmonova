import numpy as np
import corner
import matplotlib.pyplot as plt

path = '/home/ht/PycharmProjects/cosmonova/supernovaIa/'
omega_m , h = np.loadtxt(path+"cosmonovaIa.out", usecols = (0,1), unpack = True) #======= hubble's parameter and matter density =====#

logL = np.loadtxt(path+"cosmonovaIaprob.out", usecols = (0), unpack = True) #=== loglikelyhood =====#


plt.subplot(221)
plt.ylabel('freq.')
plt.xlabel('$h$')

plt.hist(h,bins = 100)

plt.subplot(222)
plt.ylabel('freq.')
plt.xlabel('$\Omega_m$')
plt.hist(omega_m,bins=100)

plt.subplot(223)
#plt.title("scatter plot: $h$ vs. $\Omega_m$ ",size = 8)
plt.xlabel('$\Omega_m$')
plt.ylabel('$h$')
plt.scatter(omega_m , h, c = -logL)
plt.savefig('params.png')
