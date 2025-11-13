from nasrparse.records.mtr import MTR_WDTH
from nasrparse.records.types import MilRouteTypeCode

from datetime import date

import unittest


class TestMTR_WDTH(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mtr_wdth = MTR_WDTH(
            "2025/10/02",
            "IR",
            "062",
            "ZDC",
            "5",
            "4 NM EITHER SIDE OF CENTERLINE FROM  A TO C;",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mtr_wdth)
        self.assertEqual(
            result,
            "MTR_WDTH ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            f"ROUTE_TYPE_CODE={MilRouteTypeCode.IFR_ROUTE!r}, "
            "ROUTE_ID='062', "
            "ARTCC='ZDC', "
            "WIDTH_SEQ_NO=5, "
            "WIDTH_TEXT='4 NM EITHER SIDE OF CENTERLINE FROM  A TO C;'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mtr_wdth.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "route_type_code",
                "route_id",
                "artcc",
                "width_seq_no",
                "width_text",
            ],
        )

    def test_to_dict(self):
        result = self.mtr_wdth.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "route_type_code": MilRouteTypeCode.IFR_ROUTE.value,
                "route_id": "062",
                "artcc": "ZDC",
                "width_seq_no": 5,
                "width_text": "4 NM EITHER SIDE OF CENTERLINE FROM  A TO C;",
            },
        )

    def test_to_str(self):
        result = self.mtr_wdth.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "route_type_code: IR, "
            "route_id: 062, "
            "artcc: ZDC, "
            "width_seq_no: 5, "
            "width_text: 4 NM EITHER SIDE OF CENTERLINE FROM  A TO C;",
        )
