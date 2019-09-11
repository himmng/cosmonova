from snfuncs import *
import snData as sn


class supercore(object):


    def __init__(self):
        pass
    def __call__(self, ctx):
        p = ctx.getParams()

        ctx.add('params_sn',p)

        #derived_params = np.random.normal(p,sn.sigma)
        #ctx.getData()['derived_params_key'] = derived_params

        omega_m, h = p
        mu_t = mu(omega_m, h, sn.z)

        ctx.add("key_data",mu_t)

    def setup(self):

        print("supernovaIa core setup is done")




