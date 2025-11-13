from nasrparse.records.mtr import MTR_BASE
from nasrparse.records.types import MilRouteTypeCode

from datetime import date

import unittest


class TestMTR_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mtr_base = MTR_BASE("2025/10/02", "IR", "062", "ZDC", "", "CONTINUOUS")

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mtr_base)
        self.assertEqual(
            result,
            "MTR_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            f"ROUTE_TYPE_CODE={MilRouteTypeCode.IFR_ROUTE!r}, "
            "ROUTE_ID='062', "
            "ARTCC='ZDC', "
            "FSS=None, "
            "TIME_OF_USE='CONTINUOUS'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mtr_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "route_type_code",
                "route_id",
                "artcc",
                "fss",
                "time_of_use",
            ],
        )

    def test_to_dict(self):
        result = self.mtr_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "route_type_code": MilRouteTypeCode.IFR_ROUTE.value,
                "route_id": "062",
                "artcc": "ZDC",
                "fss": None,
                "time_of_use": "CONTINUOUS",
            },
        )

    def test_to_str(self):
        result = self.mtr_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "route_type_code: IR, "
            "route_id: 062, "
            "artcc: ZDC, "
            "fss: None, "
            "time_of_use: CONTINUOUS",
        )
