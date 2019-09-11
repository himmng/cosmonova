import numpy as np
#N=input('enter no. of sample steps :')#-----------------no. of samples-----------------#


dbins=31 #--------------no. of bins given in the data file--------#


sigma=0.01 #-------assigning sigma for both parameters---------#

# reading the data file consisting of redshifts and distance modulus
path = '/home/ht/PycharmProjects/cosmonova/supernova_data'

z,mu_ob=np.loadtxt(path+'/jla_mub_0.txt',usecols=(0,1),unpack=True)




# reading & reshaping covarience matrix  to  31*31 matrix


cov=np.loadtxt(path+'/jla_mub_covmatrix.txt',unpack=True)
cov_err=cov.reshape((31,31))
#cov_inv=np.zeros(shape=(31,31))

cov_inv=np.linalg.inv(cov_err)