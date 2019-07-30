from bluesky import RunEngine
from bluesky.plans import count
from event_model import RunRouter
from suitcase.xdi import Serializer
from ophyd.sim import det1, det2


RE = RunEngine({})
RE.subscribe(print)

def serializer_factory(name, start_doc):
    serializer = Serializer('xdi')
    serializer('start', start_doc)
    return [serializer], []


RE.subscribe(RunRouter([serializer_factory]))

xdi_meta_data = {
    'element_symbol' : 'A',
    'element_edge'   : 'K',
    'mono_d_spacing' : 10.0
}

nx_meta_data = {
    'Source': {
        'name': 'NSLS-II'
    },
    'Instrument': {
        'name': 'BMM',
    },
    'Beam': {
        'incident_energy': 1000.0
    }
}

dets = [det1, det2]
RE(count(dets, num=5), md={'NX': nx_meta_data, 'XDI': xdi_meta_data})

# look for file

