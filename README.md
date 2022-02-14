# MCproduction_BcToBsPi

Steps to generate Private MC samples

* Create fragment for the desired decay

You can download fragment examples from https://cms-pdmv.cern.ch/mcm

In this tutorial we are using [BcToBsPi](BcToBsPi_Pythia8_13TeV_TuneCP5-fragment.py) as fragment.

* Edit and run the [prepare script](prepare-BcToBsPi_MCH_2018.sh). (Remember signing in to the GRID in order to find the pileup files in DAS (if necessary))

* You should have produced several python config files for all the steps

* Test locally using [the script](MCcrabJobScript.sh)

* Finally send the job using [crab config file](crab-MCproduction_cfg.py)


Usefull references

https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGeneration

https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGenIntro

https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3AdvancedTutorial

https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
