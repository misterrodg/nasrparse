from nasrparse.records.mtr import MTR_TERR
from nasrparse.records.types import MilRouteTypeCode

from datetime import date

import unittest


class TestMTR_TERR(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mtr_terr = MTR_TERR(
            "2025/10/02",
            "IR",
            "012",
            "ZDC",
            "5",
            "AUTHORIZED FROM A TO E, AND FROM A TO FA.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mtr_terr)
        self.assertEqual(
            result,
            "MTR_TERR ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            f"ROUTE_TYPE_CODE={MilRouteTypeCode.IFR_ROUTE!r}, "
            "ROUTE_ID='012', "
            "ARTCC='ZDC', "
            "TERRAIN_SEQ_NO=5, "
            "TERRAIN_TEXT='AUTHORIZED FROM A TO E, AND FROM A TO FA.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mtr_terr.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "route_type_code",
                "route_id",
                "artcc",
                "terrain_seq_no",
                "terrain_text",
            ],
        )

    def test_to_dict(self):
        result = self.mtr_terr.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "route_type_code": MilRouteTypeCode.IFR_ROUTE.value,
                "route_id": "012",
                "artcc": "ZDC",
                "terrain_seq_no": 5,
                "terrain_text": "AUTHORIZED FROM A TO E, AND FROM A TO FA.",
            },
        )

    def test_to_str(self):
        result = self.mtr_terr.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "route_type_code: IR, "
            "route_id: 012, "
            "artcc: ZDC, "
            "terrain_seq_no: 5, "
            "terrain_text: AUTHORIZED FROM A TO E, AND FROM A TO FA.",
        )
