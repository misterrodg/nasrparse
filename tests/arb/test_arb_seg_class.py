from nasrparse.records.arb import ARB_SEG
from nasrparse.records.types import AltitudeStructureCode, BoundaryTypeCode, HemisCode

from datetime import date

import unittest


class TestARB_SEG(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.arb_seg = ARB_SEG(
            "2025/10/02",
            "ZDC",
            "WASHINGTON",
            "ZDC*H*53890",
            "HIGH",
            "ARTCC",
            "10",
            "39",
            "10",
            "0",
            "N",
            "39.16666666",
            "80",
            "24",
            "0",
            "W",
            "-80.4",
            "/COMMON ZDC-ZID-ZOB/ TO",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.arb_seg)
        self.assertEqual(
            result,
            "ARB_SEG ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "LOCATION_ID='ZDC', "
            "LOCATION_NAME='WASHINGTON', "
            "REC_ID='ZDC*H*53890', "
            f"ALTITUDE={AltitudeStructureCode.HIGH!r}, "
            f"TYPE={BoundaryTypeCode.ARTCC!r}, "
            "POINT_SEQ=10, "
            "LAT_DEG=39, "
            "LAT_MIN=10, "
            "LAT_SEC=0.0, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.16666666, "
            "LON_DEG=80, "
            "LON_MIN=24, "
            "LON_SEC=0.0, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-80.4, "
            "BNDRY_PT_DESCRIP='/COMMON ZDC-ZID-ZOB/ TO', "
            "NAS_DESCRIP_FLAG=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.arb_seg.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "location_id",
                "location_name",
                "rec_id",
                "altitude",
                "type",
                "point_seq",
                "lat_deg",
                "lat_min",
                "lat_sec",
                "lat_hemis",
                "lat_decimal",
                "lon_deg",
                "lon_min",
                "lon_sec",
                "lon_hemis",
                "lon_decimal",
                "bndry_pt_descrip",
                "nas_descrip_flag",
            ],
        )

    def test_to_dict(self):
        result = self.arb_seg.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "location_id": "ZDC",
                "location_name": "WASHINGTON",
                "rec_id": "ZDC*H*53890",
                "altitude": AltitudeStructureCode.HIGH.value,
                "type": BoundaryTypeCode.ARTCC.value,
                "point_seq": 10,
                "lat_deg": 39,
                "lat_min": 10,
                "lat_sec": 0,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.16666666,
                "lon_deg": 80,
                "lon_min": 24,
                "lon_sec": 0,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -80.4,
                "bndry_pt_descrip": "/COMMON ZDC-ZID-ZOB/ TO",
                "nas_descrip_flag": None,
            },
        )

    def test_to_str(self):
        result = self.arb_seg.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "location_id: ZDC, "
            "location_name: WASHINGTON, "
            "rec_id: ZDC*H*53890, "
            "altitude: HIGH, "
            "type: ARTCC, "
            "point_seq: 10, "
            "lat_deg: 39, "
            "lat_min: 10, "
            "lat_sec: 0.0, "
            "lat_hemis: N, "
            "lat_decimal: 39.16666666, "
            "lon_deg: 80, "
            "lon_min: 24, "
            "lon_sec: 0.0, "
            "lon_hemis: W, "
            "lon_decimal: -80.4, "
            "bndry_pt_descrip: /COMMON ZDC-ZID-ZOB/ TO, "
            "nas_descrip_flag: None",
        )
