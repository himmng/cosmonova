import numpy as np
import corner
import matplotlib.pyplot as plt

path = '/home/ht/PycharmProjects/cosmonova/supernovaIa/'
omega_m , h = np.loadtxt(path+"cosmonovaIa.out", usecols = (0,1), unpack = True) #======= hubble's parameter and matter density =====#

logL = np.loadtxt(path+"cosmonovaIaprob.out", usecols = (0), unpack = True) #=== loglikelyhood =====#

plt.figure(figsize=(10,10))
plt.suptitle("hubble paramater $h$ vs. matter density parameter $\Omega_m$ ",size = 15)
plt.subplot(221)
plt.ylabel('freq.')
plt.xlabel('$h$')

plt.hist(h,bins = 100,color='purple')

plt.subplot(222)
plt.ylabel('freq.')
plt.xlabel('$\Omega_m$')
plt.hist(omega_m,bins=100,color='orange')

plt.subplot(212)

plt.xlabel('$\Omega_m$')
plt.ylabel('$h$')
plt.scatter(omega_m , h, c = -logL,cmap='cividis_r')

plt.savefig('hist_&_scatter.png')

a=[]
a = np.c_[h,omega_m]
fig = corner.corner(a,bins=100,color='b',weights = -logL,labels = ['$h$','$\Omega_m$'])
fig.suptitle("hubble paramater $h$ vs. matter density parameter $\Omega_m$ ")
fig.savefig('corner_plot.png')