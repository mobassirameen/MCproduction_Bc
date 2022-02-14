import FWCore.ParameterSet.Config as cms

from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(True),
                         comEnergy = cms.double(13000.),
                         ExternalDecays = cms.PSet(
                           EvtGen130 = cms.untracked.PSet(
                             decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                             particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_Bc_2014.pdl'),
                             convertPythiaCodes = cms.untracked.bool(False),
                             user_decay_embedded= cms.vstring(
                              """
                              Define Hp 0.49
                              Define Hz 0.775
                              Define Hm 0.4
                              Define pHp 2.50
                              Define pHz 0.0
                              Define pHm -0.17
                              #
                              Particle B_c+      6.27490 0.00000
                              Alias     MyB_c+  B_c+
                              Alias     MyB_c-  B_c-
                              ChargeConj MyB_c+ MyB_c-
                              #
                              Alias      MyB_s0   B_s0
                              Alias      Myanti-B_s0   anti-B_s0
                              ChargeConj Myanti-B_s0   MyB_s0 
                              Alias      MyJ/psi  J/psi
                              Alias      MyPhi    phi
                              ChargeConj MyJ/psi  MyJ/psi
                              ChargeConj MyPhi    MyPhi
                              #
                              Decay MyB_c+
                              1.0             MyB_s0      pi+         PHSP;
                              Enddecay
                              CDecay MyB_c-
                              #
                              Decay MyB_s0
                                1.000         MyJ/psi     MyPhi        PVV_CPLH 0.02 1 Hp pHp Hz pHz Hm pHm;
                              #
                              Enddecay
                              Decay Myanti-B_s0
                                1.000         MyJ/psi     MyPhi        PVV_CPLH 0.02 1 Hp pHp Hz pHz Hm pHm;
                              Enddecay
                              #
                              Decay MyJ/psi
                                1.000         mu+         mu-          PHOTOS VLL;
                              Enddecay
                              #
                              Decay MyPhi
                                1.000         K+          K-           VSS;
                              Enddecay
                              End
                              """
                             ),
                             operates_on_particles = cms.vint32(541), 
                             list_forced_decays = cms.vstring('MyB_c+','MyB_c-'),  
                           ),
                           parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                           pythia8CommonSettingsBlock,
                           pythia8CP5SettingsBlock,
                           pythia8PSweightsSettingsBlock,
                           processParameters = cms.vstring( # put below any needed pythia parameter
                            #
                            #'541:m0 = 6.2749',
                            #'541:tau0 = 0.151995',
                            #'541:mayDecay = off',
                            #
                            'ProcessLevel:all = off',
                            'ProcessLevel:resonanceDecays = on'
                            #
                           ),
                           parameterSets = cms.vstring('pythia8CommonSettings',
                                                       'pythia8CP5Settings',
                                                       'pythia8PSweightsSettings',
                                                       'processParameters'
                           )
                        )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


bcgenfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(211),
    MaxEta = cms.untracked.vdouble(3.0),
    MinEta = cms.untracked.vdouble(-3.0),
    MinPt = cms.untracked.vdouble(1.0),
    NumberDaughters = cms.untracked.int32(1),
    ParticleID = cms.untracked.int32(541),
    verbose = cms.untracked.int32(0)
)

bfilter = cms.EDFilter(
    "PythiaFilter",
    MaxEta = cms.untracked.double(9999.),
    MinEta = cms.untracked.double(-9999.),
    ParticleID = cms.untracked.int32(531)
)

jpsifilter = cms.EDFilter(
    "PythiaDauVFilter",
    MotherID = cms.untracked.int32(531),
    ParticleID = cms.untracked.int32(443),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(13, -13),
    MinPt = cms.untracked.vdouble(3.5, 3.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    verbose = cms.untracked.int32(1)
)

phifilter = cms.EDFilter(
    "PythiaDauVFilter",
    MotherID = cms.untracked.int32(531),
    ParticleID = cms.untracked.int32(333),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(321, -321),
    MinPt = cms.untracked.vdouble(0.4, 0.4),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    verbose = cms.untracked.int32(1)
)


ProductionFilterSequence = cms.Sequence(generator*bcgenfilter*bfilter*jpsifilter*phifilter)