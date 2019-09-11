import numpy as np
import corner
import matplotlib.pyplot as plt

omega_m , h = np.loadtxt("cosmosupernovaIa.out", usecols = (0,1), unpack = True) #======= hubble's parameter and matter density =====#

logL = np.loadtxt("cosmosupernovaIaprob.out", usecols = (0), unpack = True) #=== loglikelyhood =====#


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
plt.show()
