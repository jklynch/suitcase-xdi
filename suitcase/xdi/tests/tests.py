# Tests should generate (and then clean up) any files they need for testing. No
# binary files should be included in the repository.
from suitcase.xdi import export

config = """
[versions]
"XDI"                         = "# XDI/1.0 Bluesky"

[columns]
"Column.1"                    = {column_label="energy",  data_key="det", column_data="{data[det][0]}", units="eV"}
"Column.2"                    = {column_label="mutrans", data_key="det", column_data="{data[det][0]:.3}"}
"Column.3"                    = {column_label="i0",      data_key="det", column_data="{data[det][0]:.5}"}

[required_headers]
"Element.symbol"              = {data="{md[XDI][Element_symbol]}"}
"Element.edge"                = {data="{md[XDI][Element_edge]}"}
"Mono.d_spacing"              = {data="{md[XDI][Mono_d_spacing]}"}

[optional_headers]
"Facility.name"               = {data="{md[NX][Source][name]}" }
"Beamline.name"               = {data="{md[NX][Instrument][name]}" }
"Beamline.focusing"           = {data="parabolic mirror", use=true}
"Beamline.harmonic_rejection" = {data="detuned", use=true}
"Beamline.energy"             = {data="{md[NX][Beam][incident_energy]:.3f} eV", units="eV"}
"Scan.start_time"             = {}
"Scan.end_time"               = {}
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
            "XDI": {"Element_symbol": "A", "Element_edge": "K", "Mono_d_spacing": 10.0},
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
