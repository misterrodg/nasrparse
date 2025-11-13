from nasrparse.records.arb import ARB_BASE
from nasrparse.records.types import HemisCode, LocationTypeCode

from datetime import date

import unittest


class TestARB_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.arb_base = ARB_BASE(
            "2025/10/02",
            "ZDC",
            "WASHINGTON",
            "ZCW",
            "KZDC",
            "ARTCC",
            "WASHINGTON",
            "DC",
            "US",
            "39",
            "6",
            "4.38",
            "N",
            "39.10121666",
            "77",
            "32",
            "33.96",
            "W",
            "-77.54276666",
            "FACILITY LOCATED AT LEESBURG, VA",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.arb_base)
        self.assertEqual(
            result,
            "ARB_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "LOCATION_ID='ZDC', "
            "LOCATION_NAME='WASHINGTON', "
            "COMPUTER_ID='ZCW', "
            "ICAO_ID='KZDC', "
            f"LOCATION_TYPE={LocationTypeCode.ARTCC!r}, "
            "CITY='WASHINGTON', "
            "STATE='DC', "
            "COUNTRY_CODE='US', "
            "LAT_DEG=39, "
            "LAT_MIN=6, "
            "LAT_SEC=4.38, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.10121666, "
            "LON_DEG=77, "
            "LON_MIN=32, "
            "LON_SEC=33.96, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.54276666, "
            "CROSS_REF='FACILITY LOCATED AT LEESBURG, VA'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.arb_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "location_id",
                "location_name",
                "computer_id",
                "icao_id",
                "location_type",
                "city",
                "state",
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
                "cross_ref",
            ],
        )

    def test_to_dict(self):
        result = self.arb_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "location_id": "ZDC",
                "location_name": "WASHINGTON",
                "computer_id": "ZCW",
                "icao_id": "KZDC",
                "location_type": LocationTypeCode.ARTCC.value,
                "city": "WASHINGTON",
                "state": "DC",
                "country_code": "US",
                "lat_deg": 39,
                "lat_min": 6,
                "lat_sec": 4.38,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.10121666,
                "lon_deg": 77,
                "lon_min": 32,
                "lon_sec": 33.96,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.54276666,
                "cross_ref": "FACILITY LOCATED AT LEESBURG, VA",
            },
        )

    def test_to_str(self):
        result = self.arb_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "location_id: ZDC, "
            "location_name: WASHINGTON, "
            "computer_id: ZCW, "
            "icao_id: KZDC, "
            "location_type: ARTCC, "
            "city: WASHINGTON, "
            "state: DC, "
            "country_code: US, "
            "lat_deg: 39, "
            "lat_min: 6, "
            "lat_sec: 4.38, "
            "lat_hemis: N, "
            "lat_decimal: 39.10121666, "
            "lon_deg: 77, "
            "lon_min: 32, "
            "lon_sec: 33.96, "
            "lon_hemis: W, "
            "lon_decimal: -77.54276666, "
            "cross_ref: FACILITY LOCATED AT LEESBURG, VA",
        )
