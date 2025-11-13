from nasrparse.records.wxl import WXL_BASE
from nasrparse.records.types import HemisCode, MethodCode

from datetime import date

import unittest


class TestWXL_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.wxl_base = WXL_BASE(
            "2025/10/02",
            "JYO",
            "LEESBURG",
            "VA",
            "US",
            "39",
            "4",
            "40.7",
            "N",
            "39.07797222",
            "77",
            "33",
            "27",
            "W",
            "-77.5575",
            "390",
            "E",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.wxl_base)
        self.assertEqual(
            result,
            "WXL_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "WEA_ID='JYO', "
            "CITY='LEESBURG', "
            "STATE_CODE='VA', "
            "COUNTRY_CODE='US', "
            "LAT_DEG=39, "
            "LAT_MIN=4, "
            "LAT_SEC=40.7, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.07797222, "
            "LON_DEG=77, "
            "LON_MIN=33, "
            "LON_SEC=27.0, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.5575, "
            "ELEV=390, "
            f"SURVEY_METHOD_CODE={MethodCode.ESTIMATED!r}"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.wxl_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "wea_id",
                "city",
                "state_code",
                "country_code",
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
                "elev",
                "survey_method_code",
            ],
        )

    def test_to_dict(self):
        result = self.wxl_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "wea_id": "JYO",
                "city": "LEESBURG",
                "state_code": "VA",
                "country_code": "US",
                "lat_deg": 39,
                "lat_min": 4,
                "lat_sec": 40.7,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.07797222,
                "lon_deg": 77,
                "lon_min": 33,
                "lon_sec": 27.0,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.5575,
                "elev": 390,
                "survey_method_code": MethodCode.ESTIMATED.value,
            },
        )

    def test_to_str(self):
        result = self.wxl_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "wea_id: JYO, "
            "city: LEESBURG, "
            "state_code: VA, "
            "country_code: US, "
            "lat_deg: 39, "
            "lat_min: 4, "
            "lat_sec: 40.7, "
            "lat_hemis: N, "
            "lat_decimal: 39.07797222, "
            "lon_deg: 77, "
            "lon_min: 33, "
            "lon_sec: 27.0, "
            "lon_hemis: W, "
            "lon_decimal: -77.5575, "
            "elev: 390, "
            "survey_method_code: E",
        )
