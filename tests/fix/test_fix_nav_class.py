from nasrparse.records.fix import FIX_NAV
from nasrparse.records.types import HemisCode, PointCode

from datetime import date

import unittest


class TestFIX_NAV(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.fix_nav = FIX_NAV(
            "2025/10/30",
            "RUANE",
            "K6",
            "MD",
            "US",
            "AML",
            "VOR/DME",
            "16",
            "30.97",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.fix_nav)
        self.assertEqual(
            result,
            "FIX_NAV ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FIX_ID='RUANE', "
            "ICAO_REGION_CODE='K6', "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "NAV_ID='AML', "
            "NAV_TYPE='VOR/DME', "
            "BEARING=16.0, "
            "DISTANCE=30.97"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.fix_nav.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "fix_id",
                "icao_region_code",
                "state_code",
                "country_code",
                "nav_id",
                "nav_type",
                "bearing",
                "distance",
            ],
        )

    def test_to_dict(self):
        result = self.fix_nav.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "fix_id": "RUANE",
                "icao_region_code": "K6",
                "state_code": "MD",
                "country_code": "US",
                "nav_id": "AML",
                "nav_type": "VOR/DME",
                "bearing": 16.0,
                "distance": 30.97,
            },
        )

    def test_to_str(self):
        result = self.fix_nav.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "fix_id: RUANE, "
            "icao_region_code: K6, "
            "state_code: MD, "
            "country_code: US, "
            "nav_id: AML, "
            "nav_type: VOR/DME, "
            "bearing: 16.0, "
            "distance: 30.97",
        )
