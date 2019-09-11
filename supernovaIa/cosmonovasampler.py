from cosmoHammer import MpiCosmoHammerSampler
from cosmoHammer import LikelihoodComputationChain
from cosmoHammer.util import Params
from supernovaIalike import snlikeModule as slk
from supernovaIacore import supercore
params = Params(("Omega_m",[0.31,0.18,0.42,0.01]),
                ("h", [0.70,0.60,0.80,0.01]))
chain = LikelihoodComputationChain(min = params[:,1] , max = params[:,2])

chain.addCoreModule(supercore())

chain.addLikelihoodModule(slk())

chain.setup()

sampler = MpiCosmoHammerSampler(
            params= params,
            likelihoodComputationChain=chain,
            filePrefix="supernovaIa",
            walkersRatio=50,
            burninIterations=250,
            sampleIterations=250)


print("start sampling")
sampler.startSampling()
print("done!")


