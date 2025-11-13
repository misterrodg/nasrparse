from nasrparse.records.mtr import MTR_PT
from nasrparse.records.types import HemisCode, MilRouteTypeCode

from datetime import date

import unittest


class TestMTR_PT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mtr_pt = MTR_PT(
            "2025/10/02",
            "IR",
            "062",
            "ZDC",
            "10",
            "A",
            "B",
            "(1) 40 MSL-50 MSL (2) AS ASSIGNED TO (3) 40 MSL-50 MSL",
            "35",
            "24",
            "0",
            "N",
            "35.4",
            "76",
            "33",
            "0",
            "W",
            "-76.55",
            "ISO",
            "93",
            "49",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mtr_pt)
        self.assertEqual(
            result,
            "MTR_PT ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            f"ROUTE_TYPE_CODE={MilRouteTypeCode.IFR_ROUTE!r}, "
            "ROUTE_ID='062', "
            "ARTCC='ZDC', "
            "ROUTE_PT_SEQ=10, "
            "ROUTE_PT_ID='A', "
            "NEXT_ROUTE_PT_ID='B', "
            "SEGMENT_TEXT='(1) 40 MSL-50 MSL (2) AS ASSIGNED TO (3) 40 MSL-50 MSL', "
            "LAT_DEG=35, "
            "LAT_MIN=24, "
            "LAT_SEC=0.0, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=35.4, "
            "LON_DEG=76, "
            "LON_MIN=33, "
            "LON_SEC=0.0, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-76.55, "
            "NAV_ID='ISO', "
            "NAVAID_BEARING=93.0, "
            "NAVAID_DIST=49.0"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mtr_pt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "route_type_code",
                "route_id",
                "artcc",
                "route_pt_seq",
                "route_pt_id",
                "next_route_pt_id",
                "segment_text",
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
                "nav_id",
                "navaid_bearing",
                "navaid_dist",
            ],
        )

    def test_to_dict(self):
        result = self.mtr_pt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "route_type_code": MilRouteTypeCode.IFR_ROUTE.value,
                "route_id": "062",
                "artcc": "ZDC",
                "route_pt_seq": 10,
                "route_pt_id": "A",
                "next_route_pt_id": "B",
                "segment_text": "(1) 40 MSL-50 MSL (2) AS ASSIGNED TO (3) 40 MSL-50 MSL",
                "lat_deg": 35,
                "lat_min": 24,
                "lat_sec": 0.0,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 35.4,
                "lon_deg": 76,
                "lon_min": 33,
                "lon_sec": 0.0,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -76.55,
                "nav_id": "ISO",
                "navaid_bearing": 93.0,
                "navaid_dist": 49.0,
            },
        )

    def test_to_str(self):
        result = self.mtr_pt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "route_type_code: IR, "
            "route_id: 062, "
            "artcc: ZDC, "
            "route_pt_seq: 10, "
            "route_pt_id: A, "
            "next_route_pt_id: B, "
            "segment_text: (1) 40 MSL-50 MSL (2) AS ASSIGNED TO (3) 40 MSL-50 MSL, "
            "lat_deg: 35, "
            "lat_min: 24, "
            "lat_sec: 0.0, "
            "lat_hemis: N, "
            "lat_decimal: 35.4, "
            "lon_deg: 76, "
            "lon_min: 33, "
            "lon_sec: 0.0, "
            "lon_hemis: W, "
            "lon_decimal: -76.55, "
            "nav_id: ISO, "
            "navaid_bearing: 93.0, "
            "navaid_dist: 49.0",
        )
