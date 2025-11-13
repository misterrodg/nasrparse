from nasrparse.records.fix import FIX_CHRT
from nasrparse.records.types import HemisCode, PointCode

from datetime import date

import unittest


class TestFIX_CHRT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.fix_chrt = FIX_CHRT(
            "2025/10/30", "RUANE", "K6", "MD", "US", "CONTROLLER LOW"
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.fix_chrt)
        self.assertEqual(
            result,
            "FIX_CHRT ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FIX_ID='RUANE', "
            "ICAO_REGION_CODE='K6', "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "CHARTING_TYPE_DESC='CONTROLLER LOW'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.fix_chrt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "fix_id",
                "icao_region_code",
                "state_code",
                "country_code",
                "charting_type_desc",
            ],
        )

    def test_to_dict(self):
        result = self.fix_chrt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "fix_id": "RUANE",
                "icao_region_code": "K6",
                "state_code": "MD",
                "country_code": "US",
                "charting_type_desc": "CONTROLLER LOW",
            },
        )

    def test_to_str(self):
        result = self.fix_chrt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "fix_id: RUANE, "
            "icao_region_code: K6, "
            "state_code: MD, "
            "country_code: US, "
            "charting_type_desc: CONTROLLER LOW",
        )
