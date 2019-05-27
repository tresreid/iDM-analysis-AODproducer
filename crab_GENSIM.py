from CRABClient.UserUtilities import config
config = config()

sample_name = 'ggF_ctau-100000'

config.General.requestName = 'GENSIM_' + sample_name
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ggF_externalLHEProducer_and_PYTHIA8_Hadronizer_GENSIM_cfg_ctau-100000.py'
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = sample_name
config.Data.outputDatasetTag = 'GENSIM'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/mireid/ggF'

config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist = ["T3_US_FNALLPC"]
config.Site.storageSite = 'T3_US_FNALLPC'
