xdi_file_template = """\
[versions]
"XDI"                         = "# XDI/1.0 Bluesky"

[columns]
"Column.1"                    = {column_label="energy",  data_key="det1", column_data="{data[det1][0]}", units="eV"}
"Column.2"                    = {column_label="mutrans", data_key="det2", column_data="{data[det2][0]:.3}"}
"Column.3"                    = {column_label="i0",      data_key="det2", column_data="{data[det2][0]:.5}"}

[required_headers]
"Element.symbol"              = {data="{md[XDI][Element_symbol]}"}
"Element.edge"                = {data="{md[XDI][Element_edge]}"}
"Mono.d_spacing"              = {data="{md[XDI][Mono_d_spacing]}"}

[optional_headers]
"Facility.name"               = {data="{md[NX][Source][name]}"}
"Beamline.name"               = {data="{md[NX][Instrument][name]}"}
"Beamline.focusing"           = {data="parabolic mirror", type="string", units="none", use=true}
"Beamline.harmonic_rejection" = {data="detuned", type="string", units="none", use=true}
"Beamline.energy"             = {data="{md[NX][Beam][incident_energy]:.3f} eV", units="eV", use=false}
"Scan.start_time"             = {}
"Scan.end_time"               = {}
"Scan.edge_energy"            = {data="Scan_edge_energy"}
"Motor.1.set_point"           = {data="{configuration[data_keys][motor1_setpoint][precision]}", stream="baseline"}
"""


def test_write_header():
    pass
