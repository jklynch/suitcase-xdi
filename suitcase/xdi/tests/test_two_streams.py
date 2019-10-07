import pprint

from bluesky.preprocessors import SupplementalData
from bluesky.plans import count
from event_model import RunRouter
from ophyd.sim import det1, det2, motor1, motor2
from suitcase.xdi import Serializer


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


def test_two_streams(RE):
    def pretty_print(name, doc):
        pprint.pprint(name)
        pprint.pprint(doc)

    def serializer_factory(name, start_doc):
        serializer = Serializer("xdi")
        serializer("start", start_doc)
        return [serializer], []

    sd = SupplementalData()
    RE.preprocessors.append(sd)
    sd.baseline = [det1, motor1, motor2]

    RE.subscribe(pretty_print)
    RE.subscribe(RunRouter([serializer_factory]))

    suitcase_meta_data = {"config": xdi_file_template}

    xdi_meta_data = {"Element_symbol": "A", "Element_edge": "K", "Mono_d_spacing": 10.0}

    nx_meta_data = {
        "Source": {"name": "NSLS-II"},
        "Instrument": {"name": "BMM"},
        "Beam": {"incident_energy": 1000.0},
    }

    dets = [det1, det2]
    RE(
        count(dets, num=5),
        md={
            "suitcase-xdi": suitcase_meta_data,
            "NX": nx_meta_data,
            "XDI": xdi_meta_data,
        },
    )
