# Tests should generate (and then clean up) any files they need for testing. No
# binary files should be included in the repository.
from suitcase.xdi import export

config = """
[versions]
"XDI"                         = "# XDI/1.0 Bluesky"

[columns]
"Column.1"                    = {template="energy",  data_key="det", column_template="{data[det][0]}", units="eV"}
"Column.2"                    = {template="mutrans", data_key="det", column_template="{data[det][0]:.3}"}
"Column.3"                    = {template="i0",      data_key="det", column_template="{data[det][0]:.5}"}

[required_headers]
"Element.symbol"              = {template="{md[XDI][element_symbol]}"}
"Element.edge"                = {template="{md[XDI][element_edge]}"}
"Mono.d_spacing"              = {template="{md[XDI][mono_d_spacing]}"}

[optional_headers]
"Facility.name"               = {template="{md[NX][Source][name]}" }
"Beamline.name"               = {template="{md[NX][Instrument][name]}" }
"Beamline.focusing"           = {template="parabolic mirror", type="string", units="none", use=true}
"Beamline.harmonic_rejection" = {template="detuned", type="string", units="none", use=true}
"Beamline.energy"             = {template="{md[NX][Beam][incident_energy]:.3f} eV", units="eV", use=false, precision=1}
"""


def test_export(tmp_path, example_data):
    # Exercise the exporter on the myriad cases parametrized in example_data.

    # write the config file
    # it will be read by the Serializer
    config_file_path = tmp_path / "xdi.toml"
    with open(config_file_path, "wt") as config_file:
        config_file.write(config)

    documents = example_data(
        skip_tests_with=["direct_img", "direct_img_list"],
        md={
            "suitcase-xdi": {"config-file-path": str(config_file_path)},
            "XDI": {"element_symbol": "A", "element_edge": "K", "mono_d_spacing": 10.0},
            "NX": {
                "Source": {"name": "NSLS-II"},
                "Instrument": {"name": "BMM"},
                "Beam": {"incident_energy": 1000.0},
            },
        },
    )

    artifacts = export(documents, tmp_path)

    # artifacts look like
    #  {
    #    'stream_data': [PosixPath('/tmp/test_export_one_stream_multi_d11/d4ee83a9-64f7-4c25--primary.xdi')]
    #  }
    assert all([a.exists() for a in artifacts["stream_data"]])
