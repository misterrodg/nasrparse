from nasrparse.records.mtr import MTR_SOP
from nasrparse.records.types import MilRouteTypeCode

from datetime import date

import unittest


class TestMTR_SOP(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mtr_sop = MTR_SOP(
            "2025/10/02",
            "IR",
            "062",
            "ZDC",
            "5",
            "(1)   ROUTE RESERVATIONS AND BRIEF REQUIRED.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mtr_sop)
        self.assertEqual(
            result,
            "MTR_SOP ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            f"ROUTE_TYPE_CODE={MilRouteTypeCode.IFR_ROUTE!r}, "
            "ROUTE_ID='062', "
            "ARTCC='ZDC', "
            "SOP_SEQ_NO=5, "
            "SOP_TEXT='(1)   ROUTE RESERVATIONS AND BRIEF REQUIRED.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mtr_sop.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "route_type_code",
                "route_id",
                "artcc",
                "sop_seq_no",
                "sop_text",
            ],
        )

    def test_to_dict(self):
        result = self.mtr_sop.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "route_type_code": MilRouteTypeCode.IFR_ROUTE.value,
                "route_id": "062",
                "artcc": "ZDC",
                "sop_seq_no": 5,
                "sop_text": "(1)   ROUTE RESERVATIONS AND BRIEF REQUIRED.",
            },
        )

    def test_to_str(self):
        result = self.mtr_sop.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "route_type_code: IR, "
            "route_id: 062, "
            "artcc: ZDC, "
            "sop_seq_no: 5, "
            "sop_text: (1)   ROUTE RESERVATIONS AND BRIEF REQUIRED.",
        )
