import snData as sn
import numpy as np

class snlikeModule(object):
    def __init__(self):
        pass

    def computeLikelihood(self,ctx):
        x = ctx.get("key_data")
        y = sn.mu_ob
        diff = x - y
        cov_inv = sn.cov_inv
        logl = -np.dot(diff,np.dot(cov_inv,diff))/2.

        return logl

    def setup(self):

        print("supernovaIa logLikelihood setup is done")
