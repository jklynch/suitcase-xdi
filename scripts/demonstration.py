from pprint import pprint

from bluesky import RunEngine
from bluesky.plans import count
from bluesky.preprocessors import SupplementalData
from event_model import RunRouter
from suitcase.xdi import Serializer
from ophyd.sim import det1, det2, det3, motor1, motor2


def pretty_print(name, doc):
    pprint(name)
    pprint(doc)


def serializer_factory(name, start_doc):
    serializer = Serializer("xdi")
    serializer("start", start_doc)
    return [serializer], []


RE = RunEngine({})

sd = SupplementalData()
RE.preprocessors.append(sd)
sd.baseline = [det3, motor1, motor2]

RE.subscribe(pretty_print)
RE.subscribe(RunRouter([serializer_factory]))

suitcase_meta_data = {"config-file-path": "XDI.toml"}

xdi_meta_data = {"Element_symbol": "A", "Element_edge": "K", "Mono_d_spacing": 10.0}

nx_meta_data = {
    "Source": {"name": "NSLS-II"},
    "Instrument": {"name": "BMM"},
    "Beam": {"incident_energy": 1000.0},
}

dets = [det1, det2]
RE(
    count(dets, num=5),
    md={"suitcase-xdi": suitcase_meta_data, "NX": nx_meta_data, "XDI": xdi_meta_data},
)

# look for file
