XDI to NeXus Mapping
=====================

Strings
-------

Facility.name = "NSLS-II"
  NXSource.name = "NSLS-II"
Beamline.name = "BMM (06BM) -- Beamline for Materials Measurement -- NIST"
  NXInstrument.name = "BMM (06BM) -- Beamline for Materials Measurement -- NIST"
Beamline.xray_source = "NSLS-II three-pole wiggler"
  ???
Beamline.collimation = "paraboloid mirror, 5nm Rh on 30 nm Pt"
  * NXMirror.shape = "paraboloid:"
  * NXMirror.coating_material = "Rh"
  * NXMirror.coating_thickness = "5 nm"
  * MXMirror.substrate_material = "Pt"
  * NMXirror.substrate_thickness = "30 nm"

[start doc]
-----------
Beamline.harmonic_rejection = ??
  ???
Beamline.energy = 
  NXBeam.incident_energy

Detector.I0
  ???
Detector.It
  ???
Detector.Ir
  ???
Detector.fluorescence
  ???
Detector.deadtime_correction
  ???
Detector.yield
  ???
Element.symbol
  ???
Element.edge
  ???
