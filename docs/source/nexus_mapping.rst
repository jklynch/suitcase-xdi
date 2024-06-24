XDI to NeXus Mapping
=====================

Strings
-------

Facility.name = "NSLS-II"
  NXSource.name = "NSLS-II"
Beamline.name = "BMM (06BM) -- Beamline for Materials Measurement -- NIST"
  NXInstrument.name = "BMM (06BM) -- Beamline for Materials Measurement -- NIST"
Beamline.xray_source = "NSLS-II three-pole wiggler"
  * NXinsertion_device.type = 'wiggler'
  * NXinsertion_device.poles = 3

  The facility should really have NX definitions for all of its
  devices.  In fact, I propose that, as part of this exercise, those
  get written and run by some of the accelerator folk so that no one
  has to have this conversation again.

Beamline.collimation = "paraboloid mirror, 5nm Rh on 30 nm Pt"
  * NXMirror.shape = "paraboloid:"
  * NXMirror.coating_material = "Rh"
  * NXMirror.coating_thickness = "5 nm"
  * MXMirror.substrate_material = "Pt"
  * NMXirror.substrate_thickness = "30 nm"

  Close.  The problem is that, for BMM, the substrate is Si.  Two of
  our mirrors have two coatings ... Rh on top of Pt.  That said, I
  don't want to use NXMirror.(even|odd)_layer_material -- that
  suggests a different kind of mirror.  It is possible that the best
  values for material and thickness are "Rh on Pt" and "5nm on 30 nm".
  But I would want to consult with someone (perhaps Stuart) who is
  more familiar with how things are done in nexus-land.


[start doc]
-----------
Beamline.harmonic_rejection = ??
  This would fall under NXMirror

  * NXMirror.shape = flat
  
  The problem here is that the NXMirror definition does not have
  taxonomy for stripes on the mirror.  Our HR mirror has a Pt stripe
  and a bare Si stripe.  Another thing we will have to find out what
  is done or make up new taxonomy.

Beamline.energy = 
  * NXBeam.incident_energy

Detector.I0
  * NXDetector.type = ion chamber
  * NXDetector.detection_gas_path = 15cm
  * NXDetector.local_name = I0

  I don't see an NXDetector definition suitable for contents of ion chamber

Detector.It
  * NXDetector.type = ion chamber
  * NXDetector.detection_gas_path = 30cm
  * NXDetector.local_name = It

Detector.Ir
  * NXDetector.type = ion chamber
  * NXDetector.detection_gas_path = 30cm
  * NXDetector.local_name = Ir

Detector.fluorescence
  * NXDetector.type = 'SII Vortex ME4 (4-element silicon drift)'
  * NXDetector.description = 'DOI: 10.1107/S0909049510009064'

Detector.deadtime_correction

  * NXDetector.description

  What I store here is NOT NXDetector.dead_time, which is something
  that validates to time.  The closest thing in the NXDetector spec is
  description, which takes a string.

  See above.

Detector.yield
  * NXDetector.type = 'electron yield'


Element.symbol
  * Possibly use NXParameter, as in 
    NXParameter.element = 'Fe'

  NXParameter is pretty open-ended.

  Alternately, this could go in NXXas, which is an application definition

Element.edge
  * Possibly use NXParameter, as in 
    NXParameter.edge = 'K'

  NXParameter is pretty open-ended.

  Alternately, this could go in NXXas, which is an application definition
